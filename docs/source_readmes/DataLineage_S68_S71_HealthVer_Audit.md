# S68–S71: HEALTHVER train/dev schema and overlap audit

Run on Windows after extracting ZIP directly into `D:\DataLineage`:

```powershell
python "D:\DataLineage\DataLineage_S68_S71_HealthVer_Audit\run.py" --base "D:\DataLineage"
```

Inputs: `D:\DataLineage\S67_HealthVer_Acquisition\HealthVer_official\data\healthver_train.csv` and `healthver_dev.csv`, plus existing SciFact `claims_train.jsonl` and `claims_dev.jsonl`.

**Safety:** The runner never reads `healthver_test.csv` or `claims_test.jsonl`. It checks the train/dev hashes against S67, then analyzes only those splits. No model inference, held-out evaluation, or permission is conferred.

Outputs in `D:\DataLineage\S68_S71_HealthVer_Audit_Output`:
- `s68_schema_summary.json`: observed columns, counts, missingness, label distributions.
- `s70_near_overlap_review_candidates.csv`: potential token-Jaccard overlap candidates for manual review (hashes, no claim text).
- `s71_scientific_gate_report.json`: dataset structure, exact overlap, non-oracle retrieval feasibility and remaining scientific gates.

**Interpretation:** A paired evidence file is not necessarily an independent retrieval corpus. Near-duplicate screens do not certify semantic independence or absence of model pretraining exposure. Independent custody, source validity, label semantics, and formal authorization remain necessary before holdout scoring.
