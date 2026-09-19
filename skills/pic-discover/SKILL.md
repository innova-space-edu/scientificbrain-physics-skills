---
name: pic-discover
description: Discover installed/current PIC and hybrid solvers, their dimensionality, field solvers, collision models, diagnostics, output formats, GPU/MPI capabilities, examples, and version-specific constraints.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# PIC Discover

Inspect live installations or canonical upstream documentation before configuring PIC.

## Discover

For each available solver report:

- exact version/commit;
- supported dimensionality and geometry;
- electromagnetic/electrostatic/hybrid modes relevant to the task;
- particle pushers/current deposition/field solver choices;
- collisions and ionization relevant to the problem;
- boundary conditions;
- diagnostics and checkpoint/restart;
- openPMD or other output support;
- CPU/GPU and MPI/multi-node capabilities;
- closest validated example/benchmark.

Current toolkit targets WarpX, PIConGPU and EDIPIC-2D. Do not assume feature parity between them.

## Output

A version-grounded capability matrix and a shortlist for the requested physics.
