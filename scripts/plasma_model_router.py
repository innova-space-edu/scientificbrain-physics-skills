#!/usr/bin/env python3
"""Screen candidate plasma model hierarchy from physical scale ratios.

This is decision support, not a universal validity theorem.
"""
import argparse, json, math
MU0=4e-7*math.pi; EPS0=8.8541878128e-12; C=299792458.0
E=1.602176634e-19; ME=9.1093837015e-31; MP=1.67262192369e-27

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--ne",type=float,required=True); p.add_argument("--B",type=float,required=True)
 p.add_argument("--Te-ev",dest="Te",type=float,required=True); p.add_argument("--Ti-ev",dest="Ti",type=float,required=True)
 p.add_argument("--L",type=float,required=True); p.add_argument("--U",type=float,required=True)
 p.add_argument("--A",type=float,default=1.0); p.add_argument("--Z",type=float,default=1.0)
 p.add_argument("--mfp",type=float); p.add_argument("--needs-electron-kinetics",action="store_true")
 p.add_argument("--low-temperature-2d",action="store_true"); p.add_argument("--particle-through-matter",action="store_true")
 a=p.parse_args()
 if min(a.ne,a.B,a.Te,a.Ti,a.L,a.U,a.A,a.Z)<=0: raise SystemExit("required magnitudes must be > 0")
 ni=a.ne/a.Z; mi=a.A*MP
 wpe=math.sqrt(a.ne*E*E/(EPS0*ME)); wpi=math.sqrt(ni*(a.Z*E)**2/(EPS0*mi))
 de=C/wpe; di=C/wpi
 lde=math.sqrt(EPS0*(a.Te*E)/(a.ne*E*E))
 wce=E*a.B/ME; wci=a.Z*E*a.B/mi
 rhoe=math.sqrt(2*E*a.Te/ME)/wce; rhoi=math.sqrt(2*E*a.Ti/mi)/wci
 ratios={"lambdaD/L":lde/a.L,"de/L":de/a.L,"di/L":di/a.L,"rhoe/L":rhoe/a.L,"rhoi/L":rhoi/a.L}
 if a.mfp: ratios["Kn"]=a.mfp/a.L
 candidates=[]
 if a.particle_through_matter: candidates.append("Geant4 transport branch")
 else:
  candidates.append("FLASH fluid/Extended-MHD baseline")
  if ratios["di/L"]>=1e-2 or ratios["rhoi/L"]>=1e-2: candidates.append("WarpX Hybrid-PIC overlap test")
  if a.needs_electron_kinetics or ratios["de/L"]>=1e-2 or ratios["lambdaD/L"]>=1e-2:
   candidates.append("Full PIC: WarpX; compare PIConGPU for HPC-scale campaigns")
  if a.low_temperature_2d: candidates.append("EDIPIC-2D suitability check")
 out={"ratios":ratios,"candidate_hierarchy":candidates,
      "warning":"Screening only. Thresholds are heuristic; closure, collisionality, observable and benchmarks decide validity."}
 print(json.dumps(out,indent=2))
if __name__=="__main__": main()
