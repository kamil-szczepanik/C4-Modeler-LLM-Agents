"""
Test script to demonstrate the skip logic.
This will show that already-completed runs are detected and skipped.
"""

import sys
from pathlib import Path
from datetime import datetime

# Environment setup
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "false"  # Disable tracing for quick test

# Import experimental system
sys.path.insert(0, str(Path(__file__).parent / "src"))
from c4modeler.experiments import EnhancedExperimentRunner

def main():
    print("🧪 Testing Skip Logic")
    print("=" * 60)
    
    # Initialize runner
    runner = EnhancedExperimentRunner()
    runner.load_system_briefs("data/briefs")
    
    # Get the baseline condition (which should have completed runs)
    role_ablation_config = runner.config["experiments"]["role_ablation"]
    baseline_condition = None
    
    for condition in role_ablation_config["conditions"]:
        if condition["id"] == "baseline":
            baseline_condition = condition
            break
    
    if not baseline_condition:
        print("❌ baseline condition not found in config")
        return
    
    print(f"\n📋 Condition: {baseline_condition['name']}")
    print(f"   Description: {baseline_condition['description']}\n")
    
    # Run with just 1 dataset and 1 round to test skip logic quickly
    model_name = "gemini-2.5-flash-lite"
    temperature = 0.5
    
    protocol = {
        "datasets": ["clinic-management-system"],  # Just one dataset
        "rounds_per_condition": 3  # All 3 rounds should exist
    }
    
    print(f"🤖 Model: {model_name}")
    print(f"📊 Datasets: {protocol['datasets']}")
    print(f"🔄 Rounds: {protocol['rounds_per_condition']}")
    print(f"\n{'='*60}\n")
    
    try:
        result = runner._run_condition(
            baseline_condition,
            role_ablation_config,
            protocol,
            model_name,
            temperature
        )
        
        print(f"\n{'='*60}")
        print("✅ Test completed!")
        print(f"{'='*60}")
        
        # Print summary
        if "brief_results" in result:
            print(f"\n📊 Summary:")
            for brief_name, brief_data in result["brief_results"].items():
                resumed_count = sum(1 for r in brief_data if r.get("resumed_from_artifacts", False))
                new_count = len(brief_data) - resumed_count
                print(f"   {brief_name}:")
                print(f"      - Resumed from existing: {resumed_count}")
                print(f"      - Newly generated: {new_count}")
        
    except Exception as e:
        print(f"\n❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
