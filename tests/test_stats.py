import numpy as np
import pytest

from masc4.stats import (bootstrap_ci, cliffs_delta, holm, icc_a1, krippendorff_alpha_interval, ols_hc3,
                         permutation_p, spearman, strat_effect, strata)


def synthetic(effect, n=6, briefs=6, sd=0.35, seed=1):
    rng = np.random.default_rng(seed)
    a, b = {}, {}
    for i in range(briefs):
        level = 4.0 + 0.2 * i                       # briefs differ in difficulty
        a[f"b{i}"] = level + effect + rng.normal(0, sd, n)
        b[f"b{i}"] = level + rng.normal(0, sd, 2 * n)
    return a, b


def test_stratified_effect_removes_brief_differences():
    a, b = synthetic(effect=0.0, sd=1e-9)
    assert strat_effect(a, b) == pytest.approx(0.0, abs=1e-6)
    a, b = synthetic(effect=-0.3, sd=1e-9)
    assert strat_effect(a, b) == pytest.approx(-0.3, abs=1e-6)


def test_permutation_test_detects_a_real_effect_and_not_a_null_one():
    a, b = synthetic(effect=-0.4)
    assert permutation_p(a, b, n_perm=2000) < 0.01
    lo, hi = bootstrap_ci(a, b, n_boot=2000)
    assert lo < -0.4 < hi or hi < 0
    a, b = synthetic(effect=0.0, seed=3)
    assert permutation_p(a, b, n_perm=2000) > 0.05


def test_cliffs_delta_and_holm():
    assert cliffs_delta([3, 4, 5], [1, 2]) == 1.0 and cliffs_delta([1], [1]) == 0.0
    assert holm([0.01, 0.04, 0.03]) == pytest.approx([0.03, 0.06, 0.06])
    assert np.isnan(holm([0.01, float("nan")])[1])


def test_agreement_measures():
    same = np.array([[1, 1], [3, 3], [5, 5], [2, 2]], float)
    assert icc_a1(same) == pytest.approx(1.0) and krippendorff_alpha_interval(same) == pytest.approx(1.0)
    noisy = np.array([[1, 5], [5, 1], [2, 4], [4, 2]], float)
    assert icc_a1(noisy) < 0 and krippendorff_alpha_interval(noisy) < 0


def test_spearman_and_ols():
    x = np.arange(10, dtype=float)
    assert spearman(x, x ** 2) == pytest.approx(1.0) and spearman(x, -x) == pytest.approx(-1.0)
    rng = np.random.default_rng(0)
    X = np.column_stack([np.ones(200), rng.normal(size=200)])
    y = 2 + 0.5 * X[:, 1] + rng.normal(0, 0.1, 200)
    beta, se = ols_hc3(y, X)
    assert beta[1] == pytest.approx(0.5, abs=0.05) and se[1] < 0.05


def test_strata_groups_by_brief_and_drops_missing():
    rows = [{"condition": "A", "brief": "x", "m": "1"}, {"condition": "A", "brief": "x", "m": ""},
            {"condition": "A", "brief": "y", "m": "3"}, {"condition": "B", "brief": "x", "m": "9"}]
    s = strata(rows, "A", "m")
    assert sorted(s) == ["x", "y"] and list(s["x"]) == [1.0]
