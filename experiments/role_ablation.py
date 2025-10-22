"""
Role Ablation Experiment Runner
Investigates the impact of removing specific expert roles on C4 model quality.

Usage:
    python experiments/role_ablation.py --model gpt-4o-mini
    python experiments/role_ablation.py --condition baseline --brief clinic-management-system
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Environment setup
from dotenv import load_dotenv
import os
load_dotenv()

# Configure tracing
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "true")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_PROJECT"] = "C4-Experiments-RoleAblation"

from run_experiments import setup_tracing_context
from src.c4modeler.experiments import EnhancedExperimentRunner


def analyze_role_ablation_results(results):
    """Analyze and summarize role ablation experiment results."""
    
    print("\n" + "="*60)
    print("🔬 ROLE ABLATION ANALYSIS")
    print("="*60)
    
    conditions = results.get("conditions", {})
    
    # Extract key metrics for each condition
    condition_summary = {}
    for condition_id, condition_data in conditions.items():
        summary = condition_data.get("condition_summary", {})
        averages = summary.get("averages", {})
        
        condition_summary[condition_id] = {
            "name": condition_data.get("condition_metadata", {}).get("name", condition_id),
            "roles": condition_data.get("condition_metadata", {}).get("roles", []),
            "runs": summary.get("total_runs", 0),
            "iso_functional": averages.get("iso_functional_suitability", 0),
            "iso_security": averages.get("iso_security", 0),
            "iso_maintainability": averages.get("iso_maintainability", 0),
            "coupling_density": averages.get("soundness_coupling_density", 0),
            "semantic_completeness": averages.get("soundness_semantic_completeness", 0)
        }
    
    # Print detailed analysis
    baseline_metrics = condition_summary.get("baseline", {})
    
    print(f"\n📊 Condition Comparison (vs Baseline):")
    print(f"{'Condition':<20} {'Roles':<12} {'Func.Suit':<10} {'Security':<10} {'Maintain':<10} {'Coupling':<10}")
    print("-" * 80)
    
    for condition_id, data in condition_summary.items():
        func_suit = data.get("iso_functional", 0)
        security = data.get("iso_security", 0)
        maintain = data.get("iso_maintainability", 0)
        coupling = data.get("coupling_density", 0)
        
        # Calculate percentage change from baseline
        if condition_id != "baseline" and baseline_metrics:
            func_change = ((func_suit - baseline_metrics.get("iso_functional", 0)) / 
                          max(baseline_metrics.get("iso_functional", 1), 0.01) * 100)
            sec_change = ((security - baseline_metrics.get("iso_security", 0)) / 
                         max(baseline_metrics.get("iso_security", 1), 0.01) * 100)
            
            print(f"{data['name']:<20} {len(data['roles']):<12} {func_suit:.2f} ({func_change:+.1f}%) "
                  f"{security:.2f} ({sec_change:+.1f}%) {maintain:.2f} {coupling:.3f}")
        else:
            print(f"{data['name']:<20} {len(data['roles']):<12} {func_suit:.2f} "
                  f"{security:.2f} {maintain:.2f} {coupling:.3f}")
    
    # Key findings
    print(f"\n🔍 Key Findings:")
    
    # Find which role removal has biggest impact
    max_functional_drop = 0
    worst_condition = None
    for condition_id, data in condition_summary.items():
        if condition_id != "baseline" and baseline_metrics:
            functional_drop = (baseline_metrics.get("iso_functional", 0) - 
                             data.get("iso_functional", 0))
            if functional_drop > max_functional_drop:
                max_functional_drop = functional_drop
                worst_condition = data
    
    if worst_condition:
        print(f"   • Most impactful role removal: {worst_condition['name']}")
        print(f"     Functional suitability drop: {max_functional_drop:.2f} points")
    
    # Homogeneous vs heterogeneous
    architect_only = condition_summary.get("architect_only", {})
    if architect_only and baseline_metrics:
        func_diff = baseline_metrics.get("iso_functional", 0) - architect_only.get("iso_functional", 0)
        print(f"   • Homogeneous (all architects) vs Heterogeneous team:")
        print(f"     Functional suitability difference: {func_diff:.2f} points")


def main():
    parser = argparse.ArgumentParser(description="Run Role Ablation Experiment")
    parser.add_argument("--model", "-m", default="gpt-4o-mini", help="LLM model to use")
    parser.add_argument("--condition", "-c", help="Specific condition to run")
    parser.add_argument("--brief", "-b", help="Specific system brief to test")
    parser.add_argument("--output-dir", "-o", help="Output directory")
    
    args = parser.parse_args()
    
    print("🧪 Role Ablation Experiment")
    print("="*50)
    print("Purpose: Determine which roles are most critical for architectural quality")
    print("Hypothesis: Removing domain-oriented roles reduces functional suitability")
    
    with setup_tracing_context("role-ablation", args.model):
        runner = EnhancedExperimentRunner()
        runner.load_system_briefs("data/briefs")
        
        if args.condition:
            print(f"\n🎯 Running specific condition: {args.condition}")
            # This would require extending the runner to support single conditions
            print("⚠️ Single condition execution not yet implemented")
        else:
            print(f"\n🚀 Running complete Role Ablation study...")
            results = runner.run_experiment("role_ablation", args.model)
            
            # Analyze results
            analyze_role_ablation_results(results)
            
            # Save results
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_dir = Path(args.output_dir) if args.output_dir else Path("data/results/role_ablation")
            output_file = output_dir / f"role_ablation_{timestamp}.json"
            
            output_dir.mkdir(parents=True, exist_ok=True)
            
            import json
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=2)
            
            print(f"\n💾 Results saved to: {output_file}")


if __name__ == "__main__":
    main()