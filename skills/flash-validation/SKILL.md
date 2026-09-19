---
name: flash-validation
description: Validate FLASH plasma/MHD simulations with numerical convergence, benchmark tests, divergence/conservation diagnostics, solver/timestep checks, and observable-level acceptance criteria.
license: Apache-2.0
metadata:
  author: Innova Space Education / ScientificBrain
  version: 0.1.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# FLASH Validation

## Instructions

1. Identify the claims the simulation must support; validation targets observables, not merely code completion.
2. Check run integrity: clean completion/restart lineage, stable timestep behavior, no unresolved solver warnings, and expected output cadence.
3. Perform a resolution study for the main observable and compare grid/AMR choices.
4. Inspect magnetic divergence error with a stated normalization. Check mass/momentum/energy conservation only to the extent expected under boundaries and source/transport terms.
5. Run or reproduce a relevant canonical benchmark when introducing a solver/physics configuration (e.g. Brio-Wu, Orszag-Tang, Hall waves, resistive/current-sheet/Biermann cases as appropriate).
6. Distinguish physical transport coefficients from numerical diffusion by parameter/resolution comparison.
7. Use `../../references/PHYSICS_VALIDATION.md` for the shared checklist and define explicit pass/fail tolerances for the project rather than inventing universal thresholds.

## Output

Validation matrix, numerical issues, convergence evidence, benchmark comparison, accepted/rejected observables, and remaining uncertainty.
