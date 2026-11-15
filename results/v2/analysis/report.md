# Analysis report

Input: `results/v2/runs.csv` (432 runs, 432 completed). Reference: C0_baseline. Main judge: gemini-3.8-flash. Permutations: 10000; bootstrap resamples: 10000.

## 1. Runs

| Condition | Runs | Completed | Invalid output | Invalid rate |
|---|---|---|---|---|
| C0_baseline | 72 | 72 | 0 | 0.000 |
| C1_no_product_owner | 36 | 36 | 0 | 0.000 |
| C2_no_architect | 36 | 36 | 0 | 0.000 |
| C3_no_devops | 36 | 36 | 0 | 0.000 |
| C4_no_security | 36 | 36 | 0 | 0.000 |
| C5_single_architect | 36 | 36 | 0 | 0.000 |
| C6_four_architects | 36 | 36 | 0 | 0.000 |
| C7_architect_first | 36 | 36 | 0 | 0.000 |
| C8_security_first | 36 | 36 | 0 | 0.000 |
| C9_generic_team | 36 | 36 | 0 | 0.000 |
| C10_glossary_memory | 36 | 36 | 0 | 0.000 |

## 2. Descriptive statistics (mean ± SD of completed runs)

| Condition | c4_sc | gemini-3.8-flash__iso_mean | c4_sc_strict | compilation | abstraction_adherence | completeness | l1_l2_jaccard | l2_l3_consistency | gemini-3.8-flash__atam_ri | gemini-3.8-flash__req_coverage | total_elements | total_relationships | n_containers | n_turns | discussion_words |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C0_baseline | 4.568 ± 0.303 | 4.611 ± 0.258 | 3.782 ± 0.500 | 0.848 ± 0.119 | 0.976 ± 0.043 | 1.000 ± 0.000 | 0.621 ± 0.318 | 0.986 ± 0.051 | 0.807 ± 0.071 | 0.872 ± 0.101 | 58.292 ± 15.871 | 49.625 ± 13.739 | 7.639 ± 1.856 | 77.111 ± 14.849 | 9861.208 ± 1833.599 |
| C1_no_product_owner | 4.659 ± 0.313 | 4.549 ± 0.332 | 3.952 ± 0.434 | 0.859 ± 0.102 | 0.979 ± 0.040 | 1.000 ± 0.000 | 0.775 ± 0.304 | 0.975 ± 0.051 | 0.793 ± 0.078 | 0.843 ± 0.103 | 58.444 ± 13.966 | 49.139 ± 10.720 | 7.750 ± 1.500 | 58.500 ± 9.000 | 7483.889 ± 1085.128 |
| C2_no_architect | 4.795 ± 0.306 | 3.865 ± 0.494 | 4.457 ± 0.506 | 0.804 ± 0.138 | 0.963 ± 0.062 | 1.000 ± 0.000 | 0.674 ± 0.287 | 0.997 ± 0.019 | 0.600 ± 0.141 | 0.738 ± 0.153 | 40.083 ± 11.589 | 31.611 ± 10.330 | 6.083 ± 1.918 | 48.500 ± 11.508 | 6194.111 ± 1421.562 |
| C3_no_devops | 4.574 ± 0.309 | 4.549 ± 0.281 | 3.684 ± 0.505 | 0.869 ± 0.100 | 0.987 ± 0.038 | 1.000 ± 0.000 | 0.609 ± 0.351 | 0.986 ± 0.039 | 0.815 ± 0.068 | 0.858 ± 0.115 | 58.694 ± 13.446 | 48.667 ± 12.275 | 7.694 ± 1.470 | 58.167 ± 8.820 | 7478.611 ± 1157.623 |
| C4_no_security | 4.669 ± 0.252 | 4.587 ± 0.303 | 3.982 ± 0.494 | 0.866 ± 0.103 | 0.991 ± 0.030 | 1.000 ± 0.000 | 0.582 ± 0.302 | 0.995 ± 0.028 | 0.808 ± 0.092 | 0.883 ± 0.109 | 62.139 ± 20.523 | 51.583 ± 19.063 | 8.139 ± 2.086 | 60.833 ± 12.516 | 7776.361 ± 1522.037 |
| C5_single_architect | 4.808 ± 0.199 | 4.451 ± 0.321 | 3.945 ± 0.467 | 0.879 ± 0.106 | 0.973 ± 0.051 | 1.000 ± 0.000 | 0.673 ± 0.328 | 0.991 ± 0.036 | 0.736 ± 0.085 | 0.872 ± 0.119 | 54.139 ± 12.849 | 47.222 ± 11.696 | 7.361 ± 1.397 | 18.722 ± 2.794 | 2415.000 ± 332.172 |
| C6_four_architects | 4.627 ± 0.320 | 4.743 ± 0.155 | 3.737 ± 0.369 | 0.875 ± 0.111 | 0.968 ± 0.045 | 1.000 ± 0.000 | 0.611 ± 0.320 | 0.979 ± 0.041 | 0.871 ± 0.079 | 0.913 ± 0.090 | 95.306 ± 29.732 | 83.917 ± 24.711 | 10.222 ± 2.294 | 97.778 ± 18.354 | 10640.083 ± 1804.542 |
| C7_architect_first | 4.722 ± 0.292 | 4.635 ± 0.240 | 4.029 ± 0.455 | 0.880 ± 0.125 | 0.951 ± 0.084 | 1.000 ± 0.000 | 0.805 ± 0.247 | 0.979 ± 0.053 | 0.812 ± 0.073 | 0.886 ± 0.112 | 60.972 ± 14.544 | 49.611 ± 13.906 | 7.417 ± 1.713 | 75.333 ± 13.707 | 9575.528 ± 1733.031 |
| C8_security_first | 4.709 ± 0.288 | 4.406 ± 0.384 | 4.208 ± 0.490 | 0.822 ± 0.148 | 0.989 ± 0.031 | 1.000 ± 0.000 | 0.729 ± 0.323 | 1.000 ± 0.000 | 0.780 ± 0.083 | 0.819 ± 0.127 | 52.889 ± 16.777 | 42.972 ± 12.874 | 7.250 ± 1.713 | 74.000 ± 13.707 | 9385.806 ± 1669.476 |
| C9_generic_team | 4.765 ± 0.216 | 4.181 ± 0.468 | 4.246 ± 0.434 | 0.792 ± 0.130 | 0.976 ± 0.055 | 1.000 ± 0.000 | 0.740 ± 0.332 | 0.996 ± 0.024 | 0.731 ± 0.106 | 0.803 ± 0.122 | 49.056 ± 12.310 | 38.222 ± 11.974 | 8.694 ± 1.786 | 85.556 ± 14.288 | 10012.333 ± 1552.599 |
| C10_glossary_memory | 4.928 ± 0.117 | 4.326 ± 0.416 | 4.025 ± 0.559 | 0.818 ± 0.154 | 0.974 ± 0.050 | 1.000 ± 0.000 | 0.936 ± 0.131 | 0.963 ± 0.078 | 0.697 ± 0.089 | 0.798 ± 0.113 | 49.417 ± 16.102 | 43.722 ± 15.771 | 6.750 ± 1.933 | 70.000 ± 15.462 | 8783.833 ± 1820.777 |

