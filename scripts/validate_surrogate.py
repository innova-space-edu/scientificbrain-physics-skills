#!/usr/bin/env python3
import argparse, json, numpy as np

def stats(y,p):
 e=p-y; rmse=float(np.sqrt(np.mean(e*e))); scale=float(np.sqrt(np.mean(y*y)))
 return {'rmse':rmse,'nrmse_l2':rmse/scale if scale else None,'max_abs':float(np.max(np.abs(e)))}

def dd(a,axis,h): return np.gradient(a,h,axis=axis,edge_order=1)

def main():
 p=argparse.ArgumentParser(); p.add_argument('truth'); p.add_argument('pred'); p.add_argument('--fields',nargs='+',required=True); p.add_argument('--spacing',nargs='*',type=float); p.add_argument('--json-out'); a=p.parse_args()
 t=np.load(a.truth); q=np.load(a.pred); out={'fields':{}}
 for f in a.fields:
  if f not in t or f not in q: raise SystemExit(f'missing field {f}')
  if t[f].shape!=q[f].shape: raise SystemExit(f'shape mismatch {f}: {t[f].shape} vs {q[f].shape}')
  out['fields'][f]=stats(t[f],q[f])
 if all(f in q for f in ('magx','magy')) and a.spacing:
  b=[q['magx'],q['magy']]; hs=a.spacing
  div=dd(b[0],-1,hs[-1])+dd(b[1],-2,hs[-2])
  if 'magz' in q and len(hs)>=3 and q['magz'].ndim>=3: div=div+dd(q['magz'],-3,hs[-3])
  out['pred_divB_rms']=float(np.sqrt(np.mean(div*div)))
 s=json.dumps(out,indent=2); print(s)
 if a.json_out: open(a.json_out,'w').write(s+'\n')
if __name__=='__main__': main()
