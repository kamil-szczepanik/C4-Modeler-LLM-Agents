"""Post-hoc analyses of the v2 experiments (not in configs/analysis_plan.yaml; labelled as post hoc in the article).

  .venv/bin/python scripts/posthoc.py results/v2/runs.csv --out results/v2/analysis

0. Residual standard deviation within condition x brief cells.
1. Consistency across briefs: the effect of each condition on the primary outcomes within every brief, and the
   number of briefs whose effect has the sign of the stratified effect.
2. Manipulation check: hits of security, operations and user-related terms per 1,000 words, in the discussion
   (transcript) and in the final model (the YAML definitions of all levels, i.e. what the judge sees).
3. Sources of structural inconsistency: relationship endpoints that do not resolve along the C4 scope chain, per
   level and kind (defined only in another component diagram; variant of a defined name; undeclared).
4. Generation cost per run (token counts priced with masc4.pricing).
5. Judges on the control sample: distribution of the characteristic scores; brief-bootstrap CI of the Spearman
   correlation between the condition effects under both judges; per-brief differences between the judges' effects
   (t-based CI over briefs); correlations within condition x brief cells.
6. Effects on single ISO characteristics (unadjusted bootstrap CIs).
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))
sys.path.insert(0, str(REPO / "scripts"))

from analyze import fmt, load_plan, load_rows, table, write_csv  # noqa: E402
from masc4.judge import ISO_CHARACTERISTICS  # noqa: E402
from masc4.pipeline import parse_yaml_definition  # noqa: E402
from masc4.pricing import PRICES  # noqa: E402
from masc4.stats import bootstrap_ci, spearman, strat_effect, strata, to_float  # noqa: E402
from masc4.structural import _defined_names, diagrams_of  # noqa: E402

TOPICS = {
    "security": r"secur|authenticat|authori[sz]|oauth|oidc|openid|jwt|mfa|multi-factor|encrypt|tls|mtls|vault|kms|\baudit"
                r"|rbac|abac|\bwaf\b|firewall|secret|\biam\b|least privilege|zero trust|tokeni[sz]",
    "operations": r"deploy|kubernetes|\bk8s\b|helm|terraform|ci/cd|pipeline|monitor|observab|logging|\blogs?\b|metric"
                  r"|prometheus|grafana|alert|backup|replica|failover|redundan|high availability|autoscal"
                  r"|disaster recovery|health ?check|circuit breaker|retry|load balanc",
    "users": r"\busers?\b|portal|\bui\b|user interface|web app|mobile|front-?end|dashboard|notification|accessib"
             r"|self-service|\bux\b|\bspa\b|single page",
}
T975 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262, 10: 2.228}


def f(r, key):
    return to_float(r.get(key))


def norm(name) -> str:
    return re.sub(r"[^a-z0-9]", "", str(name).lower())


def n_words(text: str) -> int:
    return len(re.findall(r"\w+", text))


def residual(rows, metric, key):
    groups = collections.defaultdict(list)
    for r in rows:
        groups[key(r)].append(f(r, metric))
    return np.array([f(r, metric) - np.mean(groups[key(r)]) for r in rows])


def unresolved_endpoints(c4: dict) -> collections.Counter:
    """Count relationship endpoints that do not resolve along the C4 scope chain, by level and kind."""
    diags = [(lvl, parse_yaml_definition(art.get("yaml_definition", ""), lvl)) for lvl, _, art in diagrams_of(c4)]
    ctx = next((d for lvl, d in diags if lvl == "context"), None)
    cont = next((d for lvl, d in diags if lvl == "container"), None)
    l1 = _defined_names(ctx, "context") if ctx else set()
    l2 = _defined_names(cont, "container") if cont else set()
    l3 = set().union(*[_defined_names(d, "component") for lvl, d in diags if lvl == "component" and d])
    known = [n for n in l1 | l2 | l3 if n]
    out = collections.Counter()
    for lvl, d in diags:
        if not d:
            continue
        chain = _defined_names(d, lvl) | (l1 if lvl in ("container", "component") else set()) | (l2 if lvl == "component" else set())
        for rel in d.get("relationships") or []:
            if not isinstance(rel, dict):
                continue
            out[f"relationships_{lvl}"] += 1
            for end in (rel.get("source"), rel.get("destination")):
                if end in chain:
                    continue
                out[f"unresolved_{lvl}"] += 1
                e = norm(end)
                if end in l3:
                    out["kind_other_component_diagram"] += 1
                elif any(e == norm(x) or (len(e) > 3 and (e in norm(x) or norm(x) in e)) for x in known):
                    out["kind_name_variant"] += 1
                else:
                    out["kind_undeclared"] += 1
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv")
    ap.add_argument("--plan", default=str(REPO / "configs/analysis_plan.yaml"))
    ap.add_argument("--out", help="output directory (default: <csv dir>/analysis)")
    ap.add_argument("--n-boot", type=int, default=2000)
    args = ap.parse_args()

    plan = load_plan(Path(args.plan))
    results = Path(args.csv).parent
    rows = [r for r in load_rows(Path(args.csv)) if r["status"] == "completed"]
    out = Path(args.out) if args.out else results / "analysis"
    out.mkdir(parents=True, exist_ok=True)
    ref, judge, control, seed = plan["reference"], plan["judge"], plan["control_judge"], plan["seed"]
    conditions = [c for _, c in plan["comparison_list"]]
    briefs = plan["canonical_briefs"] + plan["complex_briefs"]
    run_dir = lambda r: results / r["condition"] / r["brief"] / f"rep{int(r['rep']):02d}"  # noqa: E731
    report = [f"# Post-hoc analyses\n\nInput: `{args.csv}` ({len(rows)} completed runs). Not part of the analysis plan.\n"]

    # 0. residual SD within condition x brief cells (compare with the pilot SDs of the sample-size calculation)
    sds = []
    for m in plan["primary_metrics"]:
        cells = collections.defaultdict(list)
        for r in rows:
            cells[(r["condition"], r["brief"])].append(f(r, m))
        dof = sum(len(v) - 1 for v in cells.values())
        sds.append({"metric": m, "pooled_within_cell_sd": float(np.sqrt(sum((len(v) - 1) * np.var(v, ddof=1) for v in cells.values()) / dof))})
    report += ["## 0. Pooled standard deviation within condition x brief cells\n",
               table(sds, ["metric", "pooled_within_cell_sd"], ["Metric", "SD"]), ""]

    # 1. consistency across briefs ----------------------------------------------------------------------
    by_brief = []
    for m in plan["primary_metrics"]:
        for c in conditions:
            per = {b: np.mean([f(r, m) for r in rows if r["condition"] == c and r["brief"] == b])
                   - np.mean([f(r, m) for r in rows if r["condition"] == ref and r["brief"] == b]) for b in briefs}
            eff = strat_effect(strata(rows, c, m), strata(rows, ref, m))
            by_brief.append({"metric": m, "condition": c, "effect": eff, **per,
                             "same_sign": str(sum(np.sign(v) == np.sign(eff) for v in per.values()))})
    report += ["## 1. Effects within each brief (condition minus reference)\n",
               table(by_brief, ["metric", "condition", "effect"] + briefs + ["same_sign"],
                     ["Metric", "Condition", "Stratified effect"] + briefs + ["Briefs with the same sign"]), ""]
    write_csv(out / "posthoc_briefs.csv", by_brief)

    # 2-4. per-run measures from the run folders ----------------------------------------------------------
    per_run = {}
    for r in rows:
        d = run_dir(r)
        c4 = json.load(open(d / "c4_model.json", encoding="utf-8"))
        meta = json.load(open(d / "run.json", encoding="utf-8"))
        model_text = "\n".join((art.get("yaml_definition") or "") for _, _, art in diagrams_of(c4)).lower()
        talk = " ".join(json.loads(line)["text"] for line in open(d / "transcript.jsonl", encoding="utf-8")).lower()
        x = {f"{where}_{k}": 1000 * len(re.findall(p, text)) / max(1, n_words(text))
             for where, text in (("discussion", talk), ("model", model_text)) for k, p in TOPICS.items()}
        x.update(unresolved_endpoints(c4))
        p_in, p_out = PRICES[meta["model_requested"]]
        x["cost_usd"] = (meta["tokens"]["input_tokens"] * p_in + meta["tokens"]["output_tokens"] * p_out) / 1e6
        per_run[id(r)] = x

    def cond_mean(c, key):
        return float(np.mean([per_run[id(r)].get(key, 0) for r in rows if r["condition"] == c]))

    topics = [{"condition": c, **{f"{w}_{k}": cond_mean(c, f"{w}_{k}") for w in ("discussion", "model") for k in TOPICS}}
              for c in [ref] + conditions]
    tcols = [f"{w}_{k}" for w in ("discussion", "model") for k in TOPICS]
    report += ["## 2. Manipulation check: topic hits per 1,000 words (means per condition)\n",
               table(topics, ["condition"] + tcols, ["Condition"] + tcols), ""]
    write_csv(out / "posthoc_topics.csv", topics)

    refs = []
    for c in [ref] + conditions:
        unres = cond_mean(c, "unresolved_context") + cond_mean(c, "unresolved_container") + cond_mean(c, "unresolved_component")
        kinds = {k: cond_mean(c, f"kind_{k}") for k in ("other_component_diagram", "name_variant", "undeclared")}
        total_kinds = sum(kinds.values()) or 1.0
        refs.append({"condition": c, "unresolved_per_run": unres, "unresolved_L3_per_run": cond_mean(c, "unresolved_component"),
                     "relationships_L3_per_run": cond_mean(c, "relationships_component"),
                     "unresolved_L3_per_L3_relationship": cond_mean(c, "unresolved_component") / max(1e-9, cond_mean(c, "relationships_component")),
                     **{f"share_{k}": v / total_kinds for k, v in kinds.items()}})
    rcols = list(refs[0])[1:]
    report += ["## 3. Unresolved relationship endpoints (means per run; shares of all unresolved endpoints)\n",
               table(refs, ["condition"] + rcols, ["Condition"] + rcols), ""]
    write_csv(out / "posthoc_references.csv", refs)

    base_cost = cond_mean(ref, "cost_usd")
    cost = [{"condition": c, "cost_usd_per_run": cond_mean(c, "cost_usd"), "relative_to_reference": cond_mean(c, "cost_usd") / base_cost}
            for c in [ref] + conditions]
    report += ["## 4. Generation cost per run (USD, list prices)\n",
               table(cost, ["condition", "cost_usd_per_run", "relative_to_reference"], ["Condition", "USD per run", "Relative to reference"]), ""]
    write_csv(out / "posthoc_cost.csv", cost)

    # 5. judges on the control sample ------------------------------------------------------------------------
    sample = [r for r in rows if f(r, f"{control}__iso_mean") is not None]
    cell = {(r["condition"], r["brief"]): r for r in sample}
    dist = []
    for who in (judge, control):
        scores = np.array([f(r, f"{who}__iso_{c}") for r in sample for c in ISO_CHARACTERISTICS])
        dist.append({"judge": who, **{str(k): float(np.mean(scores == k)) for k in range(1, 6)}})
    report += [f"## 5a. Distribution of characteristic scores on the control sample ({len(sample)} runs)\n",
               table(dist, ["judge", "1", "2", "3", "4", "5"], ["Judge", "1", "2", "3", "4", "5"]), ""]

    def effects(bs, metric, who):
        return [np.mean([f(cell[(c, b)], f"{who}__{metric}") - f(cell[(ref, b)], f"{who}__{metric}") for b in bs]) for c in conditions]
    rng = np.random.default_rng(seed)
    eff_corr = []
    for m in ("iso_mean", "atam_ri", "req_coverage"):
        boots = []
        for _ in range(args.n_boot):
            bs = list(rng.choice(briefs, len(briefs)))
            boots.append(spearman(effects(bs, m, judge), effects(bs, m, control)))
        boots = np.array(boots)
        boots = boots[~np.isnan(boots)]
        eff_corr.append({"metric": m, "spearman": spearman(effects(briefs, m, judge), effects(briefs, m, control)),
                         "ci": f"[{fmt(np.percentile(boots, 2.5), 2)}, {fmt(np.percentile(boots, 97.5), 2)}]"})
    report += ["## 5b. Spearman correlation of the condition effects under both judges (brief-bootstrap 95% CI)\n",
               table(eff_corr, ["metric", "spearman", "ci"], ["Metric", "Spearman ρ", "95% CI"]), ""]

    t = T975.get(len(briefs) - 1, 1.96)
    judge_diff = []
    targets = [("iso_mean", c, "") for c in conditions] + [
        (h["metric"].split("__", 1)[1], h["condition"], h["id"]) for h in plan["targeted_hypotheses"] if h["metric"].startswith(f"{judge}__")]
    for m, c, hid in targets:
        g = np.array([f(cell[(c, b)], f"{judge}__{m}") - f(cell[(ref, b)], f"{judge}__{m}") for b in briefs])
        k = np.array([f(cell[(c, b)], f"{control}__{m}") - f(cell[(ref, b)], f"{control}__{m}") for b in briefs])
        row = {"hypothesis": hid or "–", "metric": m, "condition": c}
        for name, v in (("main", g), ("control", k), ("difference", k - g)):
            half = t * v.std(ddof=1) / np.sqrt(len(v))
            row[f"{name}_effect"] = float(v.mean())
            row[f"{name}_ci"] = f"[{fmt(v.mean() - half, 2)}, {fmt(v.mean() + half, 2)}]"
        judge_diff.append(row)
    report += ["## 5c. Effects under both judges on the control sample, mean over briefs with t-based 95% CI\n",
               table(judge_diff, ["hypothesis", "metric", "condition", "main_effect", "main_ci", "control_effect", "control_ci",
                                  "difference_effect", "difference_ci"],
                     ["Hypothesis", "Metric", "Condition", f"Effect ({judge})", "95% CI", f"Effect ({control})", "95% CI",
                      "Difference (control - main)", "95% CI"]), ""]
    write_csv(out / "posthoc_judges.csv", judge_diff)

    cellkey = lambda r: (r["condition"], r["brief"])  # noqa: E731
    within = []
    for x, y, rs, label in (("total_elements", f"{judge}__iso_mean", rows, "all runs"),
                            ("c4_sc", f"{judge}__iso_mean", rows, "all runs"),
                            ("total_elements", "c4_sc", rows, "all runs"),
                            ("total_elements", f"{control}__iso_mean", sample, "control sample"),
                            ("c4_sc", f"{control}__iso_mean", sample, "control sample")):
        xs, ys = np.array([f(r, x) for r in rs]), np.array([f(r, y) for r in rs])
        within.append({"x": x, "y": y, "runs": label, "rho": spearman(xs, ys),
                       "rho_within_brief": spearman(residual(rs, x, lambda r: r["brief"]), residual(rs, y, lambda r: r["brief"])),
                       "rho_within_cell": spearman(residual(rs, x, cellkey), residual(rs, y, cellkey)) if rs is rows else float("nan")})
    report += ["## 5d. Spearman correlations: raw, within brief, within condition x brief cell\n",
               table(within, ["x", "y", "runs", "rho", "rho_within_brief", "rho_within_cell"],
                     ["x", "y", "Runs", "ρ", "ρ within brief", "ρ within cell"]), ""]

    # 6. single ISO characteristics -------------------------------------------------------------------------------
    chars = [{"condition": f"{ref} (mean)", **{ch: f"{np.mean([f(r, f'{judge}__iso_{ch}') for r in rows if r['condition'] == ref]):.2f}"
                                               for ch in ISO_CHARACTERISTICS}}]
    for c in conditions:
        row = {"condition": c}
        for ch in ISO_CHARACTERISTICS:
            a, b = strata(rows, c, f"{judge}__iso_{ch}"), strata(rows, ref, f"{judge}__iso_{ch}")
            lo, hi = bootstrap_ci(a, b, args.n_boot, seed)
            row[ch] = f"{strat_effect(a, b):+.2f}{'*' if lo > 0 or hi < 0 else ''}"
        chars.append(row)
    report += ["## 6. Effects on single ISO characteristics (* = 95% bootstrap CI excludes 0; unadjusted)\n",
               table(chars, ["condition"] + list(ISO_CHARACTERISTICS), ["Condition"] + list(ISO_CHARACTERISTICS)), ""]
    write_csv(out / "posthoc_iso_characteristics.csv", chars)

    (out / "posthoc.md").write_text("\n".join(report), encoding="utf-8")
    print(f"report: {out / 'posthoc.md'}")


if __name__ == "__main__":
    main()
