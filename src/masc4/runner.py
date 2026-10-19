"""Run plan execution: conditions x briefs x repetitions, resumable and parallel.

Layout: <out>/<condition_id>/<brief_id>/rep<NN>/ with run.json (metadata and status),
transcript.jsonl, llm_calls.jsonl, c4_model.json and the C4 artifacts.
A run whose run.json says "completed" or "invalid_output" is final and skipped, so an interrupted
batch can be restarted. "invalid_output" means the team produced no usable artifact (no valid YAML
after the allowed retry, or no valid glossary): this is an outcome of the condition and is reported,
not repeated. "failed" means an infrastructure error (API, network) and is repeated on the next start.
"""
from __future__ import annotations

import hashlib
import json
import random
import subprocess
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, List, Optional

from . import prompts as P
from .conditions import Condition, GenerationSettings
from .fsutil import BatchLock, write_json_atomic
from .pricing import cost_of_log
from .llm import CallLog, LLMClient
from .pipeline import C4Generator, PipelineError, RunRecord, save_record


@dataclass(frozen=True)
class RunSpec:
    condition_id: str
    brief_id: str
    rep: int

    def directory(self, out_root: Path) -> Path:
        return out_root / self.condition_id / self.brief_id / f"rep{self.rep:02d}"


def plan_runs(conditions: List[Condition], brief_ids: List[str], reps: int, seed: int) -> List[RunSpec]:
    """All runs in a seeded random order, so that time (API drift, rate limits) is not confounded with condition."""
    plan = [RunSpec(c.id, b, r) for c in conditions for b in brief_ids for r in range(1, reps + 1)]
    random.Random(seed).shuffle(plan)
    return plan


def code_version(repo: Path) -> Dict[str, object]:
    def git(*args: str) -> str:
        try:
            return subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True, timeout=10).stdout.strip()
        except Exception:
            return ""
    return {"commit": git("rev-parse", "HEAD"), "dirty": bool(git("status", "--porcelain", "--", "src", "configs"))}


