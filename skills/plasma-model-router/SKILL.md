---
name: plasma-model-router
description: Route plasma problems across FLASH MHD/Extended-MHD, WarpX Hybrid-PIC/full PIC, PIConGPU, EDIPIC-2D, and Geant4 by physical scales, observable, geometry, and computational constraints.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# Plasma Model Router

Use this skill before selecting a plasma solver.

## Routing sequence

1. Define the observable and required spatial/temporal resolution.
2. Run `plasma-regime`, `plasma-dimensionless`, and `kinetic-validity`.
3. Compare system/gradient scales with Debye length, electron/ion skin depths, electron/ion gyro-radii, mean free path, plasma/cyclotron periods, and collision times when available.
4. Build a **model hierarchy**, not a single unexplained choice:
   - fluid closure plausible → FLASH ideal/resistive/Hall/Extended-MHD;
   - ion kinetics relevant but electron kinetics/electromagnetic light waves not central → inspect WarpX Hybrid-PIC;
   - electron kinetics, sheath/distribution functions, microinstabilities, or full kinetic phase space required → full PIC;
   - large GPU/HPC full-PIC campaign → compare WarpX and PIConGPU;
   - low-temperature 2D electrostatic discharge problem → inspect EDIPIC-2D;
   - particle passage through matter/radiation transport → Geant4, not a plasma PIC solver.
5. Estimate cost and validation cases before escalating fidelity.
6. When two adjacent models are plausible, require overlap simulations and compare the target observable.

## Output

Return candidate hierarchy, rejected models with reasons, scale evidence, required benchmarks, expected data format, compute constraints, and unresolved quantities.

## Guardrails

A scale ratio is evidence, not a universal cutoff. Do not claim full PIC is intrinsically more correct for every observable. Do not route radiation transport through a plasma solver merely because particles are present.
