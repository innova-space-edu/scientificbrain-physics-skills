---
name: warpx-mcc-dsmc
description: Configure, validate, and distinguish WarpX Monte Carlo Collisions (MCC) with neutral backgrounds from DSMC particle-particle stochastic collisions and required cross-section data.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# WarpX MCC / DSMC

WarpX documents MCC for electron/ion collisions with a neutral background and DSMC for stochastic collisions between simulated particle populations.

## Instructions

1. Identify the physical collision pairs and whether the neutral/background must be dynamically represented.
2. Use MCC for the supported background-gas collision formulation when appropriate; use DSMC when both colliding populations must be represented as particles.
3. Validate cross-section source, energy range, interpolation and units. Preserve the exact cross-section files/hashes in provenance.
4. Check collision frequency against timestep/supercycling assumptions.
5. Benchmark against an official/known discharge or collision case before research production.
6. Track reaction/collision counts, particle/energy balance and distribution changes.

## Output

Collision model, species pairs, cross-section provenance, timestep relation, validation benchmark and diagnostics.
