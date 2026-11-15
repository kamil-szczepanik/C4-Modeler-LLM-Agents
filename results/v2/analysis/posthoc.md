# Post-hoc analyses

Input: `results/v2/runs.csv` (432 completed runs). Not part of the analysis plan.

## 0. Pooled standard deviation within condition x brief cells

| Metric | SD |
|---|---|
| c4_sc | 0.265 |
| gemini-3.8-flash__iso_mean | 0.294 |

## 1. Effects within each brief (condition minus reference)

| Metric | Condition | Stratified effect | clinic-management-system | library-management-system | online-bookstore | payment-fraud-screening | claims-system-modernization | cross-border-telehealth | Briefs with the same sign |
|---|---|---|---|---|---|---|---|---|---|
| c4_sc | C1_no_product_owner | 0.091 | -0.007 | 0.079 | 0.310 | -0.281 | 0.415 | 0.030 | 4 |
| c4_sc | C2_no_architect | 0.227 | 0.326 | 0.186 | 0.494 | 0.005 | 0.098 | 0.254 | 6 |
| c4_sc | C3_no_devops | 0.006 | -0.170 | -0.037 | 0.242 | -0.256 | 0.189 | 0.071 | 3 |
| c4_sc | C4_no_security | 0.101 | 0.140 | 0.178 | 0.137 | 0.058 | 0.027 | 0.063 | 6 |
| c4_sc | C5_single_architect | 0.240 | 0.282 | 0.252 | 0.235 | 0.204 | 0.401 | 0.065 | 6 |
| c4_sc | C6_four_architects | 0.059 | -0.010 | -0.006 | 0.130 | -0.191 | 0.388 | 0.040 | 3 |
| c4_sc | C7_architect_first | 0.154 | 0.129 | 0.199 | 0.181 | 0.085 | 0.206 | 0.125 | 6 |
| c4_sc | C8_security_first | 0.141 | 0.216 | 0.169 | 0.345 | -0.007 | -0.111 | 0.233 | 4 |
| c4_sc | C9_generic_team | 0.197 | 0.294 | 0.140 | 0.362 | 0.204 | 0.098 | 0.084 | 6 |
| c4_sc | C10_glossary_memory | 0.360 | 0.344 | 0.260 | 0.364 | 0.301 | 0.529 | 0.359 | 6 |
| gemini-3.8-flash__iso_mean | C1_no_product_owner | -0.062 | -0.010 | -0.073 | -0.344 | 0.031 | -0.052 | 0.073 | 4 |
| gemini-3.8-flash__iso_mean | C2_no_architect | -0.747 | -0.594 | -0.802 | -0.719 | -0.969 | -0.760 | -0.635 | 6 |
| gemini-3.8-flash__iso_mean | C3_no_devops | -0.062 | -0.219 | -0.115 | -0.010 | -0.031 | 0.010 | -0.010 | 5 |
| gemini-3.8-flash__iso_mean | C4_no_security | -0.024 | 0.010 | -0.052 | 0.031 | -0.219 | 0.135 | -0.052 | 3 |
| gemini-3.8-flash__iso_mean | C5_single_architect | -0.160 | 0.010 | -0.260 | -0.323 | -0.281 | 0.073 | -0.177 | 4 |
| gemini-3.8-flash__iso_mean | C6_four_architects | 0.132 | 0.177 | 0.073 | 0.052 | 0.281 | 0.156 | 0.052 | 6 |
| gemini-3.8-flash__iso_mean | C7_architect_first | 0.024 | -0.031 | 0.073 | -0.010 | 0.031 | 0.052 | 0.031 | 4 |
| gemini-3.8-flash__iso_mean | C8_security_first | -0.205 | -0.427 | -0.031 | -0.198 | -0.156 | -0.344 | -0.073 | 6 |
| gemini-3.8-flash__iso_mean | C9_generic_team | -0.431 | -0.698 | -0.156 | -0.135 | -0.573 | -0.469 | -0.552 | 6 |
| gemini-3.8-flash__iso_mean | C10_glossary_memory | -0.285 | -0.385 | -0.031 | -0.177 | -0.219 | -0.260 | -0.635 | 6 |

## 2. Manipulation check: topic hits per 1,000 words (means per condition)

| Condition | discussion_security | discussion_operations | discussion_users | model_security | model_operations | model_users |
|---|---|---|---|---|---|---|
| C0_baseline | 30.790 | 17.333 | 9.139 | 39.538 | 11.283 | 14.707 |
| C1_no_product_owner | 38.266 | 21.136 | 4.459 | 42.762 | 10.101 | 9.993 |
| C2_no_architect | 32.081 | 19.148 | 10.346 | 50.260 | 14.081 | 17.771 |
| C3_no_devops | 37.020 | 8.680 | 10.574 | 38.602 | 9.532 | 14.886 |
| C4_no_security | 13.296 | 20.684 | 10.749 | 27.167 | 13.761 | 16.774 |
| C5_single_architect | 21.560 | 7.521 | 8.272 | 25.713 | 7.277 | 13.305 |
| C6_four_architects | 21.882 | 11.491 | 5.764 | 30.335 | 13.856 | 10.392 |
| C7_architect_first | 32.244 | 17.498 | 9.308 | 36.537 | 10.436 | 15.294 |
| C8_security_first | 32.133 | 18.606 | 8.671 | 36.970 | 9.146 | 12.335 |
| C9_generic_team | 10.024 | 18.337 | 3.596 | 26.237 | 15.312 | 10.078 |
| C10_glossary_memory | 31.951 | 17.349 | 10.641 | 38.553 | 9.353 | 18.740 |

