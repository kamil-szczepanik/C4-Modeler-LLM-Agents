"""Show the progress of a generation batch and of its evaluation (structural metrics and each judge).

  .venv/bin/python scripts/progress.py results/smoke            # one snapshot
  .venv/bin/python scripts/progress.py results/v2 --watch 15    # refresh every 15 s (Ctrl+C to stop)
  .venv/bin/python scripts/progress.py results/v2 --planned 432 # show percentage and time left
"""
from __future__ import annotations

import argparse
import json
import time
from datetime import datetime
from pathlib import Path

# USD per 1M tokens (input, output); thinking tokens are billed as output. Gemma is free of charge.
PRICES = {"gemini-3.5-flash-lite": (0.30, 2.50), "gemini-3.1-flash-lite": (0.25, 1.50),
          "gemini-3.8-flash": (0.75, 3.75), "gemini-3.6-flash": (0.75, 3.75)}


def read_jsonl(path: Path):
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            pass  # line being written right now
    return out


def fmt_duration(seconds: float) -> str:
    seconds = int(seconds)
    return f"{seconds // 3600}h{seconds % 3600 // 60:02d}m" if seconds >= 3600 else f"{seconds // 60}m{seconds % 60:02d}s"


def cost_of(calls) -> float:
    total = 0.0
    for c in calls:
        price_in, price_out = PRICES.get(c["model"], (0.0, 0.0))
        total += (c["input_tokens"] * price_in + (c["output_tokens"] + c["thought_tokens"]) * price_out) / 1e6
    return total


def judge_progress(results: Path) -> list:
    """Per judge model: runs fully judged, judged with errors, in progress; plus structural metrics."""
    completed_runs = [p.parent for p in results.glob("*/*/rep*/run.json")
                      if (json.loads(p.read_text(encoding="utf-8")) or {}).get("status") == "completed"]
    if not completed_runs:
        return []
    models = sorted({p.stem[len("judge_calls_"):] for p in results.glob("*/*/rep*/judge_calls_*.jsonl")} |
                    {p.stem[len("judge_"):] for p in results.glob("*/*/rep*/judge_*.json")})
    lines = [f"evaluation: structural metrics {sum((d / 'structural.json').exists() for d in completed_runs)}"
             f"/{len(completed_runs)} completed runs"]
    for model in models:
        done = errors = in_progress = 0
        calls = []
        for d in completed_runs:
            calls += read_jsonl(d / f"judge_calls_{model}.jsonl")
            path = d / f"judge_{model}.json"
            if path.exists():
                try:
                    j = json.loads(path.read_text(encoding="utf-8"))
                except json.JSONDecodeError:
                    continue
                if "error" in j or j.get("errors"):
                    errors += 1
                else:
                    done += 1
            elif (d / f"judge_calls_{model}.jsonl").exists():
                in_progress += 1
        retries = sum(c["attempts"] - 1 for c in calls)
        lines.append(f"  judge {model}: {done} done, {in_progress} in progress, {errors} with errors "
                     f"(of {len(completed_runs)} completed runs)  |  {len(calls)} calls, {retries} retries, "
                     f"cost ${cost_of(calls):.2f}")
    return lines


def snapshot(results: Path, planned: int = 0) -> str:
    status = {"completed": 0, "failed": 0, "running": 0}
    running, durations, calls = [], [], []
    for meta_path in sorted(results.glob("*/*/rep*/run.json")):
        run_dir = meta_path.parent
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        status[meta["status"]] = status.get(meta["status"], 0) + 1
        run_calls = read_jsonl(run_dir / "llm_calls.jsonl")
        calls += run_calls
        started = datetime.fromisoformat(meta["started"]).timestamp()
        if meta["status"] == "running":
            now = run_calls[-1]["purpose"].rsplit("|attempt", 1)[0] if run_calls else "starting"
            running.append(f"  running  {meta['condition']} / {meta['brief']} / rep{meta['rep']:02d}: "
                           f"{len(run_calls)} calls, {fmt_duration(time.time() - started)}, now: {now}")
        elif meta.get("finished"):
            durations.append(datetime.fromisoformat(meta["finished"]).timestamp() - started)

    cost = cost_of(calls)
    done = status["completed"] + status["failed"]
    lines = [f"{results}  (updated {time.strftime('%H:%M:%S')})",
             f"runs: {status['completed']} completed, {status['failed']} failed, {status['running']} running"
             + (f"  |  {done}/{planned} = {100 * done / planned:.0f}%" if planned else "")]
    if planned and durations and status["running"]:
        avg = sum(durations) / len(durations)
        left = (planned - done) * avg / max(1, status["running"])
        lines.append(f"average run {fmt_duration(avg)}; estimated time left ~{fmt_duration(left)}")
    lines += running
    lines.append(f"generation API calls: {len(calls)} ({sum(c['attempts'] - 1 for c in calls)} retries)  |  tokens in "
                 f"{sum(c['input_tokens'] for c in calls) / 1e3:.1f}k, out {sum(c['output_tokens'] for c in calls) / 1e3:.1f}k, "
                 f"thinking {sum(c['thought_tokens'] for c in calls) / 1e3:.1f}k  |  estimated cost ${cost:.2f}")
    failed = [p.parent for p in results.glob("*/*/rep*/run.json")
              if json.loads(p.read_text(encoding="utf-8")).get("status") == "failed"]
    for f in failed[:5]:
        lines.append(f"  failed   {f.relative_to(results)}: {json.loads((f / 'run.json').read_text())['error'][:120]}")
    lines += judge_progress(results)
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("results")
    ap.add_argument("--watch", type=int, help="refresh every N seconds")
    ap.add_argument("--planned", type=int, default=0, help="total number of runs in the batch")
    args = ap.parse_args()
    if not args.watch:
        print(snapshot(Path(args.results), args.planned))
        return
    try:
        while True:
            print("\033[2J\033[H" + snapshot(Path(args.results), args.planned), flush=True)
            time.sleep(args.watch)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
