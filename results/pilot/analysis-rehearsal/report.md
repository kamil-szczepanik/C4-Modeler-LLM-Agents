# Analysis report

Input: `results/pilot/runs.csv` (19 runs, 19 completed). Reference: C0_baseline. Main judge: gemini-3.8-flash. Permutations: 1000; bootstrap resamples: 1000.

## 1. Runs

| Condition | Runs | Completed | Invalid output | Invalid rate |
|---|---|---|---|---|
| C0_baseline | 9 | 9 | 0 | 0.000 |
| C1_no_product_owner | 1 | 1 | 0 | 0.000 |
| C2_no_architect | 1 | 1 | 0 | 0.000 |
| C3_no_devops | 1 | 1 | 0 | 0.000 |
| C4_no_security | 1 | 1 | 0 | 0.000 |
| C5_single_architect | 1 | 1 | 0 | 0.000 |
| C6_four_architects | 1 | 1 | 0 | 0.000 |
| C7_architect_first | 1 | 1 | 0 | 0.000 |
| C9_security_first | 1 | 1 | 0 | 0.000 |
| C10_generic_team | 1 | 1 | 0 | 0.000 |
| C12_glossary_memory | 1 | 1 | 0 | 0.000 |

## 2. Descriptive statistics (mean ± SD of completed runs)

| Condition | c4_sc | gemini-3.8-flash__iso_mean | c4_sc_strict | compilation | abstraction_adherence | completeness | l1_l2_jaccard | l2_l3_consistency | gemini-3.8-flash__atam_ri | gemini-3.8-flash__req_coverage | total_elements | total_relationships | n_containers | n_turns | discussion_words |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C0_baseline | 4.748 ± 0.148 | 4.528 ± 0.248 | 4.133 ± 0.345 | 0.871 ± 0.079 | 0.968 ± 0.070 | 1.000 ± 0.000 | 0.775 ± 0.297 | 1.000 ± 0.000 | 0.781 ± 0.083 | 0.835 ± 0.105 | 62.889 ± 10.914 | 49.000 ± 10.500 | 8.000 ± 1.323 | 80.000 ± 10.583 | 8072.556 ± 1043.117 |
| C1_no_product_owner | 4.608 | 4.625 | 4.216 | 0.727 | 1.000 | 1.000 | 0.250 | 1.000 | 0.781 | 0.864 | 63.000 | 51.000 | 9.000 | 66.000 | 6928.000 |
| C2_no_architect | 5.000 | 3.250 | 4.143 | 0.875 | 0.875 | 1.000 | 1.000 | 1.000 | 0.625 | 0.636 | 39.000 | 35.000 | 6.000 | 48.000 | 4463.000 |
| C3_no_devops | 4.800 | 4.375 | 4.000 | 0.750 | 1.000 | 1.000 | 0.889 | 1.000 | 0.875 | 0.909 | 77.000 | 75.000 | 10.000 | 72.000 | 7203.000 |
| C4_no_security | 4.697 | 4.375 | 4.545 | 0.800 | 1.000 | 1.000 | 0.833 | 1.000 | 0.750 | 0.864 | 41.000 | 33.000 | 8.000 | 60.000 | 5941.000 |
| C5_single_architect | 4.559 | 4.625 | 2.941 | 1.000 | 1.000 | 1.000 | 0.833 | 1.000 | 0.875 | 1.000 | 71.000 | 68.000 | 11.000 | 26.000 | 2759.000 |
| C6_four_architects | 4.448 | 4.875 | 3.138 | 0.957 | 1.000 | 1.000 | 0.556 | 0.810 | 0.969 | 1.000 | 266.000 | 145.000 | 21.000 | 184.000 | 16621.000 |
| C7_architect_first | 3.529 | 4.625 | 2.794 | 0.625 | 1.000 | 1.000 | 0.125 | 1.000 | 0.875 | 1.000 | 40.000 | 34.000 | 6.000 | 64.000 | 6459.000 |
| C9_security_first | 4.922 | 4.375 | 4.609 | 0.636 | 1.000 | 1.000 | 1.000 | 0.889 | 0.844 | 0.909 | 75.000 | 64.000 | 9.000 | 88.000 | 8484.000 |
| C10_generic_team | 5.000 | 4.375 | 5.000 | 0.900 | 0.900 | 1.000 | 0.667 | 1.000 | 0.875 | 0.818 | 58.000 | 42.000 | 8.000 | 80.000 | 6451.000 |
| C12_glossary_memory | 5.000 | 3.375 | 4.359 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.531 | 0.727 | 45.000 | 39.000 | 6.000 | 64.000 | 5888.000 |

