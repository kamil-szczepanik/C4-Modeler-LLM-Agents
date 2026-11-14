"""Figures of the Results section of the article.

  .venv/bin/python scripts/figures.py results/v2/runs.csv --out results/v2/analysis

fig_forest.pdf       effects of the ten conditions on each primary outcome (ISO mean, C4-SC) with 95% bootstrap
                     CIs; filled markers: significant after the Holm correction (confirmatory_primary.csv)
fig_example_l2.svg   Container diagram of one baseline run, rendered with PlantUML (needs Java and plantuml.jar;
                     skipped otherwise) without the title and legend lines of the generated source
fig_effects.pdf      effects of the ten conditions on both primary outcomes (C4-SC, ISO mean) in one plane,
                     with 95% bootstrap CIs (from confirmatory_primary.csv of analyze.py) and the relative
                     model size as marker area
fig_iso_profile.pdf  effects on the eight ISO/IEC 25010 characteristics and the ISO mean (heatmap), with the
                     baseline means on top; bold values: 95% bootstrap CI excludes 0 (the post-hoc
                     computation of scripts/posthoc.py, section 6); outlined cells: role-specific hypotheses
Run scripts/analyze.py first. Requires matplotlib.
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))
sys.path.insert(0, str(REPO / "scripts"))

from analyze import load_plan, load_rows  # noqa: E402
from masc4.judge import ISO_CHARACTERISTICS  # noqa: E402
from masc4.stats import bootstrap_ci, strat_effect, strata, to_float  # noqa: E402

LABELS = {"C1_no_product_owner": "C1 No Product Owner", "C2_no_architect": "C2 No Architect",
          "C3_no_devops": "C3 No DevOps", "C4_no_security": "C4 No Security",
          "C5_single_architect": "C5 Single Architect", "C6_four_architects": "C6 Four Architects",
          "C7_architect_first": "C7 Architect First", "C8_security_first": "C8 Security First",
          "C9_generic_team": "C9 Generic Team", "C10_glossary_memory": "C10 Glossary Memory"}
CHAR_LABELS = {"functional_suitability": "Functional suitability", "performance_efficiency": "Performance efficiency",
               "compatibility": "Compatibility", "usability": "Usability", "reliability": "Reliability",
               "security": "Security", "maintainability": "Maintainability", "portability": "Portability"}
INK, INK2, MUTED, GRID, AXIS, NEUTRAL = "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7", "#f0efec"
SERIES = "#2a78d6"
# diverging scale: red arm (lower than the baseline) - neutral gray - blue arm (higher), equal steps per arm
DIVERGING = ["#7d1a1c", "#b42b2b", "#e34948", "#ee8b86", "#f8cfcc", NEUTRAL,
             "#cde2fb", "#86b6ef", "#3987e5", "#1c5cab", "#0d366b"]
WIDTH_IN = 31 / 6  # text width of the journal template (31 pc)

plt.rcParams.update({"font.family": ["Arial", "DejaVu Sans"], "font.size": 8, "axes.titlesize": 8,
                     "axes.labelsize": 8, "xtick.labelsize": 7.5, "ytick.labelsize": 7.5, "pdf.fonttype": 42,
                     "axes.edgecolor": AXIS, "axes.linewidth": 0.6, "xtick.color": INK2, "ytick.color": INK2,
                     "xtick.major.width": 0.6, "ytick.major.width": 0.6, "axes.labelcolor": INK})


def minus(x: float, nd: int = 2) -> str:
    s = f"{x:.{nd}f}"
    if float(s) == 0:
        s = s.lstrip("-")
    return s.replace("-", "−")


def fig_forest(plan, analysis: Path, out: Path) -> None:
    judge = plan["judge"]
    prim = {(r["metric"], r["condition"]): r for r in csv.DictReader(open(analysis / "confirmatory_primary.csv"))}
    conds = list(LABELS)
    gaps = {"C7_architect_first": 0.5, "C9_generic_team": 0.5, "C10_glossary_memory": 0.5}  # study boundaries
    ys, y = [], 0.0
    for c in conds:
        y += gaps.get(c, 0.0)
        ys.append(y)
        y += 1.0
    panels = [(f"{judge}__iso_mean", "ISO mean (judged quality)", 0.25, (-0.95, 0.3)),
              ("c4_sc", "C4-SC (structural consistency)", 0.10, (-0.15, 0.5))]
    fig, axes = plt.subplots(1, 2, figsize=(WIDTH_IN, 3.2), sharey=True, gridspec_kw={"width_ratios": [1.25, 1.0]})
    for ax, (metric, title, sesoi, xlim) in zip(axes, panels):
        ax.axvspan(-sesoi, sesoi, color=NEUTRAL, zorder=0, lw=0)
        ax.axvline(0, color=AXIS, lw=0.7, zorder=1)
        ax.grid(True, axis="x", color=GRID, lw=0.4, zorder=0)
        for c, yy in zip(conds, ys):
            r = prim[(metric, c)]
            e, lo, hi = float(r["effect"]), float(r["ci_low"]), float(r["ci_high"])
            ax.plot([lo, hi], [yy, yy], color=SERIES, lw=1.2, solid_capstyle="round", zorder=2)
            filled = r["significant"] == "yes"
            ax.scatter([e], [yy], s=30, color=SERIES if filled else "white", edgecolor=SERIES, linewidth=1.1, zorder=3)
        ax.set_xlim(*xlim)
        ax.set_title(title, fontsize=8, color=INK, pad=4)
        ax.set_xlabel("Difference from C0", fontsize=7.5)
        for s in ("top", "right", "left"):
            ax.spines[s].set_visible(False)
        ax.tick_params(axis="y", length=0)
    axes[0].set_yticks(ys)
    axes[0].set_yticklabels([LABELS[c] for c in conds], fontsize=7.5, color=INK)
    axes[0].set_ylim(ys[-1] + 0.7, -0.7)
    handles = [plt.Line2D([], [], marker="o", ls="", color=SERIES, markersize=5, label="significant (Holm)"),
               plt.Line2D([], [], marker="o", ls="", markerfacecolor="white", markeredgecolor=SERIES, markersize=5,
                          label="not significant"),
               Rectangle((0, 0), 1, 1, color=NEUTRAL, label="smallest effects of practical interest")]
    fig.legend(handles=handles, loc="lower center", ncol=3, frameon=False, fontsize=7, bbox_to_anchor=(0.6, 0.0),
               handletextpad=0.4, columnspacing=1.2)
    fig.subplots_adjust(left=0.235, right=0.985, top=0.92, bottom=0.25, wspace=0.08)
    fig.savefig(out / "fig_forest.pdf")
    fig.savefig(out / "fig_forest.png", dpi=200)
    plt.close(fig)


def fig_example(results: Path, out: Path, run: str = "C0_baseline/claims-system-modernization/rep01") -> None:
    """Container diagram of one run as SVG, rendered offline with the C4 library bundled with PlantUML."""
    import re
    import subprocess
    from masc4.structural import C4_INCLUDE, find_java
    jar = REPO / "plantuml.jar"
    if not jar.exists():
        print("plantuml.jar not found: example diagram skipped")
        return
    src = (results / run / "2_container_diagram.puml").read_text(encoding="utf-8")
    src = C4_INCLUDE.sub(r"!include <C4/\1>", src)
    src = re.sub(r"(?m)^\s*(title .*|LAYOUT_WITH_LEGEND\(\)|SHOW_LEGEND\(\))\s*\n", "", src)  # caption carries the title
    src = src.replace("@startuml", "@startuml\n!pragma layout smetana", 1)  # layout engine built into PlantUML
    svg = subprocess.run([find_java(), "-Djava.awt.headless=true", "-jar", str(jar), "-tsvg", "-pipe"],
                         input=src.encode("utf-8"), capture_output=True, check=True).stdout
    (out / "fig_example_l2.svg").write_bytes(svg)


def fig_effects(rows, plan, analysis: Path, out: Path) -> None:
    ref, judge = plan["reference"], plan["judge"]
    prim = {(r["metric"], r["condition"]): r for r in csv.DictReader(open(analysis / "confirmatory_primary.csv"))}
    size = lambda c: np.mean([to_float(r["total_elements"]) for r in rows if r["condition"] == c])  # noqa: E731
    base = size(ref)
    fig, ax = plt.subplots(figsize=(WIDTH_IN, 3.9))
    ax.add_patch(Rectangle((-0.10, -0.25), 0.20, 0.50, facecolor=NEUTRAL, edgecolor="none", zorder=0))
    ax.text(-0.095, -0.24, "smallest effects of\npractical interest", fontsize=6.5, color=MUTED, va="bottom", ha="left")
    ax.axhline(0, color=AXIS, lw=0.6, zorder=1)
    ax.axvline(0, color=AXIS, lw=0.6, zorder=1)
    ax.grid(True, color=GRID, lw=0.4, zorder=0)
    offsets = {"C1_no_product_owner": (6, -9), "C2_no_architect": (8, -3), "C3_no_devops": (-6, -10),
               "C4_no_security": (7, 4), "C5_single_architect": (8, 4), "C6_four_architects": (8, 3),
               "C7_architect_first": (8, 3), "C8_security_first": (-8, -10), "C9_generic_team": (8, -3),
               "C10_glossary_memory": (8, 3)}
    for c, label in LABELS.items():
        x, y = prim[("c4_sc", c)], prim[(f"{judge}__iso_mean", c)]
        ex, ey = float(x["effect"]), float(y["effect"])
        ax.plot([float(x["ci_low"]), float(x["ci_high"])], [ey, ey], color=SERIES, lw=0.9, alpha=0.55, zorder=2,
                solid_capstyle="round")
        ax.plot([ex, ex], [float(y["ci_low"]), float(y["ci_high"])], color=SERIES, lw=0.9, alpha=0.55, zorder=2,
                solid_capstyle="round")
        ax.scatter([ex], [ey], s=70 * (size(c) / base) ** 2, color=SERIES, edgecolor="white", linewidth=0.8, zorder=3)
        dx, dy = offsets[c]
        ax.annotate(label, (ex, ey), xytext=(dx, dy), textcoords="offset points", fontsize=7.5, color=INK,
                    ha="left" if dx > 0 else "right", va="center", zorder=4)
    ax.scatter([0], [0], marker="+", s=60, color=INK, linewidth=1.0, zorder=4)
    ax.annotate("C0 Baseline", (0, 0), xytext=(-5, 6), textcoords="offset points", fontsize=7.5, color=INK, ha="right")
    ax.text(0.475, -0.93, "more consistent,\njudged lower", fontsize=7.5, color=MUTED, style="italic", ha="right", va="bottom")
    ax.text(-0.145, 0.27, "less consistent,\njudged higher", fontsize=7.5, color=MUTED, style="italic", ha="left", va="top")
    # marker-area key: model size relative to the baseline
    for i, k in enumerate((0.75, 1.0, 1.5)):
        xk = 0.315 + i * 0.055
        ax.scatter([xk], [0.215], s=70 * k ** 2, color=SERIES, edgecolor="white", linewidth=0.8, zorder=3)
        ax.text(xk, 0.165, f"{k:g}×", fontsize=6.5, color=INK2, ha="center", va="top")
    ax.text(0.37, 0.275, "elements relative to C0", fontsize=6.5, color=INK2, ha="center", va="top")
    ax.set_xlim(-0.15, 0.48)
    ax.set_ylim(-0.95, 0.29)
    ax.set_xlabel("Difference from C0 in C4-SC (structural consistency, scale 0–5)")
    ax.set_ylabel("Difference from C0 in ISO mean\n(judged quality, scale 1–5)")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.tight_layout(pad=0.3)
    fig.savefig(out / "fig_effects.pdf")
    fig.savefig(out / "fig_effects.png", dpi=200)
    plt.close(fig)


def fig_iso_profile(rows, plan, out: Path, n_boot: int) -> None:
    ref, judge, seed = plan["reference"], plan["judge"], plan["seed"]
    metrics = [f"{judge}__iso_{c}" for c in ISO_CHARACTERISTICS] + [f"{judge}__iso_mean"]
    conds = list(LABELS)
    eff, sig = np.zeros((len(conds), len(metrics))), np.zeros((len(conds), len(metrics)), bool)
    for i, c in enumerate(conds):
        for j, m in enumerate(metrics):
            a, b = strata(rows, c, m), strata(rows, ref, m)
            lo, hi = bootstrap_ci(a, b, n_boot, seed)
            eff[i, j], sig[i, j] = strat_effect(a, b), lo > 0 or hi < 0
    means = [np.mean([to_float(r[m]) for r in rows if r["condition"] == ref]) for m in metrics]
    targeted = {(h["condition"], h["metric"]) for h in plan["targeted_hypotheses"]}

    cmap = LinearSegmentedColormap.from_list("diverging", DIVERGING)
    norm = TwoSlopeNorm(vmin=-1.2, vcenter=0.0, vmax=1.2)
    xs = list(range(len(ISO_CHARACTERISTICS))) + [len(ISO_CHARACTERISTICS) + 0.25]  # small gap before the ISO mean
    ys = [i + 0.35 + (0.12 if i >= 6 else 0) + (0.12 if i >= 8 else 0) + (0.12 if i >= 9 else 0) for i in range(len(conds))]
    fig, ax = plt.subplots(figsize=(WIDTH_IN, 4.3))
    for j, x in enumerate(xs):  # baseline means
        ax.add_patch(Rectangle((x - 0.47, -1.0), 0.94, 0.9, facecolor="#f9f9f7", edgecolor=GRID, lw=0.5))
        ax.text(x, -0.55, f"{means[j]:.2f}", ha="center", va="center", fontsize=7.5, color=INK2)
    for i, (c, y) in enumerate(zip(conds, ys)):
        for j, (m, x) in enumerate(zip(metrics, xs)):
            v = eff[i, j]
            ax.add_patch(Rectangle((x - 0.47, y - 0.45), 0.94, 0.9, facecolor=cmap(norm(v)), edgecolor="white", lw=1.0))
            ax.text(x, y, minus(v), ha="center", va="center", fontsize=7.5,
                    color="white" if abs(v) >= 0.55 else INK, fontweight="bold" if sig[i, j] else "normal")
            if (c, m) in targeted:
                ax.add_patch(Rectangle((x - 0.47, y - 0.45), 0.94, 0.9, facecolor="none", edgecolor=INK, lw=1.1, zorder=5))
    ax.set_xlim(-0.55, xs[-1] + 0.55)
    ax.set_ylim(ys[-1] + 0.55, -1.1)
    ax.set_xticks(xs)
    ax.set_xticklabels([CHAR_LABELS[c] for c in ISO_CHARACTERISTICS] + ["ISO mean"], fontsize=7.5, rotation=35,
                       ha="left", rotation_mode="anchor")
    ax.xaxis.tick_top()
    ax.set_yticks([-0.55] + ys)
    ax.set_yticklabels(["C0 Baseline (mean)"] + [LABELS[c] for c in conds], fontsize=7.5)
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    cb = fig.colorbar(sm, ax=ax, orientation="horizontal", fraction=0.045, pad=0.03, aspect=40)
    cb.set_label("Difference from C0 (points on the 1–5 scale)", fontsize=7.5, color=INK)
    cb.ax.tick_params(labelsize=6.5, length=2, width=0.5)
    cb.outline.set_visible(False)
    fig.tight_layout(pad=0.3)
    fig.savefig(out / "fig_iso_profile.pdf")
    fig.savefig(out / "fig_iso_profile.png", dpi=200)
    plt.close(fig)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv")
    ap.add_argument("--plan", default=str(REPO / "configs/analysis_plan.yaml"))
    ap.add_argument("--out", help="output directory (default: <csv dir>/analysis)")
    ap.add_argument("--n-boot", type=int, default=2000, help="bootstrap resamples for the heatmap (as in posthoc.py)")
    args = ap.parse_args()
    plan = load_plan(Path(args.plan))
    rows = [r for r in load_rows(Path(args.csv)) if r["status"] == "completed"]
    out = Path(args.out) if args.out else Path(args.csv).parent / "analysis"
    out.mkdir(parents=True, exist_ok=True)
    fig_forest(plan, out, out)
    fig_example(Path(args.csv).parent, out)
    fig_effects(rows, plan, out, out)
    fig_iso_profile(rows, plan, out, args.n_boot)
    print(f"figures: {out / 'fig_effects.pdf'}, {out / 'fig_iso_profile.pdf'}")


if __name__ == "__main__":
    main()
