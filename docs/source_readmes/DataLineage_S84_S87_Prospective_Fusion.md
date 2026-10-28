# S84–S87: Fixed-form fusion candidates and diagnostic stress test

This is a development-only methodological experiment. The candidate policies are fixed in source code; they are **not** claimed to have been preregistered before the earlier development analyses. Do not choose a winning policy based on this output and then claim independent validation.

- S84: hash check and frozen `top_doc_mean` parity.
- S85: fixed rank-discounted document margin (inverse-square weights), plus robust median comparator.
- S86: conflict-aware selective abstention diagnostic; abstention is **not** NEI.
- S87: class-specific and coverage-aware descriptive evaluation on existing SciFact development labels.

Inputs: the already frozen `s46_sentence_candidates.csv` (4,500 rows). No model downloads, test reads, or external evaluation. The runner will stop if its SHA-256 differs from the frozen reference.

Run in PowerShell after extracting into `D:\DataLineage`:

```powershell
python "D:\DataLineage\DataLineage_S84_S87_Prospective_Fusion\run.py" --candidates "D:\DataLineage\S46_S48_Dev_NonOracle_Output\s46_sentence_candidates.csv" --output "D:\DataLineage\S84_S87_Output"
```

Outputs: `s84_s87_claim_diagnostics.csv` and `s87_report.json`.

**Scientific limitation:** Rank is a retrieval relevance surrogate, not verified source provenance. This experiment cannot demonstrate source-dependence-aware fusion or Information Fusion-level novelty. Authentic source identity and independence metadata are prerequisites for such claims. External evaluator custody, contamination screening, and independent testing remain blocked.
