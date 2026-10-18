"""Evaluate generated runs (structural metrics and LLM judge) and export one CSV row per run.

Examples:
  # structural metrics only (no API calls), then the CSV
  .venv/bin/python scripts/run_evaluation.py --results results/pilot --no-judge --csv results/pilot/runs.csv
  # main judge on all completed runs
  .venv/bin/python scripts/run_evaluation.py --results results/v2 --judge-model gemini-3.8-flash \\
      --env-file "../../../.env" --workers 4 --csv results/v2/runs.csv
  # control judge on the first repetition of every condition and brief
  .venv/bin/python scripts/run_evaluation.py --results results/v2 --judge-model gemma-4-26b-a4b-it --sample-rep 1 ...

Results are cached per run (structural.json, judge_<model>.json); a judge file that
contains an error is retried on the next invocation.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from masc4.conditions import load_conditions  # noqa: E402
from masc4.judge import ISO_CHARACTERISTICS, JudgeError, judge_run, load_scenarios  # noqa: E402
from masc4.signals import install_stop_handlers  # noqa: E402
from masc4.llm import CallLog, GeminiClient, LLMError, load_api_key  # noqa: E402
from masc4.fsutil import BatchLock, write_json_atomic  # noqa: E402
from masc4.structural import evaluate_structure, find_java  # noqa: E402


def completed_runs(results: Path):
    for meta_path in sorted(results.glob("*/*/rep*/run.json")):
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        yield meta_path.parent, meta


def judge_file(run_dir: Path, model: str) -> Path:
    return run_dir / f"judge_{model}.json"


def load_judge(run_dir: Path, model: str):
    try:
        return json.loads(judge_file(run_dir, model).read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def needs_judge(run_dir: Path, model: str) -> bool:
    data = load_judge(run_dir, model)
    return data is None or "error" in data or bool(data.get("errors"))


def evaluate_run(run_dir: Path, meta: dict, briefs: dict, scenarios_dir: Path, jar: Path, judge_model, api_key,
                 force_structural: bool, java: str = "java") -> str:
    c4 = json.loads((run_dir / "c4_model.json").read_text(encoding="utf-8"))
    if force_structural or not (run_dir / "structural.json").exists():
        write_json_atomic(run_dir / "structural.json", evaluate_structure(c4, jar, java))
    if not judge_model or not needs_judge(run_dir, judge_model):
        return "ok"
    log = CallLog(run_dir / f"judge_calls_{judge_model}.jsonl")
    llm = GeminiClient(judge_model, api_key, log)
    previous = load_judge(run_dir, judge_model)
    try:
        scenarios = load_scenarios(scenarios_dir / f"{meta['brief']}.yaml")
        result = judge_run(llm, briefs[meta["brief"]], c4, scenarios, previous=previous)
        status = f"judge error: {sorted(result['errors'])}" if result.get("errors") else "ok"
    except (JudgeError, LLMError, FileNotFoundError, KeyError) as err:
        result, status = {"model": judge_model, "error": f"{type(err).__name__}: {err}"}, "judge error"
    write_json_atomic(judge_file(run_dir, judge_model), result)
    return status


def row_for(run_dir: Path, meta: dict, studies: dict) -> dict:
    row = {"condition": meta["condition"], "studies": " ".join(studies.get(meta["condition"], ())),
           "brief": meta["brief"], "rep": meta["rep"], "status": meta["status"], "memory": meta["memory"],
           "team": " -> ".join(meta["team"]), "model_versions": " ".join(meta.get("model_versions_served", [])),
           "n_llm_calls": meta.get("n_llm_calls"), "yaml_retries": meta.get("yaml_retries"),
           **{f"tokens_{k}": v for k, v in (meta.get("tokens") or {}).items()}}
    s_path = run_dir / "structural.json"
    if s_path.exists():
        s = json.loads(s_path.read_text(encoding="utf-8"))
        rv = s["reference_validity"]
        row.update({"completeness": s["completeness"]["score"], "yaml_validity": s["yaml_validity"]["score"],
                    "abstraction_adherence": s["abstraction_adherence"]["score"],
                    "compilation": s["compilation"]["score"], "reference_validity": rv["score"], "c4_sc": rv["c4_sc"],
                    "reference_validity_strict": rv["strict_score"], "cross_level_references": rv["cross_level_references"],
                    **{f"reference_validity_{k}": v for k, v in rv["per_level"].items()},
                    "l1_l2_jaccard": s["cross_level"]["l1_l2_jaccard"],
                    "l2_l3_consistency": s["cross_level"]["l2_l3_consistency"],
                    "n_containers": s["size"]["n_containers"], "total_elements": s["size"]["total_elements"],
                    "total_relationships": s["size"]["total_relationships"]})
    for j_path in sorted(run_dir.glob("judge_*.json")):
        j = json.loads(j_path.read_text(encoding="utf-8"))
        tag = j_path.stem.replace("judge_", "")
        if "error" in j or j.get("errors"):
            row[f"{tag}__error"] = j.get("error") or json.dumps(j["errors"])
        if "iso" in j:
            row[f"{tag}__iso_mean"] = j["iso"]["mean"]
            row.update({f"{tag}__iso_{k}": j["iso"]["scores"][k] for k in ISO_CHARACTERISTICS})
        if "atam" in j:
            row[f"{tag}__atam_ri"] = j["atam"]["responsiveness_index"]
            row.update({f"{tag}__atam_{k.lower()}": v for k, v in j["atam"]["by_quality_attribute"].items()})
        if "requirements" in j:
            row[f"{tag}__req_coverage"] = j["requirements"]["coverage"]
    return row


def main() -> None:
    install_stop_handlers()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--results", required=True)
    ap.add_argument("--config", default=str(REPO / "configs/conditions_v2.yaml"))
    ap.add_argument("--briefs-dir", default=str(REPO / "data/briefs"))
    ap.add_argument("--scenarios-dir", default=str(REPO / "configs/scenarios"))
    ap.add_argument("--jar", default=str(REPO / "plantuml.jar"))
    ap.add_argument("--judge-model", help="model id; omit together with --no-judge for structural metrics only")
    ap.add_argument("--no-judge", action="store_true")
    ap.add_argument("--sample-rep", type=int, help="judge only this repetition (e.g. 1 for the control judge)")
    ap.add_argument("--limit", type=int, help="evaluate at most this many runs (e.g. a quick check of a slow judge)")
    ap.add_argument("--workers", type=int, default=1)
    ap.add_argument("--env-file")
    ap.add_argument("--force-structural", action="store_true")
    ap.add_argument("--csv", help="write one row per run to this CSV file")
    args = ap.parse_args()

    results = Path(args.results)
    briefs = {p.stem: p.read_text(encoding="utf-8").replace("\r\n", "\n") for p in Path(args.briefs_dir).glob("*.yaml")}
    _, conditions = load_conditions(Path(args.config))
    studies = {c.id: c.studies for c in conditions}
    judge_model = None if args.no_judge else args.judge_model
    if not args.no_judge and not judge_model:
        sys.exit("give --judge-model or --no-judge")
    api_key = load_api_key(Path(args.env_file) if args.env_file else None) if judge_model else None

    java = find_java()
    print(f"PlantUML compilation with: {java}")
    runs = [(d, m) for d, m in completed_runs(results) if m["status"] == "completed"]
    todo = [(d, m) for d, m in runs if not args.sample_rep or m["rep"] == args.sample_rep]
    if args.limit:
        todo = todo[:args.limit]
    print(f"{len(runs)} completed runs; evaluating {len(todo)}" + (f" with judge {judge_model}" if judge_model else ""))
    counts, lock = {}, threading.Lock()
    with BatchLock(results, ".evaluation.lock"), ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {pool.submit(evaluate_run, d, m, briefs, Path(args.scenarios_dir), Path(args.jar), judge_model,
                               api_key, args.force_structural, java): d for d, m in todo}
        try:
            for fut in as_completed(futures):
                status = fut.result()
                with lock:
                    counts[status] = counts.get(status, 0) + 1
                if status != "ok":
                    print(f"  {futures[fut].relative_to(results)}: {status}")
        except KeyboardInterrupt:
            for f in futures:
                f.cancel()
            print("Interrupted: waiting for evaluations in progress; finished results are kept. "
                  "Run the same command again to continue.")
            raise
    print("evaluation:", counts)

    if args.csv:
        rows = [row_for(d, m, studies) for d, m in completed_runs(results)]
        fields = list(dict.fromkeys(k for r in rows for k in r))
        with open(args.csv, "w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
        print(f"{len(rows)} rows -> {args.csv}")


if __name__ == "__main__":
    main()