## 3. Unresolved relationship endpoints (means per run; shares of all unresolved endpoints)

| Condition | unresolved_per_run | unresolved_L3_per_run | relationships_L3_per_run | unresolved_L3_per_L3_relationship | share_other_component_diagram | share_name_variant | share_undeclared |
|---|---|---|---|---|---|---|---|
| C0_baseline | 4.375 | 4.125 | 30.236 | 0.136 | 0.092 | 0.337 | 0.571 |
| C1_no_product_owner | 3.556 | 3.444 | 31.806 | 0.108 | 0.062 | 0.352 | 0.586 |
| C2_no_architect | 1.278 | 1.194 | 16.278 | 0.073 | 0.109 | 0.174 | 0.717 |
| C3_no_devops | 4.000 | 3.750 | 29.861 | 0.126 | 0.035 | 0.319 | 0.646 |
| C4_no_security | 3.389 | 3.361 | 31.833 | 0.106 | 0.016 | 0.270 | 0.713 |
| C5_single_architect | 1.861 | 1.722 | 30.250 | 0.057 | 0.045 | 0.433 | 0.522 |
| C6_four_architects | 6.611 | 6.028 | 60.806 | 0.099 | 0.071 | 0.408 | 0.521 |
| C7_architect_first | 3.139 | 2.361 | 31.917 | 0.074 | 0.062 | 0.186 | 0.752 |
| C8_security_first | 2.500 | 2.306 | 26.111 | 0.088 | 0.089 | 0.244 | 0.667 |
| C9_generic_team | 1.889 | 1.750 | 22.528 | 0.078 | 0.015 | 0.382 | 0.603 |
| C10_glossary_memory | 0.722 | 0.500 | 25.222 | 0.020 | 0.000 | 0.077 | 0.923 |

## 4. Generation cost per run (USD, list prices)

| Condition | USD per run | Relative to reference |
|---|---|---|
| C0_baseline | 0.121 | 1.000 |
| C1_no_product_owner | 0.100 | 0.824 |
| C2_no_architect | 0.077 | 0.633 |
| C3_no_devops | 0.099 | 0.816 |
| C4_no_security | 0.103 | 0.850 |
| C5_single_architect | 0.057 | 0.470 |
| C6_four_architects | 0.156 | 1.295 |
| C7_architect_first | 0.119 | 0.983 |
| C8_security_first | 0.114 | 0.943 |
| C9_generic_team | 0.117 | 0.970 |
| C10_glossary_memory | 0.138 | 1.143 |

## 5a. Distribution of characteristic scores on the control sample (66 runs)

| Judge | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| gemini-3.8-flash | 0.000 | 0.008 | 0.104 | 0.326 | 0.562 |
| claude-sonnet-5-5 | 0.000 | 0.104 | 0.523 | 0.330 | 0.044 |

## 5b. Spearman correlation of the condition effects under both judges (brief-bootstrap 95% CI)

| Metric | Spearman ρ | 95% CI |
|---|---|---|
| iso_mean | 0.840 | [0.29, 0.91] |
| atam_ri | 0.824 | [0.27, 0.95] |
| req_coverage | 0.758 | [0.12, 0.90] |

## 5c. Effects under both judges on the control sample, mean over briefs with t-based 95% CI

