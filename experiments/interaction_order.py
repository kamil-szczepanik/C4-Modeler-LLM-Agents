"""
Interaction Order Experiment Runner
Studies how conversation sequencing affects architectural outcomes.

Usage:
    python experiments/interaction_order.py --model gpt-4o-mini
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
os.environ["LANGCHAIN_PROJECT"] = "C4-Experiments-InteractionOrder"

from run_experiments import setup_tracing_context
from src.c4modeler.experiments import EnhancedExperimentRunner


def analyze_interaction_order_results(results):
    """Analyze interaction order experiment results."""
    
    print("\n" + "="*60)
    print("🔬 INTERACTION ORDER ANALYSIS")
    print("="*60)
    
    conditions = results.get("conditions", {})
    
    # Map speaking orders to outcomes
    order_analysis = {}
    for condition_id, condition_data in conditions.items():
        metadata = condition_data.get("condition_metadata", {})
        summary = condition_data.get("condition_summary", {})
        averages = summary.get("averages", {})
        
        speaking_order = metadata.get("speaking_order", [])
        first_speaker = speaking_order[0] if speaking_order else "Unknown"
        
        order_analysis[condition_id] = {
            "first_speaker": first_speaker,
            "speaking_order": speaking_order,
            "functional_suitability": averages.get("iso_functional_suitability", 0),
            "maintainability": averages.get("iso_maintainability", 0),
            "abstraction_coherence": averages.get("soundness_abstraction_coherence", 0),
            "coupling_density": averages.get("soundness_coupling_density", 0)
        }
    
    # Analyze by first speaker
    print(f"\n📊 Results by First Speaker:")
    print(f"{'First Speaker':<20} {'Func.Suit':<12} {'Maintain':<12} {'Abs.Coher':<12} {'Coupling':<10}")
    print("-" * 75)
    
    for condition_id, data in order_analysis.items():
        first_speaker = data["first_speaker"]
        func_suit = data["functional_suitability"]
        maintain = data["maintainability"]
        abs_coher = data["abstraction_coherence"]
        coupling = data["coupling_density"]
        
        print(f"{first_speaker:<20} {func_suit:.3f} {maintain:.3f} {abs_coher:.3f} {coupling:.3f}")
    
    # Find patterns
    print(f"\n🔍 Key Patterns:")
    
    # Technical vs Business first
    technical_first = [d for d in order_analysis.values() 
                      if d["first_speaker"] in ["Architect", "DevOps Engineer", "Security Expert"]]
    business_first = [d for d in order_analysis.values() 
                     if d["first_speaker"] == "Product Owner"]
    
    if technical_first and business_first:
        tech_avg_structure = sum(d["abstraction_coherence"] for d in technical_first) / len(technical_first)
        bus_avg_functional = sum(d["functional_suitability"] for d in business_first) / len(business_first)
        
        print(f"   • Technical-first average abstraction coherence: {tech_avg_structure:.3f}")
        print(f"   • Business-first average functional suitability: {bus_avg_functional:.3f}")
    
    # Best overall combination
    best_condition = max(order_analysis.items(), 
                        key=lambda x: x[1]["functional_suitability"] + x[1]["abstraction_coherence"])
    
    print(f"   • Best overall speaking order: {' → '.join(best_condition[1]['speaking_order'])}")
    print(f"     Combined score: {best_condition[1]['functional_suitability'] + best_condition[1]['abstraction_coherence']:.3f}")


def main():
    parser = argparse.ArgumentParser(description="Run Interaction Order Experiment")
    parser.add_argument("--model", "-m", default="gpt-4o-mini", help="LLM model to use")
    parser.add_argument("--output-dir", "-o", help="Output directory")
    
    args = parser.parse_args()
    
    print("🧪 Interaction Order Experiment")
    print("="*50)
    print("Purpose: Understand how conversation sequencing affects architectural outcomes")
    print("Hypothesis: Architect-first yields higher structural validity; PO-first yields richer functional mapping")
    
    with setup_tracing_context("interaction-order", args.model):
        runner = EnhancedExperimentRunner()
        runner.load_system_briefs("data/briefs")
        
        print(f"\n🚀 Running Interaction Order study...")
        results = runner.run_experiment("interaction_order", args.model)
        
        # Analyze results
        analyze_interaction_order_results(results)
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = Path(args.output_dir) if args.output_dir else Path("data/results/interaction_order")
        output_file = output_dir / f"interaction_order_{timestamp}.json"
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        import json
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n💾 Results saved to: {output_file}")


if __name__ == "__main__":
    main()