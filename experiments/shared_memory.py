"""
Shared Memory Experiment Runner
Evaluates the impact of persistent shared knowledge on consistency.

Usage:
    python experiments/shared_memory.py --model gpt-4o-mini
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
os.environ["LANGCHAIN_PROJECT"] = "C4-Experiments-SharedMemory"

from run_experiments import setup_tracing_context
from src.c4modeler.experiments import EnhancedExperimentRunner


def analyze_shared_memory_results(results):
    """Analyze shared memory experiment results."""
    
    print("\n" + "="*60)
    print("🔬 SHARED MEMORY ANALYSIS")
    print("="*60)
    
    conditions = results.get("conditions", {})
    
    # Analyze memory type impact
    memory_analysis = {}
    for condition_id, condition_data in conditions.items():
        metadata = condition_data.get("condition_metadata", {})
        summary = condition_data.get("condition_summary", {})
        averages = summary.get("averages", {})
        
        memory_type = metadata.get("memory_type", "none")
        
        memory_analysis[condition_id] = {
            "memory_type": memory_type,
            "name": metadata.get("name", condition_id),
            "maintainability": averages.get("iso_maintainability", 0),
            "compatibility": averages.get("iso_compatibility", 0),
            "naming_consistency": averages.get("naming_consistency", 0),
            "abstraction_coherence": averages.get("soundness_abstraction_coherence", 0)
        }
    
    # Display results by memory type
    print(f"\n📊 Results by Memory Configuration:")
    print(f"{'Memory Type':<20} {'Maintain':<10} {'Compat':<10} {'Naming':<10} {'Abs.Coher':<10}")
    print("-" * 65)
    
    baseline_score = 0
    for condition_id, data in memory_analysis.items():
        memory_type = data["memory_type"]
        maintain = data["maintainability"]
        compat = data["compatibility"]
        naming = data["naming_consistency"]
        abs_coher = data["abstraction_coherence"]
        
        # Calculate composite consistency score
        consistency_score = (maintain + compat + naming + abs_coher) / 4
        
        if memory_type == "none":
            baseline_score = consistency_score
        
        print(f"{memory_type:<20} {maintain:.3f} {compat:.3f} {naming:.3f} {abs_coher:.3f}")
    
    # Memory type effectiveness
    print(f"\n🔍 Memory Type Effectiveness:")
    
    # Sort by overall consistency improvement
    sorted_conditions = sorted(memory_analysis.items(), 
                              key=lambda x: (x[1]["maintainability"] + 
                                           x[1]["naming_consistency"] + 
                                           x[1]["abstraction_coherence"]) / 3, 
                              reverse=True)
    
    print(f"   Memory Type Ranking (by consistency metrics):")
    for i, (condition_id, data) in enumerate(sorted_conditions, 1):
        consistency_avg = (data["maintainability"] + data["naming_consistency"] + 
                          data["abstraction_coherence"]) / 3
        improvement = ((consistency_avg - baseline_score) / max(baseline_score, 0.01) * 100) if baseline_score else 0
        
        print(f"   {i}. {data['memory_type']}: {consistency_avg:.3f} ({improvement:+.1f}% vs baseline)")
    
    # Specific insights
    glossary_data = next((d for d in memory_analysis.values() if d["memory_type"] == "glossary"), None)
    persistent_data = next((d for d in memory_analysis.values() if d["memory_type"] == "persistent"), None)
    
    if glossary_data:
        print(f"\n   📝 Glossary Agent Impact:")
        print(f"      Naming consistency: {glossary_data['naming_consistency']:.3f}")
        
    if persistent_data:
        print(f"\n   💾 Persistent Memory Impact:")
        print(f"      Maintainability: {persistent_data['maintainability']:.3f}")


def main():
    parser = argparse.ArgumentParser(description="Run Shared Memory Experiment")
    parser.add_argument("--model", "-m", default="gpt-4o-mini", help="LLM model to use")
    parser.add_argument("--output-dir", "-o", help="Output directory")
    
    args = parser.parse_args()
    
    print("🧪 Shared Memory Experiment")
    print("="*50)
    print("Purpose: Test whether shared glossary improves architectural consistency")
    print("Hypothesis: Glossary-based collaboration improves naming consistency and traceability")
    
    with setup_tracing_context("shared-memory", args.model):
        runner = EnhancedExperimentRunner()
        runner.load_system_briefs("data/briefs")
        
        print(f"\n🚀 Running Shared Memory study...")
        results = runner.run_experiment("shared_memory", args.model)
        
        # Analyze results
        analyze_shared_memory_results(results)
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = Path(args.output_dir) if args.output_dir else Path("data/results/shared_memory")
        output_file = output_dir / f"shared_memory_{timestamp}.json"
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        import json
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n💾 Results saved to: {output_file}")


if __name__ == "__main__":
    main()