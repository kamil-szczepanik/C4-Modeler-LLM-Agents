# C4Modeler — Collaborative LLM Agents for C4 Software Architecture

Generate C4 (Context → Container → Component) analyses, YAML definitions, and PlantUML diagrams from short system briefs using single- or multi-agent workflows. Includes structural checks (abstraction, cross-level consistency, completeness), PlantUML compilation tests, and LLM-as-a-Judge evaluations.

> This repo accompanies the HICSS paper (soon to be published).

---

## ✨ Features

* **Collaborative agents** (round-robin personas) or **simple** single-agent mode
* **End-to-end pipeline**: Brief → Analysis → YAML → PlantUML
* **Batch experiments** across `data/briefs/`
* **Evaluation suite**: compilation success, abstraction adherence, definitional & cross-level consistency, naming consistency, qualitative rubric, architect critique, security assessment
* **Mermaid graph visualization** of the workflow (optional)

---

## 📦 Install

**Python 3.10+** required. Java is needed for PlantUML compilation checks.

```bash
git clone <your-repo-url>
cd <your-repo>
pip install -e .
# (optional) If you track exact versions:
pip install -r requirements.txt
```

### Environment

Create a `.env` in repo root:

```bash
OPENAI_API_KEY=...
GEMINI_API_KEY=...     # used internally as GOOGLE_API_KEY
DEEPSEEK_API_KEY=...
XAI_API_KEY=...

LANGCHAIN_TRACING_V2=false
LANGCHAIN_API_KEY=...
LANGCHAIN_PROJECT=HICSS-C4
```

---

## 🗂️ Repo Layout

```
src/
  c4modeler/
    __init__.py
    agents.py
    evaluation.py
    experiments.py
    graph.py
    llm.py
    models.py
    pipeline.py
    prompts.py
    types.py
    utils.py
notebooks/
  01_quickstart.ipynb
data/
  briefs/       # your YAML briefs
  results/      # generated artifacts (gitignored)
paper/
  Final_HICSS_Paper.pdf
pyproject.toml
README.md
.gitignore
```

---

## 🚀 Quickstart

### Visualize the workflow (optional)

```python
from IPython.display import Image, display
from c4modeler.experiments import build_app_from_config

app = build_app_from_config(
    model_name="gpt-4o-mini",
    analysis_method="collaborative",
    collab_rounds=2,
)
display(Image(app.get_graph(xray=True).draw_mermaid_png()))
```

### Single brief (end-to-end)

```python
from c4modeler.pipeline import generate_c4_for_brief
from c4modeler.utils import load_yaml

brief = load_yaml("data/briefs/clinic-management-system.yaml")
c4_model, out_dir = generate_c4_for_brief(
    brief,
    model_name="gpt-4o-mini",          # or gemini-1.5-pro-latest, deepseek-chat, grok-3-latest...
    analysis_method="collaborative",   # or "simple"
    collab_rounds=2,
    results_dir="data/results",
)
print("Artifacts saved to:", out_dir)
```

Artifacts saved (example):

```
data/results/<timestamp>-<brief-slug>-<thread>/
  1_context_analysis.md
  1_context_definition.yaml
  1_context_diagram.puml
  2_container_analysis.md
  2_container_definition.yaml
  2_container_diagram.puml
  3_components/
    <component>_analysis.md
    <component>_definition.yaml
    <component>_diagram.puml
```

### Batch run (all briefs) + Evaluation

```python
from c4modeler.experiments import (
    build_app_from_config,
    run_all_experiments,
    run_all_evaluations,
    load_briefs_from_dir,
)

# 1) Load briefs
system_briefs = load_briefs_from_dir("data/briefs")

# 2) Generate
cfg = {
    "name": "GPT4omini_Collab_1r",
    "model_name": "gpt-4o-mini",
    "analysis_method": "collaborative",
    "collab_rounds": 1,
}
app = build_app_from_config(**{
    "model_name": cfg["model_name"],
    "analysis_method": cfg["analysis_method"],
    "collab_rounds": cfg["collab_rounds"],
})
experiment_results = run_all_experiments(app_instance=app, system_briefs_data=system_briefs)

# 3) Evaluate (structural + LLM judge)
summary = run_all_evaluations(
    experiment_results=experiment_results,
    experiment_config=cfg,
    judge_model_name="gemini-2.5-flash-preview-05-20",
)
```

---

## 🧠 Models

Defined in `c4modeler/llm.py`. Supported keys include:

* OpenAI: `gpt-4o`, `gpt-4o-mini`
* Google: `gemini-1.5-flash-latest`, `gemini-1.5-pro-latest`, `gemini-2.5-pro-preview-06-05` (mapped to `GOOGLE_API_KEY`)
* DeepSeek: `deepseek-chat`
* xAI: `grok-beta`, `grok-3-latest`

Switch via `model_name` in the functions above.

---

## ✅ Evaluation Metrics

Implemented in `c4modeler/evaluation.py`:

* **Compilation Success** (PlantUML `java -jar ... -failfast2`)
* **Abstraction Adherence** (Context vs Container vs Component rules)
* **Definitional Consistency** (YAML ↔ PlantUML)
* **Cross-Level Consistency** (Context ↔ Container ↔ Component)
* **Emergent Naming Consistency** (dominant style + outliers)
* **Qualitative Rubric** (LLM judge per diagram)
* **Principal Architect Critique** (LLM judge holistic review)
* **Security “Red Team” Assessment** (LLM judge over Container diagram)

Outputs are consolidated under `data/results/.../evaluation_summaries/` and a zip is produced for convenience.

---

## 🧪 Notebooks

* `notebooks/01_quickstart.ipynb` — graph viz, one-brief run, batch run + evaluation.

> If imports fail in Jupyter, ensure you ran `pip install -e .` from repo root and import via `from c4modeler...`.

---

## 🔧 Troubleshooting

* **Graph PNG fails** → try `app.get_graph(xray=True).draw_mermaid_inline()`, or ensure your environment supports Mermaid → PNG.
* **PlantUML check fails** → ensure Java is installed (`java -version`). The jar is auto-downloaded on first run.
* **Rate limits** → lower `collab_rounds`, use a smaller model, or set provider keys correctly in `.env`.

---

## 📄 License

MIT.

---

## 📣 Citation

Waiting for publication...
