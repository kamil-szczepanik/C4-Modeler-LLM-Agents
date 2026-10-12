"""
Test script to run only the architect_only condition from role_ablation experiment.
This is useful for testing fixes without re-running all conditions.
"""

import sys
from pathlib import Path
from datetime import datetime
import json

# Environment setup
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "true")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_PROJECT"] = f"C4-Test-ArchitectOnly-{datetime.now().strftime('%Y%m%d_%H%M%S')}"

# Import experimental system
sys.path.insert(0, str(Path(__file__).parent / "src"))
from c4modeler.experiments import EnhancedExperimentRunner

def main():
    print("🧪 Testing architect_only condition fix")
    print("=" * 60)
    
    # Initialize runner
    runner = EnhancedExperimentRunner()
    runner.load_system_briefs("data/briefs")
    
    # Get the architect_only condition from config
    role_ablation_config = runner.config["experiments"]["role_ablation"]
    architect_only_condition = None
    
    for condition in role_ablation_config["conditions"]:
        if condition["id"] == "architect_only":
            architect_only_condition = condition
            break
    
    if not architect_only_condition:
        print("❌ architect_only condition not found in config")
        return
    
    print(f"\n📋 Condition: {architect_only_condition['name']}")
    print(f"   Roles: {architect_only_condition['roles']}")
    print(f"   Description: {architect_only_condition['description']}\n")
    
    # Run just this one condition
    model_name = "gemini-2.5-flash-lite"
    temperature = 0.5
    
    protocol = runner.config.get("protocol", {
        "datasets": ["clinic-management-system"],  # Just one dataset for testing
        "rounds_per_condition": 1  # Just one round for testing
    })
    
    print(f"🤖 Model: {model_name}")
    print(f"🌡️ Temperature: {temperature}")
    print(f"📊 Datasets: {protocol['datasets']}")
    print(f"🔄 Rounds: {protocol.get('rounds_per_condition', 3)}\n")
    
    try:
        result = runner._run_condition(
            architect_only_condition,
            role_ablation_config,
            protocol,
            model_name,
            temperature
        )
        
        # Save result
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"data/results/enhanced_experiments/architect_only_test_{timestamp}.json"
        Path(output_file).parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Test completed successfully!")
        print(f"📄 Results saved to: {output_file}")
        
        # Print summary
        if "brief_results" in result:
            print(f"\n📊 Summary:")
            for brief_name, brief_data in result["brief_results"].items():
                runs = len(brief_data)
                print(f"   {brief_name}: {runs} runs")
        
    except Exception as e:
        print(f"\n❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
