# Understanding Parallelization in Your Experiment

## 🎯 Quick Answer

**Yes, you should see multiple conditions running simultaneously!** 

With the updated code, when you run:
```bash
python run_parallel_experiments.py --experiments role_ablation --model gemini-2.5-flash-lite
```

You'll see **2 conditions running in parallel** (configurable with `--max-conditions`).

## 📊 Two-Level Parallelization Architecture

### Visual Overview

```
┌─────────────────────────────────────────────────────────────────┐
│ ORCHESTRATOR (run_parallel_experiments.py)                     │
│ ProcessPoolExecutor with max_workers=3                         │
└─────────────────────────────────────────────────────────────────┘
                          │
         ┌────────────────┼────────────────┐
         │                │                │
         ▼                ▼                ▼
    ┌─────────┐      ┌─────────┐      ┌─────────┐
    │ Exp 1   │      │ Exp 2   │      │ Exp 3   │
    │ Process │      │ Process │      │ Process │
    └─────────┘      └─────────┘      └─────────┘
         │                │                │
         │                │                │
         ▼                ▼                ▼
   ┌──────────────────────────────────────────┐
   │ EnhancedExperimentRunner                 │
   │ ThreadPoolExecutor with max_workers=2    │
   └──────────────────────────────────────────┘
         │
         ├─────────┬─────────┐
         │         │         │
         ▼         ▼         ▼
    ┌────────┐ ┌────────┐ ┌────────┐
    │ Cond 1 │ │ Cond 2 │ │ Cond 3 │  ← 2 run simultaneously
    │ Thread │ │ Thread │ │ Thread │
    └────────┘ └────────┘ └────────┘
         │         │         │
         │         │         │
    Each condition runs:
    - 5 briefs × 3 rounds = 15 runs
    - Sequential within thread
```

## 🔧 Level 1: Experiment-Level Parallelization

**Where**: `run_parallel_experiments.py`  
**Technology**: `ProcessPoolExecutor` (true parallelism, separate Python processes)  
**Default**: 3 experiments at once  
**Configure**: `--max-experiments N`

### Example with 3 Experiments

```bash
python run_parallel_experiments.py \
  --experiments role_ablation interaction_order shared_memory \
  --max-experiments 3
```

**What happens**:
```
09:00 AM - Start all 3 experiments simultaneously
├─ Process 1: role_ablation starts
├─ Process 2: interaction_order starts
└─ Process 3: shared_memory starts

All run independently in parallel! ✅
```

### Your Current Case (1 Experiment)

```bash
python run_parallel_experiments.py \
  --experiments role_ablation \
  --max-experiments 3  # ← Doesn't matter, only 1 experiment to run
```

**What happens**:
```
09:00 AM - Start role_ablation
└─ Process 1: role_ablation starts
   (No other experiments to parallelize)
```

So Level 1 parallelization **doesn't help** when running a single experiment.

## ⚙️ Level 2: Condition-Level Parallelization (NEW!)

**Where**: `src/c4modeler/experiments.py`  
**Technology**: `ThreadPoolExecutor` (threads within same process)  
**Default**: 2 conditions at once  
**Configure**: `--max-conditions N`

### Example: Role Ablation (5 Conditions)

```bash
python run_parallel_experiments.py \
  --experiments role_ablation \
  --max-conditions 2  # ← Run 2 conditions simultaneously
```

**What happens**:
```
09:00 AM - Start role_ablation experiment
           └─ ThreadPoolExecutor created with max_workers=2

09:01 AM - Submit all 5 conditions to thread pool
           ├─ Thread 1: baseline condition starts
           └─ Thread 2: no_architect condition starts
           
           (Threads 3,4,5 wait in queue)

10:30 AM - baseline completes (first finish)
           └─ Thread 1: no_business_analyst condition starts
           
11:00 AM - no_architect completes
           └─ Thread 2: no_uml_expert condition starts
           
... continues until all 5 conditions complete
```

### Progress You'll See

**OLD (Sequential)**:
```
🔬 Running condition 1/5: Baseline
  📝 clinic-management-system - Round 1
  📝 clinic-management-system - Round 2
  ...
  (30 minutes later)
🔬 Running condition 2/5: No Architect
  ...
```

**NEW (Parallel with max_workers=2)**:
```
🔄 Running 5 conditions with max 2 parallel workers

(Threads start simultaneously)
Thread 1: 🔬 Running condition: Baseline
Thread 2: 🔬 Running condition: No Architect

... both running at same time ...

✅ [1/5] Completed condition: No Architect  (finished first)
Thread 2: 🔬 Running condition: No Business Analyst  (picks up next work)

✅ [2/5] Completed condition: Baseline  (finished second)
Thread 1: 🔬 Running condition: No UML Expert  (picks up next work)

... continues ...

✅ [5/5] Completed condition: Generic Roles
🎯 All 5 conditions completed!
```

## 📈 Performance Comparison

### For role_ablation: 5 conditions × 5 briefs × 3 rounds = 75 runs

