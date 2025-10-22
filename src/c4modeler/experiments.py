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
    
    def run_experiment(self, experiment_name: str, model_name: str = "gpt-4o-mini") -> Dict[str, Any]:
        """
        Run a specific enhanced experiment by name.
        
        Args:
            experiment_name: Name of experiment from config (e.g., 'role_ablation')
            model_name: LLM model to use for generation and evaluation
        
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
        
        results = {
            "experiment_metadata": {
                "name": experiment_config["name"],
                "description": experiment_config["description"],
                "purpose": experiment_config["purpose"],
                "timestamp": datetime.now().isoformat(),
                "model_name": model_name
            },
            "conditions": {},
            "aggregate_results": {},
            "statistical_analysis": {}
        }
        
        # Run each experimental condition
        for condition in experiment_config["conditions"]:
            condition_id = condition["id"]
            print(f"\n🔬 Running condition: {condition['name']}")
            
            condition_results = self._run_condition(
                condition, 
                experiment_config,
                protocol,
                model_name
            )
            
            results["conditions"][condition_id] = condition_results
        
        # Perform aggregate analysis
        results["aggregate_results"] = self._analyze_experiment_results(
            results["conditions"],
            experiment_config["metrics_focus"]
        )
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_file = f"data/results/enhanced_experiments/{experiment_name}_{timestamp}.json"
        
        # Ensure directory exists
        Path(results_file).parent.mkdir(parents=True, exist_ok=True)
        
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
        
        print(f"💾 Experiment results saved to: {results_file}")
        
        return results
    
    def _run_condition(self, condition: Dict[str, Any], experiment_config: Dict[str, Any], 
                      protocol: Dict[str, Any], model_name: str) -> Dict[str, Any]:
        """Run a single experimental condition across all briefs and rounds."""
        
        condition_results = {
            "condition_metadata": condition,
            "brief_results": {},
            "condition_summary": {}
        }
        
        datasets = protocol.get("datasets", list(self.briefs.keys()))
        rounds = protocol.get("rounds_per_condition", 3)
        
        for brief_name in datasets:
            if brief_name not in self.briefs:
                print(f"⚠️ Brief '{brief_name}' not found, skipping")
                continue
            
            brief_results = []
            
            for round_num in range(1, rounds + 1):
                print(f"  📝 {brief_name} - Round {round_num}")
                
                # Generate C4 model with condition-specific configuration
                c4_model = self._generate_c4_with_condition(
                    self.briefs[brief_name],
                    condition,
                    model_name
                )
                
                # Evaluate using enhanced metrics
                evaluation = run_enhanced_evaluation_only(
                    self.briefs[brief_name],
                    c4_model
                )
                
                round_result = {
                    "round": round_num,
                    "brief_name": brief_name,
                    "condition_id": condition["id"],
                    "c4_model": c4_model,
                    "evaluation": evaluation,
                    "timestamp": datetime.now().isoformat()
                }
                
                brief_results.append(round_result)
            
            condition_results["brief_results"][brief_name] = brief_results
        
        # Calculate condition summary
        condition_results["condition_summary"] = self._summarize_condition(
            condition_results["brief_results"],
            experiment_config["metrics_focus"]
        )
        
        return condition_results
    
    def _generate_c4_with_condition(self, system_brief: str, condition: Dict[str, Any], 
                                   model_name: str) -> Dict[str, Any]:
        """
        Generate C4 model with condition-specific agent configuration.
        Uses the integration utilities for clean pipeline execution.
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
        
        # Run the experimental pipeline
        try:
            result = create_experimental_pipeline(
                system_brief=system_brief,
                model_name=model_name,
                experiment_condition=experiment_condition,
                memory_config=memory_config
            )
            
            # Extract C4 model from the result
            if "error" in result:
                return self._create_error_model(result["error"])
            
            c4_model = extract_c4_model_from_result(result)
            return c4_model
            
        except Exception as e:
            print(f"    ❌ Error generating C4 model: {str(e)}")
            return self._create_error_model(str(e))
    
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


