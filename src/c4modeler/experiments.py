# src/experiments.py
from __future__ import annotations

import json
import re
import uuid
from datetime import datetime
from typing import Any, Dict, List

from langgraph.checkpoint.memory import InMemorySaver

from .graph import create_c4_modeler_graph
from .types import State
from .utils import (
    save_c4_artifacts,
    save_all_evaluation_reports,
    format_evaluation_report,   # if you don’t have this yet, a minimal fallback is below
    zip_folder_with_increment,
)
from .evaluation import run_full_evaluation

# --- Brief loaders (read YAML files as raw strings) --------------------------
from pathlib import Path

def load_briefs_from_dir(briefs_dir: str | Path) -> Dict[str, str]:
    """
    Scans `briefs_dir` for .yaml/.yml files and returns a dict:
      { "<brief_name>": "<raw YAML content as string>", ... }
    The brief_name is the filename without extension.
    """
    briefs: Dict[str, str] = {}
    p = Path(briefs_dir)
    if not p.exists() or not p.is_dir():
        print(f"⚠️ briefs dir not found: {p.resolve()}")
        return briefs

    for fp in sorted(p.glob("*.yml")) + sorted(p.glob("*.yaml")):
        try:
            text = fp.read_text(encoding="utf-8").strip()
            if not text:
                print(f"⚠️ Skipping empty brief: {fp.name}")
                continue
            briefs[fp.stem] = text
        except Exception as e:
            print(f"⚠️ Failed to read {fp}: {e}")
    return briefs


def load_single_brief(path: str | Path) -> Dict[str, str]:
    """
    Convenience: load a single YAML brief file and return {stem: raw_text}.
    """
    fp = Path(path)
    return {fp.stem: fp.read_text(encoding="utf-8").strip()}


# ---------------------------------------------------------------------------
# A. Build + run one experiment (compatible with your notebook’s flow)
# ---------------------------------------------------------------------------

def _initial_state(brief_str: str) -> State:
    """Initial state for the LangGraph app."""
    return {
        "messages": [],
        "system_brief": brief_str,
        "c4_model": {"context": {}, "containers": {}, "components": {}},
        # IMPORTANT: set to None so the router can populate the queue later
        "component_queue": None,
    }

def run_all_experiments(
    app_instance,
    system_briefs_data: Dict[str, str]
) -> List[Dict[str, Any]]:
    """
    Runs the LangGraph C4 model generation for each system brief (verbatim
    behavior from your notebook), and collects results.
    """
    experiment_results: List[Dict[str, Any]] = []
    print("\n--- 🚀 Starting C4 Model Generation Experiments ---")

    for brief_name, system_brief_content in system_briefs_data.items():
        print(f"\n\n{'='*80}")
        print(f"--- Processing: {brief_name} ---")
        print(f"{'='*80}\n")

        initial_state = _initial_state(system_brief_content)

        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        brief_name_slug = re.sub(r'[^a-zA-Z0-9-]', '', brief_name.replace(" ", "-").lower())
        current_thread_id = f"{timestamp}-{brief_name_slug}-{uuid.uuid4().hex[:8]}"
        config = {"configurable": {"thread_id": current_thread_id}, "recursion_limit": 200}

        print(f"\n--- LangGraph Thread ID: {current_thread_id} ---")

        # Stream execution (prints node names as in your notebook)
        for event in app_instance.stream(initial_state, config):
            print("\n" + "="*40)
            print(f"Node: {list(event.keys())[0]}")
            print("="*40)

        final_state_snapshot = app_instance.get_state(config)
        final_c4_model = final_state_snapshot.values["c4_model"]

        experiment_results.append({
            "brief_name": brief_name,
            "thread_id": current_thread_id,
            "system_brief_content": system_brief_content,
            "final_c4_model": final_c4_model,
        })

        print(f"\n--- 🎉 C4 Model Generation Complete for {brief_name}! ---")
        print(f"Final state for thread '{current_thread_id}' retrieved and stored.")

    print("\n\n--- ✅ All C4 Model Generation Experiments Complete! ---")
    return experiment_results


