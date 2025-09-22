# src/pipeline.py
from __future__ import annotations

from collections import deque
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

from .types import State, C4Model
from .utils import ensure_dir, sanitize_filename, save_c4_artifacts, load_yaml
from .graph import create_c4_modeler_graph
from .llm import ModelName

def _empty_c4_model() -> C4Model:
    return {"context": {}, "containers": {}, "components": {}}

def _initial_state(brief_str: str) -> State:
    return {
        "messages": [],
        "system_brief": brief_str,
        "c4_model": _empty_c4_model(),
        "component_queue": None,  # was: deque()
    }


def generate_c4_for_brief(
    brief: Dict[str, Any] | str,
    model_name: ModelName = "gemini-1.5-flash-latest",
    analysis_method: str = "collaborative",
    collab_rounds: int = 2,
    results_dir: str | Path = "data/results",
    result_name: Optional[str] = None,
    checkpointer=None,
) -> Tuple[C4Model, Path]:
    """
    Run the full workflow for a single brief and save artifacts.
    """
    if isinstance(brief, str):
        brief_str = brief
        brief_dict: Dict[str, Any] = {}
    else:
        import yaml as _yaml
        brief_dict = brief
        brief_str = _yaml.safe_dump(brief_dict, sort_keys=False)

    title = brief_dict.get("title") or brief_dict.get("name") or result_name or "run"
    out_path = ensure_dir(Path(results_dir) / sanitize_filename(title))

    app = create_c4_modeler_graph(
        checkpointer=checkpointer,
        model_name=model_name,
        analysis_method=analysis_method,  # "simple" | "collaborative"
        collab_rounds=collab_rounds,
    )

    state: State = _initial_state(brief_str)
    config = {"recursion_limit": 200}
    final_state: State = app.invoke(state, config)

    c4_model: C4Model = final_state["c4_model"]
    save_c4_artifacts(out_path, c4_model)
    return c4_model, out_path

def generate_c4_for_briefs_dir(
    briefs_dir: str | Path,
    model_name: ModelName = "gemini-1.5-flash-latest",
    analysis_method: str = "collaborative",
    collab_rounds: int = 2,
    results_dir: str | Path = "data/results",
    pattern: str = "*.yaml",
    checkpointer=None,
) -> Dict[str, Path]:
    """
    Batch: iterate briefs in a directory and generate outputs.
    """
    briefs_dir = Path(briefs_dir)
    outputs: Dict[str, Path] = {}

    for brief_file in sorted(briefs_dir.glob(pattern)):
        brief = load_yaml(brief_file)
        if not brief:
            print(f"Skipping (could not load): {brief_file}")
            continue
        print(f"\n=== Running brief: {brief_file.name} ===")
        _, out_path = generate_c4_for_brief(
            brief,
            model_name=model_name,
            analysis_method=analysis_method,
            collab_rounds=collab_rounds,
            results_dir=results_dir,
            checkpointer=checkpointer,
        )
        outputs[brief_file.name] = out_path

    return outputs
