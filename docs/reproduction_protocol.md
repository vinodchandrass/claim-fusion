# ClaimFusion reproduction protocol

Status: **partial reproduction package; clean-room reproduction not yet demonstrated**.

## Experimental tracks

1. HEALTHVER: data eligibility and acquisition checks, CPU domain adaptation, held-out development evaluation.
2. SciFact: development-only claim/evidence preparation, fixed retrieval, NLI transfer and evidence aggregation. No SciFact test results are claimed.
3. Matched SciFact inference: three checkpoints (frozen, weighted, unweighted) at max lengths 192 and 512. Earlier S118 comparisons were invalidated in the S131 reconciliation; do not treat S118 state records as validated comparative evidence.
4. COVID-Fact: external supplied-evidence evaluation with frozen and adapted checkpoints at length 192, without external-set tuning.

## Existing code

- `scripts/DataLineage_CPU_Domain_Adaptation/run.py`
- `scripts/DataLineage_HealthVer_Transfer/run.py`
- `scripts/DataLineage_CrossDomain_Fusion/run.py`
- `scripts/DataLineage_ConflictAware_Fusion/run.py`
- `scripts/DataLineage_S118_Matched_Inference.py`
- `scripts/S129_COVIDFact_External_Validation.py`

## Required external inputs

Do **not** assume this repository includes the datasets or checkpoint directories. Obtain source datasets from their authorized providers and arrange them in the paths documented by the original scripts. Preserve source hashes and dataset versions. Model directories require a compatible `config.json`, tokenizer files and weights. The external evaluation script expects `S127_External_Data/covidfact.jsonl` and `S7_NLI_Model` plus `CPU_Domain_Adaptation_Output/checkpoint_weighted` under `--root`.

For SciFact, supply development-only candidate rows and development gold labels, including frozen per-evidence probabilities where required. The cross-domain script accepts `--candidates`, `--model`, `--gold` and `--out`; the conflict-aware script accepts `--candidates`, `--cache`, `--gold`, `--out`. These paths are not published as public dataset downloads.

## Dependencies

The published cross-domain requirements are **not a full environment lock**. Other scripts import `numpy`, `pandas` and `scikit-learn`, in addition to `torch`, `transformers` and related packages. Before claiming exact numerical reproduction, record Python version, package versions, operating system, hardware, seeds and all input/checkpoint SHA-256 digests.

## Reproduction acceptance gates

- Input and model files exist; schemas, labels and checksums agree with original manifests.
- All scripts complete without silent omissions, data leakage or changes to frozen evaluation policy.
- Regenerated aggregate outputs are compared to published reports, with metric differences and reasons recorded.
- SciFact development outcomes remain explicitly development-only.
- COVID-Fact supplied evidence order is not represented as verified retrieval rank.
- Missing historical probabilities and the invalidated S118 comparison are disclosed, not reconstructed from assumptions.

**Current verdict:** verified public source artifacts and aggregate evidence; **not** a clean-machine reproduction certificate. The release should remain labeled as partial until all acceptance gates pass.
