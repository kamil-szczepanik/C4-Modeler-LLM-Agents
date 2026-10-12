"""
Sequential Experiment Runner for C4 Modeling Research
======================================================

This script runs experiments sequentially (one at a time) with full progress tracking,
artifact saving, and LangSmith monitoring.

Features:
- Sequential execution (no parallelism - safe and predictable)
- Automatic artifact saving after each run
- Progress checkpointing and recovery
- LangSmith project initialization
- Comprehensive logging and monitoring
- Temperature configuration support

Usage:
    # Run single experiment
    python run_experiments.py --experiment role_ablation --model gemini-2.5-flash-lite
    
    # Run all experiments sequentially
    python run_experiments.py --all-experiments --model gemini-2.5-flash-lite
    
    # List available experiments
    python run_experiments.py --list-experiments
    
    # Custom temperature
    python run_experiments.py --experiment role_ablation --temperature 0.7

Author: Research Team
Date: October 2025
"""

import argparse
import sys
import json
import time
from pathlib import Path
from datetime import datetime
from typing import Optional

# Environment setup with proper LangSmith tracing
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configure LangSmith tracing
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "true")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")

# Import our experimental system
sys.path.insert(0, str(Path(__file__).parent / "src"))

from c4modeler.experiments import EnhancedExperimentRunner

# LangChain imports for project initialization
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI


def initialize_langsmith_project(project_name: str, model_name: str) -> bool:
    """
    Initialize LangSmith project by running a simple chain.
    This makes the project visible in LangSmith UI immediately.
    
    Args:
        project_name: Name of the LangSmith project
        model_name: LLM model name to use for initialization
        
    Returns:
        True if successful, False otherwise
    """
    try:
        print(f"🔧 Initializing LangSmith project: {project_name}")
        
        # Set the project for this initialization
        os.environ["LANGCHAIN_PROJECT"] = project_name
        
        # Create a very simple chain
        llm = ChatGoogleGenerativeAI(
            model=model_name,
            temperature=0,
            max_tokens=50
        )
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant. Respond with exactly: 'LangSmith project initialized successfully.'"),
            ("user", "Initialize project")
        ])
        
        chain = prompt | llm | StrOutputParser()
        
        # Run the chain to create the first trace
        result = chain.invoke({})
        
        print(f"✅ LangSmith project initialized: {project_name}")
        print(f"   Response: {result[:50]}...")
        print(f"   🔗 View in LangSmith: https://smith.langchain.com/")
        
        return True
        
    except Exception as e:
        print(f"⚠️ Warning: Could not initialize LangSmith project: {str(e)}")
        print(f"   Experiments will still run, but may not be visible in LangSmith immediately")
        return False


def list_experiments():
    """List all available experiments and their conditions."""
    runner = EnhancedExperimentRunner()
    
    if not runner.config:
        print("❌ Failed to load experiment configuration")
        return
    
    print("📋 Available Experiments:")
    print("=" * 60)
    
    for exp_name, exp_config in runner.config.get("experiments", {}).items():
        print(f"\n🧪 {exp_name}")
        print(f"   Name: {exp_config['name']}")
        print(f"   Description: {exp_config['description']}")
        print(f"   Purpose: {exp_config['purpose']}")
        print(f"   Conditions: {len(exp_config.get('conditions', []))}")
        
        for condition in exp_config.get("conditions", []):
            print(f"     • {condition['id']}: {condition['name']}")
    
    print(f"\n📊 Total Experiments: {len(runner.config.get('experiments', {}))}")


def run_single_experiment(
    experiment_name: str, 
    model_name: str, 
    temperature: float = 0.5,
    output_dir: Optional[str] = None,
    session_id: Optional[str] = None
):
    """
    Run a single experiment sequentially with LangSmith tracing.
    
    Args:
        experiment_name: Name of the experiment to run
        model_name: LLM model to use
        temperature: LLM temperature for controlling randomness (default 0.5)
        output_dir: Optional output directory
        session_id: Optional session identifier
    """
    
    if output_dir is None:
        output_dir = f"data/results/enhanced_experiments/{experiment_name}"
    
    if session_id is None:
        session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Set up LangSmith project
    project_name = f"C4-Sequential-{experiment_name}-{session_id}"
    os.environ["LANGCHAIN_PROJECT"] = project_name
    
    print(f"\n{'='*80}")
    print(f"🚀 STARTING EXPERIMENT: {experiment_name}")
    print(f"{'='*80}")
    print(f"🤖 Model: {model_name}")
    print(f"🌡️ Temperature: {temperature}")
    print(f"📁 Output: {output_dir}")
    print(f"📅 Session: {session_id}")
    print(f"{'='*80}\n")
    
    # Initialize LangSmith project
    initialize_langsmith_project(project_name, model_name)
    
    start_time = time.time()
    
    try:
        # Initialize runner and load briefs
        runner = EnhancedExperimentRunner()
        runner.load_system_briefs("data/briefs")
        
        # Run the experiment sequentially (max_workers=1)
        print(f"\n🔄 Running conditions sequentially (one at a time)...\n")
        results = runner.run_experiment(
            experiment_name, 
            model_name, 
            max_workers=1,  # Sequential execution
            temperature=temperature
        )
        
        duration = time.time() - start_time
        
        # Save results with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_file = Path(output_dir) / f"{experiment_name}_{timestamp}_final.json"
        results_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"\n{'='*80}")
        print(f"✅ EXPERIMENT COMPLETED: {experiment_name}")
        print(f"{'='*80}")
        print(f"⏱️ Duration: {duration/60:.1f} minutes")
        print(f"📄 Results saved to: {results_file}")
        
        # Print summary
        if "conditions" in results:
            print(f"\n📊 Summary:")
            conditions = results["conditions"]
            print(f"   Total Conditions: {len(conditions)}")
            total_runs = 0
            for condition_id, condition_data in conditions.items():
                summary = condition_data.get("condition_summary", {})
                runs = summary.get('total_runs', 0)
                total_runs += runs
                print(f"   • {condition_id}: {runs} runs")
            print(f"   Total Runs: {total_runs}")
        
        print(f"{'='*80}\n")
        
        return results
        
    except Exception as e:
        duration = time.time() - start_time
        print(f"\n{'='*80}")
        print(f"❌ EXPERIMENT FAILED: {experiment_name}")
        print(f"{'='*80}")
        print(f"🚨 Error: {str(e)}")
        print(f"⏱️ Duration: {duration/60:.1f} minutes")
        print(f"{'='*80}\n")
        raise


