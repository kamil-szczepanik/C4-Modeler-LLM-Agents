"""
Parallel Experiment Orchestrator for C4 Modeling Research
==========================================================

This script orchestrates parallel execution of all 5 experiments, maximizing throughput
while respecting API rate limits and system resources.

Features:
- Parallel experiment execution (multiple experiments simultaneously)
- Parallel condition execution within experiments
- Automatic artifact saving after each run
- Progress checkpointing and recovery
- Resource management and rate limiting
- Comprehensive logging and monitoring

Usage:
    # Run all experiments in parallel (recommended)
    python run_parallel_experiments.py --model gemini-2.5-flash-lite
    
    # Run specific experiments
    python run_parallel_experiments.py --experiments role_ablation interaction_order
    
    # Control parallelism
    python run_parallel_experiments.py --max-experiments 3 --max-conditions 2
    
    # Dry run (show execution plan without running)
    python run_parallel_experiments.py --dry-run

Author: Research Team
Date: October 2025
"""

import sys
import os
import json
import argparse
import time
import signal
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
from concurrent.futures import ProcessPoolExecutor, as_completed, ThreadPoolExecutor
import multiprocessing as mp

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Environment setup
from dotenv import load_dotenv
load_dotenv()

# Configure base tracing
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "true")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")

from c4modeler.experiments import EnhancedExperimentRunner

# LangChain imports for project starter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# Global flag for graceful shutdown
shutdown_requested = False

def signal_handler(signum, frame):
    """Handle Ctrl+C gracefully."""
    global shutdown_requested
    if not shutdown_requested:
        shutdown_requested = True
        print(f"\n\n{Colors.BRIGHT_YELLOW}{'='*80}{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}⚠️  SHUTDOWN REQUESTED - Finishing current operations...{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}{'='*80}{Colors.RESET}")
        print(f"{Colors.DIM}All progress has been saved. Press Ctrl+C again to force quit.{Colors.RESET}\n")
    else:
        print(f"\n{Colors.BRIGHT_RED}Forcing shutdown...{Colors.RESET}\n")
        sys.exit(1)

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_CYAN = '\033[96m'


# ============================================================================
# LANGSMITH PROJECT INITIALIZATION
# ============================================================================