| Configuration | Time | Speed-up |
|--------------|------|----------|
| **Sequential** (old) | 37.5 hours | 1x |
| **max-conditions=2** (new) | 18.8 hours | 2x ✅ |
| **max-conditions=3** | 12.5 hours | 3x ✅ |
| **max-conditions=5** | 7.5 hours | 5x ✅ |

### Why Not max-conditions=5 (all at once)?

**Reasons for max-conditions=2 as default**:

1. **API Rate Limits**: Running too many parallel calls may hit Gemini API limits
2. **Memory Usage**: Each condition holds full C4 models in memory
3. **System Resources**: Your machine has finite CPU/RAM
4. **LangSmith Monitoring**: Easier to track with fewer parallel traces

**Recommended**: Start with 2, increase to 3 if stable.

## 🚀 Running Your Experiment Now

### Test the Parallelization

```bash
# Run with default parallelization (2 conditions at once)
python run_parallel_experiments.py \
  --experiments role_ablation \
  --model gemini-2.5-flash-lite

# Or be explicit about parallelism
python run_parallel_experiments.py \
  --experiments role_ablation \
  --model gemini-2.5-flash-lite \
  --max-conditions 2
```

### What You'll See in Terminal

```
🔧 LANGSMITH INITIALIZATION
================================================================================
🔧 Initializing LangSmith project: C4-Parallel-Study-20241023_153022
✅ LangSmith project initialized
================================================================================

🚀 PARALLEL EXPERIMENT ORCHESTRATOR
================================================================================
📊 Experiments to run: 1
🔧 Max parallel experiments: 3
⚙️ Max parallel conditions per experiment: 2  ← KEY INFO
...

🧪 Starting Enhanced Experiment: Role Ablation Study
📋 Description: ...
🎯 Purpose: ...
⚙️ Parallel conditions: 2  ← CONFIRMS PARALLELIZATION

🔄 Running 5 conditions with max 2 parallel workers  ← YOU'LL SEE THIS

... conditions start running in parallel ...
```

### What You'll See in LangSmith

**Project**: `C4-Parallel-role_ablation-20241023_153022`

**Traces appearing simultaneously**:
```
Thread 1 (baseline):
├─ 09:01:15 - Context generation started
├─ 09:02:30 - Container generation started
└─ 09:03:45 - Component generation started

Thread 2 (no_architect):  ← RUNNING AT SAME TIME
├─ 09:01:18 - Context generation started
├─ 09:02:33 - Container generation started
└─ 09:03:50 - Component generation started
```

You'll see **interleaved traces** from multiple conditions running concurrently!

## 🔍 How to Verify Parallelization is Working

### Check 1: Terminal Output

You should see multiple condition names appearing close together in time, not sequentially.

### Check 2: LangSmith Timestamps

Open LangSmith and check trace timestamps - you should see traces from different conditions with overlapping times.

### Check 3: System Resources

**Windows Task Manager**:
- Press `Ctrl+Shift+Esc`
- Check CPU usage - should be higher with parallel execution
- Look for multiple `python.exe` processes

### Check 4: Progress Files

```powershell
# Watch progress files being created
Get-ChildItem "data/results/enhanced_experiments" -Filter "*progress*" | 
  Sort-Object LastWriteTime -Descending | 
  Select-Object Name, LastWriteTime
```

With parallelization, you'll see progress files created closer together in time.

## 🎛️ Tuning Parallelization

### Conservative (Stable, Lower Risk)
```bash
--max-experiments 2 --max-conditions 2
```
- Good for: First runs, testing, limited resources
- Time: ~18-20 hours for role_ablation

### Balanced (Recommended)
```bash
--max-experiments 3 --max-conditions 2
```
- Good for: Production runs, reliable performance
- Time: ~18-20 hours for role_ablation (1 experiment only)
- Time: ~10-15 hours for 3 experiments

### Aggressive (Fast, Higher Risk)
```bash
--max-experiments 3 --max-conditions 3
```
- Good for: Powerful machines, urgent deadlines
- Time: ~12-15 hours for role_ablation
- Risk: May hit API limits, higher memory usage

### Maximum (Experimental)
```bash
--max-experiments 3 --max-conditions 5
```
- Time: ~7-10 hours for role_ablation
- Risk: High chance of API throttling, memory issues

## 💡 Key Takeaways

1. ✅ **You WILL see parallel execution** with the updated code
2. ✅ **Default 2 conditions run simultaneously** (not sequential anymore)
3. ✅ **Both experiment-level AND condition-level parallelization** active
4. ✅ **Time savings: 50%** (37.5h → 18.8h for role_ablation)
5. ✅ **Monitor in LangSmith** to see interleaved traces

## 🐛 Troubleshooting

### "I only see 1 condition running"

**Check terminal output** - look for:
```
🔄 Running 5 conditions with max 2 parallel workers
```

If you don't see this, the code wasn't updated properly.

### "Conditions still seem sequential"

**Possible causes**:
1. `--max-conditions 1` specified (check arguments)
2. GIL (Global Interpreter Lock) limitation - threads for I/O work well
3. API rate limiting causing effective serialization

### "Getting API errors"

Reduce parallelism:
```bash
--max-conditions 1  # Back to sequential
```

---

**Ready to see 2 conditions running in parallel! 🚀**
