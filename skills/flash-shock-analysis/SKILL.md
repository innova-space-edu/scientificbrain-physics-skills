---
name: flash-shock-analysis
description: Measure shock-front position, speed, thickness, jumps, and plasma/MHD observables from FLASH outputs using an explicit operational definition and uncertainty/convergence checks.
license: Apache-2.0
metadata:
  author: Innova Space Education / ScientificBrain
  version: 0.1.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# FLASH Shock Analysis

## Instructions

1. Define the shock observable and front detector before measuring: maximum density/pressure gradient, threshold crossing, fitted transition, or tracked discontinuity. State why it matches the problem.
2. Extract profiles normal to the shock. In multidimensional runs decide whether to track a local front, angular/planar average, or fitted surface.
3. Compute `x_s(t)`/`R_s(t)` then speed using a numerically stable derivative or fit; propagate temporal/spatial resolution into uncertainty.
4. Define `L_shock` explicitly (10–90% width, fitted scale length, gradient-based width, etc.). Never compare thicknesses from different definitions without conversion/context.
5. Measure upstream/downstream fields and relevant Mach/beta/current diagnostics. For magnetized-shock studies retain `n_e`, `T_e`, `B`, `J`, shock speed and thickness, plus nonideal electric-field terms when available.
6. Repeat key observables across resolution/model variants and route to `flash-validation`.

## Output

Method, front trajectory, speed, thickness, jump table, uncertainty/resolution notes, and machine-readable results.