def read_meta(run_dir: Path) -> Optional[dict]:
    try:
        return json.loads((run_dir / "run.json").read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None


FINAL_STATUSES = ("completed", "invalid_output")


def is_completed(run_dir: Path) -> bool:
    """True if the run is final: completed, or ended with an invalid output of the team (not repeated)."""
    meta = read_meta(run_dir)
    return bool(meta) and meta.get("status") in FINAL_STATUSES


def archive_previous_attempt(run_dir: Path) -> None:
    """Move files of an unfinished earlier attempt aside, so attempts are never mixed (kept for auditing)."""
    leftovers = [p for p in run_dir.iterdir() if p.name != "previous_attempts"]
    if not leftovers:
        return
    target = run_dir / "previous_attempts" / time.strftime("%Y%m%d-%H%M%S")
    suffix = 1
    while target.exists():
        target = target.with_name(f"{target.name}-{suffix}")
        suffix += 1
    target.mkdir(parents=True)
    for p in leftovers:
        p.rename(target / p.name)


def execute_run(spec: RunSpec, condition: Condition, brief_text: str, settings: GenerationSettings,
                make_llm: Callable[[str, CallLog], LLMClient], out_root: Path, code: Dict[str, object]) -> str:
    run_dir = spec.directory(out_root)
    run_dir.mkdir(parents=True, exist_ok=True)
    archive_previous_attempt(run_dir)
    call_log = CallLog(run_dir / "llm_calls.jsonl")
    llm = make_llm(settings.model, call_log)
    meta = {
        "condition": condition.id, "brief": spec.brief_id, "rep": spec.rep,
        "team": [a.display_name for a in condition.team], "team_persona_keys": condition.team_keys,
        "memory": condition.memory, "model_requested": settings.model, "temperature": settings.temperature,
        "brief_sha256": hashlib.sha256(brief_text.encode("utf-8")).hexdigest(),
        "rounds": settings.rounds, "code": code, "prompt_hashes": P.prompt_hashes(),
        "started": time.strftime("%Y-%m-%dT%H:%M:%S"), "status": "running",
    }
    (run_dir / "brief.yaml").write_text(brief_text, encoding="utf-8")   # exact input of this run
    write_json_atomic(run_dir / "run.json", meta)
    record = RunRecord()
    try:
        C4Generator(llm, condition, temperature=settings.temperature, rounds=settings.rounds).generate(brief_text, record)
        meta["status"] = "completed"
    except PipelineError as err:  # the team's output is unusable: a final outcome of this condition
        meta["status"], meta["error"] = "invalid_output", str(err)
    except Exception as err:  # API failure after retries or a bug: record it, never hide it
        meta["status"], meta["error"] = "failed", f"{type(err).__name__}: {err}"
        meta["traceback"] = traceback.format_exc(limit=5)
    save_record(record, run_dir)
    versions = sorted({r["model_version"] for r in call_log.records})
    meta.update({
        "finished": time.strftime("%Y-%m-%dT%H:%M:%S"), "model_versions_served": versions,
        "n_llm_calls": len(call_log.records), "yaml_retries": record.yaml_retries,
        "n_containers": len(record.c4_model.get("components") or {}),
        "tokens": {k: sum(r[k] for r in call_log.records) for k in ("input_tokens", "output_tokens", "thought_tokens")},
    })
    write_json_atomic(run_dir / "run.json", meta)
    if meta["status"] == "failed" and "daily quota exhausted" in meta.get("error", ""):
        return "quota"
    return meta["status"]


def run_plan(plan: List[RunSpec], conditions: Dict[str, Condition], briefs: Dict[str, str],
             settings: GenerationSettings, make_llm: Callable[[str, CallLog], LLMClient], out_root: Path,
             repo: Path, workers: int = 1, log: Callable[[str], None] = print,
             max_cost_usd: Optional[float] = None) -> Dict[str, int]:
    """Execute the plan; with max_cost_usd, no new run starts once the estimated generation cost of all
    runs in out_root (this and earlier batches) reaches the limit."""
    with BatchLock(out_root):
        return _run_plan_locked(plan, conditions, briefs, settings, make_llm, out_root, repo, workers, log,
                                max_cost_usd)


def _run_plan_locked(plan, conditions, briefs, settings, make_llm, out_root, repo, workers, log,
                     max_cost_usd=None) -> Dict[str, int]:
    code = code_version(repo)
    other_models = sorted({m["model_requested"] for s in plan for m in [read_meta(s.directory(out_root))]
                           if m and m.get("model_requested") != settings.model})
    if other_models:
        raise RuntimeError(f"{out_root} already contains runs of {other_models}; use a different --out for "
                           f"{settings.model} so that models are never mixed")
    todo = [s for s in plan if not is_completed(s.directory(out_root))]
    log(f"{len(plan)} runs planned, {len(plan) - len(todo)} already final, {len(todo)} to do "
        f"(code {str(code['commit'])[:8]}{' DIRTY' if code['dirty'] else ''})")
    counts = {"completed": 0, "failed": 0}
    lock = threading.Lock()
    stop = threading.Event()   # set on a daily-quota failure, on Ctrl+C/kill, or when the cost limit is reached
    spent = {"usd": sum(cost_of_log(p) for p in out_root.glob("*/*/rep*/llm_calls*.jsonl"))
             + sum(cost_of_log(p) for p in out_root.glob("*/*/rep*/previous_attempts/*/llm_calls*.jsonl")),
             "limit_hit": False}
    if max_cost_usd is not None:
        log(f"cost limit ${max_cost_usd:.2f}; already spent in {out_root}: ${spent['usd']:.2f}")

    def guarded(spec: RunSpec) -> str:
        if stop.is_set():
            return "skipped"
        if max_cost_usd is not None and spent["usd"] >= max_cost_usd:
            with lock:
                spent["limit_hit"] = True
            stop.set()
            return "skipped"
        status = execute_run(spec, conditions[spec.condition_id], briefs[spec.brief_id], settings, make_llm,
                             out_root, code)
        with lock:
            spent["usd"] += cost_of_log(spec.directory(out_root) / "llm_calls.jsonl")
        if status == "quota":
            stop.set()
        return status

    interrupted = False
    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        futures = {pool.submit(guarded, s): s for s in todo}
        pending = set(futures)
        while pending:
            try:
                fut = next(as_completed(pending))
            except KeyboardInterrupt:
                if interrupted:
                    raise
                interrupted = True
                stop.set()
                for f in pending:
                    f.cancel()
                log("Interrupted: no new runs will start; waiting for the runs in progress to finish "
                    "(press Ctrl+C again to abandon them - they will simply be repeated next time).")
                continue
            pending.discard(fut)
            if fut.cancelled():
                continue
            spec, status = futures[fut], fut.result()
            with lock:
                counts[status] = counts.get(status, 0) + 1
            if status != "skipped":
                done = sum(v for k, v in counts.items() if k != "skipped")
                log(f"[{done}/{len(todo)}] {spec.condition_id} {spec.brief_id} rep{spec.rep:02d}: {status}")
    if spent["limit_hit"]:
        log(f"Cost limit reached (estimated ${spent['usd']:.2f} >= ${max_cost_usd:.2f}): no new runs started. "
            "Raise --max-cost and run the same command again to continue.")
    elif interrupted:
        log("Stopped by the user. Run the same command again to continue; completed runs are kept.")
    elif stop.is_set():
        log(f"Daily API quota exhausted: stopped ({counts.get('skipped', 0)} runs not started). Run the same "
            "command again after the quota resets; only unfinished runs are repeated.")
    return counts
