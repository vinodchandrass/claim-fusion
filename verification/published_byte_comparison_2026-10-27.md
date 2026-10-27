# Published artifact byte-comparison verification — 2026-10-27

Repository commit checked: `e6eb63a09abd9a59c6faa94c84959d62d545acf8`.

All 15 selected published files were compared against the original bytes in `ClaimFusion_Selected(1).zip`. For each, the original Git blob SHA-1 was calculated and compared with the SHA-1 recorded in the GitHub repository tree. When they differed, CRLF line endings were converted to LF and the Git blob SHA-1 was recalculated.

**Result: 5/15 original files matched exactly; the other 10/15 matched exactly after CRLF-to-LF conversion; zero unexplained differences.** The comparison does not constitute independent execution of the experiments.

CRLF-to-LF-only differences:

- `results/covidfact/evaluation_summary.csv`
- `results/covidfact/paired_cluster_bootstrap.csv`
- `results/covidfact/unique_claim_sensitivity.csv`
- `results/scifact/conflict_fusion_report_DEV_ONLY.json`
- `results/scifact/crossdomain_fusion_report_DEV_ONLY.json`
- `scripts/DataLineage_S118_Matched_Inference.py`
- `verification/S118_Matched_Inference_Output/manifest.json`
- `verification/S129_COVIDFact_External_Validation/manifest.json`
- `verification/healthver/s71_scientific_gate_report.json`
- `verification/healthver/s75_scientific_gate_report.json`

Original-byte exact matches:

- `configs/DataLineage_CrossDomain_Fusion/requirements.txt`
- `scripts/DataLineage_ConflictAware_Fusion/run.py`
- `scripts/DataLineage_CrossDomain_Fusion/run.py`
- `verification/scifact/DataLineage_S113_Paired_Evidence_Gate.json`
- `verification/scifact/DataLineage_S114_Exact_Policy_Audit.json`

**Interpretation:** Git line-ending normalization fully accounts for the byte differences. The original SHA-256 index is a record of source archive bytes, not of LF-normalized repository bytes; verification of repository files must account for this distinction. No scientific measurements were recomputed.
