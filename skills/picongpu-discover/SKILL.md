---
name: picongpu-discover
description: Inspect the current PIConGPU installation/documentation for 2D3V/3D3V kinetic PIC, accelerator/HPC configuration, plugins, checkpointing, diagnostics, and openPMD output.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# PIConGPU Discover

## Instructions

- Resolve exact release/commit and build environment.
- Inspect the current parameter/template system rather than assuming syntax.
- Verify dimensionality, species, field solver/pusher configuration, collisions/ionization needed by the task, accelerator backend and MPI layout.
- Inventory plugins relevant to validation: openPMD, energy fields/particles, charge conservation, histograms/binning, particle counts, checkpoints and any project-specific diagnostics.
- Verify openPMD API availability and output configuration.
- Choose a documented example or benchmark closest to the requested physics.

## Output

Version-grounded capability/build matrix, relevant plugins, output plan, benchmark and execution constraints.
