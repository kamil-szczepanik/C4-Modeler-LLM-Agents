"""Generate C4 models for the v2 experiments.

Examples:
  # show the plan without calling any model
  .venv/bin/python scripts/run_generation.py --reps 6 --dry-run
  # pilot: all conditions, two briefs, two repetitions, on the Gemini API
  .venv/bin/python scripts/run_generation.py --briefs clinic-management-system online-bookstore \\
      --reps 2 --out results/pilot --env-file "../../../.env"
  # offline smoke test of the whole pipeline with a scripted fake model
  .venv/bin/python scripts/run_generation.py --fake --reps 1 --out results/fake
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from masc4.conditions import load_conditions  # noqa: E402
from masc4.llm import GeminiClient, load_api_key  # noqa: E402
from masc4.runner import plan_runs, run_plan  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default=str(REPO / "configs/conditions_v2.yaml"))
    ap.add_argument("--briefs-dir", default=str(REPO / "data/briefs"))
    ap.add_argument("--briefs", nargs="*", help="brief ids (file stems); default: all in --briefs-dir")
    ap.add_argument("--conditions", nargs="*", help="condition ids; default: all")
    ap.add_argument("--reps", type=int, required=True, help="repetitions per condition and brief")
    ap.add_argument("--out", default=str(REPO / "results/v2"))
    ap.add_argument("--workers", type=int, default=1, help="runs executed in parallel")
    ap.add_argument("--seed", type=int, default=2026, help="seed for the randomized run order")
    ap.add_argument("--model", help="override the generation model from the config")
    ap.add_argument("--env-file", help=".env file with GEMINI_API_KEY (if not set in the environment)")
    ap.add_argument("--dry-run", action="store_true", help="print the plan and exit")
    ap.add_argument("--fake", action="store_true", help="use the scripted fake model (no API calls)")
    args = ap.parse_args()

    settings, conditions = load_conditions(Path(args.config))
    if args.model:
        settings = type(settings)(model=args.model, temperature=settings.temperature, rounds=settings.rounds)
    if args.conditions:
        unknown = set(args.conditions) - {c.id for c in conditions}
        if unknown:
            sys.exit(f"unknown conditions: {sorted(unknown)}")
        conditions = [c for c in conditions if c.id in args.conditions]
    brief_paths = sorted(Path(args.briefs_dir).glob("*.yaml"))
    briefs = {p.stem: p.read_text(encoding="utf-8").replace("\r\n", "\n") for p in brief_paths}
    if args.briefs:
        missing = set(args.briefs) - set(briefs)
        if missing:
            sys.exit(f"unknown briefs: {sorted(missing)}")
        briefs = {k: briefs[k] for k in args.briefs}

    plan = plan_runs(conditions, sorted(briefs), args.reps, args.seed)
    print(f"model={settings.model} temperature={settings.temperature} rounds={settings.rounds}")
    print(f"{len(conditions)} conditions x {len(briefs)} briefs x {args.reps} reps = {len(plan)} runs")
    for c in conditions:
        print(f"  {c.id:24s} memory={c.memory:8s} team: {' -> '.join(a.display_name for a in c.team)}")
    if args.dry_run:
        return

    if args.fake:
        sys.path.insert(0, str(REPO / "tests"))
        from fake_responses import make_fake_llm
        make_llm = lambda model, log: make_fake_llm(call_log=log)  # noqa: E731
    else:
        api_key = load_api_key(Path(args.env_file) if args.env_file else None)
        make_llm = lambda model, log: GeminiClient(model, api_key, log)  # noqa: E731

    counts = run_plan(plan, {c.id: c for c in conditions}, briefs, settings, make_llm, Path(args.out), REPO,
                      workers=args.workers)
    print("done:", counts)


if __name__ == "__main__":
    main()
