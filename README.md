# MASC4: collaboration dynamics in LLM-based multi-agent C4 architecture design

Replication package of the article

> Kamil Szczepanik and Jarosław A. Chudziak. *Modeling and Evaluating Collaboration Dynamics in
> LLM-Based Multi-Agent Systems for Automated Software Architecture Design.* Automated Software
> Engineering (under review).

MASC4 generates C4 models of a software system (System Context, Container and Component diagrams)
from a short system brief with a team of LLM agents. At each level the team discusses the design in
round-robin turns, and processing agents turn the discussion into a report, a YAML model and a
C4-PlantUML diagram. The study varies the composition of the team, the speaking order, role
specialization and a shared memory, and evaluates the models with deterministic structural metrics
and an LLM judge (ISO/IEC 25010, ATAM scenarios, requirement coverage).

This repository contains the code, prompts, briefs, scenarios, configurations and analysis scripts
of the study, and in `results/` the raw outputs of all runs (transcripts, reports, YAML models,
diagrams, scores and the judge's justifications). Each release is archived on Zenodo: DOI to be added.

## Contents

| Path | Content |
|---|---|
| `src/masc4/prompts.py` | personas and prompts of all agents |
| `src/masc4/conditions.py` | experimental conditions (team in speaking order, memory) |
| `src/masc4/pipeline.py` | generation of one C4 model (L1 → L2 → L3, one discussion per level and container) |
| `src/masc4/llm.py` | Gemini API client with retries and call logging |
| `src/masc4/runner.py` | resumable batches of runs in a seeded random order |
| `src/masc4/structural.py` | deterministic metrics: completeness, compilation, abstraction adherence, C4-SC, cross-level consistency, size |
| `src/masc4/judge.py` | LLM judge: ISO/IEC 25010, ATAM scenarios, requirement coverage |
| `src/masc4/stats.py` | statistics of the analysis plan |
| `configs/conditions_v2.yaml` | the eleven conditions and the generation settings |
| `configs/scenarios/` | eight ATAM scenarios per brief |
| `configs/analysis_plan.yaml` | analysis plan: outcomes, hypotheses, tests |
| `data/briefs/` | the six system briefs |
| `scripts/` | command-line entry points (below) |
| `tests/` | unit tests with a scripted fake model (no API key or network needed) |

## Setup

- Python 3.9 or newer: `pip install -r requirements.txt`
- Java 11 or newer and PlantUML 1.2025.10, saved as `plantuml.jar` in the repository root
  (or passed with `--jar`); needed only for the compilation metric
- A Gemini API key (Google AI Studio) in the environment variable `GEMINI_API_KEY`, or in a
  `.env` file passed with `--env-file` (see `.env.example`)

Run the tests with `python -m pytest tests -q`.

## Reproducing the study

```bash
# 1. Generation: 11 conditions x 6 briefs x 6 repetitions, the baseline C0 twice as often
#    (432 runs in one randomized plan); --dry-run prints the plan without calling the API
python scripts/run_generation.py --reps 6 --out results/v2 --workers 6 --max-cost 60

# progress of generation and evaluation (in a second terminal)
python scripts/progress.py results/v2 --planned 432 --watch 30

# 2. Structural metrics and the main judge on all completed runs
python scripts/run_evaluation.py --results results/v2 --judge-model gemini-3.8-flash --workers 4

# 3. Control judge on the first repetition of every condition and brief (66 runs)
python scripts/run_evaluation.py --results results/v2 --judge-model gemini-3.6-flash --sample-rep 1 --workers 4

# 4. Test-retest: the main judge again on a random sample of 20 runs
python scripts/run_evaluation.py --results results/v2 --judge-model gemini-3.8-flash --sample 20 --tag retest

# 5. One CSV row per run (all metrics and judges), then the analysis of the plan
python scripts/run_evaluation.py --results results/v2 --no-judge --csv results/v2/runs.csv
python scripts/analyze.py results/v2/runs.csv --out results/v2/analysis
```

At the prices of October 2026, generation cost about 0.11 USD and the main judge about 0.04 USD
per run; a run takes 2.5–3 minutes.

**Interruptions.** All batches can be stopped with Ctrl+C and resumed with the same command.
Runs that completed, or that ended with an unusable team output (`invalid_output`: no valid YAML or
glossary after one retry), are final. Runs stopped by an infrastructure error (API, network, quota) are
repeated, and the earlier attempt is kept in `previous_attempts/`. `--max-cost` stops starting
new runs once the estimated generation cost reaches the limit, in USD.

**Unstable connection.** A model call without network waits up to 30 minutes for the connection to
return; other API errors are retried 10 times. Runs that still fail are repeated automatically after
the plan, in up to three further passes 10 minutes apart (`--repeat-failed`). Whatever remains failed
is repeated by running the same command again.

**Appendix of the article.** `scripts/export_appendix.py --paper PAPER.tex` writes the prompts,
briefs, judge rubrics and scenarios from the code into the article.

## Output of a run

`results/v2/<condition>/<brief>/repNN/`:

| File | Content |
|---|---|
| `run.json` | status, condition, team, token use, model versions, hashes of the brief and the prompts, code version |
| `brief.yaml` | the brief used for the run |
| `transcript.jsonl` | every turn of the discussions |
| `1_context_*`, `2_container_*`, `3_components/` | analysis report, YAML definition and PlantUML diagram of each level |
| `c4_model.json` | all artifacts of the run in one file |
| `glossary_after_L1.json`, `glossary_after_L2.json` | shared memory (condition C10 only) |
| `llm_calls.jsonl` | one record per model call |
| `structural.json` | deterministic metrics |
| `judge_<model>[__<tag>].json`, `judge_calls_<model>[__<tag>].jsonl` | judge scores, justifications and calls |

## Earlier versions

- Tag `hicss-2026`: the implementation that accompanies the MASC4 conference paper.
- Tag `journal-v1-as-run`: the code of the first submission of the journal article, kept unchanged.

## License

The code is released under the MIT License (`LICENSE`). The data in `results/` are released under the
Creative Commons Attribution 4.0 International License (CC BY 4.0).

## Citation

Please cite the article above; citation metadata are in `CITATION.cff`.
