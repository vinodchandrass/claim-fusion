# DataLineage CPU domain adaptation — development-only

## Purpose
Compare **unweighted** and **inverse-frequency class-weighted** fine-tuning of the same locally frozen DeBERTa NLI model on HEALTHVER training evidence pairs. Internal validation is grouped by normalized claim. Both candidates are subsequently evaluated on HEALTHVER development pairs, **not an independent test**.

## Windows PowerShell
Extract this directory under `D:\DataLineage`. In an Anaconda terminal:

```powershell
cd D:\DataLineage\DataLineage_CPU_Domain_Adaptation
python -m pip install -r requirements.txt
python .\run.py `
  --train "D:\DataLineage\S67_HealthVer_Acquisition\HealthVer_official\data\healthver_train.csv" `
  --dev "D:\DataLineage\S67_HealthVer_Acquisition\HealthVer_official\data\healthver_dev.csv" `
  --model "D:\DataLineage\S7_NLI_Model" `
  --out "D:\DataLineage\CPU_Domain_Adaptation_Output" `
  --threads 4 --batch-size 4 --grad-accum 4 --epochs 1 `
  --dev-only-after-training
```

For a quick CPU smoke run, use `--variants weighted --epochs 1` but **do not** treat a smoke run as the matched two-variant comparison. This is potentially hours of CPU training; allow sufficient memory/disk. Model files must already exist locally. No network calls or sealed-test access occur in `run.py`.

## Outputs
- `domain_adaptation_report_DEV_ONLY.json`: settings, hashes, split sizes, internal validation and HEALTHVER dev metrics.
- `dev_predictions_weighted_DEV_ONLY.csv` / `dev_predictions_unweighted_DEV_ONLY.csv`: three-class predictions, probabilities, anonymized claim-group hashes.
- `checkpoint_weighted/` and `checkpoint_unweighted/`: trained models, tokenizer and configs.

Upload **only** `domain_adaptation_report_DEV_ONLY.json` for initial scientific assessment.

## Scientific safeguards
- HEALTHVER test file is not read. Files with `test` in the supplied train/dev filename are rejected.
- Normalized-claim groups do not cross the internal training/validation split.
- Exact claim overlaps between HEALTHVER train and dev are excluded from fitting and internal validation.
- Shared evidence texts across claim groups and across HEALTHVER train/dev remain possible; report these as a limitation.
- Input order is evidence as premise, claim as hypothesis.
- Model label IDs must be contradiction=0, entailment=1, neutral=2 or the program stops.
- No development-selected model is claimed to have independent generalization. A separately authorized untouched evaluation set is still needed.
- Domain-adapted pair classification does **not** demonstrate a novel document-fusion contribution.

## CPU resource note
Fine-tuning DeBERTa-v3-base twice on CPU can take many hours. Do not interrupt if progress continues; each variant prints progress every 200 batches.
