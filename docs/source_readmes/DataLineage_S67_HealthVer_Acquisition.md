# S67 HEALTHVER acquisition and source snapshot inventory

Prerequisite: Git installed and internet connectivity on the Windows research PC.

Extract ZIP to `D:\DataLineage`, then run:

```powershell
python "D:\DataLineage\DataLineage_S67_HealthVer_Acquisition\run.py" --base "D:\DataLineage"
```

This clones the official public repository into `D:\DataLineage\S67_HealthVer_Acquisition\HealthVer_official` (only if absent), records its commit, and hashes all repository files. It **does not parse labels, perform inference, assess leakage, or authorize evaluation**. Re-running does not silently update an existing checkout. If Git is unavailable, install Git for Windows or download the repository from its official GitHub page, extract to the expected directory, and run with `--skip-clone`; note that this will not provide a Git commit ID unless `.git` metadata exists.

Upload `S67_HealthVer_Acquisition_Output\s67_acquisition_report.json` and `s67_source_file_inventory.csv` for S68 schema review. The independent evaluator must handle holdout/test split content and attest exposure/disjointness separately.

Official source: https://github.com/sarrouti/HealthVer
