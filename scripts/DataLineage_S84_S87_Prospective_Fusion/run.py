import argparse,csv,hashlib,json,statistics
from pathlib import Path
from collections import defaultdict,Counter
EXPECTED='b6724c628aebf5b112fe3c8ca74fb59eddfad1b0e1f899eaf9b300190a8dc41d'
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def sign(v):return 'SUPPORTS' if v>0 else 'REFUTES'
def mean(a):return sum(a)/len(a)
def median(a):return statistics.median(a)
def main():
 p=argparse.ArgumentParser();p.add_argument('--candidates',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 src=Path(a.candidates);digest=sha(src)
 if digest!=EXPECTED:raise SystemExit('STOP: candidate cache hash mismatch: '+digest)
 groups=defaultdict(lambda:defaultdict(list));labels={}
 with src.open(newline='',encoding='utf-8-sig') as f:
  for r in csv.DictReader(f):
   cid=r['claim_id'];rank=int(r['doc_rank']);m=float(r['p_entailment'])-float(r['p_contradiction']);groups[cid][rank].append(m)
   if r['annotation_status_DEV_ONLY'] in ('SUPPORTS','REFUTES'):labels[cid]=r['annotation_status_DEV_ONLY']
 out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
 rows=[]
 for cid,docs in groups.items():
  if set(docs)!=set(range(1,6)) or any(len(v)!=3 for v in docs.values()):raise SystemExit('STOP: unexpected 5-document x 3-sentence structure')
  margins=[mean(docs[i]) for i in range(1,6)]
  # Prospectively fixed, label-blind candidates: no parameter fitting or selection
  top=margins[0];equal=mean(margins)
  rankdiscount=sum(m/(i*i) for i,m in enumerate(margins,1))/sum(1/(i*i) for i in range(1,6))
  robustmedian=median(margins)
  # Conflict-aware decision policy: preserve top sign, abstain on sign disagreement AND weak top margin
  disagree=any(sign(x)!=sign(top) for x in margins[1:])
  guarded='ABSTAIN' if disagree and abs(top)<0.15 else sign(top)
  row={'claim_id':cid,'annotation_DEV_ONLY':labels.get(cid,'UNANNOTATED'),'top_margin':top,'equal_margin':equal,'rank_discount_margin':rankdiscount,'median_margin':robustmedian,'doc_disagreement':int(disagree),'top_pred':sign(top),'equal_pred':sign(equal),'rank_discount_pred':sign(rankdiscount),'median_pred':sign(robustmedian),'guarded_pred':guarded}
  rows.append(row)
 rows.sort(key=lambda r:int(r['claim_id']) if r['claim_id'].isdigit() else r['claim_id'])
 with (out/'s84_s87_claim_diagnostics.csv').open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 valid=[r for r in rows if r['annotation_DEV_ONLY']!='UNANNOTATED'];n=len(valid)
 stats={}
 for name in ['top','equal','rank_discount','median','guarded']:
  pred=name+'_pred';kept=[r for r in valid if r[pred]!='ABSTAIN'];correct=sum(r[pred]==r['annotation_DEV_ONLY'] for r in kept)
  stats[name]={'evaluated':len(kept),'coverage':len(kept)/n,'correct':correct,'selective_accuracy':correct/len(kept) if kept else None,'full_accuracy':correct/n if len(kept)==n else None,'abstentions':n-len(kept)}
 if stats['top']['correct']!=125 or n!=188:raise SystemExit('STOP: frozen parity failed')
 report={'phase':'S84-S87','status':'DEVELOPMENT_DIAGNOSTIC_ONLY_NOT_CONFIRMATORY','input_sha256':digest,'all_claims':len(rows),'annotated_claims':n,'frozen_top_parity':'PASS','policies':stats,'methodology':{'rank_discount':'sum(doc_margin/rank^2)/sum(1/rank^2); fixed exponent 2','median':'median of 5 document margins','guarded':'top-document sign, abstain only when another document has opposite sign and |top margin|<0.15; threshold illustrative and not validated'},'limits':['All policies evaluated on the same previously used development claims','No claim of unbiased improvement or post-hoc winner','Document IDs are grouping units, not verified source provenance','No source independence, trust or credibility measurements','No NEI prediction; ABSTAIN is not NEI','No test or external dataset accessed','Independent evaluator authorization remains pending']}
 (out/'s87_report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
 print(json.dumps({'parity':report['frozen_top_parity'],'claims':len(rows),'development_metrics':stats},indent=2))
if __name__=='__main__':main()
