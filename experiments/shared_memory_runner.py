"""
Shared Memory Experiment Runner
Investigates the impact of shared memory on agent collaboration quality.

Usage:
    python experiments/shared_memory_runner.py --model gemini-2.5-flash-lite
"""

import sys
import argparse
import json
import time
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
import os
load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "true")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_PROJECT"] = "C4-Experiments-SharedMemory"

from src.c4modeler.experiments import EnhancedExperimentRunner


def main():
    parser = argparse.ArgumentParser(description="Run Shared Memory Experiment")
    parser.add_argument("--model", "-m", default="gemini-2.5-flash-lite", help="LLM model to use")
    parser.add_argument("--output-dir", "-o", help="Output directory")
    
    args = parser.parse_args()
    
    print("🧪 Shared Memory Experiment")
    print("="*50)
    print("Purpose: Evaluate impact of shared memory on collaboration")
    print(f"Model: {args.model}")
    
    start_time = time.time()
    runner = EnhancedExperimentRunner()
    runner.load_system_briefs("data/briefs")
    
    print(f"\n🚀 Running Shared Memory study...")
    results = runner.run_experiment("shared_memory", args.model)
    
    duration = time.time() - start_time
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(args.output_dir) if args.output_dir else Path("data/results/shared_memory")
    output_file = output_dir / f"shared_memory_{timestamp}.json"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Complete! Duration: {duration/60:.1f} min")
    print(f"💾 Results: {output_file}")


if __name__ == "__main__":
    main()
