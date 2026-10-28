# S42–S44 SciFact development-only non-oracle retrieval

Run from PowerShell after extracting this folder to D:\DataLineage:

```powershell
python "D:\DataLineage\DataLineage_S42_S44_SciFact_Dev\run.py" --base "D:\DataLineage" --top-k 5
```

Reads ONLY `ScientificClaim_Benchmark_SciFact/data/data/claims_dev.jsonl` and `corpus.jsonl` (as identified in your file inventory). Writes to `D:\DataLineage\S42_S44_SciFact_Dev_Output`:
- `s42_dev_retrieval.csv`: BM25 title+abstract document rankings and original dev labels (for audit only).
- `s42_s44_report.json`: counts, hashes, and dev document-retrieval recall@K.

Gold `cited_doc_ids` are **never used for retrieval**; they are inspected after retrieval solely to compute dev recall. No NLI, no three-class claim predictions, no independent holdout evaluation, and no authentic publisher provenance is claimed. SciFact test claims are deliberately never opened. Avoid modifying frozen prior results.

For an inexpensive pilot, add `--max-claims 25`; for a full development run, omit it. Uses only Python standard library; computation can take several minutes. No placeholder CSV files required.
