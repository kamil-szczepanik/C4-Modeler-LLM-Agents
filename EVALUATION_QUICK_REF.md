# Evaluation System - Quick Reference

## 🎯 How Evaluation Works

### Current Flow (Immediate Evaluation)

```
┌─────────────────────────────────────────────────────────┐
│ For each run (5 briefs × 3 rounds × N conditions)      │
└─────────────────────────────────────────────────────────┘
                          ↓
        ┌─────────────────────────────────┐
        │  1. Generate C4 Model (~30 min) │
        └─────────────────────────────────┘
                          ↓
        ┌─────────────────────────────────┐
        │  2. Save C4 Artifacts           │ ← SAFE: Model preserved!
        │     • 1_context_*.{md,yaml,puml}│
        │     • 2_container_*             │
        │     • 3_components/             │
        └─────────────────────────────────┘
                          ↓
        ┌─────────────────────────────────┐
        │  3. Run Evaluation (~2-5 min)   │
        │     • ISO/IEC 25010             │
        │     • ATAM Scenarios            │
        │     • Architectural Soundness   │
        └─────────────────────────────────┘
                          ↓
        ┌─────────────────────────────────┐
        │  4. Save Complete Results       │
        │     • C4 model                  │
        │     • Evaluation results        │
        │     • Metadata & timestamps     │
        └─────────────────────────────────┘
```

## 📁 Where Results Are Saved

### 1. Complete Results (Model + Evaluation)

**File**: `data/results/enhanced_experiments/{experiment}_final_{timestamp}.json`

```json
{
  "conditions": {
    "baseline": {
      "brief_results": {
        "clinic-management-system": [
          {
            "round": 1,
            "c4_model": {...},           ← Full C4 model
            "evaluation": {              ← Evaluation results
              "iso25010Attributes": {...},
              "atamScenarios": {...},
              "architecturalSoundness": {...}
            },
            "artifact_path": "..."       ← Path to saved artifacts
          }
        ]
      },
      "condition_summary": {
        "averages": {                    ← Aggregated metrics
          "iso_functional_suitability": 0.876,
          "atam_responsiveness": 0.891,
          ...
        }
      }
    }
  }
}
```

### 2. C4 Artifacts (Model Files Only)

**Directory**: `data/results/enhanced_experiments/{experiment}/c4_artifacts/{run_id}/`

```
clinic_baseline_r1_20241023_143022/
├── 1_context_analysis.md      ← Human-readable analysis
├── 1_context_definition.yaml  ← Structured YAML
├── 1_context_diagram.puml     ← PlantUML diagram
├── 2_container_analysis.md
├── 2_container_definition.yaml
├── 2_container_diagram.puml
└── 3_components/
    ├── web_app_analysis.md
    ├── web_app_definition.yaml
    └── web_app_diagram.puml
```

**Note**: Evaluations are **NOT** saved here - they're in the JSON results files.

### 3. Progress Checkpoints

**File**: `data/results/enhanced_experiments/{experiment}_progress_condition_{N}_{timestamp}.json`

Same structure as final results, saved **after each condition completes**.

## 📊 Evaluation Metrics

### ISO/IEC 25010 (8 Attributes)
```python
{
  "functional_suitability": 0.876,  # Requirements coverage
  "security": 0.823,                # Security patterns
  "maintainability": 0.891,         # Code/design quality
  "reliability": 0.845,             # Error handling
  "usability": 0.789,               # Clarity & accessibility
  "performance_efficiency": 0.834,  # Response patterns
  "compatibility": 0.856,           # Integration capability
  "portability": 0.812              # Deployment flexibility
}
```

### ATAM Scenarios
```python
{
  "responsiveness_scenarios": [...],  # Performance requirements
  "modifiability_scenarios": [...],   # Change impact
  "security_scenarios": [...],        # Threat responses
  "overall_responsiveness": 0.887     # Aggregate score
}
```

### Architectural Soundness
```python
{
  "coupling_density": 0.654,         # Component coupling
  "abstraction_coherence": 0.891,    # Level separation
  "semantic_completeness": 0.834,    # Element coverage
  "cross_level_consistency": 0.876   # Cross-level alignment
}
```

## 🔧 Accessing Evaluation Results

### From Complete Results File

```python
import json
from pathlib import Path

# Load results
results_file = max(Path("data/results/enhanced_experiments").glob("role_ablation_final_*.json"))
with open(results_file) as f:
    results = json.load(f)

# Get specific evaluation
evaluation = results["conditions"]["baseline"]["brief_results"]["clinic-management-system"][0]["evaluation"]

print(f"Functional: {evaluation['iso25010Attributes']['scores']['functional_suitability']}")
print(f"ATAM: {evaluation['atamScenarios']['overall_responsiveness']}")
```

### From Summary Statistics

```python
# Get aggregated metrics across all runs
summary = results["conditions"]["baseline"]["condition_summary"]["averages"]

print(f"Avg Functional: {summary['iso_functional_suitability']:.3f}")
print(f"Avg Coupling: {summary['soundness_coupling_density']:.3f}")
```

### Re-evaluate Saved Model

```python
from c4modeler.experiments import EnhancedExperimentRunner
from c4modeler.evaluation import run_enhanced_evaluation_only

# Recover model from artifacts
runner = EnhancedExperimentRunner()
c4_model = runner.recover_artifacts_from_run("clinic_baseline_r1_20241023_143022", "role_ablation")

# Re-run evaluation
evaluation = run_enhanced_evaluation_only(brief_content, c4_model)
```

### Using Re-evaluation Script

```bash
# Re-evaluate entire experiment
python reevaluate_artifacts.py --experiment role_ablation

# Re-evaluate specific run
python reevaluate_artifacts.py --run-id clinic_baseline_r1_20241023_143022

# Save separate evaluation files in artifact directories
python reevaluate_artifacts.py --experiment role_ablation --save-separate
```

## ⚡ Performance

| Task | Duration | Notes |
|------|----------|-------|
| **C4 Generation** | ~30 min | Time-consuming, saved immediately |
| **Evaluation** | ~2-5 min | Fast, can be re-run if needed |
| **Total per run** | ~32-35 min | 86% is generation, 14% evaluation |

**Why evaluate immediately?**
- ✅ Fast (only adds 7-16% to total time)
- ✅ Complete results package
- ✅ Early quality detection
- ✅ Can still re-evaluate later if needed

## 🎯 Key Points

1. **Evaluation runs immediately** after each C4 generation
2. **Results saved together** in main JSON file (model + evaluation)
3. **C4 artifacts saved separately** for recovery (model files only)
4. **Can re-evaluate anytime** using saved artifacts
5. **Aggregated statistics** computed per condition
6. **Progress checkpoints** include all evaluation data

## 💡 Use Cases

### During Experiments
- ✅ Get complete results immediately
- ✅ Monitor quality in real-time
- ✅ All data packaged together

### After Experiments
- 🔄 Re-evaluate with updated evaluation code
- 🔄 Test different evaluation methods
- 🔄 Add new metrics retroactively
- 🔄 Compare evaluation approaches

## 🚀 Best Practice

**For your 300-run study**: Keep the current approach!

**Why?**
- Evaluation is fast (2-5 min vs 30 min generation)
- Complete results ready for analysis
- Low risk (model saved, can re-evaluate)
- Simpler workflow
- Earlier quality detection

**Only separate evaluation if**:
- Experimenting with evaluation methods
- Evaluation becomes time-consuming
- Developing new metrics iteratively

---

**See `EVALUATION_SYSTEM.md` for complete technical details**