def build_app_from_config(
    model_name: str,
    analysis_method: str,
    collab_rounds: int | None
):
    """
    Builds a LangGraph app exactly like your notebook did, using your graph factory.
    """
    checkpointer = InMemorySaver()
    app = create_c4_modeler_graph(
        checkpointer=checkpointer,
        model_name=model_name,
        analysis_method=analysis_method,       # "simple" | "collaborative"
        collab_rounds=collab_rounds or 2,      # default when None
    )
    return app


# ---------------------------------------------------------------------------
# B. Evaluate everything (compatible with your notebook’s loop)
# ---------------------------------------------------------------------------

def run_all_evaluations(
    experiment_results: List[Dict[str, Any]],
    experiment_config: Dict[str, Any],
    save_c4_artifacts_func=save_c4_artifacts,
    run_full_evaluation_func=run_full_evaluation,
    save_all_evaluation_reports_func=save_all_evaluation_reports,
    format_evaluation_report_func=format_evaluation_report,
    judge_model_name: str = "gemini-2.5-flash-preview-05-20",
) -> Dict[str, Any]:
    """
    Loops over one experiment’s runs, saves artifacts, evaluates, aggregates, and returns a summary.
    """
    print("\n" + "="*60)
    print(f"🔬 Running Evaluations (Judge: {judge_model_name}) for experiment: {experiment_config.get('name')}")
    print("="*60)

    all_reports: Dict[str, Dict[str, Any]] = {}   # thread_id -> full evaluation report
    summaries: Dict[str, Any] = {}                # thread_id -> summarized view (pretty)

    for run in experiment_results:
        brief_name = run["brief_name"]
        thread_id = run["thread_id"]
        brief_text = run["system_brief_content"]
        c4_model = run["final_c4_model"]

        print(f"\n--- Evaluating: {brief_name} (thread {thread_id}) ---")

        # 1) Save artifacts for inspection
        out_dir = f"data/results/{experiment_config.get('name')}/{thread_id}"
        save_c4_artifacts_func(out_dir, c4_model)

        # 2) Run the full evaluation (compilation, abstraction, cross-level, judge-based, etc.)
        report = run_full_evaluation_func(
            system_brief=brief_text,
            c4_model=c4_model,
            judge_model_name=judge_model_name,
            temperature=0.0,
        )

        all_reports[thread_id] = report

        # 3) Produce a concise human-readable summary (if you have one)
        try:
            summaries[thread_id] = format_evaluation_report_func(report)
        except Exception:
            # Fallback: keep the raw report if no formatter is available
            summaries[thread_id] = {
                "note": "No formatter available; returning full report.",
                "report": report,
            }

    # 4) Save a consolidated JSON for this experiment
    save_all_evaluation_reports_func(
        all_reports,
        output_filename=f"{experiment_config.get('name')}_evaluation_summary.json",
        output_dir=f"data/results/{experiment_config.get('name')}/evaluation_summaries",
    )

    print("\n--- Creating zip of evaluation results folder for convenience ---")
    zip_folder_with_increment(f"data/results/{experiment_config.get('name')}")

    return {
        "experiment": experiment_config,
        "summaries": summaries,
        "rawReports": all_reports,
    }


# ---------------------------------------------------------------------------
# C. Optional: tiny fallback for format_evaluation_report if you don’t have one
# ---------------------------------------------------------------------------

def _fallback_format_evaluation_report(report: Dict[str, Any]) -> Dict[str, Any]:
    """
    Minimal summary if utils.format_evaluation_report is not implemented.
    """
    meta = report.get("evaluationMetadata", {})
    quick = {
        "judge": meta.get("judgeModel"),
        "timestamp": meta.get("evaluationTimestamp"),
        "compilation": report.get("compilationSuccess", {}).get("score"),
        "abstraction": report.get("abstractionAdherence", {}).get("score"),
        "completeness": report.get("missingInformation", {}).get("score"),
        "naming": report.get("emergentNamingConsistency", {}).get("score"),
        "crossLevel": report.get("crossLevelConsistency", {}).get("score"),
    }
    return quick

# If format_evaluation_report is missing, monkey-patch the fallback
try:
    format_evaluation_report  # noqa: F401
except NameError:  # pragma: no cover
    format_evaluation_report = _fallback_format_evaluation_report


