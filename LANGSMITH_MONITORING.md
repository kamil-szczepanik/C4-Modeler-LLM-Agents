# LangSmith Monitoring Guide

## 🎯 Overview

The parallel experiment system now initializes LangSmith projects **immediately** so you can monitor progress in real-time from the start of execution.

## 🔧 How It Works

### Project Initialization Chain

Before running experiments, the system creates a simple LangChain chain that:
1. Sends an initial trace to LangSmith
2. Makes the project visible immediately in the LangSmith UI
3. Allows real-time monitoring from the beginning

```python
# Simple initialization chain
llm = ChatGoogleGenerativeAI(model=model_name, temperature=0, max_tokens=50)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Respond with exactly: 'LangSmith project initialized successfully.'"),
    ("user", "Initialize project")
])
chain = prompt | llm | StrOutputParser()
result = chain.invoke({})  # Creates first trace -> Project appears in LangSmith
```

### Project Structure

When you run experiments, you'll see multiple projects in LangSmith:

#### 1. Main Orchestrator Project
- **Name**: `C4-Parallel-Study-{session_id}`
- **Purpose**: Initial project creation and orchestration
- **Example**: `C4-Parallel-Study-20241023_153022`

#### 2. Individual Experiment Projects
- **Name**: `C4-Parallel-{experiment_name}-{session_id}`
- **Purpose**: All traces for a specific experiment
- **Examples**: 
  - `C4-Parallel-role_ablation-20241023_153022`
  - `C4-Parallel-interaction_order-20241023_153022`

## 📊 Monitoring Your Experiments

### LangSmith Dashboard

1. **Go to**: https://smith.langchain.com/
2. **Navigate to**: Projects tab
3. **Look for**: Projects matching your session ID

### What You'll See

```
LangSmith Projects:
├── C4-Parallel-Study-20241023_153022          (Main orchestrator)
├── C4-Parallel-role_ablation-20241023_153022  (Experiment 1)
├── C4-Parallel-interaction_order-20241023_153022 (Experiment 2)
└── C4-Parallel-shared_memory-20241023_153022  (Experiment 3)
```

### Real-Time Monitoring

Each project will show:
- ✅ **Total traces**: Number of LLM calls made
- ⏱️ **Latency**: Response times for each call
- 💰 **Cost**: Token usage and costs
- 📊 **Success rate**: Percentage of successful calls
- 🔍 **Individual traces**: Detailed view of each LLM interaction

### Example Timeline

```
09:00 AM - Orchestrator initialized
           └─ Project "C4-Parallel-Study-20241023_090000" appears in LangSmith ✅

09:01 AM - role_ablation experiment starts
           └─ Project "C4-Parallel-role_ablation-20241023_090000" appears ✅
           └─ First C4 generation begins (traces start appearing)

09:35 AM - First C4 model complete
           └─ 150+ traces visible in LangSmith
           └─ Evaluation traces appear

... continues with real-time updates
```

## 🚀 Running with Monitoring

### Basic Usage

```bash
# Run single experiment (monitor immediately)
python run_parallel_experiments.py --experiments role_ablation --model gemini-2.5-flash-lite
```

**Output includes**:
```
🔧 LANGSMITH INITIALIZATION
================================================================================
🔧 Initializing LangSmith project: C4-Parallel-Study-20241023_153022
✅ LangSmith project initialized: C4-Parallel-Study-20241023_153022
   Response: LangSmith project initialized successfully....
   🔗 View in LangSmith: https://smith.langchain.com/
================================================================================

🚀 PARALLEL EXPERIMENT ORCHESTRATOR
================================================================================
📊 Experiments to run: 1
...
📊 LangSmith Monitoring:
   Main project: C4-Parallel-Study-20241023_153022
   View at: https://smith.langchain.com/
   Individual experiments will appear as: C4-Parallel-{experiment}-{session_id}
```

### Custom Session ID

```bash
# Use custom session ID for easier tracking
python run_parallel_experiments.py \
  --experiments role_ablation \
  --model gemini-2.5-flash-lite \
  --session-id my_thesis_run_1
```

Projects will appear as:
- `C4-Parallel-Study-my_thesis_run_1`
- `C4-Parallel-role_ablation-my_thesis_run_1`

## 🔍 Trace Details

Each C4 generation creates multiple traces showing:

### Context Level
- Agent interactions (Architect, Business Analyst, UML Expert)
- Prompt templates
- Model responses
- Context diagram generation

### Container Level
- Container identification
- Dependency analysis
- Container diagram creation

### Component Level
- Component breakdowns
- Internal structure
- Detailed diagrams

### Evaluation Phase
- ISO/IEC 25010 metrics calculation
- ATAM scenario evaluation
- Architectural soundness analysis

## 💡 Monitoring Best Practices

### 1. Check Project Initialization
✅ Verify the initialization message appears before experiments start
✅ Confirm the project URL is displayed

### 2. Open LangSmith Early
Open https://smith.langchain.com/ **before** or **immediately after** starting experiments to see traces appear in real-time.

### 3. Filter by Session ID
Use the session ID (timestamp or custom) to filter projects in LangSmith dashboard.

### 4. Monitor Resource Usage
Watch for:
- **Token consumption**: Are you within budget?
- **Latency spikes**: Are API calls slowing down?
- **Error rates**: Are calls failing?

### 5. Compare Experiments
Use LangSmith's comparison features to analyze differences between experiments.

## 🐛 Troubleshooting

### Project Not Appearing?

**Check 1**: LANGCHAIN_API_KEY is set
```bash
# Verify in PowerShell
echo $env:LANGCHAIN_API_KEY
```

**Check 2**: Tracing is enabled
```bash
echo $env:LANGCHAIN_TRACING_V2
# Should output: true
```

**Check 3**: Initialization succeeded
Look for:
```
✅ LangSmith project initialized: C4-Parallel-Study-{session_id}
```

If you see:
```
⚠️ Warning: Could not initialize LangSmith project: ...
```
The experiment will still run, but traces may not be visible immediately.

### Delayed Traces?

LangSmith may have a 5-30 second delay before traces appear. The initialization chain ensures the **project** appears immediately, but individual traces may still have slight delays.

### Missing Traces?

**Cause**: Network issues or API throttling
**Solution**: Traces are buffered and will appear when connection recovers

## 📈 Performance Metrics

### Expected Trace Counts (per run)

| Phase | Traces | Duration |
|-------|--------|----------|
| Context | ~40-60 | ~10 min |
| Container | ~50-80 | ~12 min |
| Components | ~60-100 | ~8 min |
| Evaluation | ~20-30 | ~3 min |
| **Total** | **~170-270** | **~32 min** |

### For Full Experiment (75 runs)

- **Total traces**: ~12,000 - 20,000
- **Total duration**: ~18-40 hours (parallel)
- **Projects created**: 2 (main + experiment)

## 🎯 Key Benefits

1. ✅ **Immediate visibility**: Projects appear before any experiments run
2. ✅ **Real-time monitoring**: See traces as they happen
3. ✅ **Better debugging**: Catch issues early
4. ✅ **Progress tracking**: Know exactly where you are
5. ✅ **Cost monitoring**: Watch spending in real-time
6. ✅ **Performance analysis**: Identify bottlenecks immediately

## 🔗 Quick Links

- **LangSmith Dashboard**: https://smith.langchain.com/
- **LangSmith Docs**: https://docs.smith.langchain.com/
- **Project Filtering**: Use session ID to find your runs
- **Trace Analysis**: Click on any trace to see full details

---

**Now you can monitor your 75-run experiments in real-time! 🚀**