def run_all_experiments(
    model_name: str, 
    temperature: float = 0.5,
    output_dir: Optional[str] = None,
    session_id: Optional[str] = None
):
    """
    Run all experiments sequentially with LangSmith tracing.
    
    Args:
        model_name: LLM model to use
        temperature: LLM temperature for controlling randomness (default 0.5)
        output_dir: Optional output directory
        session_id: Optional session identifier
    """
    
    if output_dir is None:
        output_dir = "data/results/enhanced_experiments"
    
    if session_id is None:
        session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Set up LangSmith project
    project_name = f"C4-Sequential-AllExperiments-{session_id}"
    os.environ["LANGCHAIN_PROJECT"] = project_name
    
    print(f"\n{'='*80}")
    print(f"🚀 RUNNING ALL EXPERIMENTS SEQUENTIALLY")
    print(f"{'='*80}")
    print(f"🤖 Model: {model_name}")
    print(f"🌡️ Temperature: {temperature}")
    print(f"📁 Output: {output_dir}")
    print(f"📅 Session: {session_id}")
    print(f"{'='*80}\n")
    
    # Initialize LangSmith project
    initialize_langsmith_project(project_name, model_name)
    
    start_time = time.time()
    
    try:
        # Initialize runner and load briefs
        runner = EnhancedExperimentRunner()
        runner.load_system_briefs("data/briefs")
        
        # Get all experiment names
        all_experiments = list(runner.config.get("experiments", {}).keys())
        
        print(f"📋 Experiments to run: {len(all_experiments)}")
        for i, exp_name in enumerate(all_experiments, 1):
            exp_config = runner.config["experiments"][exp_name]
            print(f"   {i}. {exp_name}: {exp_config['name']}")
        print()
        
        # Run experiments one by one
        all_results = {
            "session_id": session_id,
            "model_name": model_name,
            "temperature": temperature,
            "start_time": datetime.now().isoformat(),
            "experiments": {}
        }
        
        for i, exp_name in enumerate(all_experiments, 1):
            print(f"\n{'='*80}")
            print(f"📊 Experiment {i}/{len(all_experiments)}: {exp_name}")
            print(f"{'='*80}\n")
            
            try:
                exp_result = runner.run_experiment(
                    exp_name, 
                    model_name,
                    max_workers=1,  # Sequential
                    temperature=temperature
                )
                all_results["experiments"][exp_name] = exp_result
                
                print(f"\n✅ Completed {i}/{len(all_experiments)}: {exp_name}")
                
            except Exception as e:
                print(f"\n❌ Failed {i}/{len(all_experiments)}: {exp_name}")
                print(f"   Error: {str(e)}")
                all_results["experiments"][exp_name] = {
                    "error": str(e),
                    "status": "failed"
                }
        
        duration = time.time() - start_time
        all_results["end_time"] = datetime.now().isoformat()
        all_results["total_duration_seconds"] = duration
        all_results["total_duration_hours"] = duration / 3600
        
        # Save comprehensive results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_file = Path(output_dir) / f"all_experiments_{timestamp}_final.json"
        results_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump(all_results, f, indent=2, ensure_ascii=False)
        
        print(f"\n{'='*80}")
        print(f"🎉 ALL EXPERIMENTS COMPLETED")
        print(f"{'='*80}")
        print(f"⏱️ Total Duration: {duration/60:.1f} minutes ({duration/3600:.2f} hours)")
        print(f"📄 Results saved to: {results_file}")
        
        # Print comprehensive summary
        print(f"\n📊 Summary:")
        total_conditions = 0
        successful_experiments = 0
        
        for exp_name, exp_results in all_results["experiments"].items():
            if "error" not in exp_results:
                successful_experiments += 1
                conditions = exp_results.get("conditions", {})
                total_conditions += len(conditions)
                print(f"   ✅ {exp_name}: {len(conditions)} conditions")
            else:
                print(f"   ❌ {exp_name}: {exp_results['error']}")
        
        print(f"\n🎯 Final Stats:")
        print(f"   Successful: {successful_experiments}/{len(all_experiments)}")
        print(f"   Total Conditions: {total_conditions}")
        print(f"{'='*80}\n")
        
        return all_results
        
    except Exception as e:
        duration = time.time() - start_time
        print(f"\n{'='*80}")
        print(f"❌ ALL EXPERIMENTS FAILED")
        print(f"{'='*80}")
        print(f"🚨 Error: {str(e)}")
        print(f"⏱️ Duration: {duration/60:.1f} minutes")
        print(f"{'='*80}\n")
        raise