## 3. Confirmatory tests: primary metrics (Holm over comparisons, per metric)

**c4_sc** (negligible = 95% CI within ±0.10)

| Study | Condition | n | Mean | Mean C0_baseline | Effect | 95% CI | Cliff's δ | p | p (Holm) | Significant | Negligible |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ablation | C1_no_product_owner | 1 | 4.608 | 4.748 | -0.174 | [-0.291, -0.058] | -0.78 (large) | 0.594 | 1.000 | no | no |
| ablation | C2_no_architect | 1 | 5.000 | 4.748 | 0.218 | [0.102, 0.334] | 1.00 (large) | 0.415 | 1.000 | no | no |
| ablation | C3_no_devops | 1 | 4.800 | 4.748 | 0.018 | [-0.098, 0.134] | 0.11 (negligible) | 1.000 | 1.000 | no | no |
| ablation | C4_no_security | 1 | 4.697 | 4.748 | -0.085 | [-0.202, 0.031] | -0.56 (large) | 0.801 | 1.000 | no | no |
| ablation | C5_single_architect | 1 | 4.559 | 4.748 | -0.224 | [-0.340, -0.107] | -0.78 (large) | 0.208 | 1.000 | no | no |
| ablation | C6_four_architects | 1 | 4.448 | 4.748 | -0.334 | [-0.450, -0.218] | -0.78 (large) | 0.208 | 1.000 | no | no |
| order | C7_architect_first | 1 | 3.529 | 4.748 | -1.253 | [-1.369, -1.137] | -1.00 (large) | 0.208 | 1.000 | no | no |
| order | C9_security_first | 1 | 4.922 | 4.748 | 0.140 | [0.023, 0.256] | 1.00 (large) | 0.415 | 1.000 | no | no |
| specialization | C10_generic_team | 1 | 5.000 | 4.748 | 0.218 | [0.102, 0.334] | 1.00 (large) | 0.415 | 1.000 | no | no |
| memory | C12_glossary_memory | 1 | 5.000 | 4.748 | 0.218 | [0.102, 0.334] | 1.00 (large) | 0.415 | 1.000 | no | no |

**gemini-3.8-flash__iso_mean** (negligible = 95% CI within ±0.25)

| Study | Condition | n | Mean | Mean C0_baseline | Effect | 95% CI | Cliff's δ | p | p (Holm) | Significant | Negligible |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ablation | C1_no_product_owner | 1 | 4.625 | 4.528 | 0.125 | [-0.188, 0.375] | 0.33 (medium) | 0.801 | 1.000 | no | no |
| ablation | C2_no_architect | 1 | 3.250 | 4.528 | -1.250 | [-1.562, -1.000] | -1.00 (large) | 0.208 | 1.000 | no | no |
| ablation | C3_no_devops | 1 | 4.375 | 4.528 | -0.125 | [-0.438, 0.125] | -0.33 (medium) | 0.801 | 1.000 | no | no |
| ablation | C4_no_security | 1 | 4.375 | 4.528 | -0.125 | [-0.438, 0.125] | -0.33 (medium) | 0.801 | 1.000 | no | no |
| ablation | C5_single_architect | 1 | 4.625 | 4.528 | 0.125 | [-0.188, 0.375] | 0.33 (medium) | 0.801 | 1.000 | no | no |
| ablation | C6_four_architects | 1 | 4.875 | 4.528 | 0.375 | [0.062, 0.625] | 0.78 (large) | 0.801 | 1.000 | no | no |
| order | C7_architect_first | 1 | 4.625 | 4.528 | 0.125 | [-0.188, 0.375] | 0.33 (medium) | 0.801 | 1.000 | no | no |
| order | C9_security_first | 1 | 4.375 | 4.528 | -0.125 | [-0.438, 0.125] | -0.33 (medium) | 0.801 | 1.000 | no | no |
| specialization | C10_generic_team | 1 | 4.375 | 4.528 | -0.125 | [-0.438, 0.125] | -0.33 (medium) | 0.801 | 1.000 | no | no |
| memory | C12_glossary_memory | 1 | 3.375 | 4.528 | -1.125 | [-1.438, -0.875] | -1.00 (large) | 0.208 | 1.000 | no | no |

