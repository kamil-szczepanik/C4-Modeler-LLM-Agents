"""
Integration utilities for the experimental configuration system.
Provides helper functions to bridge between experiments and the core pipeline.
"""

from typing import Dict, Any, List, Optional
import json
from pathlib import Path
from datetime import datetime

from .agent_factory import ExperimentalAgentFactory
from .memory import SharedMemorySystem
from .orchestrator import ExperimentalOrchestrator
from .graph import create_c4_modeler_graph


def create_experimental_pipeline(
    system_brief: str,
    model_name: str,
    experiment_condition: Dict[str, Any],
    memory_config: Optional[Dict[str, Any]] = None,
    output_dir: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create and run the complete experimental pipeline.
    
    Args:
        system_brief: The system description to model
        model_name: LLM model to use (e.g., "gpt-4o-mini")
        experiment_condition: Configuration for the experimental condition
        memory_config: Optional memory system configuration
        output_dir: Optional output directory for results
    
    Returns:
        Dictionary containing the generated C4 model and metadata
    """
    
    print(f"🔬 Running experimental pipeline")
    print(f"   Model: {model_name}")
    print(f"   Roles: {experiment_condition.get('roles', [])}")
    print(f"   Memory: {memory_config.get('type', 'none') if memory_config else 'none'}")
    
    # Create the experimental graph
    app = create_c4_modeler_graph(
        model_name=model_name,
        experiment_condition=experiment_condition,
        memory_config=memory_config
    )
    
    # Run the pipeline
    start_time = datetime.now()
    
    try:
        # Initialize State with proper structure
        from collections import deque
        from langchain_core.messages import HumanMessage
        
        initial_state = {
            "messages": [HumanMessage(content=f"Analyze this system: {system_brief}")],
            "system_brief": system_brief,
            "c4_model": {
                "context": {},
                "containers": {},
                "components": {}
            },
            "component_queue": None,  # FIXED: None triggers populate_queue after container diagram
            "experiment_condition": experiment_condition,
            "memory_system": None,
            "speaking_order": experiment_condition.get("speaking_order", experiment_condition.get("roles", [])),
            "current_speaker_index": 0,
            "experimental_metadata": {
                "condition": experiment_condition,
                "memory_config": memory_config,
                "start_time": start_time.isoformat()
            }
        }
        
        # Set proper recursion limit for complex multi-agent workflows
        config = {"recursion_limit": 400}
        result = app.invoke(initial_state, config)
        
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        
        # Add execution metadata
        result["execution_metadata"] = {
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "execution_time_seconds": execution_time,
            "model_name": model_name,
            "experiment_condition": experiment_condition,
            "memory_config": memory_config
        }
        
        # Save results if output directory specified
        if output_dir:
            save_experimental_results(result, output_dir, experiment_condition)
        
        return result
        
    except Exception as e:
        print(f"❌ Pipeline execution failed: {str(e)}")
        return {
            "error": str(e),
            "execution_metadata": {
                "start_time": start_time.isoformat(),
                "end_time": datetime.now().isoformat(),
                "failed": True,
                "model_name": model_name,
                "experiment_condition": experiment_condition
            }
        }


def save_experimental_results(
    results: Dict[str, Any],
    output_dir: str,
    experiment_condition: Dict[str, Any]
) -> str:
    """
    Save experimental results to structured output directory.
    
    Args:
        results: The pipeline results to save
        output_dir: Base output directory
        experiment_condition: The experimental condition configuration
    
    Returns:
        Path to the saved results directory
    """
    
    # Create timestamped directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    condition_name = experiment_condition.get("name", "unknown_condition")
    
    results_dir = Path(output_dir) / f"{condition_name}_{timestamp}"
    results_dir.mkdir(parents=True, exist_ok=True)
    
    # Save main results file
    results_file = results_dir / "results.json"
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    # Save individual C4 artifacts if present
    context_yaml = results.get("context_yaml")
    if context_yaml:
        with open(results_dir / "context.yaml", 'w', encoding='utf-8') as f:
            f.write(context_yaml)
    
    context_diagram = results.get("context_diagram")
    if context_diagram:
        with open(results_dir / "context.puml", 'w', encoding='utf-8') as f:
            f.write(context_diagram)
    
    container_yaml = results.get("container_yaml")
    if container_yaml:
        with open(results_dir / "containers.yaml", 'w', encoding='utf-8') as f:
            f.write(container_yaml)
    
    container_diagram = results.get("container_diagram")
    if container_diagram:
        with open(results_dir / "containers.puml", 'w', encoding='utf-8') as f:
            f.write(container_diagram)
    
    # Save component artifacts
    components = results.get("components", {})
    if components:
        components_dir = results_dir / "components"
        components_dir.mkdir(exist_ok=True)
        
        for comp_name, comp_data in components.items():
            comp_yaml = comp_data.get("yaml")
            if comp_yaml:
                with open(components_dir / f"{comp_name}.yaml", 'w', encoding='utf-8') as f:
                    f.write(comp_yaml)
            
            comp_diagram = comp_data.get("diagram")
            if comp_diagram:
                with open(components_dir / f"{comp_name}.puml", 'w', encoding='utf-8') as f:
                    f.write(comp_diagram)
    
    # Save experiment metadata
    metadata = {
        "experiment_condition": experiment_condition,
        "execution_metadata": results.get("execution_metadata", {}),
        "saved_at": datetime.now().isoformat(),
        "results_directory": str(results_dir)
    }
    
    with open(results_dir / "experiment_metadata.json", 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"💾 Results saved to: {results_dir}")
    return str(results_dir)


def validate_experiment_condition(condition: Dict[str, Any]) -> List[str]:
    """
    Validate an experimental condition configuration.
    
    Args:
        condition: The experimental condition to validate
    
    Returns:
        List of validation errors (empty if valid)
    """
    
    errors = []
    
    # Required fields
    required_fields = ["id", "name", "roles"]
    for field in required_fields:
        if field not in condition:
            errors.append(f"Missing required field: {field}")
    
    # Validate roles
    valid_roles = [
        "Product Owner", "Architect", "DevOps Engineer", "Security Expert", "Software Engineer",
        "Business Analyst", "Domain Expert"
    ]
    roles = condition.get("roles", [])
    
    if not isinstance(roles, list) or not roles:
        errors.append("Roles must be a non-empty list")
    else:
        for role in roles:
            if role not in valid_roles:
                errors.append(f"Invalid role: {role}. Valid roles: {valid_roles}")
    
    # Validate speaking order if present
    speaking_order = condition.get("speaking_order")
    if speaking_order is not None:
        if not isinstance(speaking_order, list):
            errors.append("Speaking order must be a list")
        elif set(speaking_order) != set(roles):
            errors.append("Speaking order must contain exactly the same roles as the roles list")
    
    # Validate memory type
    memory_type = condition.get("memory_type", "none")
    valid_memory_types = ["none", "glossary", "persistent", "hierarchical", "full"]
    if memory_type not in valid_memory_types:
        errors.append(f"Invalid memory type: {memory_type}. Valid types: {valid_memory_types}")
    
    # Validate role specificity
    role_specificity = condition.get("role_specificity", "generic")
    valid_specificity = ["generic", "specialized"]
    if role_specificity not in valid_specificity:
        errors.append(f"Invalid role specificity: {role_specificity}. Valid types: {valid_specificity}")
    
    return errors


def create_memory_config_from_condition(condition: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Create a memory configuration from an experimental condition.
    
    Args:
        condition: The experimental condition
    
    Returns:
        Memory configuration dictionary or None if no memory needed
    """
    
    memory_type = condition.get("memory_type", "none")
    
    if memory_type == "none":
        return None
    
    return {
        "type": memory_type,
        "enabled": True,
        "glossary_agent_active": memory_type in ["glossary", "full"],
        "persistent_memory": memory_type in ["persistent", "full"],
        "hierarchical_memory": memory_type in ["hierarchical", "full"],
        "cross_level_sharing": memory_type == "full"
    }


def extract_c4_model_from_result(result: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract C4 model data from pipeline result in standardized format.
    
    Args:
        result: The pipeline execution result (LangGraph State)
    
    Returns:
        Standardized C4 model dictionary
    """
    
    # The result should be the final State from LangGraph
    # Extract c4_model directly from the state if it exists
    if "c4_model" in result:
        return result["c4_model"]
    
    # Fallback: try to construct from individual fields (legacy compatibility)
    c4_model = {
        "context": {
            "yaml_definition": result.get("context_yaml", ""),
            "diagram": result.get("context_diagram", "")
        },
        "containers": {
            "yaml_definition": result.get("container_yaml", ""),
            "diagram": result.get("container_diagram", "")
        },
        "components": {}
    }
    
    # Extract component data
    components_data = result.get("components", {})
    if isinstance(components_data, dict):
        for comp_name, comp_data in components_data.items():
            c4_model["components"][comp_name] = {
                "yaml_definition": comp_data.get("yaml", ""),
                "diagram": comp_data.get("diagram", "")
            }
    
    return c4_model


def compare_experimental_conditions(
    baseline_results: Dict[str, Any],
    experimental_results: Dict[str, Any],
    metrics_to_compare: List[str]
) -> Dict[str, Any]:
    """
    Compare results between experimental conditions.
    
    Args:
        baseline_results: Results from baseline condition
        experimental_results: Results from experimental condition
        metrics_to_compare: List of metric names to compare
    
    Returns:
        Comparison analysis dictionary
    """
    
    comparison = {
        "baseline_condition": baseline_results.get("execution_metadata", {}).get("experiment_condition"),
        "experimental_condition": experimental_results.get("execution_metadata", {}).get("experiment_condition"),
        "metric_differences": {},
        "summary": {}
    }
    
    # Extract evaluation results
    baseline_eval = baseline_results.get("evaluation", {})
    experimental_eval = experimental_results.get("evaluation", {})
    
    # Compare specific metrics
    for metric in metrics_to_compare:
        baseline_value = extract_metric_value(baseline_eval, metric)
        experimental_value = extract_metric_value(experimental_eval, metric)
        
        if baseline_value is not None and experimental_value is not None:
            difference = experimental_value - baseline_value
            percent_change = (difference / baseline_value * 100) if baseline_value != 0 else 0
            
            comparison["metric_differences"][metric] = {
                "baseline": baseline_value,
                "experimental": experimental_value,
                "absolute_difference": difference,
                "percent_change": round(percent_change, 2)
            }
    
    # Calculate summary statistics
    if comparison["metric_differences"]:
        improvements = sum(1 for diff in comparison["metric_differences"].values() 
                          if diff["absolute_difference"] > 0)
        total_metrics = len(comparison["metric_differences"])
        
        comparison["summary"] = {
            "metrics_improved": improvements,
            "metrics_declined": total_metrics - improvements,
            "improvement_rate": round(improvements / total_metrics * 100, 1) if total_metrics > 0 else 0
        }
    
    return comparison


def extract_metric_value(evaluation: Dict[str, Any], metric_name: str) -> Optional[float]:
    """
    Extract a specific metric value from evaluation results.
    
    Args:
        evaluation: Evaluation results dictionary
        metric_name: Name of the metric to extract
    
    Returns:
        Metric value or None if not found
    """
    
    # ISO 25010 attributes
    if metric_name.startswith("iso_"):
        attr_name = metric_name[4:]  # Remove "iso_" prefix
        iso_scores = evaluation.get("iso25010Attributes", {}).get("scores", {})
        return iso_scores.get(attr_name)
    
    # ATAM scenarios
    if metric_name == "atam_responsiveness":
        return evaluation.get("atamScenarios", {}).get("overall_responsiveness")
    
    # Architectural soundness
    if metric_name.startswith("soundness_"):
        soundness_metric = metric_name[10:]  # Remove "soundness_" prefix
        return evaluation.get("architecturalSoundness", {}).get(soundness_metric)
    
    # Legacy metrics
    legacy_mapping = {
        "compilation_success": "compilationSuccess",
        "abstraction_adherence": "abstractionAdherence", 
        "missing_information": "missingInformation",
        "naming_consistency": "emergentNamingConsistency",
        "cross_level_consistency": "crossLevelConsistency"
    }
    
    if metric_name in legacy_mapping:
        legacy_key = legacy_mapping[metric_name]
        return evaluation.get(legacy_key, {}).get("score")
    
    return None