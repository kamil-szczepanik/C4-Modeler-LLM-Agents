# src/experiments.py
from __future__ import annotations

import json
import re
import uuid
import time
from datetime import datetime
from typing import Any, Dict, List, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

from langgraph.checkpoint.memory import InMemorySaver

from .graph import create_c4_modeler_graph
from .types import State
from .utils import (
    save_c4_artifacts,
    save_all_evaluation_reports,
    format_evaluation_report,   # if you don't have this yet, a minimal fallback is below
    zip_folder_with_increment,
    load_c4_model_from_artifacts,  # For recovery from saved artifacts
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
        config = {"configurable": {"thread_id": current_thread_id}, "recursion_limit": 400}

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
    collab_rounds: int | None,
    temperature: float = 0.5
):
    """
    Builds a LangGraph app exactly like your notebook did, using your graph factory.
    
    Args:
        model_name: LLM model to use
        analysis_method: "simple" | "collaborative"
        collab_rounds: Number of collaboration rounds (default 2 if None)
        temperature: LLM temperature for controlling randomness (default 0.5)
    """
    checkpointer = InMemorySaver()
    app = create_c4_modeler_graph(
        checkpointer=checkpointer,
        model_name=model_name,
        analysis_method=analysis_method,       # "simple" | "collaborative"
        collab_rounds=collab_rounds or 2,      # default when None
        temperature=temperature,
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
    judge_model_name: str = "gemini-2.5-pro",
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


# ==============================================================================
# ENHANCED EXPERIMENTS FOR JOURNAL EXTENSION
# ==============================================================================

import yaml
from .evaluation import run_enhanced_evaluation_only
from .integration import (
    create_experimental_pipeline,
    extract_c4_model_from_result,
    validate_experiment_condition,
    create_memory_config_from_condition
)

def load_experiment_config(config_path: str = "experiment_configs.yaml") -> Dict[str, Any]:
    """Load the experiment configuration from YAML file."""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"⚠️ Experiment config not found: {config_path}")
        return {}

