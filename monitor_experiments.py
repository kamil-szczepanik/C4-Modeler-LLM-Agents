"""
Real-Time Experiment Progress Monitor
=====================================

Beautiful terminal-based progress visualization for running experiments.
Shows live updates of experiment progress, artifact creation, and statistics.

Usage:
    # Monitor all experiments
    python monitor_experiments.py
    
    # Monitor specific session
    python monitor_experiments.py --session-id 20241023_153022
    
    # Auto-refresh every 5 seconds
    python monitor_experiments.py --refresh 5
    
    # Compact view
    python monitor_experiments.py --compact

Author: Research Team
Date: October 2025
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from collections import defaultdict

# ANSI color codes for terminal
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Foreground colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_RED = '\033[41m'
    BG_BLUE = '\033[44m'


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def create_progress_bar(current: int, total: int, width: int = 40, fill_char: str = '█', empty_char: str = '░') -> str:
    """Create a visual progress bar."""
    if total == 0:
        percentage = 0
    else:
        percentage = (current / total) * 100
    
    filled = int(width * current / total) if total > 0 else 0
    empty = width - filled
    
    bar = fill_char * filled + empty_char * empty
    
    # Color based on progress
    if percentage >= 100:
        color = Colors.BRIGHT_GREEN
    elif percentage >= 75:
        color = Colors.GREEN
    elif percentage >= 50:
        color = Colors.YELLOW
    elif percentage >= 25:
        color = Colors.BRIGHT_YELLOW
    else:
        color = Colors.CYAN
    
    return f"{color}{bar}{Colors.RESET} {current}/{total} ({percentage:.1f}%)"


def format_duration(seconds: float) -> str:
    """Format duration in human-readable format."""
    if seconds < 60:
        return f"{seconds:.0f}s"
    elif seconds < 3600:
        return f"{seconds/60:.1f}m"
    else:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        return f"{hours}h {minutes}m"


def estimate_remaining_time(completed: int, total: int, elapsed_seconds: float) -> str:
    """Estimate remaining time based on current progress."""
    if completed == 0 or total == 0:
        return "calculating..."
    
    avg_time_per_item = elapsed_seconds / completed
    remaining_items = total - completed
    remaining_seconds = avg_time_per_item * remaining_items
    
    return format_duration(remaining_seconds)


def scan_for_sessions() -> List[Dict[str, Any]]:
    """Scan for active and completed experiment sessions."""
    results_dir = Path("data/results/parallel_experiments")
    
    if not results_dir.exists():
        return []
    
    sessions = {}
    
    # Scan for session files
    for file_path in results_dir.glob("session_*_*.json"):
        filename = file_path.name
        
        # Extract session ID
        if "checkpoint" in filename:
            session_id = filename.replace("session_", "").replace("_checkpoint_", "_").rsplit("_", 1)[0]
            file_type = "checkpoint"
        elif "final" in filename:
            session_id = filename.replace("session_", "").replace("_final.json", "")
            file_type = "final"
        else:
            continue
        
        # Load the file
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if session_id not in sessions:
                sessions[session_id] = {
                    "session_id": session_id,
                    "files": [],
                    "latest_data": None,
                    "status": "unknown",
                    "last_update": None
                }
            
            sessions[session_id]["files"].append({
                "path": file_path,
                "type": file_type,
                "modified": datetime.fromtimestamp(file_path.stat().st_mtime)
            })
            
            # Keep the most recent data
            if (sessions[session_id]["last_update"] is None or 
                datetime.fromtimestamp(file_path.stat().st_mtime) > sessions[session_id]["last_update"]):
                sessions[session_id]["latest_data"] = data
                sessions[session_id]["last_update"] = datetime.fromtimestamp(file_path.stat().st_mtime)
                sessions[session_id]["status"] = "completed" if file_type == "final" else "in_progress"
        
        except Exception as e:
            print(f"Warning: Could not read {file_path}: {e}")
    
    return list(sessions.values())


def scan_experiment_progress(experiment_name: str) -> Dict[str, Any]:
    """Scan for experiment-level progress files."""
    results_dir = Path("data/results/enhanced_experiments")
    
    if not results_dir.exists():
        return {}
    
    # Look for both progress and final files
    progress_files = list(results_dir.glob(f"{experiment_name}_progress_*.json"))
    final_files = list(results_dir.glob(f"{experiment_name}_final_*.json"))
    all_files = progress_files + final_files
    
    if not all_files:
        return {}
    
    # Get the most recent file
    latest_file = max(all_files, key=lambda p: p.stat().st_mtime)
    
    try:
        with open(latest_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            data['_source_file'] = latest_file.name
            data['_is_final'] = 'final' in latest_file.name
            return data
    except Exception:
        return {}


def count_artifacts(experiment_name: str) -> Dict[str, int]:
    """Count generated artifacts for an experiment."""
    artifact_dir = Path(f"data/results/enhanced_experiments/{experiment_name}/c4_artifacts")
    
    if not artifact_dir.exists():
        return {"total_runs": 0, "total_files": 0}
    
    runs = list(artifact_dir.iterdir())
    total_files = sum(len(list(run_dir.glob("**/*"))) for run_dir in runs if run_dir.is_dir())
    
    return {
        "total_runs": len(runs),
        "total_files": total_files
    }


def display_session_overview(sessions: List[Dict[str, Any]], compact: bool = False):
    """Display overview of all sessions."""
    print(f"\n{Colors.BOLD}{Colors.BRIGHT_CYAN}{'='*80}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}📊 EXPERIMENT SESSIONS OVERVIEW{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}{'='*80}{Colors.RESET}\n")
    
    if not sessions:
        print(f"{Colors.YELLOW}No experiment sessions found.{Colors.RESET}")
        print(f"{Colors.DIM}Run experiments first: python run_parallel_experiments.py{Colors.RESET}\n")
        return
    
    for session in sorted(sessions, key=lambda s: s["last_update"], reverse=True):
        status_icon = "✅" if session["status"] == "completed" else "🔄"
        status_color = Colors.BRIGHT_GREEN if session["status"] == "completed" else Colors.BRIGHT_YELLOW
        
        print(f"{status_icon} {Colors.BOLD}Session: {session['session_id']}{Colors.RESET}")
        print(f"   Status: {status_color}{session['status'].upper()}{Colors.RESET}")
        print(f"   Last Update: {session['last_update'].strftime('%Y-%m-%d %H:%M:%S')}")
        
        if session["latest_data"]:
            data = session["latest_data"]
            
            # Summary
            if "summary" in data:
                summary = data["summary"]
                total = summary.get("total_experiments", 0)
                successful = summary.get("successful", 0)
                failed = summary.get("failed", 0)
                
                print(f"   Progress: {successful}/{total} experiments completed")
                
                if not compact:
                    if "experiments" in data:
                        for exp_name, exp_data in data["experiments"].items():
                            exp_status = exp_data.get("status", "unknown")
                            exp_icon = "✅" if exp_status == "success" else "❌" if exp_status == "failed" else "🔄"
                            duration = exp_data.get("duration_seconds", 0)
                            print(f"      {exp_icon} {exp_name}: {exp_status} ({format_duration(duration)})")
        
        print()


def display_detailed_progress(session_id: str, refresh_interval: int = 10, compact: bool = False):
    """Display detailed progress for a specific session with auto-refresh."""
    
    try:
        while True:
            clear_screen()
            
            # Header
            print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}{'='*80}{Colors.RESET}")
            print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}🔍 LIVE EXPERIMENT MONITOR - Session: {session_id}{Colors.RESET}")
            print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}{'='*80}{Colors.RESET}")
            print(f"{Colors.DIM}Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Auto-refresh every {refresh_interval}s | Press Ctrl+C to exit{Colors.RESET}\n")
            
            # Find session data
            sessions = scan_for_sessions()
            session_data = next((s for s in sessions if s["session_id"] == session_id), None)
            
            if not session_data:
                print(f"{Colors.YELLOW}Session '{session_id}' not found.{Colors.RESET}\n")
                available = [s["session_id"] for s in sessions]
                if available:
                    print(f"Available sessions: {', '.join(available)}\n")
                time.sleep(refresh_interval)
                continue
            
            data = session_data["latest_data"]
            
            # Overall progress
            print(f"{Colors.BOLD}📈 Overall Progress:{Colors.RESET}")
            
            if "summary" in data:
                summary = data["summary"]
                total_exp = summary.get("total_experiments", 0)
                completed_exp = summary.get("successful", 0) + summary.get("failed", 0)
                
                progress_bar = create_progress_bar(completed_exp, total_exp, width=50)
                print(f"   Experiments: {progress_bar}")
                
                if "start_time" in data:
                    start_time = datetime.fromisoformat(data["start_time"])
                    elapsed = (datetime.now() - start_time).total_seconds()
                    print(f"   Elapsed Time: {Colors.CYAN}{format_duration(elapsed)}{Colors.RESET}")
                    
                    if completed_exp > 0 and completed_exp < total_exp:
                        eta = estimate_remaining_time(completed_exp, total_exp, elapsed)
                        print(f"   Estimated Remaining: {Colors.YELLOW}{eta}{Colors.RESET}")
            
            print()
            
            # Experiment details
            if "experiments" in data:
                print(f"{Colors.BOLD}🧪 Experiment Details:{Colors.RESET}\n")
                
                for exp_name, exp_data in data["experiments"].items():
                    status = exp_data.get("status", "unknown")
                    
                    if status == "success":
                        icon = "✅"
                        color = Colors.BRIGHT_GREEN
                    elif status == "failed":
                        icon = "❌"
                        color = Colors.BRIGHT_RED
                    else:
                        icon = "🔄"
                        color = Colors.BRIGHT_YELLOW
                    
                    print(f"   {icon} {Colors.BOLD}{exp_name}{Colors.RESET}")
                    print(f"      Status: {color}{status.upper()}{Colors.RESET}")
                    
                    if "duration_seconds" in exp_data:
                        duration = exp_data["duration_seconds"]
                        print(f"      Duration: {format_duration(duration)}")
                    
                    # Check for detailed experiment progress
                    if not compact:
                        exp_progress = scan_experiment_progress(exp_name)
                        if exp_progress and "conditions" in exp_progress:
                            conditions = exp_progress["conditions"]
                            total_conditions = len(conditions)
                            completed_conditions = sum(1 for c in conditions.values() if "brief_results" in c)
                            
                            cond_bar = create_progress_bar(completed_conditions, total_conditions, width=30)
                            print(f"      Conditions: {cond_bar}")
                            
                            # Artifact count
                            artifacts = count_artifacts(exp_name)
                            if artifacts["total_runs"] > 0:
                                print(f"      Artifacts: {Colors.CYAN}{artifacts['total_runs']} runs, {artifacts['total_files']} files{Colors.RESET}")
                    
                    print()
            
            # LangSmith link
            print(f"{Colors.BOLD}🔗 LangSmith Monitoring:{Colors.RESET}")
            print(f"   Main Project: C4-Parallel-Study-{session_id}")
            print(f"   URL: {Colors.BRIGHT_BLUE}https://smith.langchain.com/{Colors.RESET}\n")
            
            # Footer
            print(f"{Colors.DIM}{'─'*80}{Colors.RESET}")
            print(f"{Colors.DIM}💡 Tip: Use --compact flag for cleaner view{Colors.RESET}")
            print(f"{Colors.DIM}📂 Results: data/results/parallel_experiments/session_{session_id}_*.json{Colors.RESET}\n")
            
            # Wait before refresh
            time.sleep(refresh_interval)
            
    except KeyboardInterrupt:
        print(f"\n\n{Colors.BRIGHT_YELLOW}Monitoring stopped by user.{Colors.RESET}\n")
        sys.exit(0)


def display_artifact_browser(experiment_name: Optional[str] = None):
    """Browse generated artifacts."""
    clear_screen()
    
    print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}{'='*80}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}📁 ARTIFACT BROWSER{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}{'='*80}{Colors.RESET}\n")
    
    base_dir = Path("data/results/enhanced_experiments")
    
    if not base_dir.exists():
        print(f"{Colors.YELLOW}No artifacts found.{Colors.RESET}\n")
        return
    
    # List all experiments
    experiment_dirs = [d for d in base_dir.iterdir() if d.is_dir() and (d / "c4_artifacts").exists()]
    
    if not experiment_dirs:
        print(f"{Colors.YELLOW}No experiment artifacts found.{Colors.RESET}\n")
        return
    
    for exp_dir in sorted(experiment_dirs):
        exp_name = exp_dir.name
        artifact_dir = exp_dir / "c4_artifacts"
        
        runs = sorted(artifact_dir.iterdir()) if artifact_dir.exists() else []
        
        print(f"{Colors.BOLD}🧪 {exp_name}{Colors.RESET}")
        print(f"   Total Runs: {Colors.CYAN}{len(runs)}{Colors.RESET}")
        
        if runs:
            total_files = sum(len(list(run_dir.glob("**/*"))) for run_dir in runs if run_dir.is_dir())
            total_size = sum(f.stat().st_size for run_dir in runs if run_dir.is_dir() for f in run_dir.glob("**/*") if f.is_file())
            
            print(f"   Total Files: {Colors.CYAN}{total_files}{Colors.RESET}")
            print(f"   Total Size: {Colors.CYAN}{total_size / (1024*1024):.2f} MB{Colors.RESET}")
            
            # Show latest runs
            latest_runs = sorted(runs, key=lambda r: r.stat().st_mtime, reverse=True)[:3]
            print(f"   Latest Runs:")
            for run in latest_runs:
                modified = datetime.fromtimestamp(run.stat().st_mtime)
                print(f"      • {Colors.DIM}{run.name}{Colors.RESET} ({modified.strftime('%H:%M:%S')})")
        
        print()


def display_experiment_live(experiment_name: str, refresh_interval: int = 10, compact: bool = False):
    """Display live progress for a specific experiment."""
    
    try:
        while True:
            clear_screen()
            
            # Header
            print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}{'='*80}{Colors.RESET}")
            print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}🔍 LIVE EXPERIMENT MONITOR - {experiment_name}{Colors.RESET}")
            print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}{'='*80}{Colors.RESET}")
            print(f"{Colors.DIM}Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Auto-refresh every {refresh_interval}s | Press Ctrl+C to exit{Colors.RESET}\n")
            
            # Get experiment progress
            exp_data = scan_experiment_progress(experiment_name)
            
            if not exp_data:
                print(f"{Colors.YELLOW}No progress data found for '{experiment_name}'.{Colors.RESET}")
                print(f"{Colors.DIM}Waiting for experiment to start...{Colors.RESET}\n")
                time.sleep(refresh_interval)
                continue
            
            # Status
            is_final = exp_data.get('_is_final', False)
            source_file = exp_data.get('_source_file', 'unknown')
            
            status_icon = "✅" if is_final else "🔄"
            status_text = "COMPLETED" if is_final else "IN PROGRESS"
            status_color = Colors.BRIGHT_GREEN if is_final else Colors.BRIGHT_YELLOW
            
            print(f"{Colors.BOLD}Status:{Colors.RESET} {status_icon} {status_color}{status_text}{Colors.RESET}")
            print(f"{Colors.DIM}Source: {source_file}{Colors.RESET}\n")
            
            # Conditions progress
            if "conditions" in exp_data:
                conditions = exp_data["conditions"]
                total_conditions = len(conditions)
                
                # Count completed conditions
                completed_conditions = 0
                total_runs = 0
                completed_runs = 0
                
                for cond_id, cond_data in conditions.items():
                    if isinstance(cond_data, dict) and "brief_results" in cond_data:
                        completed_conditions += 1
                        for brief_name, brief_results in cond_data.get("brief_results", {}).items():
                            total_runs += len(brief_results) if isinstance(brief_results, list) else 0
                            completed_runs += len(brief_results) if isinstance(brief_results, list) else 0
                
                print(f"{Colors.BOLD}📈 Overall Progress:{Colors.RESET}")
                cond_bar = create_progress_bar(completed_conditions, total_conditions, width=50)
                print(f"   Conditions: {cond_bar}")
                
                if total_runs > 0:
                    run_bar = create_progress_bar(completed_runs, total_runs, width=50)
                    print(f"   Total Runs: {run_bar}")
                
                print()
                
                # Condition details
                if not compact:
                    print(f"{Colors.BOLD}🔬 Condition Details:{Colors.RESET}\n")
                    
                    for cond_id, cond_data in conditions.items():
                        if not isinstance(cond_data, dict):
                            continue
                        
                        cond_meta = cond_data.get("condition_metadata", {})
                        cond_name = cond_meta.get("name", cond_id)
                        
                        has_results = "brief_results" in cond_data
                        icon = "✅" if has_results else "⏳"
                        color = Colors.BRIGHT_GREEN if has_results else Colors.DIM
                        
                        print(f"   {icon} {color}{cond_name}{Colors.RESET}")
                        
                        if has_results:
                            brief_results = cond_data.get("brief_results", {})
                            runs_count = sum(len(results) for results in brief_results.values() if isinstance(results, list))
                            print(f"      Runs completed: {runs_count}")
                            
                            # Show artifacts
                            artifacts = cond_data.get("artifact_locations", {})
                            if artifacts:
                                print(f"      Artifacts saved: {len(artifacts)} locations")
                        
                        print()
            
            # Artifacts summary
            artifacts = count_artifacts(experiment_name)
            if artifacts["total_runs"] > 0:
                print(f"{Colors.BOLD}💾 Saved Artifacts:{Colors.RESET}")
                print(f"   Total Runs: {Colors.CYAN}{artifacts['total_runs']}{Colors.RESET}")
                print(f"   Total Files: {Colors.CYAN}{artifacts['total_files']}{Colors.RESET}")
                print()
            
            # LangSmith
            print(f"{Colors.BOLD}🔗 LangSmith:{Colors.RESET}")
            print(f"   Project: C4-Parallel-{experiment_name}-*")
            print(f"   URL: {Colors.BRIGHT_BLUE}https://smith.langchain.com/{Colors.RESET}\n")
            
            # Footer
            print(f"{Colors.DIM}{'─'*80}{Colors.RESET}")
            print(f"{Colors.DIM}💡 View artifacts: python monitor_experiments.py --artifacts{Colors.RESET}")
            print(f"{Colors.DIM}📂 Results: data/results/enhanced_experiments/{experiment_name}_*.json{Colors.RESET}\n")
            
            # Exit if completed
            if is_final:
                print(f"{Colors.BRIGHT_GREEN}✨ Experiment completed! Monitor will refresh every {refresh_interval}s (Ctrl+C to exit){Colors.RESET}\n")
            
            time.sleep(refresh_interval)
            
    except KeyboardInterrupt:
        print(f"\n\n{Colors.BRIGHT_YELLOW}Monitoring stopped by user.{Colors.RESET}\n")
        sys.exit(0)


def main():
    parser = argparse.ArgumentParser(
        description="Monitor experiment progress in real-time",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Show all sessions (one-time)
  python monitor_experiments.py
  
  # Monitor specific experiment (RECOMMENDED)
  python monitor_experiments.py --experiment role_ablation --refresh 5
  
  # Monitor by session ID
  python monitor_experiments.py --session-id 20241023_153022 --refresh 5
  
  # Compact view with faster refresh
  python monitor_experiments.py --experiment role_ablation --compact --refresh 3
  
  # Browse artifacts
  python monitor_experiments.py --artifacts
        """
    )
    
    parser.add_argument(
        '--experiment',
        type=str,
        default=None,
        help='Monitor specific experiment by name (e.g., role_ablation)'
    )
    
    parser.add_argument(
        '--session-id',
        type=str,
        default=None,
        help='Monitor specific session ID (for orchestrator-level monitoring)'
    )
    
    parser.add_argument(
        '--refresh',
        type=int,
        default=10,
        help='Auto-refresh interval in seconds (default: 10)'
    )
    
    parser.add_argument(
        '--compact',
        action='store_true',
        help='Show compact view with less details'
    )
    
    parser.add_argument(
        '--artifacts',
        action='store_true',
        help='Browse generated artifacts'
    )
    
    args = parser.parse_args()
    
    # Enable ANSI colors on Windows
    if os.name == 'nt':
        os.system('color')
    
    if args.artifacts:
        display_artifact_browser()
    elif args.experiment:
        # Monitor specific experiment (RECOMMENDED)
        display_experiment_live(args.experiment, args.refresh, args.compact)
    elif args.session_id:
        # Monitor by session ID (orchestrator level)
        display_detailed_progress(args.session_id, args.refresh, args.compact)
    else:
        # Show overview
        sessions = scan_for_sessions()
        
        # Also check for running experiments
        results_dir = Path("data/results/enhanced_experiments")
        running_experiments = set()
        
        if results_dir.exists():
            # Check for progress files
            progress_files = list(results_dir.glob("*_progress_*.json"))
            for pf in progress_files:
                exp_name = pf.name.split('_progress_')[0]
                running_experiments.add(exp_name)
            
            # Check for final files (completed)
            final_files = list(results_dir.glob("*_final_*.json"))
            for ff in final_files:
                exp_name = ff.name.split('_final_')[0]
                running_experiments.add(exp_name)
            
            # Check for artifact directories (experiments that started)
            for item in results_dir.iterdir():
                if item.is_dir() and (item / "c4_artifacts").exists():
                    running_experiments.add(item.name)
        
        # Display what we found
        if sessions:
            display_session_overview(sessions, args.compact)
        
        if running_experiments:
            print(f"\n{Colors.BOLD}{Colors.BRIGHT_CYAN}{'='*80}{Colors.RESET}")
            print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}🧪 DETECTED EXPERIMENTS{Colors.RESET}")
            print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}{'='*80}{Colors.RESET}\n")
            
            for exp_name in sorted(running_experiments):
                exp_data = scan_experiment_progress(exp_name)
                
                if exp_data:
                    is_final = exp_data.get('_is_final', False)
                    icon = "✅" if is_final else "🔄"
                    status = "Completed" if is_final else "Running"
                    color = Colors.BRIGHT_GREEN if is_final else Colors.BRIGHT_YELLOW
                    
                    print(f"{icon} {Colors.BOLD}{exp_name}{Colors.RESET}")
                    print(f"   Status: {color}{status}{Colors.RESET}")
                    
                    # Show progress if available
                    if "conditions" in exp_data:
                        total_cond = len(exp_data["conditions"])
                        completed_cond = sum(1 for c in exp_data["conditions"].values() 
                                           if isinstance(c, dict) and "brief_results" in c)
                        print(f"   Progress: {completed_cond}/{total_cond} conditions")
                    
                    # Show artifacts
                    artifacts = count_artifacts(exp_name)
                    if artifacts["total_runs"] > 0:
                        print(f"   Artifacts: {artifacts['total_runs']} runs, {artifacts['total_files']} files")
                else:
                    print(f"🔄 {Colors.BOLD}{exp_name}{Colors.RESET}")
                    print(f"   Status: {Colors.BRIGHT_YELLOW}Starting...{Colors.RESET}")
                    artifacts = count_artifacts(exp_name)
                    if artifacts["total_runs"] > 0:
                        print(f"   Artifacts: {artifacts['total_runs']} runs")
                
                print()
            
            print(f"{Colors.BRIGHT_YELLOW}💡 To monitor live, run:{Colors.RESET}")
            for exp in sorted(running_experiments):
                print(f"{Colors.BRIGHT_CYAN}   python monitor_experiments.py --experiment {exp} --refresh 5{Colors.RESET}")
            print()
        
        # If nothing found
        if not sessions and not running_experiments:
            print(f"\n{Colors.BOLD}{Colors.BRIGHT_CYAN}{'='*80}{Colors.RESET}")
            print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}📊 EXPERIMENT MONITOR{Colors.RESET}")
            print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}{'='*80}{Colors.RESET}\n")
            print(f"{Colors.YELLOW}No experiment sessions or experiments found.{Colors.RESET}")
            print(f"{Colors.DIM}Run experiments first: python run_parallel_experiments.py{Colors.RESET}\n")
            return
        
        # If there's an active session, offer to monitor it
        if sessions:
            active_sessions = [s for s in sessions if s["status"] == "in_progress"]
            if active_sessions:
                print(f"{Colors.BRIGHT_YELLOW}💡 Found active session(s)!{Colors.RESET}")
                print(f"{Colors.DIM}   To monitor by session ID, run:{Colors.RESET}")
                for session in active_sessions:
                    print(f"{Colors.BRIGHT_CYAN}   python monitor_experiments.py --session-id {session['session_id']}{Colors.RESET}")
                print()


if __name__ == "__main__":
    main()
