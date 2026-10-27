# DataLineage — S131 evidence reconciliation and decision lock

Date: 2026-10-25. Status: evidence reconciliation, **not submission approval**.

## 1. Authoritative result tables

### SciFact development (188 annotated claims)
Source: `S122_Consolidated/accuracy.csv`. These are historical development results, **not** a matched-control causal estimate of domain adaptation.

| Checkpoint | Policy | Correct/188 | Accuracy | Macro-F1 |
|---|---|---:|---:|---:|
| Frozen | Top document | 125 | 0.6649 | 0.6647 |
| Weighted adapted | Top document | 149 | 0.7926 | 0.7644 |
| Frozen | Five-document mean | 101 | 0.5372 | 0.5275 |
| Weighted adapted | Five-document mean | 139 | 0.7394 | 0.7150 |
| Frozen | Rank-discounted | 103 | 0.5479 | 0.5410 |
| Weighted adapted | Rank-discounted | 142 | 0.7553 | 0.7350 |
| Frozen | Document majority | 84 | 0.4468 | 0.4177 |
| Weighted adapted | Document majority | 130 | 0.6915 | 0.6538 |

Historical top-document weighted-minus-frozen difference: +24/188 = +12.77 percentage points; paired McNemar exact p=0.00267, claim bootstrap 95% CI [+4.79,+20.74] percentage points (`S122_Consolidated/paired_comparisons.csv`). The original frozen/adapted inference configurations were not fully matched; avoid causal attribution. S118's claim-first matched inference was invalidated. S121 evidence-first spot replication is a **100-pair check**, not a complete replacement of S122.

### COVID-Fact external supplied-evidence classification (4,086 records; 10,389 pairs)
Source: `s129inspect/evaluation_summary.csv` and `paired_cluster_bootstrap.csv`.

| Checkpoint | Policy | Accuracy | Macro-F1 |
|---|---|---:|---:|
| Frozen | First passage | 0.6752 | 0.6595 |
| Weighted adapted | First passage | 0.5656 | 0.5655 |
| Frozen | Mean passages | 0.7002 | 0.6860 |
| Weighted adapted | Mean passages | 0.6050 | 0.6050 |
| Frozen | Rank-discounted passages | 0.6968 | 0.6824 |
| Weighted adapted | Rank-discounted passages | 0.5986 | 0.5986 |

Weighted-minus-frozen mean-fusion macro-F1 = −0.08104, claim-cluster bootstrap 95% CI [−0.09545,−0.06672]. The mean-fusion SUPPORTS recall changes 0.7685→0.9383 while REFUTED recall changes 0.6685→0.4502. Frozen-only correct=710; weighted-only correct=321 (S130). Unique normalized claims=4,080; the previously reported 4,048 was erroneous. This is supplied-evidence classification, **not** end-to-end retrieval verification. The evidence list is not an authenticated retrieval ranking.

## 2. Algorithmic claim boundary

Source: `S125_RAEF_v1/development_summary.csv`. RAEF-v1 matched top-document predictions exactly on 188 SciFact development claims for both checkpoints: 125/188 frozen and 149/188 weighted, 0 rescues, 0 regressions. **No demonstrated gain**. Do not describe RAEF as an effective novel fusion improvement. No external RAEF performance is established by S129.

## 3. Interpretation hierarchy

**Direct observations:** adaptation's SciFact historical development advantage; COVID-Fact external disadvantage; class-recall shift toward SUPPORTS; opposite direction of mean-versus-first aggregation across evaluation settings.

**Plausible explanations, not established mechanisms:** label construction, synthetic REFUTED examples, evidence selection/ordering, domain and source differences, class-prior/calibration shifts. These explanations cannot be promoted to causal findings without appropriate controls.

**Unsupported claims to remove:** generalizable positive transfer; universally harmful or helpful aggregation; causal effect of adaptation from historical unmatched settings; leakage-free guarantee; full retrieval performance on COVID-Fact; RAEF superiority; Q1 journal readiness.

## 4. Required source and methods disclosures

- Describe SciFact development annotation subset (188/300), with 112 unannotated claims excluded rather than labelled NEI.
- Keep S118 claim-first invalidated results out of primary tables; explain S120 correction and S121 100-pair reproduction.
- Record S129 evidence-first order, max length 192, checkpoint SHA-256, no fine-tuning and fixed policies.
- Note that 4,086 COVID-Fact rows include 4,080 unique normalized claims; report unique-claim sensitivity and cluster-aware intervals.
- Explain claim-level versus passage-level labels, source/evidence dependence and possible synthetic negatives.
- Preserve negative results and absence of RAEF improvement.

## 5. Decision and stopping rule

**Decision:** Do not submit the existing manuscript to *Information Fusion* as a novel superior fusion method. Stop exploratory model development. A descriptive negative-transfer paper is supportable, but *Information Fusion* competitiveness remains weak without a genuinely new conceptual or mechanistic contribution. No new experiment is authorized or implied by this document.

**Next editorial action:** reconcile the actual manuscript against this lock, rewrite claims and limitations, and choose a suitable venue. Do not deliver a final manuscript package until that manuscript-level reconciliation and references/figure verification are complete.
