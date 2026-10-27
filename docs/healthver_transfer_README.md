# HEALTHVER cross-domain NLI component transfer

Run on the existing Anaconda environment, without touching sealed tests:

```powershell
python "D:\DataLineage\DataLineage_HealthVer_Transfer\run.py" --dev "D:\DataLineage\S67_HealthVer_Acquisition\HealthVer_official\data\healthver_dev.csv" --model "D:\DataLineage\S7_NLI_Model" --out "D:\DataLineage\HealthVer_Transfer_Output" --batch-size 8 --bootstrap 1000
```

Dependencies: `torch`, `transformers` and the existing local DeBERTa NLI model. CPU supported; adjust batch size if memory constrained.

Outputs: `healthver_transfer_report.json`, `healthver_dev_pair_predictions.csv`. Upload only the JSON report initially.

Safety: verifies exact official development CSV SHA-256, refuses a test-named file, loads the local model offline, checks label order, and does not train/tune. Bootstrap clusters repeated evidence pairs by normalized claim. The split is *development only*, and evidence reuse can induce additional dependence not covered by claim clustering. A pair-level NLI score is not a claim-level document-fusion score. The runner cannot establish a novel fusion contribution or independent validation.