## 3. Confirmatory tests: primary metrics (Holm over comparisons, per metric)

**c4_sc** (negligible = 95% CI within ±0.10)

| Study | Condition | n | Mean | Mean C0_baseline | Effect | 95% CI | Cliff's δ | p | p (Holm) | Significant | Negligible |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ablation | C1_no_product_owner | 36 | 4.659 | 4.568 | 0.091 | [-0.017, 0.196] | 0.23 (small) | 0.149 | 0.446 | no | no |
| ablation | C2_no_architect | 36 | 4.795 | 4.568 | 0.227 | [0.115, 0.333] | 0.50 (large) | 0.000 | 0.002 | yes | no |
| ablation | C3_no_devops | 36 | 4.574 | 4.568 | 0.006 | [-0.107, 0.113] | 0.03 (negligible) | 0.920 | 0.920 | no | no |
| ablation | C4_no_security | 36 | 4.669 | 4.568 | 0.101 | [0.005, 0.197] | 0.20 (small) | 0.076 | 0.305 | no | no |
| ablation | C5_single_architect | 36 | 4.808 | 4.568 | 0.240 | [0.154, 0.326] | 0.51 (large) | 0.000 | 0.001 | yes | no |
| ablation | C6_four_architects | 36 | 4.627 | 4.568 | 0.059 | [-0.059, 0.168] | 0.15 (small) | 0.351 | 0.702 | no | no |
| order | C7_architect_first | 36 | 4.722 | 4.568 | 0.154 | [0.038, 0.260] | 0.36 (medium) | 0.010 | 0.062 | no | no |
| order | C8_security_first | 36 | 4.709 | 4.568 | 0.141 | [0.042, 0.240] | 0.29 (small) | 0.016 | 0.079 | no | no |
| specialization | C9_generic_team | 36 | 4.765 | 4.568 | 0.197 | [0.109, 0.287] | 0.40 (medium) | 0.001 | 0.006 | yes | no |
| memory | C10_glossary_memory | 36 | 4.928 | 4.568 | 0.360 | [0.288, 0.433] | 0.78 (large) | 0.000 | 0.001 | yes | no |

**gemini-3.8-flash__iso_mean** (negligible = 95% CI within ±0.25)

