---
name: picongpu-run
description: Configure and run large-scale PIConGPU kinetic plasma simulations with explicit parameter provenance, GPU/MPI decomposition, diagnostics, checkpoints, openPMD output and convergence criteria.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# PIConGPU Run

## Instructions

1. Require a completed `picongpu-discover` report.
2. Define mesh, timestep, species/macroparticle initialization, boundaries, physics modules and diagnostic plugins using the current PIConGPU configuration model.
3. Plan accelerator/MPI decomposition and memory before launch; distinguish weak/strong scaling tests from physics production.
4. Enable checkpoint/restart and openPMD output for reproducibility and common analysis.
5. Track charge conservation, field/particle energy, particle counts, wall time and GPU memory.
6. Validate against a smaller WarpX/full-PIC overlap case or a documented benchmark where appropriate.
7. Perform mesh/time/particle-number convergence for the target observable.

## Output

Run configuration, resource layout, launch command/template, diagnostics, checkpoints, openPMD files and validation record.
