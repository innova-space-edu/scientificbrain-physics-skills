#!/usr/bin/env python3
import argparse,csv,json,math,statistics
def q(xs,p):
 ys=sorted(xs); x=(len(ys)-1)*p; lo=int(math.floor(x)); hi=int(math.ceil(x))
 return ys[lo] if lo==hi else ys[lo]*(hi-x)+ys[hi]*(x-lo)
def main():
 p=argparse.ArgumentParser(); p.add_argument("csv"); p.add_argument("--column",required=True); a=p.parse_args()
 vals=[]
 with open(a.csv,newline="",encoding="utf-8") as f:
  for r in csv.DictReader(f):
   try: vals.append(float(r[a.column]))
   except (ValueError,KeyError): pass
 if not vals: raise SystemExit("no numeric samples")
 out={"column":a.column,"n":len(vals),"mean":statistics.fmean(vals),"sd":statistics.stdev(vals) if len(vals)>1 else 0.0,
      "q025":q(vals,.025),"median":q(vals,.5),"q975":q(vals,.975),"min":min(vals),"max":max(vals)}
 print(json.dumps(out,indent=2))
if __name__=="__main__": main()
