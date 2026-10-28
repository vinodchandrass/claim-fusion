import argparse,csv,hashlib,json,math
from pathlib import Path
from collections import Counter,defaultdict
EXPECTED='b6724c628aebf5b112fe3c8ca74fb59eddfad1b0e1f899eaf9b300190a8dc41d'
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def read(p):
 with open(p,encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(p,rows):
 if not rows:return
 with open(p,'w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def safeacc(rows,key):
 a=[r for r in rows if r['annotated']];return {'correct':sum(r[key] for r in a),'n':len(a),'accuracy':sum(r[key] for r in a)/len(a) if a else None}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--candidates',required=True);ap.add_argument('--output',required=True);a=ap.parse_args();p=Path(a.candidates);out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
 if sha(p)!=EXPECTED:raise SystemExit('STOP: frozen candidate SHA256 mismatch')
 records=read(p);groups=defaultdict(list)
 for r in records:groups[r['claim_id']].append(r)
 rows=[];docrows=[]
 for cid,items in sorted(groups.items(),key=lambda x:int(x[0])):
  docs=defaultdict(list)
  for r in items:docs[int(r['doc_rank'])].append(r)
  if len(docs)!=5 or any(len(v)!=3 for v in docs.values()):raise ValueError(f'Unexpected document structure: {cid}')
  doc=[]
  for rank,rr in sorted(docs.items()):
   ent=sum(float(z['p_entailment']) for z in rr)/3;con=sum(float(z['p_contradiction']) for z in rr)/3
   doc.append((rank,ent-con,ent,con))
  ann=items[0]['annotation_status_DEV_ONLY'];annotated=ann in ('SUPPORTS','REFUTES')
  top=doc[0][1];avg=sum(d[1] for d in doc)/5
  pred=lambda v:'SUPPORTS' if v>0 else 'REFUTES'
  topc=int(pred(top)==ann) if annotated else None;avgc=int(pred(avg)==ann) if annotated else None
  pos=sum(d[1]>0 for d in doc);neg=5-pos;disagree=pos>0 and neg>0
  maxabs=max(abs(d[1]) for d in doc)
  rows.append({'claim_id':cid,'annotation_DEV_ONLY':ann,'annotated':annotated,'top_correct_DEV_ONLY':topc,'equal_correct_DEV_ONLY':avgc,'top_margin':top,'equal_margin':avg,'sign_disagreement':disagree,'n_positive_documents':pos,'n_negative_documents':neg,'top_vs_equal_flip':pred(top)!=pred(avg),'max_absolute_doc_margin':maxabs,'top_doc_abs_margin':abs(top),'retrieved_gold_sentence_DEV_ONLY':any(z['gold_sentence_DEV_ONLY']=='1' for z in items),'top_doc_gold_sentence_DEV_ONLY':any(z['gold_sentence_DEV_ONLY']=='1' for z in docs[1])})
  for rank,margin,ent,con in doc:docrows.append({'claim_id':cid,'rank':rank,'margin':margin,'entailment_mean':ent,'contradiction_mean':con,'prediction':pred(margin),'annotation_DEV_ONLY':ann,'annotated':annotated,'correct_DEV_ONLY':int(pred(margin)==ann) if annotated else ''})
 write(out/'s80_claim_mechanism_diagnostics.csv',rows);write(out/'s81_rankwise_document_diagnostics.csv',docrows)
 arows=[r for r in rows if r['annotated']]
 strata={}
 for name,filterfn in [('disagreement',lambda r:r['sign_disagreement']),('no_disagreement',lambda r:not r['sign_disagreement']),('gold_sentence_retrieved',lambda r:r['retrieved_gold_sentence_DEV_ONLY']),('gold_sentence_missing',lambda r:not r['retrieved_gold_sentence_DEV_ONLY']),('top_doc_gold_found',lambda r:r['top_doc_gold_sentence_DEV_ONLY']),('top_doc_gold_missing',lambda r:not r['top_doc_gold_sentence_DEV_ONLY']),('SUPPORTS',lambda r:r['annotation_DEV_ONLY']=='SUPPORTS'),('REFUTES',lambda r:r['annotation_DEV_ONLY']=='REFUTES')]:
  rr=[r for r in arows if filterfn(r)];n=len(rr);strata[name]={'n':n,'top_correct':sum(r['top_correct_DEV_ONLY'] for r in rr),'equal_correct':sum(r['equal_correct_DEV_ONLY'] for r in rr),'top_accuracy':sum(r['top_correct_DEV_ONLY'] for r in rr)/n if n else None,'equal_accuracy':sum(r['equal_correct_DEV_ONLY'] for r in rr)/n if n else None,'paired_rescues_equal':sum(r['equal_correct_DEV_ONLY']==1 and r['top_correct_DEV_ONLY']==0 for r in rr),'paired_regressions_equal':sum(r['equal_correct_DEV_ONLY']==0 and r['top_correct_DEV_ONLY']==1 for r in rr)}
 rankwise={str(i):{'n':sum(r['rank']==i and r['annotated'] for r in docrows),'correct':sum(r['rank']==i and r['annotated'] and r['correct_DEV_ONLY']==1 for r in docrows)} for i in range(1,6)}
 report={'phase':'S80-S83','status':'EXPLORATORY_MECHANISM_DIAGNOSTIC_NOT_VALIDATION','input_sha256':sha(p),'claims':len(rows),'annotated_binary_claims':len(arows),'candidate_sentences':len(records),'top_policy':safeacc(rows,'top_correct_DEV_ONLY'),'equal_policy':safeacc(rows,'equal_correct_DEV_ONLY'),'cross_document_sign_disagreement_all':sum(r['sign_disagreement'] for r in rows),'cross_document_sign_disagreement_annotated':sum(r['sign_disagreement'] for r in arows),'top_equal_prediction_flips_annotated':sum(r['top_vs_equal_flip'] for r in arows),'strata':strata,'rankwise_individual_doc_binary_accuracy':rankwise,'scientific_interpretation':'Descriptive decomposition of previously observed development results. Does not identify causality or establish provenance independence.','guardrails':['No new policy selected or tuned','No new NLI inference','No sealed test access','Document identifiers do not certify independent sources','No novel fusion advantage established','No generalization estimate','Gold sentence flags used only for post hoc development diagnostics']}
 (out/'s83_mechanism_report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
 print('S80-S83 COMPLETE; dev-only; top:',report['top_policy'],'equal:',report['equal_policy'])
if __name__=='__main__':main()
