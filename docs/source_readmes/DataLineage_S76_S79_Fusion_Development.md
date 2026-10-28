# S76–S79: Document-grouped fusion diagnostics (development-only)

This package runs on the previously frozen S46 cached NLI scores. It is an **exploratory method-development experiment**, not a new independent evaluation or a provenance-aware model. It does not read test files or perform NLI inference.

## Run on Windows

```powershell
python "D:\DataLineage\DataLineage_S76_S79_Fusion_Development\run.py" `
  --candidates "D:\DataLineage\S46_S48_Dev_NonOracle_Output\s46_sentence_candidates.csv" `
  --output "D:\DataLineage\S76_S79_Fusion_Development_Output"
```

## Operators (fixed in source code)

- `top_doc_mean`: the frozen S53 comparator; mean entailment and contradiction probabilities over sentences in the rank-1 document.
- `five_doc_equal_mean`: mean of each document's mean probabilities across the five retrieved documents. No claim of source independence.
- `five_doc_majority_vote`: majority of document-level entailment versus contradiction margins, ties classified REFUTES.
- Diagnostic-only abstention: top-document margin magnitude below 0.15. This threshold is a pre-specified illustrative value, **not calibrated**.

Labels are used only for the 188 annotated SUPPORTS/REFUTES development claims. The other 112 claims are UNANNOTATED, not NEI. A fixed 10,000-resample claim-level bootstrap describes paired development differences; its intervals are **not** selection-adjusted or confirmatory.

## Scientific gates

The next substantive step requires authentic source metadata (publisher, URL/DOI, publication identity, shared-origin links) before source-dependence-aware fusion can be implemented or evaluated. Do not use page IDs or retrieved document IDs as a surrogate for verified independent sources. Independent holdout evaluation requires separate custody, exposure review, and approval.