| Study | Condition | n | Mean | Mean C0_baseline | Effect | 95% CI | Cliff's δ | p | p (Holm) | Significant | Negligible |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ablation | C1_no_product_owner | 36 | 4.549 | 4.611 | -0.062 | [-0.165, 0.031] | -0.08 (negligible) | 0.242 | 0.838 | no | yes |
| ablation | C2_no_architect | 36 | 3.865 | 4.611 | -0.747 | [-0.896, -0.595] | -0.82 (large) | 0.000 | 0.001 | yes | no |
| ablation | C3_no_devops | 36 | 4.549 | 4.611 | -0.062 | [-0.156, 0.028] | -0.13 (negligible) | 0.209 | 0.838 | no | yes |
| ablation | C4_no_security | 36 | 4.587 | 4.611 | -0.024 | [-0.106, 0.059] | -0.00 (negligible) | 0.611 | 1.000 | no | yes |
| ablation | C5_single_architect | 36 | 4.451 | 4.611 | -0.160 | [-0.248, -0.073] | -0.30 (small) | 0.002 | 0.011 | yes | yes |
| ablation | C6_four_architects | 36 | 4.743 | 4.611 | 0.132 | [0.069, 0.198] | 0.31 (small) | 0.002 | 0.011 | yes | yes |
| order | C7_architect_first | 36 | 4.635 | 4.611 | 0.024 | [-0.052, 0.101] | 0.06 (negligible) | 0.584 | 1.000 | no | yes |
| order | C8_security_first | 36 | 4.406 | 4.611 | -0.205 | [-0.321, -0.094] | -0.31 (small) | 0.000 | 0.003 | yes | no |
| specialization | C9_generic_team | 36 | 4.181 | 4.611 | -0.431 | [-0.561, -0.304] | -0.58 (large) | 0.000 | 0.001 | yes | no |
| memory | C10_glossary_memory | 36 | 4.326 | 4.611 | -0.285 | [-0.406, -0.161] | -0.43 (medium) | 0.000 | 0.002 | yes | no |

## 4. Confirmatory tests: role-specific hypotheses (Holm over the list)

| Id | Condition | Metric | Expected | n | Effect | 95% CI | p | p (Holm) | Supported |
|---|---|---|---|---|---|---|---|---|---|
| H1 | C1_no_product_owner | gemini-3.8-flash__req_coverage | lower | 36 | -0.028 | [-0.059, 0.003] | 0.093 | 0.558 | no |
| H2 | C1_no_product_owner | gemini-3.8-flash__iso_usability | lower | 36 | -0.403 | [-0.639, -0.167] | 0.004 | 0.029 | yes |
| H3 | C2_no_architect | c4_sc_strict | lower | 36 | 0.675 | [0.495, 0.855] | 0.000 | 0.001 | no |
| H4 | C2_no_architect | gemini-3.8-flash__iso_maintainability | lower | 36 | -0.944 | [-1.181, -0.694] | 0.000 | 0.001 | yes |
| H5 | C3_no_devops | gemini-3.8-flash__iso_reliability | lower | 36 | -0.083 | [-0.319, 0.139] | 0.620 | 1.000 | no |
| H6 | C4_no_security | gemini-3.8-flash__iso_security | lower | 36 | -0.083 | [-0.153, 0.000] | 0.221 | 1.000 | no |
| H7 | C5_single_architect | gemini-3.8-flash__req_coverage | lower | 36 | 0.001 | [-0.027, 0.028] | 0.969 | 1.000 | no |
| H8 | C6_four_architects | gemini-3.8-flash__iso_usability | lower | 36 | 0.069 | [-0.167, 0.319] | 0.646 | 1.000 | no |
| H9 | C7_architect_first | gemini-3.8-flash__req_coverage | lower | 36 | 0.014 | [-0.023, 0.049] | 0.424 | 1.000 | no |
| H10 | C9_generic_team | gemini-3.8-flash__iso_security | lower | 36 | -0.389 | [-0.583, -0.194] | 0.000 | 0.001 | yes |
| H11 | C10_glossary_memory | l1_l2_jaccard | higher | 36 | 0.315 | [0.241, 0.389] | 0.000 | 0.001 | yes |

## 5. Exploratory comparisons (unadjusted p-values)