## 4. Confirmatory tests: role-specific hypotheses (Holm over the list)

| Id | Condition | Metric | Expected | n | Effect | 95% CI | p | p (Holm) | Supported |
|---|---|---|---|---|---|---|---|---|---|
| H1 | C1_no_product_owner | gemini-3.8-flash__req_coverage | lower | 1 | 0.034 | [-0.023, 0.102] | 0.809 | 1.000 | no |
| H2 | C1_no_product_owner | gemini-3.8-flash__iso_usability | lower | 1 | -1.000 | [-1.750, -0.250] | 0.605 | 1.000 | no |
| H3 | C2_no_architect | c4_sc_strict | lower | 1 | -0.037 | [-0.319, 0.255] | 0.801 | 1.000 | no |
| H4 | C2_no_architect | gemini-3.8-flash__iso_maintainability | lower | 1 | -2.500 | [-3.000, -2.000] | 0.208 | 1.000 | no |
| H5 | C3_no_devops | gemini-3.8-flash__iso_reliability | lower | 1 | 0.250 | [-0.500, 1.000] | 1.000 | 1.000 | no |
| H6 | C4_no_security | gemini-3.8-flash__iso_security | lower | 1 | 0.000 | [0.000, 0.000] | 1.000 | 1.000 | no |
| H7 | C5_single_architect | gemini-3.8-flash__req_coverage | lower | 1 | 0.170 | [0.114, 0.239] | 0.404 | 1.000 | no |
| H8 | C6_four_architects | gemini-3.8-flash__iso_usability | lower | 1 | 0.000 | [-0.750, 0.750] | 1.000 | 1.000 | no |
| H9 | C7_architect_first | gemini-3.8-flash__req_coverage | lower | 1 | 0.170 | [0.114, 0.239] | 0.404 | 1.000 | no |
| H10 | C10_generic_team | gemini-3.8-flash__iso_security | lower | 1 | -1.000 | [-1.000, -1.000] | 0.208 | 1.000 | no |
| H11 | C12_glossary_memory | l1_l2_jaccard | higher | 1 | 0.000 | [0.000, 0.000] | 1.000 | 1.000 | no |

## 5. Exploratory comparisons (unadjusted p-values)