def validate_environment():
    """Validate that the environment is properly configured."""
    issues = []
    
    # Check for required API keys based on model
    if not os.getenv("OPENAI_API_KEY"):
        issues.append("Missing OPENAI_API_KEY (required for GPT models)")
    
    if not os.getenv("GOOGLE_API_KEY"):
        issues.append("Missing GOOGLE_API_KEY (required for Gemini models)")
    
    # Check LangSmith configuration
    if not os.getenv("LANGCHAIN_API_KEY"):
        issues.append("Missing LANGCHAIN_API_KEY (required for tracing)")
    
    # Check for experiment config file
    if not Path("experiment_configs.yaml").exists():
        issues.append("Missing experiment_configs.yaml file")
    
    # Check for data directory
    if not Path("data/briefs").exists():
        issues.append("Missing data/briefs directory")
    
    if issues:
        print("⚠️ Environment Issues Found:")
        for issue in issues:
            print(f"   • {issue}")
        return False
    
    print("✅ Environment validation passed")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Sequential Experiment Runner for C4 Modeling Research (runs one at a time)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run single experiment with default settings
  python run_experiments.py --experiment role_ablation
  
  # Run single experiment with custom temperature
  python run_experiments.py --experiment role_ablation --temperature 0.7
  
  # Run all experiments sequentially
  python run_experiments.py --all-experiments
  
  # List available experiments
  python run_experiments.py --list-experiments
  
  # Validate environment
  python run_experiments.py --validate-env
  
  # Use specific model
  python run_experiments.py --experiment role_ablation --model gemini-2.5-flash-lite

Note: This runner executes everything sequentially (one at a time).
For parallel execution, use run_parallel_experiments.py instead.
        """
    )
    
    parser.add_argument(
        "--experiment", "-e",
        help="Name of specific experiment to run (e.g., role_ablation)"
    )
    
    parser.add_argument(
        "--all-experiments", "-a",
        action="store_true",
        help="Run all experiments"
    )
    
    parser.add_argument(
        "--list-experiments", "-l",
        action="store_true",
        help="List all available experiments"
    )
    
    parser.add_argument(
        "--model", "-m",
        default="gemini-2.5-flash-lite",
        help="LLM model to use (default: gemini-2.5-flash-lite)"
    )
    
    parser.add_argument(
        "--temperature", "-t",
        type=float,
        default=0.5,
        help="LLM temperature for controlling randomness (default: 0.5, range: 0.0-1.0)"
    )
    
    parser.add_argument(
        "--session-id", "-s",
        type=str,
        default=None,
        help="Custom session ID (default: auto-generated timestamp)"
    )
    
    parser.add_argument(
        "--output-dir", "-o",
        help="Output directory for results (default: auto-generated)"
    )
    
    parser.add_argument(
        "--validate-env", "-v",
        action="store_true",
        help="Validate environment configuration"
    )
    
    parser.add_argument(
        "--no-tracing",
        action="store_true",
        help="Disable LangSmith tracing"
    )
    
    args = parser.parse_args()
    
    # Handle no-tracing option
    if args.no_tracing:
        os.environ["LANGCHAIN_TRACING_V2"] = "false"
        print("🔇 LangSmith tracing disabled")
    
    # Handle list experiments
    if args.list_experiments:
        list_experiments()
        return
    
    # Handle environment validation
    if args.validate_env:
        if validate_environment():
            print("🎉 Environment is properly configured!")
        else:
            print("❌ Please fix environment issues before running experiments")
            sys.exit(1)
        return
    
    # Validate environment before running experiments
    if not validate_environment():
        print("❌ Environment validation failed. Use --validate-env for details.")
        sys.exit(1)
    
    # Handle experiments
    if args.all_experiments:
        run_all_experiments(
            args.model, 
            temperature=args.temperature,
            output_dir=args.output_dir,
            session_id=args.session_id
        )
    elif args.experiment:
        run_single_experiment(
            args.experiment, 
            args.model,
            temperature=args.temperature,
            output_dir=args.output_dir,
            session_id=args.session_id
        )
    else:
        print("❌ Please specify either --experiment <name> or --all-experiments")
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()