| Metric | Condition | n | Effect | 95% CI | p (unadjusted) |
|---|---|---|---|---|---|
| c4_sc_strict | C1_no_product_owner | 36 | 0.170 | [0.012, 0.322] | 0.092 |
| c4_sc_strict | C2_no_architect | 36 | 0.675 | [0.502, 0.859] | 0.000 |
| c4_sc_strict | C3_no_devops | 36 | -0.097 | [-0.289, 0.089] | 0.359 |
| c4_sc_strict | C4_no_security | 36 | 0.201 | [0.016, 0.388] | 0.042 |
| c4_sc_strict | C5_single_architect | 36 | 0.163 | [-0.020, 0.353] | 0.106 |
| c4_sc_strict | C6_four_architects | 36 | -0.044 | [-0.202, 0.115] | 0.642 |
| c4_sc_strict | C7_architect_first | 36 | 0.248 | [0.074, 0.428] | 0.014 |
| c4_sc_strict | C8_security_first | 36 | 0.427 | [0.282, 0.577] | 0.000 |
| c4_sc_strict | C9_generic_team | 36 | 0.465 | [0.293, 0.635] | 0.000 |
| c4_sc_strict | C10_glossary_memory | 36 | 0.243 | [0.079, 0.416] | 0.024 |
| compilation | C1_no_product_owner | 36 | 0.011 | [-0.028, 0.053] | 0.630 |
| compilation | C2_no_architect | 36 | -0.044 | [-0.095, 0.006] | 0.096 |
| compilation | C3_no_devops | 36 | 0.021 | [-0.020, 0.059] | 0.371 |
| compilation | C4_no_security | 36 | 0.018 | [-0.021, 0.057] | 0.447 |
| compilation | C5_single_architect | 36 | 0.031 | [-0.009, 0.072] | 0.184 |
| compilation | C6_four_architects | 36 | 0.027 | [-0.016, 0.068] | 0.264 |
| compilation | C7_architect_first | 36 | 0.032 | [-0.011, 0.074] | 0.196 |
| compilation | C8_security_first | 36 | -0.026 | [-0.076, 0.025] | 0.339 |
| compilation | C9_generic_team | 36 | -0.055 | [-0.098, -0.010] | 0.031 |
| compilation | C10_glossary_memory | 36 | -0.030 | [-0.085, 0.025] | 0.276 |
| abstraction_adherence | C1_no_product_owner | 36 | 0.003 | [-0.013, 0.019] | 0.734 |
| abstraction_adherence | C2_no_architect | 36 | -0.014 | [-0.037, 0.006] | 0.195 |
| abstraction_adherence | C3_no_devops | 36 | 0.011 | [-0.004, 0.025] | 0.199 |
| abstraction_adherence | C4_no_security | 36 | 0.015 | [0.003, 0.027] | 0.058 |
| abstraction_adherence | C5_single_architect | 36 | -0.003 | [-0.019, 0.014] | 0.750 |
| abstraction_adherence | C6_four_architects | 36 | -0.008 | [-0.024, 0.008] | 0.346 |
| abstraction_adherence | C7_architect_first | 36 | -0.025 | [-0.055, 0.001] | 0.043 |
| abstraction_adherence | C8_security_first | 36 | 0.013 | [-0.001, 0.027] | 0.106 |
| abstraction_adherence | C9_generic_team | 36 | -0.000 | [-0.017, 0.016] | 0.994 |
| abstraction_adherence | C10_glossary_memory | 36 | -0.002 | [-0.020, 0.016] | 0.835 |
| completeness | C1_no_product_owner | 36 | 0.000 | [0.000, 0.000] | 1.000 |
| completeness | C2_no_architect | 36 | 0.000 | [0.000, 0.000] | 1.000 |
| completeness | C3_no_devops | 36 | 0.000 | [0.000, 0.000] | 1.000 |
| completeness | C4_no_security | 36 | 0.000 | [0.000, 0.000] | 1.000 |
| completeness | C5_single_architect | 36 | 0.000 | [0.000, 0.000] | 1.000 |
| completeness | C6_four_architects | 36 | 0.000 | [0.000, 0.000] | 1.000 |
| completeness | C7_architect_first | 36 | 0.000 | [0.000, 0.000] | 1.000 |
| completeness | C8_security_first | 36 | 0.000 | [0.000, 0.000] | 1.000 |
| completeness | C9_generic_team | 36 | 0.000 | [0.000, 0.000] | 1.000 |
| completeness | C10_glossary_memory | 36 | 0.000 | [0.000, 0.000] | 1.000 |
| l1_l2_jaccard | C1_no_product_owner | 36 | 0.153 | [0.033, 0.266] | 0.016 |
| l1_l2_jaccard | C2_no_architect | 36 | 0.052 | [-0.060, 0.154] | 0.408 |
| l1_l2_jaccard | C3_no_devops | 36 | -0.012 | [-0.119, 0.093] | 0.857 |
| l1_l2_jaccard | C4_no_security | 36 | -0.039 | [-0.148, 0.070] | 0.521 |
| l1_l2_jaccard | C5_single_architect | 36 | 0.052 | [-0.071, 0.166] | 0.419 |
| l1_l2_jaccard | C6_four_architects | 36 | -0.010 | [-0.123, 0.102] | 0.871 |
| l1_l2_jaccard | C7_architect_first | 36 | 0.184 | [0.079, 0.283] | 0.005 |
| l1_l2_jaccard | C8_security_first | 36 | 0.108 | [0.009, 0.205] | 0.081 |
| l1_l2_jaccard | C9_generic_team | 36 | 0.119 | [-0.004, 0.246] | 0.071 |
| l1_l2_jaccard | C10_glossary_memory | 36 | 0.315 | [0.241, 0.384] | 0.000 |
| l2_l3_consistency | C1_no_product_owner | 36 | -0.011 | [-0.030, 0.008] | 0.308 |
| l2_l3_consistency | C2_no_architect | 36 | 0.011 | [-0.001, 0.024] | 0.244 |
| l2_l3_consistency | C3_no_devops | 36 | 0.000 | [-0.015, 0.016] | 1.000 |
| l2_l3_consistency | C4_no_security | 36 | 0.009 | [-0.005, 0.023] | 0.407 |
| l2_l3_consistency | C5_single_architect | 36 | 0.005 | [-0.011, 0.020] | 0.666 |
| l2_l3_consistency | C6_four_architects | 36 | -0.007 | [-0.022, 0.009] | 0.499 |
| l2_l3_consistency | C7_architect_first | 36 | -0.007 | [-0.025, 0.012] | 0.511 |
| l2_l3_consistency | C8_security_first | 36 | 0.014 | [0.004, 0.027] | 0.152 |
| l2_l3_consistency | C9_generic_team | 36 | 0.010 | [-0.003, 0.025] | 0.342 |
| l2_l3_consistency | C10_glossary_memory | 36 | -0.023 | [-0.048, 0.001] | 0.061 |
| gemini-3.8-flash__atam_ri | C1_no_product_owner | 36 | -0.015 | [-0.036, 0.010] | 0.314 |
| gemini-3.8-flash__atam_ri | C2_no_architect | 36 | -0.207 | [-0.250, -0.165] | 0.000 |
| gemini-3.8-flash__atam_ri | C3_no_devops | 36 | 0.008 | [-0.016, 0.030] | 0.610 |
| gemini-3.8-flash__atam_ri | C4_no_security | 36 | 0.001 | [-0.028, 0.030] | 0.967 |
| gemini-3.8-flash__atam_ri | C5_single_architect | 36 | -0.071 | [-0.094, -0.047] | 0.000 |
| gemini-3.8-flash__atam_ri | C6_four_architects | 36 | 0.063 | [0.039, 0.089] | 0.000 |
| gemini-3.8-flash__atam_ri | C7_architect_first | 36 | 0.005 | [-0.018, 0.029] | 0.735 |
| gemini-3.8-flash__atam_ri | C8_security_first | 36 | -0.027 | [-0.054, 0.002] | 0.077 |
| gemini-3.8-flash__atam_ri | C9_generic_team | 36 | -0.076 | [-0.109, -0.045] | 0.000 |
| gemini-3.8-flash__atam_ri | C10_glossary_memory | 36 | -0.110 | [-0.139, -0.082] | 0.000 |
| gemini-3.8-flash__req_coverage | C1_no_product_owner | 36 | -0.028 | [-0.059, 0.003] | 0.097 |
| gemini-3.8-flash__req_coverage | C2_no_architect | 36 | -0.133 | [-0.167, -0.095] | 0.000 |
| gemini-3.8-flash__req_coverage | C3_no_devops | 36 | -0.013 | [-0.046, 0.018] | 0.447 |
| gemini-3.8-flash__req_coverage | C4_no_security | 36 | 0.011 | [-0.021, 0.043] | 0.522 |
| gemini-3.8-flash__req_coverage | C5_single_architect | 36 | 0.001 | [-0.026, 0.027] | 0.966 |
| gemini-3.8-flash__req_coverage | C6_four_architects | 36 | 0.041 | [0.016, 0.066] | 0.005 |
| gemini-3.8-flash__req_coverage | C7_architect_first | 36 | 0.014 | [-0.022, 0.051] | 0.430 |
| gemini-3.8-flash__req_coverage | C8_security_first | 36 | -0.052 | [-0.089, -0.014] | 0.005 |
| gemini-3.8-flash__req_coverage | C9_generic_team | 36 | -0.069 | [-0.107, -0.032] | 0.001 |
| gemini-3.8-flash__req_coverage | C10_glossary_memory | 36 | -0.074 | [-0.108, -0.039] | 0.000 |

