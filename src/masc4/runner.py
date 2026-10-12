"""Run plan execution: conditions x briefs x repetitions, resumable and parallel.

Layout: <out>/<condition_id>/<brief_id>/rep<NN>/ with run.json (metadata and status),
transcript.jsonl, llm_calls.jsonl, c4_model.json and the C4 artifacts.
A run whose run.json says "completed" is skipped, so an interrupted batch can be restarted.
"""
from __future__ import annotations

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


def is_completed(run_dir: Path) -> bool:
    meta = run_dir / "run.json"
    if not meta.exists():
        return False
    try:
        return json.loads(meta.read_text(encoding="utf-8")).get("status") == "completed"
    except json.JSONDecodeError:
        return False


def execute_run(spec: RunSpec, condition: Condition, brief_text: str, settings: GenerationSettings,
                make_llm: Callable[[str, CallLog], LLMClient], out_root: Path, code: Dict[str, object]) -> str:
    run_dir = spec.directory(out_root)
    run_dir.mkdir(parents=True, exist_ok=True)
    calls_path = run_dir / "llm_calls.jsonl"
    if calls_path.exists():  # previous failed attempt: keep its log for auditing
        calls_path.rename(run_dir / f"llm_calls.failed-{int(time.time())}.jsonl")
    call_log = CallLog(calls_path)
    llm = make_llm(settings.model, call_log)
    meta = {
        "condition": condition.id, "brief": spec.brief_id, "rep": spec.rep,
        "team": [a.display_name for a in condition.team], "team_persona_keys": condition.team_keys,
        "memory": condition.memory, "model_requested": settings.model, "temperature": settings.temperature,
        "rounds": settings.rounds, "code": code, "prompt_hashes": P.prompt_hashes(),
        "started": time.strftime("%Y-%m-%dT%H:%M:%S"), "status": "running",
    }
    (run_dir / "run.json").write_text(json.dumps(meta, indent=1), encoding="utf-8")
    record = RunRecord()
    try:
        C4Generator(llm, condition, temperature=settings.temperature, rounds=settings.rounds).generate(brief_text, record)
        meta["status"] = "completed"
    except PipelineError as err:
        meta["status"], meta["error"] = "failed", str(err)
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
    (run_dir / "run.json").write_text(json.dumps(meta, indent=1), encoding="utf-8")
    return meta["status"]


def run_plan(plan: List[RunSpec], conditions: Dict[str, Condition], briefs: Dict[str, str],
             settings: GenerationSettings, make_llm: Callable[[str, CallLog], LLMClient], out_root: Path,
             repo: Path, workers: int = 1, log: Callable[[str], None] = print) -> Dict[str, int]:
    code = code_version(repo)
    todo = [s for s in plan if not is_completed(s.directory(out_root))]
    log(f"{len(plan)} runs planned, {len(plan) - len(todo)} already completed, {len(todo)} to do "
        f"(code {str(code['commit'])[:8]}{' DIRTY' if code['dirty'] else ''})")
    counts = {"completed": 0, "failed": 0}
    lock = threading.Lock()
    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        futures = {pool.submit(execute_run, s, conditions[s.condition_id], briefs[s.brief_id], settings,
                               make_llm, out_root, code): s for s in todo}
        for i, fut in enumerate(as_completed(futures), 1):
            spec = futures[fut]
            status = fut.result()
            with lock:
                counts[status] = counts.get(status, 0) + 1
            log(f"[{i}/{len(todo)}] {spec.condition_id} {spec.brief_id} rep{spec.rep:02d}: {status}")
    return counts
