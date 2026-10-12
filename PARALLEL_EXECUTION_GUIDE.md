# Parallel Experiment Execution Guide

## Overview

This system enables professional parallel execution of all 5 C4 modeling experiments, reducing total execution time from ~30 hours (sequential) to ~6-8 hours (parallel).

## Features

✅ **Multi-Level Parallelization**: Run multiple experiments simultaneously + parallel conditions within experiments  
✅ **Automatic Artifact Saving**: Every C4 model saved immediately after generation  
✅ **Progress Checkpointing**: Resume from any point if interrupted  
✅ **Resource Management**: Control parallelism to respect API rate limits  
✅ **Comprehensive Monitoring**: Real-time progress tracking and logging  

## Quick Start

### 1. Run All Experiments in Parallel (Recommended)

```bash
python run_parallel_experiments.py --model gemini-2.5-flash-lite
```

This will:
- Run all 5 experiments simultaneously (3 at a time by default)
- Each experiment runs 2 conditions in parallel
- Total time: ~6-8 hours for all 300 runs
- Cost: ~$50-80 with Gemini

### 2. See Execution Plan (Dry Run)

```bash
python run_parallel_experiments.py --dry-run
```

Shows:
- Number of runs per experiment
- Estimated sequential vs parallel time
- Cost estimates
- Resource requirements

### 3. Run Specific Experiments

```bash
python run_parallel_experiments.py --experiments role_ablation interaction_order
```

### 4. Control Parallelism

```bash
# Conservative (lower API usage)
python run_parallel_experiments.py --max-experiments 2 --max-conditions 1

# Aggressive (faster, higher API usage)
python run_parallel_experiments.py --max-experiments 5 --max-conditions 3
```

## Individual Experiment Runners

For maximum control, run experiments individually:

### Role Ablation
```bash
python experiments/role_ablation.py --model gemini-2.5-flash-lite
```

### Interaction Order
```bash
python experiments/interaction_order_runner.py --model gemini-2.5-flash-lite
```

### Shared Memory
```bash
python experiments/shared_memory_runner.py --model gemini-2.5-flash-lite
```

### Specialization & Diversity
Use the main parallel runner or implement similar dedicated scripts.

## Monitoring Progress

### Real-Time Monitoring

```bash
# Watch orchestrator checkpoints
watch -n 10 'ls -lh data/results/parallel_experiments/'

# Monitor experiment artifacts
watch -n 30 'du -sh data/results/enhanced_experiments/*/c4_artifacts/'
```

### Check Saved Artifacts

```python
from c4modeler.experiments import EnhancedExperimentRunner

runner = EnhancedExperimentRunner()

# List all saved artifacts for an experiment
artifacts = runner.list_available_artifacts("role_ablation")
print(f"Found {len(artifacts)} saved runs")

# Recover a specific model
c4_model = runner.recover_artifacts_from_run(artifacts[0], "role_ablation")
```

## Directory Structure

```
data/results/
├── parallel_experiments/              # Orchestrator results
│   ├── session_20241023_140000_checkpoint_1.json
│   ├── session_20241023_140000_checkpoint_2.json
│   └── session_20241023_140000_final.json
│
├── enhanced_experiments/              # Individual experiment results
│   ├── role_ablation/
│   │   ├── c4_artifacts/             # ✨ C4 models saved here
│   │   │   ├── clinic_baseline_r1_20241023_143022/
│   │   │   │   ├── 1_context_analysis.md
│   │   │   │   ├── 1_context_definition.yaml
│   │   │   │   ├── 1_context_diagram.puml
│   │   │   │   ├── 2_container_analysis.md
│   │   │   │   ├── 2_container_definition.yaml
│   │   │   │   ├── 2_container_diagram.puml
│   │   │   │   └── 3_components/...
│   │   │   └── clinic_baseline_r2_20241023_145511/
│   │   ├── role_ablation_progress_condition_1.json
│   │   └── role_ablation_final.json
│   │
│   ├── interaction_order/
│   │   └── c4_artifacts/...
│   └── ...
```

## Recovery & Fault Tolerance

### If Execution Fails

1. **Check Progress Files**: Examine latest checkpoint to see what completed
   ```bash
   ls -lt data/results/parallel_experiments/
   cat data/results/parallel_experiments/session_*_checkpoint_*.json
   ```

2. **Check Saved Artifacts**: All generated C4 models are preserved
   ```python
   runner.list_available_artifacts("experiment_name")
   ```

3. **Resume Execution**: Run only incomplete experiments
   ```bash
   # Check which experiments completed
   python -c "import json; print(json.load(open('data/results/parallel_experiments/session_*_final.json'))['experiments'].keys())"
   
   # Run remaining experiments
   python run_parallel_experiments.py --experiments specialization diversity
   ```

