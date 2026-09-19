#!/usr/bin/env python3
"""Export selected FLASH/yt fields to a uniform covering-grid NPZ.
Requires yt and numpy. Use for regular-grid PhysicsNeMo experiments.
"""
import argparse, json
from pathlib import Path
import numpy as np
import yt

def resolve(ds,name):
 matches=[f for f in ds.field_list+ds.derived_field_list if f[1].strip()==name.strip()]
 if not matches: raise KeyError(f'field {name!r} not found')
 return matches[0]

def main():
 p=argparse.ArgumentParser(); p.add_argument('plotfile'); p.add_argument('--fields',nargs='+',required=True); p.add_argument('--level',type=int,default=0); p.add_argument('--out',required=True); a=p.parse_args()
 ds=yt.load(a.plotfile); dims=np.array(ds.domain_dimensions,dtype=int)*(2**a.level)
 cg=ds.covering_grid(level=a.level,left_edge=ds.domain_left_edge,dims=dims)
 arrays={}; fmap={}
 for n in a.fields:
  f=resolve(ds,n); arrays[n]=np.asarray(cg[f]); fmap[n]=list(f)
 arrays['time']=np.asarray(float(ds.current_time)); arrays['left_edge']=np.asarray(ds.domain_left_edge); arrays['right_edge']=np.asarray(ds.domain_right_edge)
 np.savez_compressed(a.out,**arrays)
 meta={'source':str(Path(a.plotfile).resolve()),'level':a.level,'dims':dims.tolist(),'fields':fmap,'time':str(ds.current_time),'geometry':str(ds.geometry)}
 Path(a.out+'.json').write_text(json.dumps(meta,indent=2)+'\n')
 print(a.out)
if __name__=='__main__': main()
