# Reproducibility and provenance policy

## Study
Reliability of Cross-Domain Adaptation and Evidence Aggregation in Scientific Claim Verification.

## Evidence classes

1. **Source artifacts**: original evaluation scripts, input manifests and immutable provenance evidence; preserve file hashes.
2. **Derived outputs**: prediction summaries, fusion-policy comparisons and bootstrap confidence intervals; preserve exact computation protocols.
3. **Historical records**: prior results that have been reconciled but cannot be fully re-executed from the currently available source artifacts; label clearly as historical.

## Verification gates before uploading experimental outputs

- Establish the original file path, provenance, digest and intended role.
- Check that the file contains no credentials, identifying information or unauthorized redistributed source data.
- Reconcile reported values with the corresponding evaluation code and protocol.
- Distinguish development-only evaluation from independent testing.
- Record dependency versions and random seeds where known.
- Document missing historical frozen probabilities and any input-length confounding without implying that these were resolved.

## Boundaries

SciFact evidence-aggregation development results must not be presented as a held-out test evaluation. COVID-Fact results require their own evaluation protocol and paired resampling description. HEALTHVER adaptation results must not be claimed to establish generalization to every scientific domain.

## Publication policy

Do not publish the journal submission source, manuscript PDF, unpublished figures or external datasets here. Do not add a license until rights and distribution intentions are established.

## Current repository status

This document is a protocol, not evidence that scripts or experiments have been uploaded or reproduced.