### Manual Recovery

If you need to recover specific C4 models:

```python
from pathlib import Path
from c4modeler.experiments import EnhancedExperimentRunner

runner = EnhancedExperimentRunner()

# Find all artifact directories
artifact_dirs = list(Path("data/results/enhanced_experiments").rglob("c4_artifacts/*"))
print(f"Found {len(artifact_dirs)} artifact sets")

# Recover any specific model
run_id = "clinic_baseline_r1_20241023_143022"
model = runner.recover_artifacts_from_run(run_id, "role_ablation")
```

## Performance & Cost Optimization

### Recommended Settings

| Setting | Conservative | Balanced | Aggressive |
|---------|-------------|----------|------------|
| max-experiments | 2 | 3 | 5 |
| max-conditions | 1 | 2 | 3 |
| Est. Duration | 10-12 hours | 6-8 hours | 4-6 hours |
| API Load | Low | Medium | High |
| Risk of Rate Limiting | Very Low | Low | Medium |

### Cost Estimates (Gemini 2.5 Flash)

- Per run: $0.20 - $0.35
- 300 runs total: $60 - $105
- Your $300 credit covers: **850-1500 runs** 

### API Rate Limits

**Google (Gemini)**:
- Requests per minute: 60-300 (tier dependent)
- Tokens per minute: 1-4M (tier dependent)
- Recommended: `--max-experiments 3 --max-conditions 2`

**OpenAI (GPT-4)**:
- Requests per minute: 500-10,000 (tier dependent)
- Recommended: `--max-experiments 4 --max-conditions 3`

## Troubleshooting

### "Too Many Requests" Error

```bash
# Reduce parallelism
python run_parallel_experiments.py --max-experiments 2 --max-conditions 1
```

### Out of Memory

```bash
# Reduce experiment-level parallelism (experiments run in separate processes)
python run_parallel_experiments.py --max-experiments 2
```

### Verify Artifact Completeness

```python
from pathlib import Path

artifact_base = Path("data/results/enhanced_experiments/role_ablation/c4_artifacts")

for run_dir in artifact_base.iterdir():
    required = ["1_context_definition.yaml", "2_container_definition.yaml"]
    missing = [f for f in required if not (run_dir / f).exists()]
    
    if missing:
        print(f"⚠️ {run_dir.name}: Missing {missing}")
    else:
        print(f"✅ {run_dir.name}: Complete")
```

## Advanced Usage

### Custom Session Management

```bash
# Start with custom session ID for tracking
python run_parallel_experiments.py --session-id my_full_study_v1
```

### Integration with Cluster/Cloud

The parallel runner uses Python's `ProcessPoolExecutor`, which works on:
- ✅ Local multi-core machines
- ✅ Cloud VMs (AWS, GCP, Azure)
- ✅ HPC clusters (with proper Python environment)

### Environment Variables

```bash
# Control tracing
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_PROJECT="My-Custom-Study"

# Set API keys
export GOOGLE_API_KEY="your-key"
export OPENAI_API_KEY="your-key"
```

## Best Practices

1. **Start with Dry Run**: Always check execution plan first
2. **Monitor Progress**: Use watch commands or separate terminal
3. **Conservative First**: Start with lower parallelism, increase if stable
4. **Check Artifacts**: Verify saved models are complete after each checkpoint
5. **Use Tmux/Screen**: For long-running sessions on remote servers
6. **Set Quotas**: Monitor your API usage/costs in provider dashboard

## Complete Example Workflow

```bash
# 1. Check the plan
python run_parallel_experiments.py --dry-run

# 2. Start parallel execution in tmux
tmux new -s experiments
python run_parallel_experiments.py --model gemini-2.5-flash-lite

# 3. Monitor in separate terminal (detach tmux with Ctrl+B, D)
watch -n 30 'python -c "from pathlib import Path; print(len(list(Path(\"data/results/enhanced_experiments\").rglob(\"c4_artifacts/*\"))))"'

# 4. After completion, analyze results
python -c "
import json
from pathlib import Path

final_file = max(Path('data/results/parallel_experiments').glob('*final.json'))
results = json.load(open(final_file))

print(f\"Session: {results['session_id']}\")
print(f\"Duration: {results['total_duration_hours']:.1f} hours\")
print(f\"Success Rate: {results['summary']['success_rate']:.1f}%\")
"
```

## Support

For issues or questions:
1. Check artifact directories to ensure models are being saved
2. Review checkpoint files for progress tracking
3. Verify API keys and rate limits
4. Use `--dry-run` to validate configuration

---

**Ready to run your 300 experiments professionally! 🚀**
