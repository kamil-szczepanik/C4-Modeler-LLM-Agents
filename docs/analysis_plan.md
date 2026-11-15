# Analysis plan of the experiments

Status: approved by both authors before the main data collection; amended before any data were collected (Section 9).
Pilot data (October 2026) were used only to choose the sample size, to test the
software, and to rehearse this analysis; they are not part of the confirmatory analysis.
The machine-readable version of this plan is `configs/analysis_plan.yaml` in the code
repository; the analysis is executed by `scripts/analyze.py`.

## 1. Research questions

- **RQ1 (roles):** How does each expert role contribute to the structural and semantic quality of the generated C4 models?
- **RQ2 (interaction parameters):** How do speaking order, role specialization and a shared memory affect quality and consistency?
- **RQ3 (evaluation):** How reliable and how informative is an LLM-judge evaluation grounded in ISO/IEC 25010 and ATAM scenarios, compared with deterministic structural metrics?

## 2. Design

**Conditions:** 11 conditions in four studies. Every study compares its conditions with the shared baseline C0.

| Study | Condition | Team, in speaking order |
|---|---|---|
| all | C0 baseline | Product Owner → Software Architect → DevOps Specialist → Security Specialist |
| Ablation | C1 | without Product Owner |
| Ablation | C2 | without Software Architect |
| Ablation | C3 | without DevOps Specialist |
| Ablation | C4 | without Security Specialist |
| Ablation | C5 | a single Software Architect |
| Ablation | C6 | four Software Architects |
| Order | C7 | Software Architect first (rotation of C0) |
| Order | C8 | Security Specialist first (rotation of C0) |
| Specialization | C9 | four generic Software Engineers |
| Memory | C10 | C0 team with the Glossary Agent (shared knowledge context K, built after L1 and L2, injected into L2 and L3) |

**Generation settings:**
- **Briefs:** six briefs: three canonical (Clinic, Library, Bookstore) and three complex (Payment Fraud Screening, Claims System Modernization, Cross-Border Telehealth).
- **Repetitions:** 6 per condition and brief, giving **36 runs per condition**; C0 gets 12 per brief (**72 runs**). Total: 432 runs.
- **Run order:** randomized with a fixed seed.
- **Models:**
  - generation: `gemini-3.5-flash-lite`, temperature 0.5, 2 discussion rounds per level;
  - main judge: `gemini-3.8-flash`, temperature 0;
  - control judge: `claude-sonnet-5-5` (Anthropic, another model family), medium thinking effort, default sampling (the model does not accept a temperature setting).
- **Unchanged during data collection:** prompts, briefs, ATAM scenarios and judge rubrics.

## 3. Experimental unit and sample size

- **Experimental unit:** one run, i.e. the generation of one complete C4 model (L1, L2 and one L3 diagram per container) for one brief under one condition.
- **Analysis:** all analyses are stratified by brief.

**Pilot variability:** four C0 runs on the same brief gave run-to-run standard deviations of 0.14 for C4-SC and 0.35 for the judge's ISO mean. These estimates are rough: they rest on only four runs, made with the earlier version of the turn prompt.

**Detectable effects (36 vs. 72 runs, α = 0.05, power 0.80, normal approximation):**

| | In standard deviations | C4-SC | ISO mean |
|---|---|---|---|
| Uncorrected | about 0.57 SD | about 0.08 | about 0.20 |
| Bonferroni-level threshold (worst case of Holm) | about 0.75 SD | about 0.10 | about 0.26 |

**Stopping rule:** data collection stops when every condition has its planned number of final runs. If the budget limit stops the batch earlier, the analysis uses the runs completed by then and the shortfall is reported. Because the run order is randomized, an early stop does not favour any condition.

**Run outcomes:**
- *Infrastructure failures* (API, network, quota) are repeated, because they are unrelated to the condition.
- *Invalid outputs* are final and are not repeated. An output is invalid when no valid YAML is produced after the one allowed retry, or no valid glossary JSON.
- Invalid outputs are reported per condition as an outcome and excluded from the metric analyses, because no model exists for them.

