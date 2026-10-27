# Reproducibility readiness audit (2026-10-27)

Scope: static inspection of the four scripts in `scripts/`, the published requirements file, and README. **No experiments were executed.** This audit does not certify end-to-end reproducibility.

## Gate results

| Gate | Status | Evidence and required action |
|---|---|---|
| Published source integrity | PASS (content-equivalent) | Original-vs-GitHub byte comparison in `verification/published_byte_comparison_2026-10-27.md`; Git line-ending normalization accounts for differences. |
| Original aggregate result provenance | PARTIAL | Development-only reports and manifests present; input artifacts referenced by manifests are not all distributed. |
| Dependency installation | NOT READY | Published `configs/DataLineage_CrossDomain_Fusion/requirements.txt` lists torch, transformers, sentencepiece and safetensors; S118/S129 additionally import numpy and pandas, and S129 requires scikit-learn. Versions/environment are not frozen for all scripts. |
| Dataset availability | BLOCKED | SciFact candidates, labels, adapted prediction cache, and COVID-Fact source JSONL are not in the repository. Obtain from authorized source or provide locally. |
| Checkpoint availability | BLOCKED | Scripts require local S7_NLI_Model and CPU_Domain_Adaptation_Output checkpoints; weights/tokenizers are intentionally excluded. |
| Portable execution | PARTIAL | SciFact scripts accept explicit candidate/model/output paths. S118/S129 accept `--root` but assume a specific directory tree and default to `D:\DataLineage`. |
| Independently reproduced results | NOT TESTED | Neither clean-environment execution nor numerical output reconciliation was performed in this audit. |

## Script entry points and minimum input contract

- `scripts/DataLineage_CrossDomain_Fusion/run.py`: requires `--candidates`, `--model`, `--out`; optional `--gold`. Needs SciFact candidate CSV with claims, documents, sentences, ranks and frozen probabilities, and an adapted local NLI checkpoint. Development-only analysis.
- `scripts/DataLineage_ConflictAware_Fusion/run.py`: requires `--candidates`, `--cache`, `--gold`, `--out`. The cached predictions must match candidate identity row by row. Development-only, claim-disjoint cross-fitting, not independent test validation.
- `scripts/DataLineage_S118_Matched_Inference.py`: accepts `--root`, `--batch-size`, `--device`; expects 4,500 candidate rows for 300 claims in `CrossDomain_Fusion_Output/adapted_scifact_candidates_DEV_ONLY.csv` and three model directories under root. Evaluates frozen, weighted, unweighted checkpoints at max lengths 192 and 512. Its published manifest does not replace the absent inference input/output CSVs.
- `scripts/S129_COVIDFact_External_Validation.py`: accepts `--root`, `--batch-size`, `--device`; expects `S127_External_Data/covidfact.jsonl` and two checkpoint directories. Uses supplied evidence order, **not a verified retrieval ranking**. COVID-Fact claim truth labels are not necessarily evidence-level NLI annotations.

## Scientific interpretation safeguards

- SciFact fusion comparisons are development-only; do not claim an independent SciFact test result.
- Frozen-vs-adapted SciFact comparisons from historical runs can be confounded by different maximum input lengths (512 vs 192); use the matched-length design only when actual paired outputs support a comparison.
- External COVID-Fact evaluation uses supplied evidence and must not be described as an independently validated retrieval-and-verification pipeline.
- Preserve negative external generalization findings and historical probability/provenance limitations.
- Do not upload raw datasets, restricted model weights, claim-level predictions, manuscript or figures without separate authorization.

## Finite close-out plan

1. Document access instructions for required external inputs and the original checkpoint layout; do not redistribute restricted artifacts.
2. Add a tested environment specification and a preflight-only input validator; avoid changing frozen original scripts.
3. Run a clean-environment preflight and, only if all authorized inputs are available, a controlled reproduction with output hash/metric reconciliation.
4. If inputs are unavailable, explicitly release as **artifact-verified, not independently reproduced** and stop; do not imply full reproduction.
