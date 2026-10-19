"""Statistics for the pre-registered analysis (numpy only).

Comparisons are always "condition vs. reference (C0)" stratified by brief:
the effect is the average over briefs of the within-brief difference in means,
tested with a within-brief permutation test and bracketed by a within-brief
(stratified) bootstrap confidence interval.
"""
from __future__ import annotations

from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np

Strata = Dict[str, np.ndarray]   # brief -> values of one condition (NaN removed)


def strat_effect(a: Strata, b: Strata) -> float:
    """Mean over shared briefs of (mean of a - mean of b) within the brief."""
    briefs = [k for k in a if k in b and len(a[k]) and len(b[k])]
    if not briefs:
        return float("nan")
    return float(np.mean([a[k].mean() - b[k].mean() for k in briefs]))


def permutation_p(a: Strata, b: Strata, n_perm: int = 10_000, seed: int = 0) -> float:
    """Two-sided p-value; labels are permuted within each brief only."""
    briefs = [k for k in a if k in b and len(a[k]) and len(b[k])]
    if not briefs:
        return float("nan")
    observed = abs(strat_effect(a, b))
    rng = np.random.default_rng(seed)
    pooled = {k: np.concatenate([a[k], b[k]]) for k in briefs}
    sizes = {k: len(a[k]) for k in briefs}
    exceed = 0
    for _ in range(n_perm):
        diffs = []
        for k in briefs:
            perm = rng.permutation(pooled[k])
            diffs.append(perm[:sizes[k]].mean() - perm[sizes[k]:].mean())
        exceed += abs(np.mean(diffs)) >= observed - 1e-12
    return (exceed + 1) / (n_perm + 1)


def bootstrap_ci(a: Strata, b: Strata, n_boot: int = 10_000, seed: int = 0, level: float = 0.95) -> Tuple[float, float]:
    """Percentile CI of strat_effect, resampling runs within each brief and condition."""
    briefs = [k for k in a if k in b and len(a[k]) and len(b[k])]
    if not briefs:
        return float("nan"), float("nan")
    rng = np.random.default_rng(seed)
    stats = np.empty(n_boot)
    for i in range(n_boot):
        stats[i] = np.mean([rng.choice(a[k], len(a[k])).mean() - rng.choice(b[k], len(b[k])).mean() for k in briefs])
    lo, hi = np.percentile(stats, [100 * (1 - level) / 2, 100 * (1 + level) / 2])
    return float(lo), float(hi)


def cliffs_delta(x: Sequence[float], y: Sequence[float]) -> float:
    x, y = np.asarray(x, float), np.asarray(y, float)
    if not len(x) or not len(y):
        return float("nan")
    diff = x[:, None] - y[None, :]
    return float((np.sum(diff > 0) - np.sum(diff < 0)) / diff.size)


def delta_magnitude(d: float) -> str:
    if np.isnan(d):
        return "n/a"
    d = abs(d)
    return "negligible" if d < 0.147 else "small" if d < 0.33 else "medium" if d < 0.474 else "large"


def holm(pvalues: Sequence[float]) -> List[float]:
    """Holm-adjusted p-values (NaN entries are left as NaN and not counted)."""
    p = np.asarray(pvalues, float)
    valid = np.where(~np.isnan(p))[0]
    adjusted = np.full(len(p), np.nan)
    order = valid[np.argsort(p[valid])]
    running = 0.0
    for rank, i in enumerate(order):
        running = max(running, (len(valid) - rank) * p[i])
        adjusted[i] = min(1.0, running)
    return adjusted.tolist()


def rankdata(x: np.ndarray) -> np.ndarray:
    order = np.argsort(x, kind="mergesort")
    ranks = np.empty(len(x))
    sorted_x = x[order]
    i = 0
    while i < len(x):
        j = i
        while j + 1 < len(x) and sorted_x[j + 1] == sorted_x[i]:
            j += 1
        ranks[order[i:j + 1]] = (i + j) / 2 + 1
        i = j + 1
    return ranks