## 4. Outcomes

**Primary (confirmatory):**
1. **C4-SC:** C4 structural consistency = 5 × the share of relationships whose endpoints resolve along the C4 scope chain (same diagram, then the Container and Context levels), pooled over all diagrams of a run.
2. **ISO mean:** the main judge's mean score over the eight ISO/IEC 25010:2011 characteristics (1–5 each).

**Secondary:**

| Metric | Definition | Status |
|---|---|---|
| strict C4-SC | endpoints defined in the same diagram | targeted hypothesis H3, otherwise exploratory |
| compilation | share of diagrams that compile in PlantUML | exploratory |
| abstraction adherence | share of diagrams passing the level rules | exploratory |
| completeness | share of expected artifacts present | exploratory |
| L1→L2 consistency | Jaccard similarity of people and external systems | targeted H11 |
| L2→L3 consistency | share of component diagrams whose parent container and non-component elements exist at L2 | exploratory |
| ATAM responsiveness index | mean of (score − 1)/4 over the 8 scenarios of the brief | exploratory |
| requirement coverage | (full + 0.5 × partial) / number of requirements | targeted H1, H7, H9 |
| single ISO characteristics | judge scores per characteristic | targeted H2, H4–H6, H8, H10 |

**Covariates and descriptives:** total number of elements and relationships, number of containers, number of discussion turns and words.

**Pilot check of the outcomes:** no hypothesis is stated on L2→L3 consistency, because it was 1.0 in all nine pilot runs of C0, leaving no room for a memory effect. ISO performance efficiency and compatibility were also at the maximum in all C0 pilot runs; they stay in the ISO mean, and the ceiling analysis (Section 7) reports this.

## 5. Hypotheses

**Primary.** Each of the ten conditions differs from C0 on each primary metric (two-sided). Expected directions:
- lower for C1–C5 and C9;
- higher for C10 on C4-SC;
- no directional expectation for C6, C7 and C8.

**Role-specific (confirmatory, two-sided tests, expected direction):**

| Id | Condition | Metric | Expected |
|---|---|---|---|
| H1 | C1 no Product Owner | requirement coverage | lower |
| H2 | C1 no Product Owner | ISO usability | lower |
| H3 | C2 no Software Architect | strict C4-SC | lower |
| H4 | C2 no Software Architect | ISO maintainability | lower |
| H5 | C3 no DevOps Specialist | ISO reliability | lower |
| H6 | C4 no Security Specialist | ISO security | lower |
| H7 | C5 single architect | requirement coverage | lower |
| H8 | C6 four architects | ISO usability | lower |
| H9 | C7 architect first | requirement coverage | lower |
| H10 | C9 generic team | ISO security | lower |
| H11 | C10 shared memory | L1→L2 consistency | higher |

A role-specific hypothesis counts as *supported* only if the Holm-adjusted p is below 0.05 *and* the effect has the expected sign.

## 6. Statistical analysis

**Effect:** the difference between the condition and C0 in the mean of the metric, computed within each brief and averaged over the briefs (equal weights).

**Test:** two-sided permutation test with condition labels permuted within each brief (10,000 permutations).

**Interval:** 95% percentile bootstrap, resampling runs within each brief and condition (10,000 resamples).

**Effect size:** Cliff's δ on the pooled runs, with magnitude thresholds of 0.147, 0.33 and 0.474. Every condition covers the six briefs in equal proportions, so pooling does not mix brief differences into δ.

**Multiplicity:**
- Holm correction over the ten comparisons, separately for each primary metric.
- Holm correction over the eleven role-specific hypotheses.
- Exploratory analyses report unadjusted p-values and are labelled as exploratory.

