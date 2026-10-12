# Evaluation System - How It Works

## 📊 Evaluation Flow

### Current Implementation

The evaluation happens **immediately after each C4 model is generated**, following this sequence:

```
For each experiment:
  For each condition:
    For each dataset (brief):
      For each round (1-3):
        1. 🎨 Generate C4 model (~30 min)           ← Time-consuming
        2. 💾 Save C4 artifacts immediately         ← SAFE: Model preserved
        3. 🔍 Run evaluation (~2-5 min)             ← Fast
        4. 📝 Save results (with evaluation)        ← Both saved together
```

### What Gets Evaluated

Each run is evaluated using **three comprehensive frameworks**:

#### 1. ISO/IEC 25010 Quality Attributes
- **Functional Suitability**: Does it meet requirements?
- **Security**: Are security patterns present?
- **Maintainability**: Is the architecture maintainable?
- **Reliability**: Error handling and resilience
- **Usability**: Clarity and accessibility
- **Performance Efficiency**: Response patterns
- **Compatibility**: Integration capabilities
- **Portability**: Deployment flexibility

#### 2. ATAM (Architecture Tradeoff Analysis Method)
- **Responsiveness Scenarios**: Performance requirements
- **Modifiability Scenarios**: Change impact
- **Security Scenarios**: Threat responses
- **Overall Responsiveness Score**: Aggregate quality

#### 3. Architectural Soundness Metrics
- **Coupling Density**: How tightly coupled are components?
- **Abstraction Coherence**: Proper level separation?
- **Semantic Completeness**: All necessary elements present?
- **Cross-Level Consistency**: Alignment across C4 levels

## 💾 Where Evaluation Results Are Saved

### 1. Embedded in Main Results Files

**Location**: `data/results/enhanced_experiments/{experiment}_final_{timestamp}.json`

**Structure**:
```json
{
  "experiment_metadata": {...},
  "conditions": {
    "baseline": {
      "brief_results": {
        "clinic-management-system": [
          {
            "round": 1,
            "c4_model": {...},
            "evaluation": {                    ← EVALUATION HERE
              "iso25010Attributes": {...},
              "atamScenarios": {...},
              "architecturalSoundness": {...}
            }
          }
        ]
      },
      "condition_summary": {
        "averages": {
          "iso_functional_suitability": 0.876,
          "iso_security": 0.823,
          "atam_responsiveness": 0.891,
          "soundness_coupling_density": 0.654,
          ...
        }
      }
    }
  }
}
```

### 2. Progress Checkpoints

**Location**: `data/results/enhanced_experiments/{experiment}_progress_condition_{N}_{timestamp}.json`

Same structure as above, but saved after **each condition completes** for fault tolerance.

### 3. C4 Artifacts (Models Only)

**Location**: `data/results/enhanced_experiments/{experiment}/c4_artifacts/{run_id}/`

These contain **only the C4 model artifacts** (YAML, PlantUML, analysis), **not** the evaluation results. This is by design - evaluations are lightweight and can be re-run if needed.

## 🎯 Evaluation Timing Strategy

### Why Evaluate Immediately?

**Advantages**:
✅ Complete results package (model + evaluation)  
✅ Evaluation is fast (2-5 min vs 30 min generation)  
✅ Results ready for analysis immediately  
✅ Can catch generation issues early  

**Disadvantages**:
⚠️ If evaluation fails, need to re-run it (but model is saved)  
⚠️ Slightly longer per-run time  

### Alternative: Separate Evaluation Phase

We could separate generation and evaluation into two phases:

**Phase 1: Generation Only**
```
For all experiments/conditions/briefs/rounds:
  - Generate C4 model
  - Save artifacts
  - Skip evaluation
```

**Phase 2: Evaluation Only**
```
For all saved artifacts:
  - Load C4 model
  - Run evaluation
  - Save evaluation results
```

## 🔧 Implementing Separate Evaluation

If you want to **separate generation from evaluation**, here's how:

### Option 1: Modify _run_condition to Skip Evaluation

```python
def _run_condition(self, ..., skip_evaluation=False):
    ...
    # Generate C4 model
    c4_model = self._generate_c4_with_condition(...)
    
    # Save artifacts
    save_c4_artifacts(artifact_dir, c4_model)
    
    # Optional evaluation
    if not skip_evaluation:
        evaluation = run_enhanced_evaluation_only(brief, c4_model)
    else:
        evaluation = None  # Skip for now
    
    round_result = {
        "c4_model": c4_model,
        "evaluation": evaluation,  # Will be None if skipped
        ...
    }
```

### Option 2: Batch Evaluation Script

Create a script to evaluate all saved artifacts:

```python
def evaluate_all_saved_artifacts(experiment_name: str):
    """Evaluate all saved C4 artifacts that haven't been evaluated yet."""
    
    artifacts_dir = Path(f"data/results/enhanced_experiments/{experiment_name}/c4_artifacts")
    
    for run_dir in artifacts_dir.iterdir():
        # Load C4 model from artifacts
        c4_model = load_c4_model_from_artifacts(run_dir)
        
        # Load corresponding brief
        brief_name = extract_brief_name_from_run_id(run_dir.name)
        brief = load_brief(brief_name)
        
        # Run evaluation
        evaluation = run_enhanced_evaluation_only(brief, c4_model)
        
        # Save evaluation separately
        eval_file = run_dir / "evaluation_results.json"
        with open(eval_file, 'w') as f:
            json.dump(evaluation, f, indent=2)
```

