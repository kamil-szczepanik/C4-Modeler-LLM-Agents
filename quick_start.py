#!/usr/bin/env python3
"""
Quick Start Script for Parallel Experiments
===========================================

This script provides an interactive CLI for starting experiments.

Usage:
    python quick_start.py
"""

import sys
import os
import subprocess
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from dotenv import load_dotenv
load_dotenv()


def check_environment():
    """Check if environment is properly configured."""
    print("\n🔍 Checking Environment...")
    print("="*60)
    
    issues = []
    
    # Check API keys
    api_keys = {
        "GOOGLE_API_KEY": "Google (Gemini)",
        "OPENAI_API_KEY": "OpenAI (GPT)",
        "DEEPSEEK_API_KEY": "DeepSeek"
    }
    
    print("\n📋 API Keys:")
    for key, provider in api_keys.items():
        if os.getenv(key):
            print(f"  ✅ {provider}: Set")
        else:
            print(f"  ⚠️  {provider}: Not set")
    
    # Check critical files
    print("\n📁 Configuration Files:")
    files_to_check = [
        "experiment_configs.yaml",
        "data/briefs/clinic-management-system.yaml",
        "data/briefs/library-management-system.yaml"
    ]
    
    for file in files_to_check:
        if Path(file).exists():
            print(f"  ✅ {file}")
        else:
            print(f"  ❌ {file} - MISSING!")
            issues.append(f"Missing file: {file}")
    
    # Check LangSmith (optional)
    print("\n🔍 LangSmith Tracing:")
    if os.getenv("LANGCHAIN_API_KEY"):
        print(f"  ✅ Enabled")
    else:
        print(f"  ⚠️  Disabled (optional)")
    
    print("\n" + "="*60)
    
    if issues:
        print("\n❌ Issues found:")
        for issue in issues:
            print(f"  - {issue}")
        return False
    else:
        print("\n✅ Environment check passed!")
        return True


def show_menu():
    """Display the main menu."""
    print("\n" + "="*60)
    print("🚀 C4 MODELER - PARALLEL EXPERIMENT LAUNCHER")
    print("="*60)
    print("\n📊 Choose execution mode:\n")
    print("  1. 🎯 Full Study - All 300 runs (parallel, ~6-8 hours)")
    print("  2. 🧪 Single Experiment (select which one)")
    print("  3. 📋 Custom - Choose experiments to run")
    print("  4. 👀 Dry Run - Show execution plan")
    print("  5. 📊 Check Progress - View current study status")
    print("  6. 🔍 Environment Check")
    print("  7. ❌ Exit")
    print("\n" + "="*60)


def get_model_choice():
    """Get model selection from user."""
    print("\n🤖 Select Model:\n")
    print("  1. gemini-2.5-flash-lite (Recommended, fast, cheap)")
    print("  2. gemini-2.5-flash")
    print("  3. gpt-4o-mini")
    print("  4. gpt-4o")
    print("  5. Custom")
    
    choice = input("\nEnter choice (1-5) [1]: ").strip() or "1"
    
    models = {
        "1": "gemini-2.5-flash-lite",
        "2": "gemini-2.5-flash",
        "3": "gpt-4o-mini",
        "4": "gpt-4o"
    }
    
    if choice == "5":
        return input("Enter custom model name: ").strip()
    
    return models.get(choice, "gemini-2.5-flash-lite")


def run_full_study():
    """Run the complete study with all experiments."""
    print("\n🎯 FULL STUDY MODE")
    print("="*60)
    
    model = get_model_choice()
    
    print(f"\n📊 Configuration:")
    print(f"  Model: {model}")
    print(f"  Experiments: All 5")
    print(f"  Total runs: 300")
    print(f"  Estimated time: 6-8 hours")
    print(f"  Estimated cost: $60-105")
    
    confirm = input("\n⚠️  This will run for several hours. Continue? (yes/no) [no]: ").strip().lower()
    
    if confirm == "yes":
        print("\n🚀 Starting parallel experiments...")
        print("💡 Tip: Use Ctrl+C to interrupt (progress will be saved)")
        
        cmd = [
            "python", "run_parallel_experiments.py",
            "--model", model,
            "--max-experiments", "3",
            "--max-conditions", "2"
        ]
        
        subprocess.run(cmd)
    else:
        print("❌ Cancelled")