| Metric | Condition | n | Effect | 95% CI | p (unadjusted) |
|---|---|---|---|---|---|
| c4_sc_strict | C1_no_product_owner | 1 | 0.036 | [-0.246, 0.328] | 1.000 |
| c4_sc_strict | C2_no_architect | 1 | -0.037 | [-0.319, 0.255] | 0.801 |
| c4_sc_strict | C3_no_devops | 1 | -0.180 | [-0.462, 0.112] | 0.594 |
| c4_sc_strict | C4_no_security | 1 | 0.365 | [0.084, 0.658] | 0.594 |
| c4_sc_strict | C5_single_architect | 1 | -1.239 | [-1.520, -0.947] | 0.208 |
| c4_sc_strict | C6_four_architects | 1 | -1.042 | [-1.324, -0.750] | 0.208 |
| c4_sc_strict | C7_architect_first | 1 | -1.386 | [-1.668, -1.094] | 0.208 |
| c4_sc_strict | C9_security_first | 1 | 0.429 | [0.148, 0.721] | 0.404 |
| c4_sc_strict | C10_generic_team | 1 | 0.820 | [0.538, 1.112] | 0.208 |
| c4_sc_strict | C12_glossary_memory | 1 | 0.179 | [-0.103, 0.471] | 0.594 |
| compilation | C1_no_product_owner | 1 | -0.104 | [-0.172, -0.036] | 0.610 |
| compilation | C2_no_architect | 1 | 0.044 | [-0.024, 0.111] | 1.000 |
| compilation | C3_no_devops | 1 | -0.081 | [-0.149, -0.014] | 0.801 |
| compilation | C4_no_security | 1 | -0.031 | [-0.099, 0.036] | 1.000 |
| compilation | C5_single_architect | 1 | 0.169 | [0.101, 0.236] | 0.415 |
| compilation | C6_four_architects | 1 | 0.125 | [0.058, 0.193] | 0.415 |
| compilation | C7_architect_first | 1 | -0.206 | [-0.274, -0.139] | 0.208 |
| compilation | C9_security_first | 1 | -0.195 | [-0.263, -0.127] | 0.208 |
| compilation | C10_generic_team | 1 | 0.069 | [0.001, 0.136] | 0.610 |
| compilation | C12_glossary_memory | 1 | 0.169 | [0.101, 0.236] | 0.415 |
| abstraction_adherence | C1_no_product_owner | 1 | 0.050 | [0.000, 0.150] | 1.000 |
| abstraction_adherence | C2_no_architect | 1 | -0.075 | [-0.125, 0.025] | 1.000 |
| abstraction_adherence | C3_no_devops | 1 | 0.050 | [0.000, 0.150] | 1.000 |
| abstraction_adherence | C4_no_security | 1 | 0.050 | [0.000, 0.150] | 1.000 |
| abstraction_adherence | C5_single_architect | 1 | 0.050 | [0.000, 0.150] | 1.000 |
| abstraction_adherence | C6_four_architects | 1 | 0.050 | [0.000, 0.150] | 1.000 |
| abstraction_adherence | C7_architect_first | 1 | 0.050 | [0.000, 0.150] | 1.000 |
| abstraction_adherence | C9_security_first | 1 | 0.050 | [0.000, 0.150] | 1.000 |
| abstraction_adherence | C10_generic_team | 1 | -0.050 | [-0.100, 0.050] | 1.000 |
| abstraction_adherence | C12_glossary_memory | 1 | 0.050 | [0.000, 0.150] | 1.000 |
| completeness | C1_no_product_owner | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| completeness | C2_no_architect | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| completeness | C3_no_devops | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| completeness | C4_no_security | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| completeness | C5_single_architect | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| completeness | C6_four_architects | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| completeness | C7_architect_first | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| completeness | C9_security_first | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| completeness | C10_generic_team | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| completeness | C12_glossary_memory | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| l1_l2_jaccard | C1_no_product_owner | 1 | -0.750 | [-0.750, -0.750] | 0.208 |
| l1_l2_jaccard | C2_no_architect | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| l1_l2_jaccard | C3_no_devops | 1 | -0.111 | [-0.111, -0.111] | 0.208 |
| l1_l2_jaccard | C4_no_security | 1 | -0.167 | [-0.167, -0.167] | 0.208 |
| l1_l2_jaccard | C5_single_architect | 1 | -0.167 | [-0.167, -0.167] | 0.208 |
| l1_l2_jaccard | C6_four_architects | 1 | -0.444 | [-0.444, -0.444] | 0.208 |
| l1_l2_jaccard | C7_architect_first | 1 | -0.875 | [-0.875, -0.875] | 0.208 |
| l1_l2_jaccard | C9_security_first | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| l1_l2_jaccard | C10_generic_team | 1 | -0.333 | [-0.333, -0.333] | 0.208 |
| l1_l2_jaccard | C12_glossary_memory | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| l2_l3_consistency | C1_no_product_owner | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| l2_l3_consistency | C2_no_architect | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| l2_l3_consistency | C3_no_devops | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| l2_l3_consistency | C4_no_security | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| l2_l3_consistency | C5_single_architect | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| l2_l3_consistency | C6_four_architects | 1 | -0.190 | [-0.190, -0.190] | 0.208 |
| l2_l3_consistency | C7_architect_first | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| l2_l3_consistency | C9_security_first | 1 | -0.111 | [-0.111, -0.111] | 0.208 |
| l2_l3_consistency | C10_generic_team | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| l2_l3_consistency | C12_glossary_memory | 1 | 0.000 | [0.000, 0.000] | 1.000 |
| gemini-3.8-flash__atam_ri | C1_no_product_owner | 1 | 0.000 | [-0.078, 0.109] | 1.000 |
| gemini-3.8-flash__atam_ri | C2_no_architect | 1 | -0.156 | [-0.234, -0.047] | 0.602 |
| gemini-3.8-flash__atam_ri | C3_no_devops | 1 | 0.094 | [0.016, 0.203] | 0.602 |
| gemini-3.8-flash__atam_ri | C4_no_security | 1 | -0.031 | [-0.109, 0.078] | 1.000 |
| gemini-3.8-flash__atam_ri | C5_single_architect | 1 | 0.094 | [0.016, 0.203] | 0.602 |
| gemini-3.8-flash__atam_ri | C6_four_architects | 1 | 0.188 | [0.109, 0.297] | 0.404 |
| gemini-3.8-flash__atam_ri | C7_architect_first | 1 | 0.094 | [0.016, 0.203] | 0.602 |
| gemini-3.8-flash__atam_ri | C9_security_first | 1 | 0.062 | [-0.016, 0.172] | 0.602 |
| gemini-3.8-flash__atam_ri | C10_generic_team | 1 | 0.094 | [0.016, 0.203] | 0.602 |
| gemini-3.8-flash__atam_ri | C12_glossary_memory | 1 | -0.250 | [-0.328, -0.141] | 0.208 |
| gemini-3.8-flash__req_coverage | C1_no_product_owner | 1 | 0.034 | [-0.023, 0.102] | 0.809 |
| gemini-3.8-flash__req_coverage | C2_no_architect | 1 | -0.193 | [-0.250, -0.125] | 0.208 |
| gemini-3.8-flash__req_coverage | C3_no_devops | 1 | 0.080 | [0.023, 0.148] | 0.610 |
| gemini-3.8-flash__req_coverage | C4_no_security | 1 | 0.034 | [-0.023, 0.102] | 0.809 |
| gemini-3.8-flash__req_coverage | C5_single_architect | 1 | 0.170 | [0.114, 0.239] | 0.404 |
| gemini-3.8-flash__req_coverage | C6_four_architects | 1 | 0.170 | [0.114, 0.239] | 0.404 |
| gemini-3.8-flash__req_coverage | C7_architect_first | 1 | 0.170 | [0.114, 0.239] | 0.404 |
| gemini-3.8-flash__req_coverage | C9_security_first | 1 | 0.080 | [0.023, 0.148] | 0.610 |
| gemini-3.8-flash__req_coverage | C10_generic_team | 1 | -0.011 | [-0.068, 0.057] | 1.000 |
| gemini-3.8-flash__req_coverage | C12_glossary_memory | 1 | -0.102 | [-0.159, -0.034] | 0.610 |

