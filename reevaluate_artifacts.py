"""
Re-Evaluation Utility for Saved C4 Artifacts
============================================

This script allows you to re-evaluate saved C4 models without regenerating them.
Useful for:
- Testing new evaluation metrics
- Updating evaluation code
- Adding evaluations to runs that were generated without evaluation
- Comparing different evaluation methods

Usage:
    # Re-evaluate all artifacts for an experiment
    python reevaluate_artifacts.py --experiment role_ablation
    
    # Re-evaluate specific run
    python reevaluate_artifacts.py --run-id clinic_baseline_r1_20241023_143022
    
    # Save separate evaluation files
    python reevaluate_artifacts.py --experiment role_ablation --save-separate
"""

import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from dotenv import load_dotenv
load_dotenv()

from c4modeler.experiments import EnhancedExperimentRunner, load_briefs_from_dir
from c4modeler.evaluation import run_enhanced_evaluation_only
from c4modeler.utils import load_c4_model_from_artifacts


def extract_brief_name_from_run_id(run_id: str) -> str:
    """Extract brief name from run ID format: {brief}_{condition}_r{round}_{timestamp}"""
    parts = run_id.split('_')
    
    # Handle multi-word brief names (e.g., clinic-management-system)
    # Everything before the condition part
    for i, part in enumerate(parts):
        if part in ['baseline', 'nosecurity', 'nodomain', 'nointegration', 'sequential', 'parallel']:
            return '_'.join(parts[:i]).replace('_', '-')
    
    # Fallback: first part
    return parts[0]


def reevaluate_single_artifact(
    artifact_dir: Path,
    briefs: Dict[str, str],
    save_separate: bool = False
) -> Dict[str, Any]:
    """
    Re-evaluate a single C4 artifact.
    
    Args:
        artifact_dir: Path to artifact directory
        briefs: Dictionary of brief names to brief content
        save_separate: Whether to save evaluation as separate file
    
    Returns:
        Evaluation results dictionary
    """
    print(f"\n🔍 Evaluating: {artifact_dir.name}")
    
    # Load C4 model from artifacts
    try:
        c4_model = load_c4_model_from_artifacts(artifact_dir)
        print(f"  ✅ Loaded C4 model")
    except Exception as e:
        print(f"  ❌ Failed to load C4 model: {str(e)}")
        return None
    
    # Determine which brief this is
    run_id = artifact_dir.name
    brief_name = extract_brief_name_from_run_id(run_id)
    
    if brief_name not in briefs:
        print(f"  ⚠️ Brief '{brief_name}' not found in loaded briefs")
        print(f"  Available briefs: {list(briefs.keys())}")
        return None
    
    brief_content = briefs[brief_name]
    print(f"  📄 Using brief: {brief_name}")
    
    # Run evaluation
    try:
        evaluation = run_enhanced_evaluation_only(brief_content, c4_model)
        print(f"  ✅ Evaluation complete")
        
        # Add metadata
        evaluation["reevaluation_metadata"] = {
            "reevaluated_at": datetime.now().isoformat(),
            "run_id": run_id,
            "brief_name": brief_name
        }
        
        # Save if requested
        if save_separate:
            eval_file = artifact_dir / "evaluation_results.json"
            with open(eval_file, 'w', encoding='utf-8') as f:
                json.dump(evaluation, f, indent=2, ensure_ascii=False)
            print(f"  💾 Saved to: {eval_file.name}")
        
        return evaluation
        
    except Exception as e:
        print(f"  ❌ Evaluation failed: {str(e)}")
        return None


