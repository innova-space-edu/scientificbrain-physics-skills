---
name: plasma-regime
description: Route a plasma problem to the physical models that need to be tested before compute — ideal/resistive/extended MHD versus hybrid/kinetic — using explicit scale and closure checks rather than intuition.
license: Apache-2.0
metadata:
  author: Innova Space Education / ScientificBrain
  version: 0.1.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# Plasma Regime Selection

Use this skill before selecting a solver/model for a new plasma problem.

## Instructions

1. Collect density/composition, electron and ion temperature, magnetic field, characteristic length and time/velocity scales, geometry, expected gradients, collisional information, and target observable.
2. Invoke or reproduce the calculations in `../../scripts/plasma_regime.py`. At minimum inspect `d_i/L`, gyro-radius ratios, plasma beta, Alfvén Mach number, and magnetic Reynolds/Lundquist numbers when resistivity is known. Add Knudsen/collision checks when data permit.
3. Treat scale ratios as screening evidence, not universal thresholds. State assumptions and uncertainty.
4. If fluid closure is plausible, identify which hierarchy must be compared: ideal MHD → resistive MHD → Hall/extended-MHD. If kinetic scales/collisionality undermine closure, flag that FLASH-MHD may be insufficient and route future work to a hybrid/PIC solver instead of forcing a FLASH result.
5. Tie the model choice to the observable. A bulk shock position may converge under a fluid model even when microstructure does not.
6. Record the regime assessment in the run manifest so later surrogate data retain the physics assumptions that generated them.

## Output

Return: known inputs and units; computed scale ratios; candidate model hierarchy; missing quantities that block a stronger conclusion; and the minimum comparison simulations needed to test model adequacy.

## Guardrails

Do not claim Hall/kinetic irrelevance from `d_i/L` alone. Do not infer collisionality without collision/mfp information. Do not choose a more complex model solely because it is available.