## 6. Sensitivity: effects adjusted for model size (brief fixed effects + log elements, HC3)

Not enough runs for this model (needs at least 3 runs per parameter).

## 7. Exploratory: effects on canonical vs. complex briefs

| Briefs | Metric | Condition | Effect | 95% CI |
|---|---|---|---|---|
| canonical | c4_sc | C1_no_product_owner | -0.174 | [-0.291, -0.058] |
| canonical | c4_sc | C2_no_architect | 0.218 | [0.102, 0.334] |
| canonical | c4_sc | C3_no_devops | 0.018 | [-0.098, 0.134] |
| canonical | c4_sc | C4_no_security | -0.085 | [-0.202, 0.031] |
| canonical | c4_sc | C5_single_architect | -0.224 | [-0.340, -0.107] |
| canonical | c4_sc | C6_four_architects | -0.334 | [-0.450, -0.218] |
| canonical | c4_sc | C7_architect_first | -1.253 | [-1.369, -1.137] |
| canonical | c4_sc | C9_security_first | 0.140 | [0.023, 0.256] |
| canonical | c4_sc | C10_generic_team | 0.218 | [0.102, 0.334] |
| canonical | c4_sc | C12_glossary_memory | 0.218 | [0.102, 0.334] |
| canonical | gemini-3.8-flash__iso_mean | C1_no_product_owner | 0.125 | [-0.188, 0.375] |
| canonical | gemini-3.8-flash__iso_mean | C2_no_architect | -1.250 | [-1.562, -1.000] |
| canonical | gemini-3.8-flash__iso_mean | C3_no_devops | -0.125 | [-0.438, 0.125] |
| canonical | gemini-3.8-flash__iso_mean | C4_no_security | -0.125 | [-0.438, 0.125] |
| canonical | gemini-3.8-flash__iso_mean | C5_single_architect | 0.125 | [-0.188, 0.375] |
| canonical | gemini-3.8-flash__iso_mean | C6_four_architects | 0.375 | [0.062, 0.625] |
| canonical | gemini-3.8-flash__iso_mean | C7_architect_first | 0.125 | [-0.188, 0.375] |
| canonical | gemini-3.8-flash__iso_mean | C9_security_first | -0.125 | [-0.438, 0.125] |
| canonical | gemini-3.8-flash__iso_mean | C10_generic_team | -0.125 | [-0.438, 0.125] |
| canonical | gemini-3.8-flash__iso_mean | C12_glossary_memory | -1.125 | [-1.438, -0.875] |
| complex | c4_sc | C1_no_product_owner | – | [–, –] |
| complex | c4_sc | C2_no_architect | – | [–, –] |
| complex | c4_sc | C3_no_devops | – | [–, –] |
| complex | c4_sc | C4_no_security | – | [–, –] |
| complex | c4_sc | C5_single_architect | – | [–, –] |
| complex | c4_sc | C6_four_architects | – | [–, –] |
| complex | c4_sc | C7_architect_first | – | [–, –] |
| complex | c4_sc | C9_security_first | – | [–, –] |
| complex | c4_sc | C10_generic_team | – | [–, –] |
| complex | c4_sc | C12_glossary_memory | – | [–, –] |
| complex | gemini-3.8-flash__iso_mean | C1_no_product_owner | – | [–, –] |
| complex | gemini-3.8-flash__iso_mean | C2_no_architect | – | [–, –] |
| complex | gemini-3.8-flash__iso_mean | C3_no_devops | – | [–, –] |
| complex | gemini-3.8-flash__iso_mean | C4_no_security | – | [–, –] |
| complex | gemini-3.8-flash__iso_mean | C5_single_architect | – | [–, –] |
| complex | gemini-3.8-flash__iso_mean | C6_four_architects | – | [–, –] |
| complex | gemini-3.8-flash__iso_mean | C7_architect_first | – | [–, –] |
| complex | gemini-3.8-flash__iso_mean | C9_security_first | – | [–, –] |
| complex | gemini-3.8-flash__iso_mean | C10_generic_team | – | [–, –] |
| complex | gemini-3.8-flash__iso_mean | C12_glossary_memory | – | [–, –] |