def reevaluate_experiment(
    experiment_name: str,
    save_separate: bool = False,
    save_consolidated: bool = True
) -> Dict[str, Any]:
    """
    Re-evaluate all artifacts for an experiment.
    
    Args:
        experiment_name: Name of the experiment
        save_separate: Save individual evaluation files in artifact dirs
        save_consolidated: Save consolidated results file
    
    Returns:
        Dictionary with all evaluation results
    """
    print(f"\n{'='*80}")
    print(f"🔬 RE-EVALUATING EXPERIMENT: {experiment_name}")
    print(f"{'='*80}")
    
    # Load briefs
    runner = EnhancedExperimentRunner()
    runner.load_system_briefs("data/briefs")
    briefs = runner.briefs
    
    # Find all artifact directories
    artifacts_base = Path(f"data/results/enhanced_experiments/{experiment_name}/c4_artifacts")
    
    if not artifacts_base.exists():
        print(f"❌ No artifacts found for experiment: {experiment_name}")
        return None
    
    artifact_dirs = [d for d in artifacts_base.iterdir() if d.is_dir()]
    print(f"\n📊 Found {len(artifact_dirs)} artifact sets to evaluate")
    
    # Re-evaluate all
    all_evaluations = {}
    successful = 0
    failed = 0
    
    for artifact_dir in artifact_dirs:
        evaluation = reevaluate_single_artifact(artifact_dir, briefs, save_separate)
        
        if evaluation:
            all_evaluations[artifact_dir.name] = evaluation
            successful += 1
        else:
            failed += 1
    
    # Summary
    print(f"\n{'='*80}")
    print(f"📊 RE-EVALUATION SUMMARY")
    print(f"{'='*80}")
    print(f"  ✅ Successful: {successful}/{len(artifact_dirs)}")
    print(f"  ❌ Failed: {failed}/{len(artifact_dirs)}")
    
    # Save consolidated results
    if save_consolidated and all_evaluations:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = Path(f"data/results/enhanced_experiments/{experiment_name}/reevaluation_{timestamp}.json")
        
        consolidated = {
            "reevaluation_metadata": {
                "timestamp": datetime.now().isoformat(),
                "experiment_name": experiment_name,
                "total_runs": len(artifact_dirs),
                "successful": successful,
                "failed": failed
            },
            "evaluations": all_evaluations
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(consolidated, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Consolidated results saved: {output_file}")
    
    return all_evaluations


def reevaluate_single_run(
    run_id: str,
    experiment_name: str = None
) -> Dict[str, Any]:
    """
    Re-evaluate a specific run by run_id.
    
    Args:
        run_id: The unique run identifier
        experiment_name: Experiment name (auto-detected if None)
    """
    print(f"\n🔍 Re-evaluating specific run: {run_id}")
    
    # Load briefs
    runner = EnhancedExperimentRunner()
    runner.load_system_briefs("data/briefs")
    briefs = runner.briefs
    
    # Find the artifact directory
    if experiment_name:
        artifact_dir = Path(f"data/results/enhanced_experiments/{experiment_name}/c4_artifacts/{run_id}")
    else:
        # Search all experiments
        base_dir = Path("data/results/enhanced_experiments")
        artifact_dirs = list(base_dir.rglob(f"c4_artifacts/{run_id}"))
        
        if not artifact_dirs:
            print(f"❌ Run ID not found: {run_id}")
            return None
        
        if len(artifact_dirs) > 1:
            print(f"⚠️ Multiple matches found for run_id: {run_id}")
            for d in artifact_dirs:
                print(f"  - {d}")
            artifact_dir = artifact_dirs[0]
            print(f"Using first match: {artifact_dir}")
        else:
            artifact_dir = artifact_dirs[0]
    
    if not artifact_dir.exists():
        print(f"❌ Artifact directory not found: {artifact_dir}")
        return None
    
    # Re-evaluate
    evaluation = reevaluate_single_artifact(artifact_dir, briefs, save_separate=True)
    
    if evaluation:
        print(f"\n✅ Re-evaluation complete!")
        
        # Print key metrics
        print(f"\n📊 Key Metrics:")
        if "iso25010Attributes" in evaluation:
            scores = evaluation["iso25010Attributes"].get("scores", {})
            print(f"  ISO Functional: {scores.get('functional_suitability', 0):.3f}")
            print(f"  ISO Security: {scores.get('security', 0):.3f}")
            print(f"  ISO Maintainability: {scores.get('maintainability', 0):.3f}")
        
        if "atamScenarios" in evaluation:
            print(f"  ATAM Responsiveness: {evaluation['atamScenarios'].get('overall_responsiveness', 0):.3f}")
        
        if "architecturalSoundness" in evaluation:
            soundness = evaluation["architecturalSoundness"]
            print(f"  Coupling Density: {soundness.get('coupling_density', 0):.3f}")
            print(f"  Abstraction Coherence: {soundness.get('abstraction_coherence', 0):.3f}")
    
    return evaluation


def main():
    parser = argparse.ArgumentParser(
        description="Re-evaluate saved C4 artifacts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Re-evaluate all artifacts for an experiment
  python reevaluate_artifacts.py --experiment role_ablation
  
  # Re-evaluate specific run
  python reevaluate_artifacts.py --run-id clinic_baseline_r1_20241023_143022
  
  # Save separate evaluation files
  python reevaluate_artifacts.py --experiment role_ablation --save-separate
  
  # Re-evaluate without saving consolidated file
  python reevaluate_artifacts.py --experiment role_ablation --no-consolidated
        """
    )
    
    parser.add_argument(
        '--experiment',
        type=str,
        help='Experiment name to re-evaluate all artifacts'
    )
    
    parser.add_argument(
        '--run-id',
        type=str,
        help='Specific run ID to re-evaluate'
    )
    
    parser.add_argument(
        '--save-separate',
        action='store_true',
        help='Save individual evaluation files in artifact directories'
    )
    
    parser.add_argument(
        '--no-consolidated',
        action='store_true',
        help='Do not save consolidated results file'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.experiment and not args.run_id:
        print("❌ Error: Must specify either --experiment or --run-id")
        parser.print_help()
        sys.exit(1)
    
    if args.experiment and args.run_id:
        print("❌ Error: Cannot specify both --experiment and --run-id")
        parser.print_help()
        sys.exit(1)
    
    # Execute
    if args.experiment:
        results = reevaluate_experiment(
            args.experiment,
            save_separate=args.save_separate,
            save_consolidated=not args.no_consolidated
        )
        
        if results:
            print(f"\n🎉 Re-evaluation complete!")
            print(f"📊 Evaluated {len(results)} runs")
        else:
            print(f"\n❌ Re-evaluation failed")
            sys.exit(1)
    
    elif args.run_id:
        result = reevaluate_single_run(args.run_id)
        
        if result:
            print(f"\n🎉 Re-evaluation complete!")
        else:
            print(f"\n❌ Re-evaluation failed")
            sys.exit(1)


if __name__ == "__main__":
    main()
