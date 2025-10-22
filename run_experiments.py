"""
Main experiment runner for the C4-Modeler-LLM-Agents journal extension.
Provides CLI interface to run individual experiments or full experimental suites.

Usage:
    python run_experiments.py --experiment role_ablation --model gpt-4o-mini
    python run_experiments.py --all-experiments --model gpt-4o-mini
    python run_experiments.py --list-experiments
"""

import argparse
import sys
import json
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
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "C4 Modeler Agents - Extended")

# Set up API keys for different LLM providers
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")
os.environ["DEEPSEEK_API_KEY"] = os.getenv("DEEPSEEK_API_KEY", "")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY", "")
os.environ["XAI_API_KEY"] = os.getenv("XAI_API_KEY", "")

# Import our experimental system
sys.path.insert(0, str(Path(__file__).parent / "src"))

from c4modeler.experiments import EnhancedExperimentRunner
from c4modeler.integration import validate_experiment_condition


def setup_tracing_context(experiment_name: str, model_name: str):
    """Set up LangSmith tracing context for the experiment."""
    import langsmith as ls
    
    # Create a project name specific to the experiment
    project_name = f"C4-Experiments-{experiment_name}-{model_name}"
    
    print(f"🔍 LangSmith Tracing Configuration:")
    print(f"   Project: {project_name}")
    print(f"   Tracing: {os.getenv('LANGCHAIN_TRACING_V2', 'disabled')}")
    
    return ls.tracing_context(
        project_name=project_name,
        enabled=True,
        tags=[experiment_name, model_name, "journal-extension"],
        metadata={
            "experiment_type": experiment_name,
            "model": model_name,
            "timestamp": datetime.now().isoformat(),
            "purpose": "journal-extension-experiments"
        }
    )


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


def run_single_experiment(experiment_name: str, model_name: str, output_dir: Optional[str] = None):
    """Run a single experiment with LangSmith tracing."""
    
    if output_dir is None:
        output_dir = f"data/results/enhanced_experiments/{experiment_name}"
    
    print(f"🚀 Running Experiment: {experiment_name}")
    print(f"🤖 Model: {model_name}")
    print(f"📁 Output Directory: {output_dir}")
    print("=" * 60)
    
    # Set up tracing context
    with setup_tracing_context(experiment_name, model_name):
        try:
            # Initialize runner and load briefs
            runner = EnhancedExperimentRunner()
            runner.load_system_briefs("data/briefs")
            
            # Run the experiment
            results = runner.run_experiment(experiment_name, model_name)
            
            # Save results with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            results_file = Path(output_dir) / f"{experiment_name}_{timestamp}_results.json"
            results_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(results_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            
            print(f"\n✅ Experiment completed successfully!")
            print(f"📄 Results saved to: {results_file}")
            
            # Print summary
            if "aggregate_results" in results:
                print(f"\n📊 Quick Summary:")
                conditions = results["conditions"]
                print(f"   Total Conditions: {len(conditions)}")
                for condition_id, condition_data in conditions.items():
                    summary = condition_data.get("condition_summary", {})
                    print(f"   {condition_id}: {summary.get('total_runs', 0)} runs")
            
            return results
            
        except Exception as e:
            print(f"❌ Experiment failed: {str(e)}")
            raise


def run_all_experiments(model_name: str, output_dir: Optional[str] = None):
    """Run all experiments with LangSmith tracing."""
    
    if output_dir is None:
        output_dir = "data/results/enhanced_experiments"
    
    print(f"🚀 Running ALL Experiments")
    print(f"🤖 Model: {model_name}")
    print(f"📁 Output Directory: {output_dir}")
    print("=" * 60)
    
    # Set up general tracing context
    with setup_tracing_context("all-experiments", model_name):
        try:
            # Initialize runner and load briefs
            runner = EnhancedExperimentRunner()
            runner.load_system_briefs("data/briefs")
            
            # Run all experiments
            all_results = runner.run_all_experiments(model_name)
            
            # Save comprehensive results
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            results_file = Path(output_dir) / f"all_experiments_{timestamp}_results.json"
            results_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(results_file, 'w', encoding='utf-8') as f:
                json.dump(all_results, f, indent=2, ensure_ascii=False)
            
            print(f"\n✅ All experiments completed!")
            print(f"📄 Results saved to: {results_file}")
            
            # Print comprehensive summary
            print(f"\n📊 Comprehensive Summary:")
            experiments = all_results.get("experiments", {})
            total_conditions = 0
            successful_experiments = 0
            
            for exp_name, exp_results in experiments.items():
                if "error" not in exp_results:
                    successful_experiments += 1
                    conditions = exp_results.get("conditions", {})
                    total_conditions += len(conditions)
                    print(f"   ✅ {exp_name}: {len(conditions)} conditions")
                else:
                    print(f"   ❌ {exp_name}: {exp_results['error']}")
            
            print(f"\n🎯 Final Stats:")
            print(f"   Successful Experiments: {successful_experiments}/{len(experiments)}")
            print(f"   Total Conditions: {total_conditions}")
            
            return all_results
            
        except Exception as e:
            print(f"❌ All experiments failed: {str(e)}")
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
        description="Run C4-Modeler-LLM-Agents experiments for journal extension",
        formatter_class=argparse.RawDescriptionHelpFormatter
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
        default="gpt-4o-mini",
        help="LLM model to use (default: gpt-4o-mini)"
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
        run_all_experiments(args.model, args.output_dir)
    elif args.experiment:
        run_single_experiment(args.experiment, args.model, args.output_dir)
    else:
        print("❌ Please specify either --experiment <name> or --all-experiments")
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()