---
name: warpx-pic
description: Configure and validate WarpX full kinetic PIC for plasma problems requiring electron/ion phase-space physics, with explicit numerical heating, noise, resolution and convergence controls.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# WarpX Full PIC

## Instructions

1. Establish why full kinetics are required.
2. Resolve the physically required Debye/skin/gyro/time scales for the target observable and field solver.
3. Choose particles-per-cell, particle shape, filtering/smoothing and timestep with a convergence/noise plan.
4. Record initialization distributions, species weights, boundaries, collisions/ionization and diagnostics.
5. Monitor numerical heating, charge conservation, energy balance, particle loss and field noise.
6. Use openPMD output for canonical particle/field exchange when practical.
7. Require particle-number and mesh/timestep convergence for the observable; one expensive run is not validation.

## Output

Numerical design, input, convergence matrix, diagnostic set and validity limitations.