class EnhancedExperimentRunner:
    """
    Runner for the enhanced experiments defined in the journal extension.
    Handles role ablation, interaction order, specialization, memory, and diversity studies.
    """
    
    def __init__(self, config_path: str = "experiment_configs.yaml"):
        self.config = load_experiment_config(config_path)
        self.briefs = {}
        self.results = {}
    
    def load_system_briefs(self, briefs_dir: str = "data/briefs"):
        """Load all system briefs for experiments."""
        self.briefs = load_briefs_from_dir(briefs_dir)
        print(f"📚 Loaded {len(self.briefs)} system briefs: {list(self.briefs.keys())}")
    
    def recover_artifacts_from_run(self, run_id: str, experiment_name: str) -> Dict[str, Any]:
        """
        Recover C4 model artifacts from a previously saved run.
        
        Args:
            run_id: The unique run identifier
            experiment_name: Name of the experiment
        
        Returns:
            Recovered C4 model or None if not found
        """
        artifact_dir = Path(f"data/results/enhanced_experiments/{experiment_name}/c4_artifacts/{run_id}")
        
        if not artifact_dir.exists():
            print(f"⚠️ Artifact directory not found: {artifact_dir}")
            return None
        
        try:
            c4_model = load_c4_model_from_artifacts(artifact_dir)
            print(f"✅ Recovered C4 model from: {artifact_dir}")
            return c4_model
        except Exception as e:
            print(f"❌ Failed to recover artifacts: {str(e)}")
            return None
    
    def list_available_artifacts(self, experiment_name: str) -> List[str]:
        """
        List all available artifact directories for an experiment.
        
        Args:
            experiment_name: Name of the experiment
        
        Returns:
            List of run IDs with saved artifacts
        """
        artifacts_base = Path(f"data/results/enhanced_experiments/{experiment_name}/c4_artifacts")
        
        if not artifacts_base.exists():
            print(f"ℹ️ No artifacts directory found for experiment: {experiment_name}")
            return []
        
        run_ids = [d.name for d in artifacts_base.iterdir() if d.is_dir()]
        print(f"📂 Found {len(run_ids)} saved artifact sets for {experiment_name}")
        
        return run_ids
    
    def run_experiment(self, experiment_name: str, model_name: str = "gpt-4o-mini", 
                      max_workers: int = 2, temperature: float = 0.5) -> Dict[str, Any]:
        """
        Run a specific enhanced experiment by name.
        
        Args:
            experiment_name: Name of experiment from config (e.g., 'role_ablation')
            model_name: LLM model to use for generation and evaluation
            max_workers: Maximum number of conditions to run in parallel (default: 2)
            temperature: LLM temperature for controlling randomness (default: 0.5)
        
        Returns:
            Dictionary containing experiment results and analysis
        """
        if experiment_name not in self.config.get("experiments", {}):
            raise ValueError(f"Experiment '{experiment_name}' not found in config")
        
        experiment_config = self.config["experiments"][experiment_name]
        protocol = self.config.get("protocol", {})
        
        print(f"\n🧪 Starting Enhanced Experiment: {experiment_config['name']}")
        print(f"📋 Description: {experiment_config['description']}")
        print(f"🎯 Purpose: {experiment_config['purpose']}")
        print(f"⚙️ Parallel conditions: {max_workers}")
        
        results = {
            "experiment_metadata": {
                "name": experiment_config["name"],
                "description": experiment_config["description"],
                "purpose": experiment_config["purpose"],
                "timestamp": datetime.now().isoformat(),
                "model_name": model_name,
                "temperature": temperature,
                "max_parallel_conditions": max_workers
            },
            "conditions": {},
            "aggregate_results": {},
            "statistical_analysis": {}
        }
        
        # Run experimental conditions in parallel using ThreadPoolExecutor
        conditions_list = experiment_config["conditions"]
        total_conditions = len(conditions_list)
        
        print(f"\n� Running {total_conditions} conditions with max {max_workers} parallel workers")
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all condition tasks
            future_to_condition = {
                executor.submit(
                    self._run_condition,
                    condition,
                    experiment_config,
                    protocol,
                    model_name,
                    temperature
                ): (idx, condition)
                for idx, condition in enumerate(conditions_list, 1)
            }
            
            # Process results as they complete
            completed_count = 0
            for future in as_completed(future_to_condition):
                condition_idx, condition = future_to_condition[future]
                condition_id = condition["id"]
                completed_count += 1
                
                try:
                    condition_results = future.result()
                    results["conditions"][condition_id] = condition_results
                    
                    print(f"\n✅ [{completed_count}/{total_conditions}] Completed condition: {condition['name']}")
                    
                    # 💾 SAVE INTERMEDIATE RESULTS after each condition completes
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    intermediate_file = f"data/results/enhanced_experiments/{experiment_name}_progress_condition_{completed_count}_{timestamp}.json"
                    
                    Path(intermediate_file).parent.mkdir(parents=True, exist_ok=True)
                    
                    with open(intermediate_file, 'w', encoding='utf-8') as f:
                        json.dump(results, f, indent=2, ensure_ascii=False)
                    
                    print(f"    💾 Progress checkpoint saved: {Path(intermediate_file).name}")
                    
                except Exception as e:
                    print(f"\n❌ [{completed_count}/{total_conditions}] Failed condition {condition['name']}: {str(e)}")
                    results["conditions"][condition_id] = {
                        "condition_metadata": condition,
                        "error": str(e),
                        "status": "failed"
                    }
        
        print(f"\n🎯 All {total_conditions} conditions completed!")
        
        # Perform aggregate analysis
        results["aggregate_results"] = self._analyze_experiment_results(
            results["conditions"],
            experiment_config["metrics_focus"]
        )
        
        # Save final results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_file = f"data/results/enhanced_experiments/{experiment_name}_final_{timestamp}.json"
        
        # Ensure directory exists
        Path(results_file).parent.mkdir(parents=True, exist_ok=True)
        
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Experiment complete! Final results saved to: {results_file}")
        
        return results
    
    def _run_condition(self, condition: Dict[str, Any], experiment_config: Dict[str, Any], 
                      protocol: Dict[str, Any], model_name: str, temperature: float = 0.5) -> Dict[str, Any]:
        """
        Run a single experimental condition across all briefs and rounds.
        
        Args:
            condition: Experimental condition configuration
            experiment_config: Overall experiment configuration
            protocol: Experimental protocol (datasets, rounds, etc.)
            model_name: LLM model to use
            temperature: LLM temperature for controlling randomness (default 0.5)
        """
        
        condition_results = {
            "condition_metadata": condition,
            "brief_results": {},
            "condition_summary": {},
            "artifact_locations": {}  # Track where artifacts are saved
        }
        
        datasets = protocol.get("datasets", list(self.briefs.keys()))
        rounds = protocol.get("rounds_per_condition", 3)
        
        # Create base directory for this condition's artifacts
        experiment_name = experiment_config.get("name", "unknown_experiment").replace(" ", "_")
        condition_id = condition.get("id", "unknown_condition")
        
        # Pre-scan to see what exists (for user visibility)
        total_runs = len(datasets) * rounds
        existing_runs = 0
        
        print(f"\n🔍 Checking for existing artifacts...")
        for brief_name in datasets:
            for round_num in range(1, rounds + 1):
                if self._find_existing_artifact(experiment_name, brief_name, condition_id, round_num):
                    existing_runs += 1
        
        if existing_runs > 0:
            print(f"   ✅ Found {existing_runs}/{total_runs} completed runs")
            print(f"   🔄 Will run {total_runs - existing_runs} new runs")
        else:
            print(f"   🆕 No existing runs found, will run all {total_runs} runs")
        
        for brief_name in datasets:
            if brief_name not in self.briefs:
                print(f"⚠️ Brief '{brief_name}' not found, skipping")
                continue
            
            brief_results = []
            
            for round_num in range(1, rounds + 1):
                print(f"  📝 {brief_name} - Round {round_num}")
                
                # Check if this run already exists (for resume capability)
                existing_artifact = self._find_existing_artifact(
                    experiment_name, brief_name, condition_id, round_num
                )
                
                if existing_artifact:
                    print(f"    ✅ Found existing artifacts, loading from: {existing_artifact}")
                    
                    try:
                        # Load C4 model from existing artifacts
                        c4_model = load_c4_model_from_artifacts(existing_artifact)
                        
                        # Check if it's an error model (contains "# Error:" in definitions)
                        is_error = any("# Error:" in str(v) for v in c4_model.get("context", {}).values())
                        
                        if is_error:
                            print(f"    ⚠️ Existing artifacts contain errors, re-running...")
                        else:
                            # Valid existing run - use it and skip generation
                            evaluation = run_enhanced_evaluation_only(
                                self.briefs[brief_name],
                                c4_model
                            )
                            
                            round_result = {
                                "round": round_num,
                                "brief_name": brief_name,
                                "condition_id": condition["id"],
                                "run_id": Path(existing_artifact).name,
                                "artifact_path": existing_artifact,
                                "c4_model": c4_model,
                                "evaluation": evaluation,
                                "timestamp": datetime.now().isoformat(),
                                "resumed_from_artifacts": True
                            }
                            
                            brief_results.append(round_result)
                            condition_results["artifact_locations"][Path(existing_artifact).name] = existing_artifact
                            
                            print(f"    ⏭️ Skipped (already completed)")
                            continue  # Skip to next round
                            
                    except Exception as e:
                        print(f"    ⚠️ Failed to load existing artifacts: {str(e)}, re-running...")
                
                # Generate new C4 model (either no existing artifacts or they were invalid)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                run_id = f"{brief_name}_{condition_id}_r{round_num}_{timestamp}"
                artifact_dir = Path(f"data/results/enhanced_experiments/{experiment_name}/c4_artifacts/{run_id}")
                
                # Generate C4 model with condition-specific configuration
                c4_model = self._generate_c4_with_condition(
                    self.briefs[brief_name],
                    condition,
                    model_name,
                    temperature
                )
                
                # ✨ SAVE C4 ARTIFACTS IMMEDIATELY after generation
                try:
                    artifact_dir.mkdir(parents=True, exist_ok=True)
                    save_c4_artifacts(artifact_dir, c4_model)
                    # Use string representation to avoid Path.relative_to() issues with mixed path types
                    print(f"    💾 Saved C4 artifacts to: {artifact_dir}")
                    artifact_path = str(artifact_dir.absolute())
                except Exception as e:
                    print(f"    ⚠️ Failed to save C4 artifacts: {str(e)}")
                    artifact_path = None
                
                # Evaluate using enhanced metrics
                evaluation = run_enhanced_evaluation_only(
                    self.briefs[brief_name],
                    c4_model
                )
                
                round_result = {
                    "round": round_num,
                    "brief_name": brief_name,
                    "condition_id": condition["id"],
                    "run_id": run_id,
                    "artifact_path": artifact_path,  # Store location for recovery
                    "c4_model": c4_model,
                    "evaluation": evaluation,
                    "timestamp": datetime.now().isoformat()
                }
                
                brief_results.append(round_result)
                
                # Track artifact location
                if artifact_path:
                    condition_results["artifact_locations"][run_id] = artifact_path
            
            condition_results["brief_results"][brief_name] = brief_results
        
        # Calculate condition summary
        condition_results["condition_summary"] = self._summarize_condition(
            condition_results["brief_results"],
            experiment_config["metrics_focus"]
        )
        
        return condition_results
    
    def _generate_c4_with_condition(self, system_brief: str, condition: Dict[str, Any], 
                                   model_name: str, temperature: float = 0.5) -> Dict[str, Any]:
        """
        Generate C4 model with condition-specific agent configuration.
        Uses the integration utilities for clean pipeline execution.
        
        Args:
            system_brief: The system description to model
            condition: Experimental condition configuration
            model_name: LLM model to use
            temperature: LLM temperature for controlling randomness (default 0.5)
        """
        
        # Validate the condition first
        validation_errors = validate_experiment_condition(condition)
        if validation_errors:
            print(f"    ⚠️ Condition validation errors: {validation_errors}")
            return self._create_error_model(f"Validation failed: {validation_errors}")
        
        # Extract condition parameters
        roles = condition.get("roles", ["Architect"])
        speaking_order = condition.get("speaking_order", roles)
        memory_type = condition.get("memory_type", "none")
        role_specificity = condition.get("role_specificity", "generic")
        
        print(f"    🤖 Generating with roles: {roles}")
        print(f"    🗣️ Speaking order: {speaking_order}")
        print(f"    🧠 Memory type: {memory_type}")
        print(f"    🎭 Role specificity: {role_specificity}")
        
        # Create experimental configuration
        experiment_condition = {
            "roles": roles,
            "speaking_order": speaking_order,
            "memory_type": memory_type,
            "role_specificity": role_specificity
        }
        
        # Create memory configuration
        memory_config = create_memory_config_from_condition(condition)
        
        # Run the experimental pipeline with retry logic for transient API errors
        max_retries = 3
        retry_delay = 5  # seconds
        
        for attempt in range(1, max_retries + 1):
            try:
                result = create_experimental_pipeline(
                    system_brief=system_brief,
                    model_name=model_name,
                    experiment_condition=experiment_condition,
                    memory_config=memory_config,
                    temperature=temperature
                )
                
                # Extract C4 model from the result
                if "error" in result:
                    # Check if it's a retryable error (500 Internal Server Error)
                    error_msg = result["error"]
                    if "500" in str(error_msg) or "Internal" in str(error_msg):
                        if attempt < max_retries:
                            wait_time = retry_delay * attempt  # Exponential backoff
                            print(f"    ⚠️ Transient API error (attempt {attempt}/{max_retries}), retrying in {wait_time}s...")
                            time.sleep(wait_time)
                            continue
                    return self._create_error_model(result["error"])
                
                c4_model = extract_c4_model_from_result(result)
                
                # Success! Log if this was a retry
                if attempt > 1:
                    print(f"    ✅ Succeeded on retry attempt {attempt}")
                
                return c4_model
                
            except Exception as e:
                error_str = str(e)
                # Check if it's a retryable error (Google API 500, rate limits, etc.)
                is_retryable = any(keyword in error_str for keyword in [
                    "500", "Internal", "internal error", 
                    "rate limit", "quota", "temporarily unavailable"
                ])
                
                if is_retryable and attempt < max_retries:
                    wait_time = retry_delay * attempt  # Exponential backoff
                    print(f"    ⚠️ Transient error (attempt {attempt}/{max_retries}): {error_str[:100]}")
                    print(f"    🔄 Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                    continue
                else:
                    print(f"    ❌ Error generating C4 model (attempt {attempt}): {error_str}")
                    return self._create_error_model(error_str)
        
        # If we exhausted all retries
        return self._create_error_model(f"Failed after {max_retries} attempts")
    
    def _find_existing_artifact(self, experiment_name: str, brief_name: str, 
                               condition_id: str, round_num: int) -> Optional[str]:
        """
        Find existing artifact directory for a specific run.
        Returns the directory path if found, None otherwise.
        
        Args:
            experiment_name: Name of the experiment (e.g., "Role_Ablation_Study")
            brief_name: Name of the brief (e.g., "clinic-management-system")
            condition_id: Condition ID (e.g., "baseline", "architect_only")
            round_num: Round number (1, 2, 3, etc.)
        """
        # Look for artifact directories matching this run
        artifact_base = Path(f"data/results/enhanced_experiments/{experiment_name}/c4_artifacts")
        
        if not artifact_base.exists():
            return None
        
        # Pattern: {brief_name}_{condition_id}_r{round_num}_*
        pattern = f"{brief_name}_{condition_id}_r{round_num}_*"
        
        matching_dirs = list(artifact_base.glob(pattern))
        
        if matching_dirs:
            # Return the most recent one (sorted by name, which includes timestamp)
            most_recent = sorted(matching_dirs)[-1]
            
            # Verify it has the required files
            required_files = [
                "1_context_definition.yaml",
                "2_container_definition.yaml"
            ]
            
            if all((most_recent / f).exists() for f in required_files):
                return str(most_recent.absolute())
        
        return None
    
    def _create_error_model(self, error_message: str) -> Dict[str, Any]:
        """Create a minimal error model structure."""
        return {
            "context": {
                "yaml_definition": f"# Error: {error_message}",
                "diagram": f"# Error: {error_message}"
            },
            "containers": {
                "yaml_definition": f"# Error: {error_message}",
                "diagram": f"# Error: {error_message}"
            },
            "components": {}
        }
    
    def _summarize_condition(self, brief_results: Dict[str, List[Dict]], 
                           metrics_focus: List[str]) -> Dict[str, Any]:
        """Calculate summary statistics for a condition across all briefs and rounds."""
        
        summary = {
            "total_runs": 0,
            "metrics": {},
            "averages": {},
            "std_deviations": {}
        }
        
        # Collect all metric values
        metric_values = {}
        
        for brief_name, rounds in brief_results.items():
            for round_result in rounds:
                summary["total_runs"] += 1
                evaluation = round_result["evaluation"]
                
                # Extract ISO 25010 scores
                iso_scores = evaluation.get("iso25010Attributes", {}).get("scores", {})
                for attr, score in iso_scores.items():
                    metric_key = f"iso_{attr}"
                    if metric_key not in metric_values:
                        metric_values[metric_key] = []
                    metric_values[metric_key].append(score)
                
                # Extract ATAM scores
                atam_data = evaluation.get("atamScenarios", {})
                overall_resp = atam_data.get("overall_responsiveness", 0)
                metric_values.setdefault("atam_responsiveness", []).append(overall_resp)
                
                # Extract soundness metrics
                soundness = evaluation.get("architecturalSoundness", {})
                for metric in ["coupling_density", "abstraction_coherence", "semantic_completeness"]:
                    value = soundness.get(metric, 0)
                    metric_values.setdefault(f"soundness_{metric}", []).append(value)
        
        # Calculate statistics
        import statistics
        for metric, values in metric_values.items():
            if values:
                summary["averages"][metric] = round(statistics.mean(values), 3)
                if len(values) > 1:
                    summary["std_deviations"][metric] = round(statistics.stdev(values), 3)
                else:
                    summary["std_deviations"][metric] = 0.0
        
        summary["metrics"] = metric_values
        
        return summary
    
    def _analyze_experiment_results(self, conditions: Dict[str, Any], 
                                  metrics_focus: List[str]) -> Dict[str, Any]:
        """Perform statistical analysis across experimental conditions."""
        
        analysis = {
            "condition_comparison": {},
            "effect_sizes": {},
            "statistical_tests": {},
            "key_findings": []
        }
        
        # Compare conditions on focused metrics
        condition_names = list(conditions.keys())
        
        for metric in metrics_focus:
            metric_comparison = {}
            
            for condition_id, condition_data in conditions.items():
                summary = condition_data["condition_summary"]
                
                # Map metric focus to actual metric names
                actual_metric = self._map_focus_metric_to_actual(metric)
                
                if actual_metric in summary["averages"]:
                    metric_comparison[condition_id] = {
                        "mean": summary["averages"][actual_metric],
                        "std": summary["std_deviations"].get(actual_metric, 0),
                        "n": summary["total_runs"]
                    }
            
            analysis["condition_comparison"][metric] = metric_comparison
            
            # Calculate effect sizes (simplified)
            if len(metric_comparison) >= 2:
                conditions_list = list(metric_comparison.items())
                baseline = conditions_list[0][1]["mean"]
                
                for condition_id, stats in conditions_list[1:]:
                    effect_size = abs(stats["mean"] - baseline) / max(stats["std"], 0.1)
                    analysis["effect_sizes"][f"{metric}_{condition_id}_vs_baseline"] = round(effect_size, 3)
        
        return analysis
    
    def _map_focus_metric_to_actual(self, focus_metric: str) -> str:
        """Map experiment focus metrics to actual evaluation metric names."""
        mapping = {
            "ISO_Functional_Suitability": "iso_functional_suitability",
            "ISO_Security": "iso_security", 
            "ISO_Maintainability": "iso_maintainability",
            "ATAM_Scenario_Responsiveness": "atam_responsiveness",
            "Coupling_Density": "soundness_coupling_density",
            "Semantic_Completeness": "soundness_semantic_completeness",
            "Abstraction_Coherence": "soundness_abstraction_coherence"
        }
        return mapping.get(focus_metric, focus_metric.lower())
    
    def run_all_experiments(self, model_name: str = "gpt-4o-mini") -> Dict[str, Any]:
        """Run all defined experiments."""
        
        print("🚀 Starting All Enhanced Experiments")
        
        if not self.briefs:
            self.load_system_briefs()
        
        all_results = {
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "model_name": model_name,
                "total_experiments": len(self.config.get("experiments", {}))
            },
            "experiments": {}
        }
        
        for exp_name in self.config.get("experiments", {}):
            print(f"\n{'='*60}")
            print(f"Starting Experiment: {exp_name}")
            print(f"{'='*60}")
            
            try:
                result = self.run_experiment(exp_name, model_name)
                all_results["experiments"][exp_name] = result
                print(f"✅ Completed: {exp_name}")
            except Exception as e:
                print(f"❌ Failed: {exp_name} - {str(e)}")
                all_results["experiments"][exp_name] = {"error": str(e)}
        
        # Save comprehensive results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_file = f"data/results/enhanced_experiments/all_experiments_{timestamp}.json"
        
        Path(results_file).parent.mkdir(parents=True, exist_ok=True)
        
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump(all_results, f, indent=2)
        
        print(f"\n🎉 All experiments completed! Results saved to: {results_file}")
        
        return all_results