## 6. Sensitivity: effects adjusted for model size (brief fixed effects + log elements, HC3)

| Metric | Condition | Adjusted effect | 95% CI |
|---|---|---|---|
| c4_sc | C1_no_product_owner | 0.091 | [-0.035, 0.217] |
| c4_sc | C2_no_architect | 0.225 | [0.093, 0.357] |
| c4_sc | C3_no_devops | 0.006 | [-0.119, 0.132] |
| c4_sc | C4_no_security | 0.101 | [-0.005, 0.207] |
| c4_sc | C5_single_architect | 0.239 | [0.142, 0.336] |
| c4_sc | C6_four_architects | 0.062 | [-0.081, 0.204] |
| c4_sc | C7_architect_first | 0.154 | [0.038, 0.271] |
| c4_sc | C8_security_first | 0.140 | [0.022, 0.258] |
| c4_sc | C9_generic_team | 0.196 | [0.091, 0.301] |
| c4_sc | C10_glossary_memory | 0.358 | [0.272, 0.444] |
| gemini-3.8-flash__iso_mean | C1_no_product_owner | -0.067 | [-0.176, 0.041] |
| gemini-3.8-flash__iso_mean | C2_no_architect | -0.553 | [-0.714, -0.393] |
| gemini-3.8-flash__iso_mean | C3_no_devops | -0.071 | [-0.169, 0.026] |
| gemini-3.8-flash__iso_mean | C4_no_security | -0.049 | [-0.137, 0.040] |
| gemini-3.8-flash__iso_mean | C5_single_architect | -0.127 | [-0.230, -0.024] |
| gemini-3.8-flash__iso_mean | C6_four_architects | -0.112 | [-0.208, -0.017] |
| gemini-3.8-flash__iso_mean | C7_architect_first | -0.004 | [-0.083, 0.075] |
| gemini-3.8-flash__iso_mean | C8_security_first | -0.152 | [-0.268, -0.036] |
| gemini-3.8-flash__iso_mean | C9_generic_team | -0.344 | [-0.475, -0.214] |
| gemini-3.8-flash__iso_mean | C10_glossary_memory | -0.193 | [-0.329, -0.058] |

