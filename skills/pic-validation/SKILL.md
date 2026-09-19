---
name: pic-validation
description: Validate PIC/hybrid simulations using charge/current conservation, energy balance, numerical-heating/noise tests, particle/mesh/time convergence, benchmark overlap, and distribution-level diagnostics.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# PIC / Hybrid Validation

## Minimum checks

- mesh and timestep convergence for the target observable;
- particles-per-cell/macroparticle convergence and statistical noise;
- charge conservation/Gauss-law diagnostics supported by the solver;
- total/field/particle energy accounting as applicable;
- numerical heating and distribution-function distortion;
- boundary particle/energy fluxes;
- collision/reaction count consistency when MCC/DSMC is active;
- checkpoint/restart reproducibility;
- comparison to a documented benchmark;
- overlap comparison with adjacent fidelity (FLASH ↔ Hybrid or Hybrid ↔ full PIC) when possible.

Use a quantitative acceptance matrix; do not declare validity from visually plausible fields.

## Output

Validation matrix, convergence plots/statistics, failed criteria, accepted observables and domain of validity.
