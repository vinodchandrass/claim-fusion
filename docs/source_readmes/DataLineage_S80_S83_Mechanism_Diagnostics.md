# S80-S83 — Development mechanism diagnostics

This combined package analyzes the already frozen S46 NLI cache. It never reads SciFact or HEALTHVER test splits, does not retrain, and does not choose a new model. It measures rank-specific errors, cross-document disagreement, paired classification transitions and retrieval-stratified failure patterns. Gold evidence flags are used only in post-hoc descriptive analysis of the development set.

Windows PowerShell (extract ZIP directly into D:\DataLineage):

```powershell
python "D:\DataLineage\DataLineage_S80_S83_Mechanism_Diagnostics\run.py" --candidates "D:\DataLineage\S46_S48_Dev_NonOracle_Output\s46_sentence_candidates.csv" --output "D:\DataLineage\S80_S83_Mechanism_Output"
```

Outputs: s80_claim_mechanism_diagnostics.csv, s81_rankwise_document_diagnostics.csv, s83_mechanism_report.json. Upload s83_mechanism_report.json for interpretation.

Integrity gate: S46 input must have SHA-256 b6724c628aebf5b112fe3c8ca74fb59eddfad1b0e1f899eaf9b300190a8dc41d.

**Important**: This diagnostic cannot establish causality, source independence, or a novel provenance-aware fusion advantage. Subsequent genuine fusion research requires authentic provenance metadata and an independently controlled evaluation.
