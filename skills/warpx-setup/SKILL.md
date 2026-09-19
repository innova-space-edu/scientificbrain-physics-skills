---
name: warpx-setup
description: Build reproducible WarpX input/PICMI configurations with explicit geometry, resolution, timestep, particles-per-cell, boundaries, field solver, collisions, diagnostics, restart, and provenance.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# WarpX Setup

## Instructions

1. Start from `warpx-discover` and a validated example closest to the physical regime.
2. Define geometry, domain, mesh, AMR if used, timestep, field solver, species, particle initialization, particles-per-cell, shape order, pusher/deposition choices, boundaries and diagnostics.
3. Demonstrate that mesh/timestep resolve the scales required by the chosen model; do not automatically force electron-scale resolution for Hybrid-PIC.
4. Add collisions only through `warpx-mcc-dsmc` when justified.
5. Configure openPMD output when the campaign will feed the canonical data layer.
6. Preserve the full input/PICMI script, WarpX version, build configuration and launch command.
7. Validate a small case before scaling.

## Output

Reproducible configuration, scale-resolution table, launch plan, output plan and validation benchmark.
