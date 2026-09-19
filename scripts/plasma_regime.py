#!/usr/bin/env python3
"""Compute screening-scale plasma/MHD quantities in SI units.

This script supports model-selection discussion; it does not declare a fluid or
kinetic model valid by itself. Threshold labels are deliberately qualitative.
"""
import argparse, json, math

MU0 = 4e-7 * math.pi
EPS0 = 8.8541878128e-12
C = 299792458.0
E = 1.602176634e-19
ME = 9.1093837015e-31
MP = 1.67262192369e-27

def band(x):
    if x is None: return "unknown"
    if x < 1e-2: return "small compared with system scale"
    if x < 1e-1: return "transitional screening range"
    return "not small compared with system scale"

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--ne', type=float, required=True, help='electron density [m^-3]')
    p.add_argument('--B', type=float, required=True, help='magnetic field [T]')
    p.add_argument('--Te-ev', dest='Te', type=float, required=True)
    p.add_argument('--Ti-ev', dest='Ti', type=float, required=True)
    p.add_argument('--A', type=float, default=1.0, help='ion mass number')
    p.add_argument('--Z', type=float, default=1.0, help='mean ion charge')
    p.add_argument('--L', type=float, required=True, help='system/gradient scale [m]')
    p.add_argument('--U', type=float, required=True, help='characteristic flow speed [m/s]')
    p.add_argument('--eta-ohm-m', type=float, default=None, help='electrical resistivity [ohm m]')
    p.add_argument('--mfp', type=float, default=None, help='optional mean free path [m]')
    p.add_argument('--json', action='store_true')
    a=p.parse_args()
    if min(a.ne,a.B,a.Te,a.Ti,a.A,a.Z,a.L,a.U) <= 0:
        raise SystemExit('all required physical magnitudes must be > 0')
    ni=a.ne/a.Z; mi=a.A*MP; rho=ni*mi
    wpi=math.sqrt(ni*(a.Z*E)**2/(EPS0*mi)); di=C/wpi
    wci=a.Z*E*a.B/mi; wce=E*a.B/ME
    vthi=math.sqrt(2*E*a.Ti/mi); vthe=math.sqrt(2*E*a.Te/ME)
    rhoi=vthi/wci; rhoe=vthe/wce
    va=a.B/math.sqrt(MU0*rho)
    pth=a.ne*E*a.Te + ni*E*a.Ti
    beta=2*MU0*pth/(a.B*a.B)
    out={
      'ion_density_m-3':ni,'mass_density_kg_m-3':rho,
      'ion_inertial_length_m':di,'di_over_L':di/a.L,'di_over_L_screen':band(di/a.L),
      'ion_gyro_radius_m':rhoi,'rho_i_over_L':rhoi/a.L,'rho_i_over_L_screen':band(rhoi/a.L),
      'electron_gyro_radius_m':rhoe,'rho_e_over_L':rhoe/a.L,
      'alfven_speed_m_s':va,'alfven_mach':a.U/va,'plasma_beta':beta,
      'omega_ci_rad_s':wci,'omega_ce_rad_s':wce,
    }
    if a.eta_ohm_m is not None:
        out['magnetic_reynolds']=MU0*a.U*a.L/a.eta_ohm_m
        out['lundquist']=MU0*va*a.L/a.eta_ohm_m
    if a.mfp is not None:
        out['knudsen']=a.mfp/a.L
        out['knudsen_screen']=band(a.mfp/a.L)
    out['interpretation']='Screening only: model validity requires collision, closure, geometry, timescale, and benchmark checks.'
    if a.json: print(json.dumps(out,indent=2))
    else:
        for k,v in out.items(): print(f'{k}: {v}')
if __name__=='__main__': main()
