#!/usr/bin/env python3
"""Generate reproducible scalar Monte Carlo samples from a JSON specification.

Spec example:
{"B":{"dist":"normal","mean":2.0,"sd":0.1},"Te":{"dist":"uniform","low":8,"high":12}}
"""
import argparse,csv,json,math,random

def draw(rng,s):
 d=s["dist"].lower()
 if d=="normal": return rng.gauss(float(s["mean"]),float(s["sd"]))
 if d=="uniform": return rng.uniform(float(s["low"]),float(s["high"]))
 if d=="lognormal": return rng.lognormvariate(float(s["mu"]),float(s["sigma"]))
 if d=="triangular": return rng.triangular(float(s["low"]),float(s["high"]),float(s.get("mode",(s["low"]+s["high"])/2)))
 if d=="fixed": return float(s["value"])
 raise ValueError(f"unsupported distribution: {d}")

def main():
 p=argparse.ArgumentParser(); p.add_argument("spec"); p.add_argument("--n",type=int,required=True)
 p.add_argument("--seed",type=int,default=1); p.add_argument("--out",required=True); a=p.parse_args()
 if a.n<1: raise SystemExit("--n must be >= 1")
 spec=json.load(open(a.spec,encoding="utf-8")); rng=random.Random(a.seed); names=list(spec)
 with open(a.out,"w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=["sample_id","seed"]+names); w.writeheader()
  for i in range(a.n):
   row={"sample_id":i,"seed":a.seed}
   for name in names: row[name]=draw(rng,spec[name])
   w.writerow(row)
 meta={"seed":a.seed,"n":a.n,"spec":spec,"note":"Independent scalar sampling only; correlations require a validated correlated sampler."}
 open(a.out+".json","w",encoding="utf-8").write(json.dumps(meta,indent=2)+"\n")
 print(a.out)
if __name__=="__main__": main()