## 8. Judge reliability (ICC(A,1), Krippendorff's α interval, exact agreement)

| Comparison | Metric | n | ICC(A,1) | α | Exact agreement |
|---|---|---|---|---|---|
| test-retest | iso_mean | 0 | – | – | – |
| test-retest | atam_ri | 0 | – | – | – |
| test-retest | req_coverage | 0 | – | – | – |
| test-retest | iso_functional_suitability | 0 | – | – | – |
| test-retest | iso_performance_efficiency | 0 | – | – | – |
| test-retest | iso_compatibility | 0 | – | – | – |
| test-retest | iso_usability | 0 | – | – | – |
| test-retest | iso_reliability | 0 | – | – | – |
| test-retest | iso_security | 0 | – | – | – |
| test-retest | iso_maintainability | 0 | – | – | – |
| test-retest | iso_portability | 0 | – | – | – |
| second judge | iso_mean | 0 | – | – | – |
| second judge | atam_ri | 0 | – | – | – |
| second judge | req_coverage | 0 | – | – | – |
| second judge | iso_functional_suitability | 0 | – | – | – |
| second judge | iso_performance_efficiency | 0 | – | – | – |
| second judge | iso_compatibility | 0 | – | – | – |
| second judge | iso_usability | 0 | – | – | – |
| second judge | iso_reliability | 0 | – | – | – |
| second judge | iso_security | 0 | – | – | – |
| second judge | iso_maintainability | 0 | – | – | – |
| second judge | iso_portability | 0 | – | – | – |

## 9. Convergent validity and size bias (Spearman ρ, bootstrap 95% CI)

| x | y | ρ | 95% CI |
|---|---|---|---|
| c4_sc | gemini-3.8-flash__iso_mean | -0.666 | [-0.882, -0.286] |
| compilation | gemini-3.8-flash__iso_mean | -0.149 | [-0.603, 0.357] |
| total_elements | gemini-3.8-flash__iso_mean | 0.345 | [-0.182, 0.749] |
| total_elements | c4_sc | -0.033 | [-0.547, 0.520] |
| gemini-3.8-flash__req_coverage | gemini-3.8-flash__iso_functional_suitability | 0.692 | [0.370, 0.877] |

## 10. Ceiling: share of runs at the maximum score

| briefs | functional_suitability | performance_efficiency | compatibility | usability | reliability | security | maintainability | portability | c4_sc |
|---|---|---|---|---|---|---|---|---|---|
| all | 0.474 | 0.842 | 0.947 | 0.158 | 0.368 | 0.789 | 0.474 | 0.474 | 0.158 |
| canonical | 0.500 | 0.812 | 0.938 | 0.062 | 0.312 | 0.812 | 0.500 | 0.562 | 0.188 |
| complex | 0.333 | 1.000 | 1.000 | 0.667 | 0.667 | 0.667 | 0.333 | 0.000 | 0.000 |
