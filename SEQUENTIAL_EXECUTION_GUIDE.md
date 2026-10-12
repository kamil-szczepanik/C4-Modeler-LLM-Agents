# Sequential Experiment Execution Guide

## Overview

Use `run_experiments.py` to run experiments **sequentially** (one at a time) - safe, predictable, and easier to monitor.

## Key Features

✅ **Sequential Execution** - Everything runs one at a time  
✅ **LangSmith Integration** - Initializes project with simple chain  
✅ **Temperature Control** - Configurable randomness (default: 0.5)  
✅ **Progress Tracking** - Automatic saving after each condition  
✅ **Session Management** - Unique session IDs for tracking  
✅ **Environment Validation** - Checks API keys before running  

## Basic Usage

### Run Single Experiment

```bash
# Default settings (temperature=0.5, gemini-2.5-flash-lite)
python run_experiments.py --experiment role_ablation

# Custom temperature
python run_experiments.py --experiment role_ablation --temperature 0.7

# Different model
python run_experiments.py --experiment role_ablation --model gpt-4o-mini

# Custom session ID
python run_experiments.py --experiment role_ablation --session-id my_test_run
```

### Run All Experiments

```bash
# Run all experiments one by one
python run_experiments.py --all-experiments

# With custom temperature
python run_experiments.py --all-experiments --temperature 0.6
```

### List Experiments

```bash
python run_experiments.py --list-experiments
```

### Validate Environment

```bash
python run_experiments.py --validate-env
```

## Command Line Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--experiment` | `-e` | Specific experiment to run | - |
| `--all-experiments` | `-a` | Run all experiments | - |
| `--list-experiments` | `-l` | List available experiments | - |
| `--model` | `-m` | LLM model to use | `gemini-2.5-flash-lite` |
| `--temperature` | `-t` | LLM temperature (0.0-1.0) | `0.5` |
| `--session-id` | `-s` | Custom session identifier | Auto-generated |
| `--output-dir` | `-o` | Output directory | Auto-generated |
| `--validate-env` | `-v` | Validate environment | - |
| `--no-tracing` | - | Disable LangSmith tracing | - |

## Execution Flow

```
1. Initialize LangSmith project (runs simple chain)
2. Load experiment configuration
3. Load system briefs
4. For each condition:
   a. Generate C4 model
   b. Save artifacts immediately
   c. Run evaluation
   d. Save results
5. Generate final summary
```

## LangSmith Integration

The script automatically:
- Creates a unique LangSmith project per experiment
- Runs a simple chain to initialize the project
- Makes the project visible in LangSmith UI immediately
- Project name format: `C4-Sequential-{experiment}-{session_id}`

## Output Structure

```
data/results/enhanced_experiments/
├── {experiment_name}/
│   ├── c4_artifacts/
│   │   ├── {brief}_{condition}_r{run}_{timestamp}/
│   │   │   ├── 1_context/
│   │   │   ├── 2_containers/
│   │   │   └── 3_components/
│   └── {experiment_name}_{timestamp}_final.json
```

## Sequential vs Parallel

| Feature | `run_experiments.py` (Sequential) | `run_parallel_experiments.py` (Parallel) |
|---------|-----------------------------------|------------------------------------------|
| **Execution** | One at a time | Multiple simultaneously |
| **Speed** | Slower | Faster |
| **Monitoring** | Easier to follow | More complex |
| **Resource Usage** | Lower | Higher |
| **API Rate Limits** | Safer | May hit limits |
| **Debugging** | Easier | Harder |
| **Recommended For** | Development, testing, debugging | Production runs |

## Examples

### Example 1: Quick Test Run

```bash
# Test role ablation with single condition
python run_experiments.py --experiment role_ablation --temperature 0.5
```

### Example 2: Full Study

```bash
# Run all experiments with optimal temperature
python run_experiments.py --all-experiments --temperature 0.5
```

### Example 3: Debugging

```bash
# Run with deterministic mode for debugging
python run_experiments.py --experiment role_ablation --temperature 0.0
```

### Example 4: Custom Session

```bash
# Run with named session for tracking
python run_experiments.py --experiment role_ablation --session-id test_v1
```

## Monitoring Progress

Watch the terminal output for real-time progress:

```
🚀 STARTING EXPERIMENT: role_ablation
==================================================
🤖 Model: gemini-2.5-flash-lite
🌡️ Temperature: 0.5
📁 Output: data/results/enhanced_experiments/role_ablation
📅 Session: 20251027_120000
==================================================

🔧 Initializing LangSmith project: C4-Sequential-role_ablation-20251027_120000
✅ LangSmith project initialized
   🔗 View in LangSmith: https://smith.langchain.com/

🔄 Running conditions sequentially (one at a time)...

[1/5] Processing condition: baseline...
  📝 clinic-management-system - Round 1
    💾 Saved C4 artifacts
  📝 clinic-management-system - Round 2
    💾 Saved C4 artifacts
  ...
```

## Troubleshooting

### Issue: API Key Missing

```bash
python run_experiments.py --validate-env
```

Fix: Add required keys to `.env` file.

### Issue: Temperature Out of Range

Use values between 0.0 and 1.0:
- `0.0` = Deterministic (identical outputs)
- `0.5` = Balanced (recommended)
- `1.0` = Maximum creativity

### Issue: LangSmith Not Showing Project

The script automatically runs a simple chain to initialize the project.
Check the output for confirmation or visit https://smith.langchain.com/

## Tips

1. **Start Sequential**: Always test with sequential execution first
2. **Monitor Output**: Watch terminal for progress and errors
3. **Check Artifacts**: Artifacts saved immediately after each run
4. **Use Temperature 0.5**: Good balance between variance and quality
5. **Name Sessions**: Use `--session-id` for organized tracking

---

**Date**: October 27, 2025  
**Version**: 2.0  
**Status**: Updated with temperature control and LangSmith initialization