## 📈 Current Best Practice (Recommendation)

**Keep the current approach** for your 300-run study:

### Why?

1. **Evaluation is Fast**: 2-5 minutes vs 30 minutes for generation
2. **Low Risk**: If evaluation fails, you can re-run (model is saved)
3. **Complete Results**: Everything packaged together
4. **Simpler Analysis**: All data in one JSON file
5. **Early Detection**: Catch model quality issues during generation

### When to Separate?

Consider separating **only if**:
- You need to experiment with different evaluation methods
- Evaluation becomes time-consuming (e.g., using LLM judges)
- You want to add evaluations after the fact
- You're doing iterative evaluation development

## 🔍 Accessing Evaluation Results

### From Progress Files

```python
import json
from pathlib import Path

# Load latest results
results_file = max(Path("data/results/enhanced_experiments").glob("role_ablation_final_*.json"))

with open(results_file) as f:
    results = json.load(f)

# Access evaluation for specific run
condition = results["conditions"]["baseline"]
run_evaluation = condition["brief_results"]["clinic-management-system"][0]["evaluation"]

print(f"ISO Functional: {run_evaluation['iso25010Attributes']['scores']['functional_suitability']}")
print(f"ATAM Responsiveness: {run_evaluation['atamScenarios']['overall_responsiveness']}")
```

### From Summary Statistics

```python
# Get aggregated metrics
summary = condition["condition_summary"]["averages"]

print(f"Average Functional Suitability: {summary['iso_functional_suitability']:.3f}")
print(f"Average Coupling Density: {summary['soundness_coupling_density']:.3f}")
```

### Re-evaluate a Saved Model

```python
from c4modeler.experiments import EnhancedExperimentRunner
from c4modeler.evaluation import run_enhanced_evaluation_only

runner = EnhancedExperimentRunner()

# Recover model
c4_model = runner.recover_artifacts_from_run("clinic_baseline_r1_20241023_143022", "role_ablation")

# Re-run evaluation with different parameters or updated evaluation code
evaluation = run_enhanced_evaluation_only(brief_text, c4_model)

print(json.dumps(evaluation, indent=2))
```

## 📊 Evaluation Results Summary

### What's in an Evaluation Result?

```json
{
  "evaluationMetadata": {
    "evaluationTimestamp": "2024-10-23T14:30:22",
    "evaluationType": "enhanced_only"
  },
  
  "iso25010Attributes": {
    "scores": {
      "functional_suitability": 0.876,
      "security": 0.823,
      "maintainability": 0.891,
      "reliability": 0.845,
      "usability": 0.789,
      "performance_efficiency": 0.834,
      "compatibility": 0.856,
      "portability": 0.812
    },
    "detailed_analysis": {...}
  },
  
  "atamScenarios": {
    "responsiveness_scenarios": [...],
    "modifiability_scenarios": [...],
    "security_scenarios": [...],
    "overall_responsiveness": 0.887
  },
  
  "architecturalSoundness": {
    "coupling_density": 0.654,
    "abstraction_coherence": 0.891,
    "semantic_completeness": 0.834,
    "cross_level_consistency": 0.876
  }
}
```

### Aggregated in Condition Summary

```json
{
  "condition_summary": {
    "total_runs": 15,  // 5 briefs × 3 rounds
    "averages": {
      "iso_functional_suitability": 0.876,
      "iso_security": 0.823,
      "iso_maintainability": 0.891,
      "atam_responsiveness": 0.887,
      "soundness_coupling_density": 0.654,
      "soundness_abstraction_coherence": 0.891,
      "soundness_semantic_completeness": 0.834
    },
    "std_deviations": {
      "iso_functional_suitability": 0.045,
      ...
    }
  }
}
```

## 🎯 Summary

**Current System**:
- ✅ Evaluation runs **immediately** after each C4 generation
- ✅ Results saved **together** with C4 model in main JSON file
- ✅ C4 artifacts saved **separately** for recovery
- ✅ Progress checkpoints include **full evaluation data**
- ✅ Aggregated statistics computed **per condition**

**Result Files**:
1. **Main results**: `{experiment}_final_{timestamp}.json` - Complete data
2. **Progress checkpoints**: `{experiment}_progress_condition_{N}.json` - Incremental saves
3. **C4 artifacts**: `c4_artifacts/{run_id}/` - Model files only (evaluation not needed for recovery)

**This design is optimal for your use case** because:
- Evaluation is fast compared to generation
- All data packaged together for easy analysis
- Can still recover and re-evaluate from saved artifacts if needed
- Progress tracking includes evaluation results
- No need for complex two-phase execution

---

**Want to separate evaluation?** I can add that functionality, but it's not necessary for the 300-run study. The current approach is simpler and more efficient! 🚀