def initialize_langsmith_project(project_name: str, model_name: str):
    """
    Initialize LangSmith project by running a simple chain.
    This makes the project visible in LangSmith UI immediately.
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


# ============================================================================
# EXPERIMENT EXECUTION FUNCTIONS
# ============================================================================

def run_single_experiment_parallel(
    experiment_name: str,
    model_name: str,
    max_workers: int = 2,
    session_id: str = None,
    temperature: float = 0.5
    ) -> Dict[str, Any]:
    """
    Run a single experiment with parallel condition execution.
    
    This function is designed to be called in a separate process.
    
    Args:
        experiment_name: Name of the experiment to run
        model_name: LLM model to use
        max_workers: Maximum parallel conditions
        session_id: Unique session identifier
        temperature: LLM temperature for controlling randomness (default 0.5)
    """
    # Set up tracing for this process
    experiment_project_name = f"C4-Parallel-{experiment_name}-{session_id}"
    os.environ["LANGCHAIN_PROJECT"] = experiment_project_name
    
    # Initialize this experiment's project in LangSmith
    initialize_langsmith_project(experiment_project_name, model_name)
    
    print(f"\n{'='*80}")
    print(f"🚀 STARTING EXPERIMENT: {experiment_name}")
    print(f"{'='*80}")
    print(f"🤖 Model: {model_name}")
    print(f"🌡️ Temperature: {temperature}")
    print(f"⚙️ Max parallel conditions: {max_workers}")
    print(f"📅 Session: {session_id}")
    
    start_time = time.time()
    
    try:
        # Initialize runner in this process
        runner = EnhancedExperimentRunner("experiment_configs.yaml")
        runner.load_system_briefs("data/briefs")
        
        # Run the experiment (conditions will be parallelized internally)
        result = runner.run_experiment(experiment_name, model_name, max_workers=max_workers, temperature=temperature)
        
        duration = time.time() - start_time
        
        print(f"\n{'='*80}")
        print(f"✅ COMPLETED: {experiment_name}")
        print(f"⏱️ Duration: {duration/60:.1f} minutes")
        print(f"{'='*80}\n")
        
        return {
            "experiment_name": experiment_name,
            "status": "success",
            "duration_seconds": duration,
            "result": result
        }
        
    except Exception as e:
        duration = time.time() - start_time
        
        print(f"\n{'='*80}")
        print(f"❌ FAILED: {experiment_name}")
        print(f"🚨 Error: {str(e)}")
        print(f"⏱️ Duration: {duration/60:.1f} minutes")
        print(f"{'='*80}\n")
        
        return {
            "experiment_name": experiment_name,
            "status": "failed",
            "duration_seconds": duration,
            "error": str(e)
        }


def run_parallel_experiments(
    experiments: List[str],
    model_name: str,
    max_experiment_workers: int = 3,
    max_condition_workers: int = 2,
    session_id: Optional[str] = None,
    temperature: float = 0.5
) -> Dict[str, Any]:
    """
    Run multiple experiments in parallel using process pool.
    
    Args:
        experiments: List of experiment names to run
        model_name: LLM model to use
        max_experiment_workers: Max number of experiments to run simultaneously
        max_condition_workers: Max parallel conditions within each experiment
        session_id: Unique session identifier
        temperature: LLM temperature for controlling randomness (default 0.5)
    
    Returns:
        Dictionary with all results and metadata
    """
    if session_id is None:
        session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Set up the main project name
    main_project_name = f"C4-Parallel-Study-{session_id}"
    
    # Initialize LangSmith project to make it visible immediately
    print("\n" + "="*80)
    print("🔧 LANGSMITH INITIALIZATION")
    print("="*80)
    initialize_langsmith_project(main_project_name, model_name)
    print("="*80)
    
    print("\n" + "="*80)
    print("🚀 PARALLEL EXPERIMENT ORCHESTRATOR")
    print("="*80)
    print(f"📊 Experiments to run: {len(experiments)}")
    print(f"🔧 Max parallel experiments: {max_experiment_workers}")
    print(f"⚙️ Max parallel conditions per experiment: {max_condition_workers}")
    print(f"🤖 Model: {model_name}")
    print(f"🌡️ Temperature: {temperature}")
    print(f"📅 Session ID: {session_id}")
    print(f"⏰ Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)
    
    orchestrator_start = time.time()
    
    # Results tracking
    all_results = {
        "session_id": session_id,
        "model_name": model_name,
        "temperature": temperature,
        "start_time": datetime.now().isoformat(),
        "experiments": {},
        "summary": {}
    }
    
    # Use ProcessPoolExecutor for true parallelism
    with ProcessPoolExecutor(max_workers=max_experiment_workers) as executor:
        # Submit all experiments
        future_to_experiment = {
            executor.submit(
                run_single_experiment_parallel,
                exp_name,
                model_name,
                max_condition_workers,
                session_id,
                temperature
            ): exp_name
            for exp_name in experiments
        }
        
        print(f"\n📋 Submitted {len(experiments)} experiments to executor")
        print("⏳ Waiting for experiments to complete...\n")
        
        # Process results as they complete
        completed_count = 0
        for future in as_completed(future_to_experiment):
            exp_name = future_to_experiment[future]
            completed_count += 1
            
            try:
                result = future.result()
                all_results["experiments"][exp_name] = result
                
                status_icon = "✅" if result["status"] == "success" else "❌"
                print(f"{status_icon} [{completed_count}/{len(experiments)}] {exp_name} - {result['status']}")
                
                # Save intermediate progress
                save_orchestrator_progress(all_results, session_id, completed_count)
                
            except Exception as e:
                print(f"❌ [{completed_count}/{len(experiments)}] {exp_name} - exception: {str(e)}")
                all_results["experiments"][exp_name] = {
                    "experiment_name": exp_name,
                    "status": "exception",
                    "error": str(e)
                }
    
    # Finalize results
    orchestrator_end = time.time()
    total_duration = orchestrator_end - orchestrator_start
    
    all_results["end_time"] = datetime.now().isoformat()
    all_results["total_duration_seconds"] = total_duration
    all_results["total_duration_hours"] = total_duration / 3600
    
    # Calculate summary statistics
    successful = len([r for r in all_results["experiments"].values() if r["status"] == "success"])
    failed = len(all_results["experiments"]) - successful
    
    all_results["summary"] = {
        "total_experiments": len(experiments),
        "successful": successful,
        "failed": failed,
        "success_rate": (successful / len(experiments) * 100) if experiments else 0,
        "average_duration_minutes": sum(
            r.get("duration_seconds", 0) for r in all_results["experiments"].values()
        ) / len(experiments) / 60 if experiments else 0
    }
    
    # Save final results
    save_final_orchestrator_results(all_results, session_id)
    
    # Print final summary
    print_final_summary(all_results)
    
    return all_results


def save_orchestrator_progress(results: Dict, session_id: str, checkpoint: int):
    """Save intermediate progress of the orchestrator."""
    progress_dir = Path("data/results/parallel_experiments")
    progress_dir.mkdir(parents=True, exist_ok=True)
    
    progress_file = progress_dir / f"session_{session_id}_checkpoint_{checkpoint}.json"
    
    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"  💾 Progress saved: {progress_file.name}")


def save_final_orchestrator_results(results: Dict, session_id: str):
    """Save final orchestrator results."""
    results_dir = Path("data/results/parallel_experiments")
    results_dir.mkdir(parents=True, exist_ok=True)
    
    final_file = results_dir / f"session_{session_id}_final.json"
    
    with open(final_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Final results saved: {final_file}")


def print_final_summary(results: Dict):
    """Print comprehensive final summary."""
    print("\n" + "="*80)
    print("🎉 PARALLEL EXECUTION COMPLETE")
    print("="*80)
    
    summary = results["summary"]
    
    print(f"⏰ Total Duration: {results['total_duration_hours']:.2f} hours")
    print(f"📊 Experiments: {summary['total_experiments']}")
    print(f"✅ Successful: {summary['successful']}")
    print(f"❌ Failed: {summary['failed']}")
    print(f"📈 Success Rate: {summary['success_rate']:.1f}%")
    print(f"⏱️ Average Duration: {summary['average_duration_minutes']:.1f} minutes per experiment")
    
    print(f"\n📋 Individual Experiment Results:")
    for exp_name, exp_result in results["experiments"].items():
        status_icon = "✅" if exp_result["status"] == "success" else "❌"
        duration = exp_result.get("duration_seconds", 0) / 60
        print(f"  {status_icon} {exp_name}: {exp_result['status']} ({duration:.1f} min)")
    
    print("\n" + "="*80)


def show_execution_plan(
    experiments: List[str],
    model_name: str,
    max_experiment_workers: int,
    max_condition_workers: int
):
    """Display the execution plan without running experiments."""
    
    # Load configuration
    runner = EnhancedExperimentRunner("experiment_configs.yaml")
    runner.load_system_briefs("data/briefs")
    
    print("\n" + "="*80)
    print("📋 EXECUTION PLAN (DRY RUN)")
    print("="*80)
    print(f"🤖 Model: {model_name}")
    print(f"🔧 Max parallel experiments: {max_experiment_workers}")
    print(f"⚙️ Max parallel conditions per experiment: {max_condition_workers}")
    
    total_runs = 0
    estimated_time_sequential = 0
    estimated_time_parallel = 0
    
    print(f"\n📊 Experiments to Execute:")
    for i, exp_name in enumerate(experiments, 1):
        exp_config = runner.config["experiments"][exp_name]
        conditions = len(exp_config["conditions"])
        datasets = len(runner.briefs)
        rounds = runner.config["protocol"]["rounds_per_condition"]
        
        exp_runs = conditions * datasets * rounds
        total_runs += exp_runs
        
        # Estimate time (30 min per run)
        exp_sequential_time = exp_runs * 30  # minutes
        exp_parallel_time = exp_sequential_time / max_condition_workers  # rough estimate
        
        estimated_time_sequential += exp_sequential_time
        estimated_time_parallel = max(estimated_time_parallel, exp_parallel_time)
        
        print(f"\n  {i}. {exp_config['name']}")
        print(f"     ID: {exp_name}")
        print(f"     Conditions: {conditions}")
        print(f"     Datasets: {datasets}")
        print(f"     Rounds: {rounds}")
        print(f"     Total runs: {exp_runs}")
        print(f"     Est. time (sequential): {exp_sequential_time/60:.1f} hours")
        print(f"     Est. time (parallel): {exp_parallel_time/60:.1f} hours")
    
    print(f"\n{'='*80}")
    print(f"📈 TOTALS:")
    print(f"   Total experiments: {len(experiments)}")
    print(f"   Total runs: {total_runs}")
    print(f"   Est. sequential time: {estimated_time_sequential/60:.1f} hours")
    print(f"   Est. parallel time: {estimated_time_parallel/60:.1f} hours")
    print(f"   Time savings: {(1 - estimated_time_parallel/estimated_time_sequential)*100:.1f}%")
    print(f"   Cost estimate (Gemini): ${total_runs * 0.25:.2f} - ${total_runs * 0.35:.2f}")
    print(f"{'='*80}\n")


# ============================================================================
# MAIN CLI
# ============================================================================

def main():
    # Set up signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    
    parser = argparse.ArgumentParser(
        description="Run C4 modeling experiments in parallel",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run all experiments with default settings
  python run_parallel_experiments.py --model gemini-2.5-flash-lite
  
  # Run specific experiments
  python run_parallel_experiments.py --experiments role_ablation interaction_order
  
  # Control parallelism for resource management
  python run_parallel_experiments.py --max-experiments 2 --max-conditions 3
  
  # Show execution plan without running
  python run_parallel_experiments.py --dry-run
  
  # Resume from a specific session (manual recovery)
  python run_parallel_experiments.py --session-id 20241023_140000
        """
    )
    
    parser.add_argument(
        '--model',
        type=str,
        default='gemini-2.5-flash-lite',
        help='LLM model to use (default: gemini-2.5-flash-lite)'
    )
    
    parser.add_argument(
        '--experiments',
        type=str,
        nargs='+',
        default=None,
        help='Specific experiments to run (default: all)'
    )
    
    parser.add_argument(
        '--max-experiments',
        type=int,
        default=3,
        help='Maximum number of experiments to run in parallel (default: 3)'
    )
    
    parser.add_argument(
        '--max-conditions',
        type=int,
        default=2,
        help='Maximum number of conditions to run in parallel per experiment (default: 2)'
    )
    
    parser.add_argument(
        '--session-id',
        type=str,
        default=None,
        help='Custom session ID (default: auto-generated timestamp)'
    )
    
    parser.add_argument(
        '--temperature',
        type=float,
        default=0.5,
        help='LLM temperature for controlling randomness (default: 0.5, range: 0.0-1.0)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show execution plan without running experiments'
    )
    
    args = parser.parse_args()
    
    # Load available experiments
    runner = EnhancedExperimentRunner("experiment_configs.yaml")
    all_experiments = list(runner.config.get("experiments", {}).keys())
    
    # Determine which experiments to run
    if args.experiments:
        experiments_to_run = args.experiments
        # Validate experiment names
        invalid = [e for e in experiments_to_run if e not in all_experiments]
        if invalid:
            print(f"❌ Error: Invalid experiment names: {invalid}")
            print(f"Available experiments: {all_experiments}")
            sys.exit(1)
    else:
        experiments_to_run = all_experiments
    
    # Dry run mode
    if args.dry_run:
        show_execution_plan(
            experiments_to_run,
            args.model,
            args.max_experiments,
            args.max_conditions
        )
        return
    
    # Validate API keys
    required_keys = {
        'gpt': 'OPENAI_API_KEY',
        'gemini': 'GOOGLE_API_KEY',
        'deepseek': 'DEEPSEEK_API_KEY'
    }
    
    model_provider = None
    for provider, key_name in required_keys.items():
        if provider in args.model.lower():
            model_provider = provider
            if not os.getenv(key_name):
                print(f"❌ Error: {key_name} not set in environment")
                print(f"Please configure your .env file with the required API key")
                sys.exit(1)
            break
    
    # Run parallel experiments
    print("\n🚀 Starting parallel experiment execution...")
    print(f"💡 Tip: Monitor progress in separate terminal with:")
    print(f"   python monitor_experiments.py --experiment role_ablation --refresh 5")
    print(f"\n📊 LangSmith Monitoring:")
    print(f"   Main project: C4-Parallel-Study-{args.session_id if args.session_id else datetime.now().strftime('%Y%m%d_%H%M%S')}")
    print(f"   View at: https://smith.langchain.com/")
    print(f"   Individual experiments will appear as: C4-Parallel-{{experiment}}-{{session_id}}")
    print(f"\n{Colors.BRIGHT_YELLOW}⚠️  To stop: Press Ctrl+C (will finish current operation safely){Colors.RESET}")
    print(f"{Colors.DIM}   All progress is auto-saved after each condition completes{Colors.RESET}\n")
    
    try:
        results = run_parallel_experiments(
            experiments=experiments_to_run,
            model_name=args.model,
            max_experiment_workers=args.max_experiments,
            max_condition_workers=args.max_conditions,
            session_id=args.session_id,
            temperature=args.temperature
        )
    except KeyboardInterrupt:
        print(f"\n\n{Colors.BRIGHT_YELLOW}{'='*80}{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}⚠️  EXPERIMENT INTERRUPTED BY USER{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}{'='*80}{Colors.RESET}")
        print(f"{Colors.BRIGHT_GREEN}✅ Progress has been saved!{Colors.RESET}")
        print(f"\n📂 Check saved results:")
        print(f"   Progress files: data/results/enhanced_experiments/*_progress_*.json")
        print(f"   Artifacts: data/results/enhanced_experiments/*/c4_artifacts/")
        print(f"\n💡 To view what was completed:")
        print(f"   python monitor_experiments.py")
        print(f"\n{Colors.BRIGHT_YELLOW}{'='*80}{Colors.RESET}\n")
        sys.exit(130)  # Standard exit code for Ctrl+C
    
    # Print artifact locations
    print(f"\n📂 ARTIFACTS SAVED TO:")
    print(f"   Experiment artifacts: data/results/enhanced_experiments/")
    print(f"   Orchestrator results: data/results/parallel_experiments/")
    print(f"   Session ID: {results['session_id']}")
    
    sys.exit(0 if results['summary']['failed'] == 0 else 1)


if __name__ == "__main__":
    # Ensure proper multiprocessing on Windows
    mp.freeze_support()
    main()
