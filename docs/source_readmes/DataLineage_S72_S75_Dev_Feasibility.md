# S72–S75 HEALTHVER development-only feasibility audit

Run in PowerShell after extracting ZIP directly to `D:\DataLineage`:

```powershell
python "D:\DataLineage\DataLineage_S72_S75_Dev_Feasibility\run.py" --base "D:\DataLineage"
```

Outputs are written to `D:\DataLineage\S72_S75_Dev_Feasibility_Output`.

S72: source SHA-256, row counts and labels. S73: duplicate claim/evidence structure, conflicting labels for identical normalized claim–evidence pairs. S74: evidence-pool reuse and dev evidence coverage from train-only candidate pool (NOT non-oracle retrieval validation). S75: scientific gate. The script reads **only** `healthver_train.csv` and `healthver_dev.csv`. It never reads test splits, SciFact files, or performs model inference. Claims and evidence in detailed CSV are represented by SHA-256 digests rather than their full text.

Upload `s73_label_structure_report.json`, `s74_retrieval_feasibility_report.json`, `s75_scientific_gate_report.json` after running.
