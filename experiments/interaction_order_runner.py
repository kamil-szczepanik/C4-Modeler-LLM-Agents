"""
Interaction Order Experiment Runner
Investigates how the sequence of agent interactions affects C4 model quality.

Usage:
    python experiments/interaction_order_runner.py --model gemini-2.5-flash-lite
    python experiments/interaction_order_runner.py --parallel --max-workers 3
"""

import sys
import argparse
import json
import time
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

from src.c4modeler.experiments import EnhancedExperimentRunner


def analyze_interaction_order_results(results):
    """Analyze and summarize interaction order experiment results."""
    
    print("\n" + "="*60)
    print("🔬 INTERACTION ORDER ANALYSIS")
    print("="*60)
    
    conditions = results.get("conditions", {})
    
    for condition_id, condition_data in conditions.items():
        metadata = condition_data.get("condition_metadata", {})
        summary = condition_data.get("condition_summary", {})
        averages = summary.get("averages", {})
        
        print(f"\n📊 Condition: {metadata.get('name', condition_id)}")
        print(f"   Speaking Order: {' → '.join(metadata.get('speaking_order', []))}")
        print(f"   Total Runs: {summary.get('total_runs', 0)}")
        print(f"\n   Key Metrics:")
        print(f"   - ISO Functional: {averages.get('iso_functional_suitability', 0):.3f}")
        print(f"   - ISO Maintainability: {averages.get('iso_maintainability', 0):.3f}")
        print(f"   - ATAM Responsiveness: {averages.get('atam_responsiveness', 0):.3f}")
        print(f"   - Abstraction Coherence: {averages.get('soundness_abstraction_coherence', 0):.3f}")
    
    # Compare speaking orders
    print(f"\n🔍 Speaking Order Impact:")
    print(f"   Hypothesis: Architecture-first approach yields better structural quality")
    
    baseline_score = None
    for condition_id, condition_data in conditions.items():
        metadata = condition_data.get("condition_metadata", {})
        summary = condition_data.get("condition_summary", {})
        averages = summary.get("averages", {})
        
        composite = averages.get('soundness_abstraction_coherence', 0)
        
        if 'baseline' in condition_id.lower():
            baseline_score = composite
        
        order_str = ' → '.join(metadata.get('speaking_order', [])[:2])
        print(f"   {order_str}: {composite:.3f}")
    
    print("="*60)


def main():
    parser = argparse.ArgumentParser(description="Run Interaction Order Experiment")
    parser.add_argument("--model", "-m", default="gemini-2.5-flash-lite", help="LLM model to use")
    parser.add_argument("--output-dir", "-o", help="Output directory")
    parser.add_argument("--parallel", action="store_true", help="Run conditions in parallel")
    parser.add_argument("--max-workers", type=int, default=2, help="Max parallel workers")
    
    args = parser.parse_args()
    
    print("🧪 Interaction Order Experiment")
    print("="*50)
    print("Purpose: Determine optimal agent interaction sequence")
    print("Hypothesis: Architecture-first order produces better structure")
    print(f"Model: {args.model}")
    
    start_time = time.time()
    
    runner = EnhancedExperimentRunner()
    runner.load_system_briefs("data/briefs")
    
    print(f"\n🚀 Running complete Interaction Order study...")
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    results = runner.run_experiment("interaction_order", args.model)
    
    duration = time.time() - start_time
    
    # Analyze results
    analyze_interaction_order_results(results)
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(args.output_dir) if args.output_dir else Path("data/results/interaction_order")
    output_file = output_dir / f"interaction_order_{timestamp}.json"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*50}")
    print(f"✅ Experiment Complete!")
    print(f"⏱️ Duration: {duration/60:.1f} minutes")
    print(f"💾 Results saved to: {output_file}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