def run_single_experiment():
    """Run a single experiment."""
    print("\n🧪 SINGLE EXPERIMENT MODE")
    print("="*60)
    
    experiments = {
        "1": ("role_ablation", "Role Ablation"),
        "2": ("interaction_order", "Interaction Order"),
        "3": ("specialization", "Agent Specialization"),
        "4": ("shared_memory", "Shared Memory"),
        "5": ("diversity", "Team Diversity")
    }
    
    print("\nSelect experiment:\n")
    for key, (_, name) in experiments.items():
        print(f"  {key}. {name}")
    
    choice = input("\nEnter choice (1-5): ").strip()
    
    if choice not in experiments:
        print("❌ Invalid choice")
        return
    
    exp_id, exp_name = experiments[choice]
    model = get_model_choice()
    
    print(f"\n📊 Configuration:")
    print(f"  Experiment: {exp_name}")
    print(f"  Model: {model}")
    print(f"  Estimated time: 1-2 hours")
    
    confirm = input("\nContinue? (yes/no) [yes]: ").strip().lower() or "yes"
    
    if confirm == "yes":
        print(f"\n🚀 Starting {exp_name}...")
        
        cmd = [
            "python", "run_parallel_experiments.py",
            "--model", model,
            "--experiments", exp_id
        ]
        
        subprocess.run(cmd)
    else:
        print("❌ Cancelled")


def run_custom():
    """Run custom selection of experiments."""
    print("\n📋 CUSTOM EXPERIMENT SELECTION")
    print("="*60)
    
    all_experiments = [
        "role_ablation",
        "interaction_order",
        "specialization",
        "shared_memory",
        "diversity"
    ]
    
    print("\nAvailable experiments:")
    for i, exp in enumerate(all_experiments, 1):
        print(f"  {i}. {exp}")
    
    selections = input("\nEnter numbers separated by spaces (e.g., 1 2 3): ").strip().split()
    
    try:
        selected_experiments = [all_experiments[int(s)-1] for s in selections]
    except (ValueError, IndexError):
        print("❌ Invalid selection")
        return
    
    model = get_model_choice()
    
    print(f"\n📊 Configuration:")
    print(f"  Experiments: {', '.join(selected_experiments)}")
    print(f"  Model: {model}")
    
    confirm = input("\nContinue? (yes/no) [yes]: ").strip().lower() or "yes"
    
    if confirm == "yes":
        print("\n🚀 Starting experiments...")
        
        cmd = [
            "python", "run_parallel_experiments.py",
            "--model", model,
            "--experiments"
        ] + selected_experiments
        
        subprocess.run(cmd)
    else:
        print("❌ Cancelled")


def run_dry_run():
    """Show execution plan without running."""
    print("\n👀 DRY RUN MODE")
    print("="*60)
    
    model = get_model_choice()
    
    cmd = [
        "python", "run_parallel_experiments.py",
        "--model", model,
        "--dry-run"
    ]
    
    subprocess.run(cmd)


def check_progress():
    """Check progress of current or previous studies."""
    print("\n📊 CHECKING PROGRESS")
    print("="*60)
    
    # Check for progress files
    progress_dir = Path("data/results/parallel_experiments")
    
    if not progress_dir.exists():
        print("\n❌ No experiments have been run yet")
        return
    
    checkpoint_files = list(progress_dir.glob("*checkpoint*.json"))
    final_files = list(progress_dir.glob("*final*.json"))
    
    if final_files:
        print(f"\n✅ Found {len(final_files)} completed study sessions")
        latest = max(final_files, key=lambda p: p.stat().st_mtime)
        print(f"   Latest: {latest.name}")
    
    if checkpoint_files:
        print(f"\n⏳ Found {len(checkpoint_files)} progress checkpoints")
        latest = max(checkpoint_files, key=lambda p: p.stat().st_mtime)
        print(f"   Latest: {latest.name}")
    
    # Check artifacts
    artifact_dirs = list(Path("data/results/enhanced_experiments").rglob("c4_artifacts/*"))
    if artifact_dirs:
        print(f"\n💾 Found {len(artifact_dirs)} saved C4 model artifacts")
    
    print("\n💡 Use the notebook or Python scripts to analyze detailed results")


def main():
    """Main interactive loop."""
    
    while True:
        show_menu()
        choice = input("\nEnter choice (1-7): ").strip()
        
        if choice == "1":
            run_full_study()
        elif choice == "2":
            run_single_experiment()
        elif choice == "3":
            run_custom()
        elif choice == "4":
            run_dry_run()
        elif choice == "5":
            check_progress()
        elif choice == "6":
            check_environment()
        elif choice == "7":
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        # Initial environment check
        if not check_environment():
            print("\n⚠️  Please fix environment issues before continuing")
            input("Press Enter to continue anyway, or Ctrl+C to exit...")
        
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user. Goodbye!")
        sys.exit(0)
