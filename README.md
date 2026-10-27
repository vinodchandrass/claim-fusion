# ClaimFusion

Reproducibility workspace for the empirical study **Reliability of Cross-Domain Adaptation and Evidence Aggregation in Scientific Claim Verification**.

## Scope

This repository is intended to document and, once verified, distribute research code, experimental configurations, provenance records, aggregate results, and reproduction instructions for scientific claim verification across domains. It is **not** a manuscript repository.

## Current status

**Artifact publication and static reproducibility audit complete; independent reproduction not yet established.** Verified original experimental scripts, selected aggregate results, manifests, and checksum records are deposited. Datasets, model checkpoints and individual predictions are not redistributed. See [reproducibility readiness audit](docs/reproducibility_readiness_audit.md) and [published-byte verification](verification/published_byte_comparison_2026-10-27.md).

## Repository structure

- `scripts/`: verified evaluation and evidence-aggregation implementations
- `configs/`: evaluation settings and frozen experiment configurations
- `results/`: verified, redistribution-cleared experimental outputs
- `verification/`: hashes, source manifests and reconciliation records
- `docs/`: protocols, dataset access guidance and reproduction instructions

The directories contain only the selected, verified artifacts; they are not a complete runnable distribution.

## Data and materials policy

Do not commit the journal manuscript, submitted PDF, unpublished figures, copyrighted datasets, restricted checkpoints, credentials, tokens, or unverified experimental outputs. Source datasets should be obtained from their original providers under their respective conditions.

## Reproducibility status

**Not yet independently reproducible from this repository.** A future verified release will identify the available artifacts and the exact reproduction boundary. In particular, historical frozen multi-document inference outputs must not be represented as fully reconstructed if their source probabilities are unavailable.

## Research contact

Vinod Chandra S. S.