**Sensitivity:** effects on the primary metrics re-estimated by OLS with brief fixed effects and log(total elements) as a covariate, with HC3 standard errors. This checks whether an effect is only a by-product of model size, for example because fewer agents produce smaller models.

**Exploratory:**
- effects computed separately on canonical and complex briefs;
- invalid-output rates per condition;
- decomposition of the team effect: three further contrasts between conditions, estimated like the comparisons with C0 (stratified effect, bootstrap CI, unadjusted permutation test) for both primary outcomes:
  - C6 vs. C5: team size and discussion length without role diversity (four identical architects vs. one);
  - C6 vs. C9: role specialization at equal team size and homogeneity (four architects vs. four generic engineers);
  - C7 vs. C1: presence of the Product Owner with the same opening speaker (the Software Architect opens both).
  Together with C0 vs. C6 (role diversity at equal size and specialization, a confirmatory comparison) they separate the effects of team size, diversity and specialization.

**Interpretation:**
- Non-significant results are reported as such, with their confidence intervals.
- A difference is called negligible only if its 95% CI lies entirely within ±0.25 ISO points or ±0.10 C4-SC points, the smallest effects we consider practically relevant. Otherwise a non-significant result is reported as inconclusive.

## 7. Evaluation quality (RQ3)

- **Test-retest:** the main judge re-evaluates a random sample of 20 completed runs (fixed seed).
- **Control judge:** `claude-sonnet-5-5` evaluates the first repetition of every condition and brief (66 runs) with the same prompts. It comes from another provider and model family than the generator and the main judge, so it tests whether the main judge favours its own family (R3.2).
- **Agreement statistics** (both comparisons; ISO mean, ATAM index, requirement coverage and each ISO characteristic): ICC(A,1), Krippendorff's α (interval), the mean difference between the two judgements with a bootstrap 95% CI, Spearman ρ, and exact agreement for the integer ISO scores. ICC and α measure absolute agreement and are lowered by a constant offset; the mean difference and ρ separate offset from ranking.
- **Judge dependence of the conclusions:** on the control sample, the effects of the ten conditions on the ISO mean, ATAM index and requirement coverage, estimated under both judges for the same runs; number of effects with the same direction and Spearman ρ between the two sets of effects. Exploratory.
- **Convergent validity:** Spearman ρ (bootstrap 95% CI) between C4-SC and the ISO mean, between compilation and the ISO mean, and between requirement coverage and ISO functional suitability.
- **Size bias:** Spearman ρ between the total number of elements and both the ISO mean and C4-SC.
- **Ceiling:** share of runs at the maximum score per ISO characteristic and for C4-SC, overall and separately for canonical and complex briefs. Also under both judges on the control sample. This addresses R1.4: does the ceiling depend on the task, and on the judge?

## 8. Deviations

Any deviation from this plan (changed analyses, additional analyses, problems during data collection) will be reported in the paper and in the response to the reviewers, together with its reason.

## 9. Amendments before data collection

Made after the plan was approved and before any run of the main study was generated or judged:

1. **Control judge from another model family.** `claude-sonnet-5-5` replaces `gemini-3.6-flash`, because R3.2 asked to verify at least part of the results with an independent LLM family; a second Gemini model cannot do that.
2. **Agreement statistics extended.** A test of the Claude judge on three pilot runs showed scores about one point lower than those of the Gemini judge. ICC(A,1) alone would mix such an offset with disagreement about the ranking, so the mean difference, Spearman ρ and the comparison of condition effects under both judges were added.
3. **Judge robustness.** Up to three attempts per judge task (previously two), and the ATAM task states the number of scenarios, because the Claude judge occasionally returned an incomplete scenario list. Both changes apply to all judges.
4. **Decomposition of the team effect.** Three exploratory contrasts between conditions (C6 vs. C5, C6 vs. C9, C7 vs. C1) were added while the generation was running and before any outcome was computed, because the ablation conditions change team size and, for C1, the opening speaker as well as the roles.

