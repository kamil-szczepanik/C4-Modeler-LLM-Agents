"""Pre-registered analysis of the v2 experiments (configs/analysis_plan.yaml).

  .venv/bin/python scripts/analyze.py results/v2/runs.csv --out results/v2/analysis

Input: the CSV written by scripts/run_evaluation.py (one row per run, including the
control-judge and retest columns once those evaluations exist). Output: report.md and CSV
tables. Pilot data can be used to rehearse the analysis code; its numbers are not interpreted.
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
from pathlib import Path
from typing import Dict, List

import numpy as np
import yaml

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from masc4.judge import ISO_CHARACTERISTICS  # noqa: E402
from masc4.stats import (bootstrap_ci, cliffs_delta, delta_magnitude, holm, icc_a1,  # noqa: E402
                         krippendorff_alpha_interval, ols_hc3, permutation_p, spearman, spearman_ci, strat_effect,
                         strata, to_float)


def load_plan(path: Path) -> dict:
    plan = yaml.safe_load(path.read_text(encoding="utf-8"))
    judge = plan["judge"]

    def sub(x):
        return x.replace("{judge}", judge) if isinstance(x, str) else x
    plan["primary_metrics"] = [sub(m) for m in plan["primary_metrics"]]
    plan["secondary_metrics"] = [sub(m) for m in plan["secondary_metrics"]]
    for h in plan["targeted_hypotheses"]:
        h["metric"] = sub(h["metric"])
    plan["sesoi"] = {sub(m): v for m, v in (plan.get("sesoi") or {}).items()}
    plan["comparison_list"] = [(study, c) for study, conds in plan["comparisons"].items() for c in conds]
    return plan


def load_rows(path: Path) -> List[dict]:
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    for r in rows:
        strict = to_float(r.get("reference_validity_strict"))
        r["c4_sc_strict"] = "" if strict is None else 5 * strict
    return rows


def fmt(x, nd=3) -> str:
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "–"
    if isinstance(x, (int, np.integer)):
        return str(x)
    return f"{x:.{nd}f}"


def compare(rows, condition, reference, metric, n_perm, n_boot, seed) -> dict:
    a, b = strata(rows, condition, metric), strata(rows, reference, metric)
    flat_a = np.concatenate(list(a.values())) if a else np.array([])
    flat_b = np.concatenate(list(b.values())) if b else np.array([])
    effect = strat_effect(a, b)
    lo, hi = bootstrap_ci(a, b, n_boot, seed)
    delta = cliffs_delta(flat_a, flat_b)
    return {"condition": condition, "metric": metric, "n": len(flat_a), "n_ref": len(flat_b),
            "mean": float(flat_a.mean()) if len(flat_a) else float("nan"),
            "mean_ref": float(flat_b.mean()) if len(flat_b) else float("nan"),
            "effect": effect, "ci_low": lo, "ci_high": hi, "cliffs_delta": delta,
            "magnitude": delta_magnitude(delta), "p": permutation_p(a, b, n_perm, seed)}


def table(rows: List[dict], cols: List[str], headers: List[str]) -> str:
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    for r in rows:
        out.append("| " + " | ".join(r[c] if isinstance(r[c], str) else fmt(r[c]) for c in cols) + " |")
    return "\n".join(out)


def write_csv(path: Path, rows: List[dict]) -> None:
    if not rows:
        return
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def agreement(rows, col_a, col_b, integer_scores: bool, n_boot: int = 2000, seed: int = 0) -> dict:
    """Agreement of two judges on the same runs: absolute (ICC(A,1), alpha), systematic offset (mean
    difference b - a with a bootstrap CI), rank agreement (Spearman) and, for integer scores, exact agreement."""
    pairs = np.array([(to_float(r.get(col_a)), to_float(r.get(col_b))) for r in rows
                      if to_float(r.get(col_a)) is not None and to_float(r.get(col_b)) is not None], float)
    if len(pairs) < 2:
        return {"n": len(pairs), "icc_a1": float("nan"), "alpha": float("nan"), "exact": float("nan"),
                "mean_diff": float("nan"), "diff_ci": "–", "spearman": float("nan")}
    diff = pairs[:, 1] - pairs[:, 0]
    rng = np.random.default_rng(seed)
    boots = [rng.choice(diff, len(diff)).mean() for _ in range(n_boot)]
    lo, hi = np.percentile(boots, [2.5, 97.5])
    return {"n": len(pairs), "icc_a1": icc_a1(pairs), "alpha": krippendorff_alpha_interval(pairs),
            "exact": float(np.mean(np.isclose(pairs[:, 0], pairs[:, 1]))) if integer_scores else float("nan"),
            "mean_diff": float(diff.mean()), "diff_ci": f"[{fmt(lo)}, {fmt(hi)}]",
            "spearman": spearman(pairs[:, 0], pairs[:, 1])}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv")
    ap.add_argument("--plan", default=str(REPO / "configs/analysis_plan.yaml"))
    ap.add_argument("--out", help="output directory (default: <csv dir>/analysis)")
    ap.add_argument("--quick", action="store_true", help="1,000 permutations/resamples (for rehearsals only)")
    args = ap.parse_args()

    plan = load_plan(Path(args.plan))
    all_rows = load_rows(Path(args.csv))
    rows = [r for r in all_rows if r["status"] == "completed"]
    out = Path(args.out) if args.out else Path(args.csv).parent / "analysis"
    out.mkdir(parents=True, exist_ok=True)
    ref, judge, alpha, seed = plan["reference"], plan["judge"], plan["alpha"], plan["seed"]
    n_perm = 1000 if args.quick else plan["n_permutations"]
    n_boot = 1000 if args.quick else plan["n_bootstrap"]
    conditions = [ref] + [c for _, c in plan["comparison_list"]]
    report = [f"# Analysis report\n\nInput: `{args.csv}` ({len(all_rows)} runs, {len(rows)} completed). "
              f"Reference: {ref}. Main judge: {judge}. Permutations: {n_perm}; bootstrap resamples: {n_boot}.\n"]

    # 1. run accounting -------------------------------------------------------------------------
    acc = []
    for c in conditions:
        rs = [r for r in all_rows if r["condition"] == c]
        n_inv = sum(r["status"] == "invalid_output" for r in rs)
        acc.append({"condition": c, "runs": str(len(rs)), "completed": str(sum(r["status"] == "completed" for r in rs)),
                    "invalid_output": str(n_inv), "invalid_rate": n_inv / len(rs) if rs else float("nan")})
    report += ["## 1. Runs\n", table(acc, ["condition", "runs", "completed", "invalid_output", "invalid_rate"],
                                       ["Condition", "Runs", "Completed", "Invalid output", "Invalid rate"]), ""]
    write_csv(out / "runs_accounting.csv", acc)

    # 2. descriptives -----------------------------------------------------------------------------
    metrics = list(dict.fromkeys(plan["primary_metrics"] + plan["secondary_metrics"] + [plan["size_covariate"]]
                                 + plan.get("descriptive_extras", [])))
    desc = []
    for c in conditions:
        d = {"condition": c}
        for m in metrics:
            vals = [to_float(r.get(m)) for r in rows if r["condition"] == c]
            vals = [v for v in vals if v is not None]
            d[m] = f"{np.mean(vals):.3f} ± {np.std(vals, ddof=1):.3f}" if len(vals) > 1 else (fmt(vals[0]) if vals else "–")
        desc.append(d)
    report += ["## 2. Descriptive statistics (mean ± SD of completed runs)\n",
               table(desc, ["condition"] + metrics, ["Condition"] + metrics), ""]
    write_csv(out / "descriptives.csv", desc)

    # 3. confirmatory, primary --------------------------------------------------------------------
    primary = []
    report.append("## 3. Confirmatory tests: primary metrics (Holm over comparisons, per metric)\n")
    for m in plan["primary_metrics"]:
        res = [dict(compare(rows, c, ref, m, n_perm, n_boot, seed), study=s) for s, c in plan["comparison_list"]]
        for r, p_adj in zip(res, holm([r["p"] for r in res])):
            r["p_holm"] = p_adj
            r["significant"] = "yes" if p_adj < alpha else "no"
            r["ci"] = f"[{fmt(r['ci_low'])}, {fmt(r['ci_high'])}]"
            r["delta_txt"] = f"{fmt(r['cliffs_delta'], 2)} ({r['magnitude']})"
            bound = plan["sesoi"].get(m)
            r["negligible"] = ("–" if bound is None or math.isnan(r["ci_low"])
                               else "yes" if -bound < r["ci_low"] and r["ci_high"] < bound else "no")
        primary += res
        report += [f"**{m}** (negligible = 95% CI within ±{fmt(plan['sesoi'].get(m), 2)})\n",
                   table(res, ["study", "condition", "n", "mean", "mean_ref", "effect", "ci", "delta_txt",
                               "p", "p_holm", "significant", "negligible"],
                         ["Study", "Condition", "n", "Mean", f"Mean {ref}", "Effect", "95% CI",
                          "Cliff's δ", "p", "p (Holm)", "Significant", "Negligible"]), ""]
    write_csv(out / "confirmatory_primary.csv", primary)

    # 4. confirmatory, targeted hypotheses --------------------------------------------------------------
    targeted = []
    for h in plan["targeted_hypotheses"]:
        r = compare(rows, h["condition"], ref, h["metric"], n_perm, n_boot, seed)
        r.update(id=h["id"], expected=h["expected"])
        targeted.append(r)
    for r, p_adj in zip(targeted, holm([r["p"] for r in targeted])):
        r["p_holm"] = p_adj
        direction_ok = (r["effect"] < 0) if r["expected"] == "lower" else (r["effect"] > 0)
        r["supported"] = "yes" if (p_adj < alpha and direction_ok) else "no"
        r["ci"] = f"[{fmt(r['ci_low'])}, {fmt(r['ci_high'])}]"
    report += ["## 4. Confirmatory tests: role-specific hypotheses (Holm over the list)\n",
               table(targeted, ["id", "condition", "metric", "expected", "n", "effect", "ci", "p", "p_holm", "supported"],
                     ["Id", "Condition", "Metric", "Expected", "n", "Effect", "95% CI", "p", "p (Holm)", "Supported"]), ""]
    write_csv(out / "confirmatory_targeted.csv", targeted)

    # 5. exploratory ---------------------------------------------------------------------------------
    explo = []
    for m in plan["secondary_metrics"]:
        for s, c in plan["comparison_list"]:
            r = compare(rows, c, ref, m, max(1000, n_perm // 5), max(1000, n_boot // 5), seed)
            r["study"] = s
            r["ci"] = f"[{fmt(r['ci_low'])}, {fmt(r['ci_high'])}]"
            explo.append(r)
    report += ["## 5. Exploratory comparisons (unadjusted p-values)\n",
               table(explo, ["metric", "condition", "n", "effect", "ci", "p"],
                     ["Metric", "Condition", "n", "Effect", "95% CI", "p (unadjusted)"]), ""]
    write_csv(out / "exploratory.csv", explo)

    # 6. sensitivity: adjusted for model size --------------------------------------------------------
    sens = []
    briefs = sorted({r["brief"] for r in rows})
    for m in plan["primary_metrics"]:
        data = [r for r in rows if r["condition"] in conditions and to_float(r.get(m)) is not None
                and to_float(r.get(plan["size_covariate"])) not in (None, 0)]
        n_params = len(conditions) + len(briefs)
        if len(data) < 3 * n_params:     # too few runs for a non-saturated model (e.g. pilot data)
            continue
        cols = [c for _, c in plan["comparison_list"]]
        X = np.array([[1.0] + [float(r["brief"] == b) for b in briefs[1:]] + [float(r["condition"] == c) for c in cols]
                      + [math.log(to_float(r[plan["size_covariate"]]))] for r in data])
        y = np.array([to_float(r[m]) for r in data])
        beta, se = ols_hc3(y, X)
        off = len(briefs)
        for i, c in enumerate(cols):
            b_, s_ = beta[off + i], se[off + i]
            sens.append({"metric": m, "condition": c, "adjusted_effect": b_, "ci": f"[{fmt(b_ - 1.96 * s_)}, {fmt(b_ + 1.96 * s_)}]"})
    report += ["## 6. Sensitivity: effects adjusted for model size (brief fixed effects + log elements, HC3)\n",
               table(sens, ["metric", "condition", "adjusted_effect", "ci"], ["Metric", "Condition", "Adjusted effect", "95% CI"])
               if sens else "Not enough runs for this model (needs at least 3 runs per parameter).", ""]
    write_csv(out / "sensitivity_size.csv", sens)

    # 7. brief type (exploratory) -----------------------------------------------------------------------
    by_type = []
    for kind in ("canonical_briefs", "complex_briefs"):
        subset = [r for r in rows if r["brief"] in plan[kind]]
        for m in plan["primary_metrics"]:
            for s, c in plan["comparison_list"]:
                a, b = strata(subset, c, m), strata(subset, ref, m)
                lo, hi = bootstrap_ci(a, b, max(1000, n_boot // 5), seed)
                by_type.append({"briefs": kind.split("_")[0], "metric": m, "condition": c,
                                "effect": strat_effect(a, b), "ci": f"[{fmt(lo)}, {fmt(hi)}]"})
    report += ["## 7. Exploratory: effects on canonical vs. complex briefs\n",
               table(by_type, ["briefs", "metric", "condition", "effect", "ci"], ["Briefs", "Metric", "Condition", "Effect", "95% CI"]), ""]
    write_csv(out / "brief_type.csv", by_type)

    # 8. measurement quality (RQ3) ------------------------------------------------------------------
    meas = []
    control = plan["control_judge"]
    for label, other in (("test-retest", f"{judge}__{plan['retest_tag']}"), ("control judge", control)):
        for m in ["iso_mean", "atam_ri", "req_coverage"] + [f"iso_{c}" for c in ISO_CHARACTERISTICS]:
            a = agreement(all_rows, f"{judge}__{m}", f"{other}__{m}",
                          integer_scores=m.startswith("iso_") and m != "iso_mean", seed=seed)
            meas.append({"comparison": label, "metric": m, "n": str(a["n"]), "icc_a1": a["icc_a1"],
                         "alpha": a["alpha"], "mean_diff": a["mean_diff"], "diff_ci": a["diff_ci"],
                         "spearman": a["spearman"], "exact_agreement": a["exact"]})
    report += ["## 8. Judge reliability (second judgement minus main judge, same runs)\n",
               "ICC(A,1) and α measure absolute agreement, so a constant offset between judges lowers them; "
               "the mean difference shows that offset and Spearman ρ whether the judges rank the runs alike.\n",
               table(meas, ["comparison", "metric", "n", "icc_a1", "alpha", "mean_diff", "diff_ci", "spearman",
                            "exact_agreement"],
                     ["Comparison", "Metric", "n", "ICC(A,1)", "α", "Mean difference", "95% CI", "Spearman ρ",
                      "Exact agreement"]), ""]
    write_csv(out / "judge_reliability.csv", meas)

    # 8b. do the conclusions depend on the judge? effects of the conditions under both judges, same runs
    sample = [r for r in rows if to_float(r.get(f"{control}__iso_mean")) is not None]
    effects, agree = [], []
    for m in ("iso_mean", "atam_ri", "req_coverage"):
        pairs = []
        for s, c in plan["comparison_list"]:
            e_main = strat_effect(strata(sample, c, f"{judge}__{m}"), strata(sample, ref, f"{judge}__{m}"))
            e_ctrl = strat_effect(strata(sample, c, f"{control}__{m}"), strata(sample, ref, f"{control}__{m}"))
            known = not (np.isnan(e_main) or np.isnan(e_ctrl))
            effects.append({"metric": m, "condition": c, "effect_main_judge": e_main, "effect_control_judge": e_ctrl,
                            "same_direction": ("yes" if np.sign(e_main) == np.sign(e_ctrl) else "no") if known else "–"})
            if known:
                pairs.append((e_main, e_ctrl))
        pairs = np.array(pairs, float).reshape(-1, 2)
        agree.append({"metric": m, "conditions": str(len(pairs)),
                      "same_direction": str(int(np.sum(np.sign(pairs[:, 0]) == np.sign(pairs[:, 1])))),
                      "spearman": spearman(pairs[:, 0], pairs[:, 1]) if len(pairs) else float("nan")})
    report += ["## 8b. Effects of the conditions under both judges (control-judge sample, same runs)\n",
               table(agree, ["metric", "conditions", "same_direction", "spearman"],
                     ["Metric", "Conditions", "Same direction", "Spearman ρ of the effects"]), "",
               table(effects, ["metric", "condition", "effect_main_judge", "effect_control_judge", "same_direction"],
                     ["Metric", "Condition", f"Effect ({judge})", f"Effect ({control})", "Same direction"]), ""]
    write_csv(out / "judge_effect_agreement.csv", effects)

    corr = []
    for x, y in (("c4_sc", f"{judge}__iso_mean"), ("compilation", f"{judge}__iso_mean"),
                 ("total_elements", f"{judge}__iso_mean"), ("total_elements", "c4_sc"),
                 (f"{judge}__req_coverage", f"{judge}__iso_functional_suitability")):
        xs = [to_float(r.get(x)) for r in rows]
        ys = [to_float(r.get(y)) for r in rows]
        xs, ys = np.array([v if v is not None else np.nan for v in xs]), np.array([v if v is not None else np.nan for v in ys])
        lo, hi = spearman_ci(xs, ys, seed=seed)
        corr.append({"x": x, "y": y, "rho": spearman(xs, ys), "ci": f"[{fmt(lo)}, {fmt(hi)}]"})
    report += ["## 9. Convergent validity and size bias (Spearman ρ, bootstrap 95% CI)\n",
               table(corr, ["x", "y", "rho", "ci"], ["x", "y", "ρ", "95% CI"]), ""]
    write_csv(out / "correlations.csv", corr)

    ceiling = []
    for kind in ("all", "canonical_briefs", "complex_briefs"):
        subset = rows if kind == "all" else [r for r in rows if r["brief"] in plan[kind]]
        entry = {"briefs": kind.split("_")[0]}
        for c in ISO_CHARACTERISTICS:
            vals = [to_float(r.get(f"{judge}__iso_{c}")) for r in subset]
            vals = [v for v in vals if v is not None]
            entry[c] = float(np.mean(np.array(vals) == 5)) if vals else float("nan")
        c4 = [to_float(r.get("c4_sc")) for r in subset]
        c4 = [v for v in c4 if v is not None]
        entry["c4_sc"] = float(np.mean(np.isclose(c4, 5))) if c4 else float("nan")
        ceiling.append(entry)
    for who in (judge, control):     # is the ceiling a property of the judge? both judges on the same runs
        entry = {"briefs": f"control sample, {who}"}
        for c in ISO_CHARACTERISTICS:
            vals = [to_float(r.get(f"{who}__iso_{c}")) for r in sample]
            vals = [v for v in vals if v is not None]
            entry[c] = float(np.mean(np.array(vals) == 5)) if vals else float("nan")
        entry["c4_sc"] = "–"
        ceiling.append(entry)
    cols = ["briefs"] + list(ISO_CHARACTERISTICS) + ["c4_sc"]
    report += ["## 10. Ceiling: share of runs at the maximum score\n", table(ceiling, cols, cols), ""]
    write_csv(out / "ceiling.csv", ceiling)

    (out / "report.md").write_text("\n".join(report), encoding="utf-8")
    print(f"report: {out / 'report.md'}")


if __name__ == "__main__":
    main()
