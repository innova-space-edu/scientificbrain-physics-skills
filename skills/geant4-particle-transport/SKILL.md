---
name: geant4-particle-transport
description: Route and prepare Geant4 Monte Carlo simulations for particle passage through matter, radiation transport, detector response, shielding, and space-radiation problems outside plasma-PIC scope.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.1
  tags:
    - physics
    - plasma
    - scientificbrain
---

# Geant4 Particle Transport

Use Geant4 when the primary problem is stochastic transport/interactions of particles through matter rather than self-consistent plasma kinetics.

## Instructions

1. Define particles, source spectrum/angular distribution, materials, geometry, scoring quantities and required physics processes.
2. Discover the current Geant4 release and physics-list guidance from official documentation.
3. Select a reference physics list or custom process set based on the energy/domain; document why.
4. Define production cuts, step controls and scoring volumes with convergence checks.
5. Preserve random seeds, Geant4 version, geometry/material definitions and physics list.
6. Validate against known benchmark/data where available and report statistical confidence intervals.
7. Export scored quantities into the canonical data/provenance layer, not as undocumented histograms.

## Output

Transport model, source/material/geometry specification, physics-list rationale, scoring plan, sample-count/statistical criteria and provenance.

## Source-grounded anchors

Validated against Geant4 v11.4.2:
- `examples/basic/B1/` for application structure, materials, primary source and scoring;
- `examples/advanced/gorad/` for spacecraft/radiation-analysis workflows;
- `examples/extended/electromagnetic/TestEm0/` and `TestEm1/` for EM validation patterns.

Do not copy B1's QBBC list or any example physics list into a new problem without a domain-specific justification. Preserve Geant4 datasets, physics list, cuts, seed policy, geometry/material and scorer definitions.

See `../../references/GEANT4_SOURCE_MAP.md`.
