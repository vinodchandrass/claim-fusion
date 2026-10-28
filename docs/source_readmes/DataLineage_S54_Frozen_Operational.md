# S54 — Frozen operational replay + independent custody gate

Runs **only on S46 cached development candidates**. It does not access SciFact test data, choose a new policy, or tune thresholds. It replays the preselected `top_doc_mean` rule from S53, separating operational inference from gold-label diagnostics.

## PowerShell

```powershell
python "D:\DataLineage\DataLineage_S54_Frozen_Operational\run.py" `
 --candidates "D:\DataLineage\S46_S48_Dev_NonOracle_Output\s46_sentence_candidates.csv" `
 --frozen-policy "D:\DataLineage\S53_local_audit\s53_frozen_policy.json" `
 --transitions "D:\DataLineage\S53_local_audit\s53_paired_transitions.csv" `
 --output "D:\DataLineage\S54_Frozen_Replay_Output"
```

If the S53 files are not on your computer, use the two bundled `s53_*.json/csv` files instead (copied from the prior verified audit). Do **not** run this script on the sealed SciFact test set. If the S46 cache is elsewhere, locate it with `Get-ChildItem D:\DataLineage -Recurse -Filter s46_sentence_candidates.csv`.

## Scientific controls

- Operational CSV has **no gold labels, gold flags, or oracle evidence**.
- Development transition comparison is optional and performed only **after** predictions.
- Independent custody attestation and external manifest are **metadata-only**; they do not unlock sealed evaluation.
- A signed independent-custodian protocol, source provenance, disjointness, no-prior-exposure, and three-class NEI protocol remain unresolved.
- The 125/188 result is exploratory because the operator was selected on the same development claims.

## Next genuine milestone

Acquire a separately custodied, unexposed, claim-independent evaluation dataset and its corpus; validate exposure and provenance before any labels are unsealed. A new binary classifier alone is not a provenance-aware fusion contribution.