## 7. Exploratory: effects on canonical vs. complex briefs

| Briefs | Metric | Condition | Effect | 95% CI |
|---|---|---|---|---|
| canonical | c4_sc | C1_no_product_owner | 0.128 | [-0.017, 0.266] |
| canonical | c4_sc | C2_no_architect | 0.335 | [0.235, 0.439] |
| canonical | c4_sc | C3_no_devops | 0.011 | [-0.117, 0.146] |
| canonical | c4_sc | C4_no_security | 0.152 | [0.043, 0.259] |
| canonical | c4_sc | C5_single_architect | 0.256 | [0.142, 0.370] |
| canonical | c4_sc | C6_four_architects | 0.038 | [-0.092, 0.165] |
| canonical | c4_sc | C7_architect_first | 0.169 | [-0.031, 0.326] |
| canonical | c4_sc | C8_security_first | 0.243 | [0.129, 0.357] |
| canonical | c4_sc | C9_generic_team | 0.265 | [0.155, 0.368] |
| canonical | c4_sc | C10_glossary_memory | 0.323 | [0.228, 0.421] |
| canonical | gemini-3.8-flash__iso_mean | C1_no_product_owner | -0.142 | [-0.281, -0.007] |
| canonical | gemini-3.8-flash__iso_mean | C2_no_architect | -0.705 | [-0.872, -0.538] |
| canonical | gemini-3.8-flash__iso_mean | C3_no_devops | -0.115 | [-0.236, 0.007] |
| canonical | gemini-3.8-flash__iso_mean | C4_no_security | -0.003 | [-0.101, 0.090] |
| canonical | gemini-3.8-flash__iso_mean | C5_single_architect | -0.191 | [-0.312, -0.062] |
| canonical | gemini-3.8-flash__iso_mean | C6_four_architects | 0.101 | [0.017, 0.188] |
| canonical | gemini-3.8-flash__iso_mean | C7_architect_first | 0.010 | [-0.101, 0.122] |
| canonical | gemini-3.8-flash__iso_mean | C8_security_first | -0.219 | [-0.365, -0.080] |
| canonical | gemini-3.8-flash__iso_mean | C9_generic_team | -0.330 | [-0.476, -0.177] |
| canonical | gemini-3.8-flash__iso_mean | C10_glossary_memory | -0.198 | [-0.302, -0.090] |
| complex | c4_sc | C1_no_product_owner | 0.054 | [-0.113, 0.210] |
| complex | c4_sc | C2_no_architect | 0.119 | [-0.091, 0.313] |
| complex | c4_sc | C3_no_devops | 0.001 | [-0.195, 0.174] |
| complex | c4_sc | C4_no_security | 0.050 | [-0.109, 0.221] |
| complex | c4_sc | C5_single_architect | 0.223 | [0.099, 0.353] |
| complex | c4_sc | C6_four_architects | 0.079 | [-0.125, 0.264] |
| complex | c4_sc | C7_architect_first | 0.139 | [0.010, 0.277] |
| complex | c4_sc | C8_security_first | 0.038 | [-0.117, 0.205] |
| complex | c4_sc | C9_generic_team | 0.129 | [-0.009, 0.274] |
| complex | c4_sc | C10_glossary_memory | 0.396 | [0.298, 0.511] |
| complex | gemini-3.8-flash__iso_mean | C1_no_product_owner | 0.017 | [-0.132, 0.149] |
| complex | gemini-3.8-flash__iso_mean | C2_no_architect | -0.788 | [-1.038, -0.545] |
| complex | gemini-3.8-flash__iso_mean | C3_no_devops | -0.010 | [-0.156, 0.132] |
| complex | gemini-3.8-flash__iso_mean | C4_no_security | -0.045 | [-0.170, 0.090] |
| complex | gemini-3.8-flash__iso_mean | C5_single_architect | -0.128 | [-0.253, -0.010] |
| complex | gemini-3.8-flash__iso_mean | C6_four_architects | 0.163 | [0.073, 0.257] |
| complex | gemini-3.8-flash__iso_mean | C7_architect_first | 0.038 | [-0.069, 0.142] |
| complex | gemini-3.8-flash__iso_mean | C8_security_first | -0.191 | [-0.378, -0.021] |
| complex | gemini-3.8-flash__iso_mean | C9_generic_team | -0.531 | [-0.757, -0.319] |
| complex | gemini-3.8-flash__iso_mean | C10_glossary_memory | -0.372 | [-0.594, -0.146] |

