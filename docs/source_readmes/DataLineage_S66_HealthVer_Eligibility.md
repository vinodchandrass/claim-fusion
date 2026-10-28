# S66 — HEALTHVER candidate metadata intake (no evaluation)

This package deliberately does **not** download or parse HealthVer claim/evidence data. It lists local candidate filenames and byte sizes only; hashes are not computed for potentially sealed external files. It computes SHA-256 for six previously exposed/frozen **local development** artifacts, and does not open SciFact test.

## Windows
Extract ZIP to `D:\DataLineage`, then:

```powershell
python "D:\DataLineage\DataLineage_S66_HealthVer_Eligibility\run.py" --base "D:\DataLineage"
```

If an independent evaluator has already acquired a candidate snapshot and permits **metadata-only** inventory:

```powershell
python "D:\DataLineage\DataLineage_S66_HealthVer_Eligibility\run.py" --base "D:\DataLineage" --candidate-dir "D:\ExternalCandidate\HealthVer"
```

Outputs: `S66_HealthVer_Eligibility_Output/s66_eligibility_report.json`, `s66_candidate_file_inventory.csv`, `s66_local_frozen_reference_hashes.csv`.

**IMPORTANT**: A metadata-only pass does not establish license compliance, dataset independence, overlap clearance, retrieval suitability, or label compatibility. No claims of independent evaluation may be made. A separate independent evaluator must establish provenance, license, exposure history, and prospective split-level protocol before any holdout content is accessed.
