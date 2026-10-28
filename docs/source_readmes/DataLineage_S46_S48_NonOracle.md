# S46–S48: SciFact development-only non-oracle sentence evidence and frozen NLI

## Requirements
- Python 3.10+ (standard library for sentence selection)
- Optional NLI: torch and transformers installed, frozen local model `D:\DataLineage\S7_NLI_Model`.

## Run
```
python "D:\DataLineage\DataLineage_S46_S48_NonOracle\run.py" --base "D:\DataLineage" --top-docs 5 --sentences-per-doc 3 --nli --model "D:\DataLineage\S7_NLI_Model"
```
If transformers/torch are unavailable, omit `--nli --model ...` for the retrieval-only analysis. This runner does not install packages or download model weights.

## Outputs
- `S46_S48_Dev_NonOracle_Output/s46_sentence_candidates.csv`: selected sentences and NLI probabilities if enabled.
- `S46_S48_Dev_NonOracle_Output/s47_claim_diagnostics.csv`: gold sentence coverage and exploratory binary predictions.
- `S46_S48_Dev_NonOracle_Output/s48_report.json`: integrity hashes, class distribution, evidence recall, conditional binary accuracy.

## Integrity and scientific limits
- Only `claims_dev.jsonl` is loaded; `claims_test.jsonl` is forbidden by name and never accessed.
- Gold evidence and labels are consulted only AFTER lexical sentence selection, for evaluation.
- Abstract is read as an indexed list of sentences from the original SciFact corpus, preserving sentence IDs.
- SciFact unannotated claims are NOT relabeled as FEVER NEI.
- Binary NLI max-score is an exploratory baseline, not calibrated or a validated fusion method.
- SciFact development data has prior project exposure; no independent validation claim.
- No publisher-level independence or authentic version metadata is established.