## 7b. Exploratory: decomposition of the team effect (unadjusted p-values)

| Condition | Reference | Isolates | Metric | n | n ref | Effect | 95% CI | p (unadjusted) |
|---|---|---|---|---|---|---|---|---|
| C6_four_architects | C5_single_architect | team size and discussion length, without role diversity | c4_sc | 36 | 36 | -0.181 | [-0.297, -0.080] | 0.002 |
| C6_four_architects | C5_single_architect | team size and discussion length, without role diversity | gemini-3.8-flash__iso_mean | 36 | 36 | 0.292 | [0.212, 0.372] | 0.000 |
| C6_four_architects | C9_generic_team | role specialization at equal team size and homogeneity | c4_sc | 36 | 36 | -0.139 | [-0.260, -0.033] | 0.033 |
| C6_four_architects | C9_generic_team | role specialization at equal team size and homogeneity | gemini-3.8-flash__iso_mean | 36 | 36 | 0.562 | [0.441, 0.691] | 0.000 |
| C7_architect_first | C1_no_product_owner | presence of the Product Owner, same opening speaker | c4_sc | 36 | 36 | 0.063 | [-0.068, 0.188] | 0.377 |
| C7_architect_first | C1_no_product_owner | presence of the Product Owner, same opening speaker | gemini-3.8-flash__iso_mean | 36 | 36 | 0.087 | [-0.010, 0.191] | 0.150 |

## 8. Judge reliability (second judgement minus main judge, same runs)

ICC(A,1) and α measure absolute agreement, so a constant offset between judges lowers them; the mean difference shows that offset and Spearman ρ whether the judges rank the runs alike.

| Comparison | Metric | n | ICC(A,1) | α | Mean difference | 95% CI | Spearman ρ | Exact agreement |
|---|---|---|---|---|---|---|---|---|
| test-retest | iso_mean | 20 | 0.809 | 0.806 | 0.013 | [-0.094, 0.119] | 0.788 | – |
| test-retest | atam_ri | 20 | 0.885 | 0.883 | 0.009 | [-0.020, 0.036] | 0.831 | – |
| test-retest | req_coverage | 20 | 0.829 | 0.826 | 0.007 | [-0.018, 0.032] | 0.819 | – |
| test-retest | iso_functional_suitability | 20 | 0.905 | 0.902 | 0.100 | [0.000, 0.250] | 0.916 | 0.900 |
| test-retest | iso_performance_efficiency | 20 | 0.729 | 0.726 | -0.050 | [-0.300, 0.150] | 0.714 | 0.750 |
| test-retest | iso_compatibility | 20 | 0.578 | 0.571 | 0.100 | [-0.100, 0.300] | 0.579 | 0.800 |
| test-retest | iso_usability | 20 | 0.884 | 0.881 | 0.100 | [0.000, 0.250] | 0.895 | 0.900 |
| test-retest | iso_reliability | 20 | 0.906 | 0.904 | -0.050 | [-0.200, 0.100] | 0.918 | 0.850 |
| test-retest | iso_security | 20 | 0.496 | 0.494 | -0.050 | [-0.200, 0.100] | 0.490 | 0.850 |
| test-retest | iso_maintainability | 20 | 0.729 | 0.726 | -0.050 | [-0.250, 0.200] | 0.558 | 0.750 |
| test-retest | iso_portability | 20 | 0.509 | 0.508 | 0.000 | [-0.250, 0.200] | 0.486 | 0.700 |
| control judge | iso_mean | 66 | 0.085 | -0.537 | -1.131 | [-1.227, -1.034] | 0.401 | – |
| control judge | atam_ri | 66 | 0.100 | -0.546 | -0.326 | [-0.346, -0.305] | 0.652 | – |
| control judge | req_coverage | 66 | 0.370 | 0.201 | -0.153 | [-0.179, -0.131] | 0.579 | – |
| control judge | iso_functional_suitability | 66 | 0.101 | -0.328 | -1.227 | [-1.409, -1.045] | 0.215 | 0.197 |
| control judge | iso_performance_efficiency | 66 | 0.141 | -0.310 | -1.273 | [-1.439, -1.121] | 0.415 | 0.076 |
| control judge | iso_compatibility | 66 | 0.087 | -0.489 | -1.394 | [-1.530, -1.258] | 0.368 | 0.045 |
| control judge | iso_usability | 66 | 0.107 | -0.320 | -1.182 | [-1.364, -1.015] | 0.333 | 0.167 |
| control judge | iso_reliability | 66 | 0.296 | 0.018 | -1.227 | [-1.379, -1.076] | 0.650 | 0.091 |
| control judge | iso_security | 66 | 0.406 | 0.295 | -0.561 | [-0.682, -0.439] | 0.531 | 0.455 |
| control judge | iso_maintainability | 66 | 0.127 | -0.232 | -0.955 | [-1.121, -0.803] | 0.266 | 0.242 |
| control judge | iso_portability | 66 | 0.077 | -0.400 | -1.227 | [-1.394, -1.061] | 0.225 | 0.106 |