def spearman(x: Sequence[float], y: Sequence[float]) -> float:
    x, y = np.asarray(x, float), np.asarray(y, float)
    keep = ~(np.isnan(x) | np.isnan(y))
    if keep.sum() < 3:
        return float("nan")
    rx, ry = rankdata(x[keep]), rankdata(y[keep])
    if rx.std() == 0 or ry.std() == 0:
        return float("nan")
    return float(np.corrcoef(rx, ry)[0, 1])


def spearman_ci(x: Sequence[float], y: Sequence[float], n_boot: int = 5_000, seed: int = 0) -> Tuple[float, float]:
    x, y = np.asarray(x, float), np.asarray(y, float)
    keep = ~(np.isnan(x) | np.isnan(y))
    x, y = x[keep], y[keep]
    if len(x) < 5:
        return float("nan"), float("nan")
    rng = np.random.default_rng(seed)
    vals = []
    for _ in range(n_boot):
        idx = rng.integers(0, len(x), len(x))
        r = spearman(x[idx], y[idx])
        if not np.isnan(r):
            vals.append(r)
    return (float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5))) if vals else (float("nan"),) * 2


def icc_a1(ratings: np.ndarray) -> float:
    """ICC(A,1): two-way model, absolute agreement, single rater (McGraw & Wong 1996).

    `ratings` has one row per rated object and one column per rater (no missing values)."""
    r = np.asarray(ratings, float)
    r = r[~np.isnan(r).any(axis=1)]
    n, k = r.shape
    if n < 2 or k < 2:
        return float("nan")
    grand = r.mean()
    ss_rows = k * ((r.mean(axis=1) - grand) ** 2).sum()
    ss_cols = n * ((r.mean(axis=0) - grand) ** 2).sum()
    ss_err = ((r - grand) ** 2).sum() - ss_rows - ss_cols
    ms_r, ms_c, ms_e = ss_rows / (n - 1), ss_cols / (k - 1), ss_err / ((n - 1) * (k - 1))
    denom = ms_r + (k - 1) * ms_e + k * (ms_c - ms_e) / n
    return float((ms_r - ms_e) / denom) if denom else float("nan")


def krippendorff_alpha_interval(ratings: np.ndarray) -> float:
    """Krippendorff's alpha with the interval metric, complete data (rows = objects, columns = raters)."""
    r = np.asarray(ratings, float)
    r = r[~np.isnan(r).any(axis=1)]
    n, k = r.shape
    if n < 2 or k < 2:
        return float("nan")
    values = r.ravel()
    d_o = np.mean([np.mean((row[:, None] - row[None, :])[~np.eye(k, dtype=bool)] ** 2) for row in r])
    d_e = np.mean((values[:, None] - values[None, :])[~np.eye(len(values), dtype=bool)] ** 2)
    return float(1 - d_o / d_e) if d_e else float("nan")


def ols_hc3(y: np.ndarray, X: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """OLS coefficients and HC3 heteroscedasticity-robust standard errors."""
    XtX_inv = np.linalg.pinv(X.T @ X)
    beta = XtX_inv @ X.T @ y
    resid = y - X @ beta
    h = np.einsum("ij,jk,ik->i", X, XtX_inv, X)
    w = resid ** 2 / np.clip(1 - h, 1e-12, None) ** 2
    cov = XtX_inv @ (X.T * w) @ X @ XtX_inv
    return beta, np.sqrt(np.clip(np.diag(cov), 0, None))


def strata(rows: List[dict], condition: str, metric: str, brief_key: str = "brief") -> Strata:
    """Values of `metric` for `condition`, grouped by brief (missing values dropped)."""
    out: Dict[str, List[float]] = {}
    for r in rows:
        if r["condition"] != condition:
            continue
        v = to_float(r.get(metric))
        if v is not None:
            out.setdefault(r[brief_key], []).append(v)
    return {k: np.asarray(v, float) for k, v in out.items()}


def to_float(value) -> Optional[float]:
    try:
        v = float(value)
    except (TypeError, ValueError):
        return None
    return None if np.isnan(v) else v
