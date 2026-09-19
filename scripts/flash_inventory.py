#!/usr/bin/env python3
import argparse, json, os
from pathlib import Path

CHECKS={
 'usm_mhd_config':'source/physics/Hydro/HydroMain/unsplit/MHD_StaggeredMesh/Config',
 'magnetic_resistivity':'source/physics/materialProperties/MagneticResistivity',
 'hall_whistler':'source/Simulation/SimulationMain/magnetoHD/HallWhistlerWaves',
 'hall_drift':'source/Simulation/SimulationMain/magnetoHD/HallDriftWaves',
 'gem_challenge':'source/Simulation/SimulationMain/magnetoHD/GEM_challenge',
 'resistive':'source/Simulation/SimulationMain/magnetoHD/Resistive',
 'orszag_tang':'source/Simulation/SimulationMain/magnetoHD/OrszagTang',
 'brio_wu':'source/Simulation/SimulationMain/magnetoHD/BrioWu',
 'biermann_cartesian':'source/Simulation/SimulationMain/magnetoHD/2DCartesianBiermannTest',
 'aniso_cond':'source/Simulation/SimulationMain/magnetoHD/AnisoCond',
 'zpinch':'source/Simulation/SimulationMain/magnetoHD/ZPinch',
}
SWITCHES=['use_Hall','use_Biermann','use_Biermann1T','use_Biermann3T','use_Nernst','use_Seebeck','use_CrossFIeld','useCrossMagRes','hallVelocity']

def main():
 p=argparse.ArgumentParser(); p.add_argument('--flash-root',default=os.getenv('FLASH_ROOT')); p.add_argument('--json',action='store_true'); a=p.parse_args()
 if not a.flash_root: raise SystemExit('set --flash-root or FLASH_ROOT')
 root=Path(a.flash_root).resolve(); release=(root/'RELEASE').read_text(errors='ignore').splitlines()[0] if (root/'RELEASE').exists() else 'unknown'
 found={k:(root/v).exists() for k,v in CHECKS.items()}
 cfg=root/CHECKS['usm_mhd_config']; txt=cfg.read_text(errors='ignore') if cfg.exists() else ''
 switches={s:(s in txt) for s in SWITCHES}
 out={'flash_root':str(root),'release':release,'paths':found,'extended_mhd_switches':switches}
 if a.json: print(json.dumps(out,indent=2))
 else:
  print('FLASH:',release); print('root:',root)
  for k,v in found.items(): print(f'{k}: {"FOUND" if v else "missing"}')
  print('Extended-MHD switches in live USM Config:')
  for k,v in switches.items(): print(f'  {k}: {v}')
if __name__=='__main__': main()