## 8b. Effects of the conditions under both judges (control-judge sample, same runs)

| Metric | Conditions | Same direction | Spearman ρ of the effects |
|---|---|---|---|
| iso_mean | 10 | 7 | 0.840 |
| atam_ri | 10 | 7 | 0.824 |
| req_coverage | 10 | 8 | 0.758 |

| Metric | Condition | Effect (gemini-3.8-flash) | Effect (claude-sonnet-5-5) | Same direction |
|---|---|---|---|---|
| iso_mean | C1_no_product_owner | 0.000 | 0.146 | no |
| iso_mean | C2_no_architect | -0.604 | -0.250 | yes |
| iso_mean | C3_no_devops | -0.104 | 0.146 | no |
| iso_mean | C4_no_security | 0.083 | 0.167 | yes |
| iso_mean | C5_single_architect | -0.125 | -0.125 | yes |
| iso_mean | C6_four_architects | 0.292 | 0.167 | yes |
| iso_mean | C7_architect_first | 0.062 | 0.250 | yes |
| iso_mean | C8_security_first | 0.083 | 0.188 | yes |
| iso_mean | C9_generic_team | -0.312 | 0.000 | no |
| iso_mean | C10_glossary_memory | 0.000 | 0.000 | yes |
| atam_ri | C1_no_product_owner | 0.021 | -0.005 | no |
| atam_ri | C2_no_architect | -0.182 | -0.073 | yes |
| atam_ri | C3_no_devops | -0.010 | -0.016 | yes |
| atam_ri | C4_no_security | 0.021 | -0.005 | no |
| atam_ri | C5_single_architect | -0.057 | -0.078 | yes |
| atam_ri | C6_four_architects | 0.062 | 0.010 | yes |
| atam_ri | C7_architect_first | -0.010 | 0.000 | no |
| atam_ri | C8_security_first | 0.021 | 0.016 | yes |
| atam_ri | C9_generic_team | -0.094 | -0.052 | yes |
| atam_ri | C10_glossary_memory | -0.094 | -0.036 | yes |
| req_coverage | C1_no_product_owner | 0.109 | 0.035 | yes |
| req_coverage | C2_no_architect | -0.066 | -0.022 | yes |
| req_coverage | C3_no_devops | -0.004 | 0.013 | no |
| req_coverage | C4_no_security | 0.064 | 0.101 | yes |
| req_coverage | C5_single_architect | 0.102 | 0.042 | yes |
| req_coverage | C6_four_architects | 0.110 | 0.146 | yes |
| req_coverage | C7_architect_first | 0.051 | 0.044 | yes |
| req_coverage | C8_security_first | 0.039 | 0.052 | yes |
| req_coverage | C9_generic_team | 0.006 | 0.027 | yes |
| req_coverage | C10_glossary_memory | 0.020 | -0.010 | no |

## 9. Convergent validity and size bias (Spearman ρ, bootstrap 95% CI)

| x | y | ρ | 95% CI |
|---|---|---|---|
| c4_sc | gemini-3.8-flash__iso_mean | -0.114 | [-0.212, -0.015] |
| compilation | gemini-3.8-flash__iso_mean | 0.087 | [-0.013, 0.186] |
| total_elements | gemini-3.8-flash__iso_mean | 0.458 | [0.375, 0.533] |
| total_elements | c4_sc | -0.121 | [-0.215, -0.017] |
| gemini-3.8-flash__req_coverage | gemini-3.8-flash__iso_functional_suitability | 0.410 | [0.326, 0.488] |

## 10. Ceiling: share of runs at the maximum score

| briefs | functional_suitability | performance_efficiency | compatibility | usability | reliability | security | maintainability | portability | c4_sc |
|---|---|---|---|---|---|---|---|---|---|
| all | 0.655 | 0.697 | 0.787 | 0.336 | 0.491 | 0.840 | 0.648 | 0.139 | 0.213 |
| canonical | 0.583 | 0.792 | 0.907 | 0.269 | 0.477 | 0.880 | 0.690 | 0.199 | 0.218 |
| complex | 0.727 | 0.602 | 0.667 | 0.403 | 0.505 | 0.801 | 0.606 | 0.079 | 0.208 |
| control sample, gemini-3.8-flash | 0.682 | 0.667 | 0.727 | 0.288 | 0.500 | 0.864 | 0.652 | 0.121 | – |
| control sample, claude-sonnet-5-5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.348 | 0.000 | 0.000 | – |