| Hypothesis | Metric | Condition | Effect (gemini-3.8-flash) | 95% CI | Effect (claude-sonnet-5-5) | 95% CI | Difference (control - main) | 95% CI |
|---|---|---|---|---|---|---|---|---|
| – | iso_mean | C1_no_product_owner | 0.000 | [-0.74, 0.74] | 0.146 | [-0.24, 0.53] | 0.146 | [-0.64, 0.93] |
| – | iso_mean | C2_no_architect | -0.604 | [-1.03, -0.18] | -0.250 | [-0.72, 0.22] | 0.354 | [-0.20, 0.91] |
| – | iso_mean | C3_no_devops | -0.104 | [-0.38, 0.18] | 0.146 | [-0.22, 0.51] | 0.250 | [-0.25, 0.75] |
| – | iso_mean | C4_no_security | 0.083 | [-0.15, 0.31] | 0.167 | [-0.03, 0.36] | 0.083 | [-0.26, 0.42] |
| – | iso_mean | C5_single_architect | -0.125 | [-0.50, 0.25] | -0.125 | [-0.29, 0.04] | 0.000 | [-0.33, 0.33] |
| – | iso_mean | C6_four_architects | 0.292 | [0.09, 0.49] | 0.167 | [-0.14, 0.47] | -0.125 | [-0.55, 0.30] |
| – | iso_mean | C7_architect_first | 0.062 | [-0.32, 0.44] | 0.250 | [-0.03, 0.53] | 0.188 | [-0.40, 0.77] |
| – | iso_mean | C8_security_first | 0.083 | [-0.20, 0.37] | 0.188 | [-0.24, 0.62] | 0.104 | [-0.58, 0.79] |
| – | iso_mean | C9_generic_team | -0.312 | [-0.79, 0.16] | 0.000 | [-0.38, 0.38] | 0.312 | [-0.05, 0.67] |
| – | iso_mean | C10_glossary_memory | 0.000 | [-0.28, 0.28] | 0.000 | [-0.32, 0.32] | 0.000 | [-0.45, 0.45] |
| H1 | req_coverage | C1_no_product_owner | 0.109 | [-0.08, 0.30] | 0.035 | [-0.11, 0.18] | -0.074 | [-0.22, 0.07] |
| H2 | iso_usability | C1_no_product_owner | -0.333 | [-1.60, 0.94] | 0.000 | [0.00, 0.00] | 0.333 | [-0.94, 1.60] |
| H4 | iso_maintainability | C2_no_architect | -1.000 | [-1.94, -0.06] | 0.000 | [-0.66, 0.66] | 1.000 | [0.06, 1.94] |
| H5 | iso_reliability | C3_no_devops | 0.333 | [-0.52, 1.19] | 0.667 | [-0.42, 1.75] | 0.333 | [-0.21, 0.88] |
| H6 | iso_security | C4_no_security | -0.167 | [-0.60, 0.26] | -0.167 | [-0.60, 0.26] | 0.000 | [0.00, 0.00] |
| H7 | req_coverage | C5_single_architect | 0.102 | [-0.06, 0.26] | 0.042 | [-0.07, 0.16] | -0.059 | [-0.22, 0.10] |
| H8 | iso_usability | C6_four_architects | 0.167 | [-0.62, 0.96] | 0.167 | [-0.26, 0.60] | 0.000 | [-0.94, 0.94] |
| H9 | req_coverage | C7_architect_first | 0.051 | [-0.10, 0.20] | 0.044 | [-0.06, 0.14] | -0.006 | [-0.11, 0.09] |
| H10 | iso_security | C9_generic_team | -0.333 | [-1.19, 0.52] | -0.500 | [-1.07, 0.07] | -0.167 | [-0.96, 0.62] |

## 5d. Spearman correlations: raw, within brief, within condition x brief cell

| x | y | Runs | ρ | ρ within brief | ρ within cell |
|---|---|---|---|---|---|
| total_elements | gemini-3.8-flash__iso_mean | all runs | 0.458 | 0.520 | 0.328 |
| c4_sc | gemini-3.8-flash__iso_mean | all runs | -0.114 | -0.158 | -0.005 |
| total_elements | c4_sc | all runs | -0.121 | -0.154 | 0.069 |
| total_elements | claude-sonnet-5-5__iso_mean | control sample | 0.586 | 0.512 | – |
| c4_sc | claude-sonnet-5-5__iso_mean | control sample | -0.284 | -0.295 | – |

## 6. Effects on single ISO characteristics (* = 95% bootstrap CI excludes 0; unadjusted)

| Condition | functional_suitability | performance_efficiency | compatibility | usability | reliability | security | maintainability | portability |
|---|---|---|---|---|---|---|---|---|
| C0_baseline (mean) | 4.67 | 4.75 | 4.90 | 4.35 | 4.39 | 4.94 | 4.75 | 4.14 |
| C1_no_product_owner | -0.00 | -0.03 | -0.10 | -0.40* | +0.08 | -0.03 | -0.00 | -0.03 |
| C2_no_architect | -1.11* | -0.94* | -0.62* | -0.71* | -0.92* | -0.39* | -0.94* | -0.33* |
| C3_no_devops | +0.03 | +0.06 | -0.07 | -0.01 | -0.08 | -0.03 | -0.19* | -0.19* |
| C4_no_security | +0.06 | +0.08 | -0.01 | +0.07 | -0.08 | -0.08 | -0.08 | -0.14 |
| C5_single_architect | +0.14 | -0.17 | -0.12 | -0.38* | -0.33* | -0.14* | -0.08 | -0.19* |
| C6_four_architects | +0.28* | +0.22* | -0.01 | +0.07 | +0.42* | -0.00 | -0.00 | +0.08 |
| C7_architect_first | +0.17 | -0.03 | -0.07 | +0.04 | +0.19 | -0.03 | +0.03 | -0.11 |
| C8_security_first | -0.14 | -0.14 | -0.10 | -0.60* | -0.03 | -0.22* | -0.08 | -0.33* |
| C9_generic_team | -0.58* | -0.19 | -0.37* | -0.90* | -0.33* | -0.39* | -0.31* | -0.36* |
| C10_glossary_memory | -0.42* | -0.36* | -0.18* | -0.10 | -0.36* | -0.39* | -0.17 | -0.31* |
