---
name: kinetic-validity
description: Assess when fluid, Hall/extended-MHD, hybrid-PIC, or full kinetic/PIC descriptions are credible using scale separation, collisionality, distribution-function and observable requirements.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# Kinetic Validity

## Checks

Evaluate, when inputs allow:

- Debye length vs grid/system/gradient scale;
- electron and ion skin depths;
- electron and ion gyro-radii;
- plasma and cyclotron frequencies relative to target timescales;
- mean-free-path/Knudsen number and collision frequencies;
- drift/beam/non-Maxwellian evidence;
- temperature anisotropy;
- sheath or double-layer relevance;
- electron inertia and pressure-tensor relevance;
- whether the observable depends on particle distribution tails rather than moments.

Use `../../scripts/plasma_model_router.py` for screening quantities. Add project-specific closure tests where needed.

## Decision logic

- Fluid moments can be credible when kinetic scales are well separated and the required closure is justified for the observable.
- Hall/extended-MHD becomes a candidate when two-fluid/nonideal terms matter while a fluid description remains defensible.
- Hybrid-PIC is a candidate when kinetic ions matter but fluid electrons are adequate.
- Full PIC is a candidate when electron kinetics or distribution-level physics are required.

Never reduce this to one numerical threshold.

## Output

Known scales, missing scales, closure risks, candidate fidelity levels, and the minimum cross-model comparison needed.
