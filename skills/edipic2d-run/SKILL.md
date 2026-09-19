---
name: edipic2d-run
description: Prepare, execute, and validate EDIPIC-2D low-temperature plasma simulations with reproducible input files, dependency provenance, particle/noise checks, and canonical output conversion.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# EDIPIC-2D Run

## Instructions

- Require a suitability report from `edipic2d-discover`.
- Start from a verified example/input configuration.
- Record geometry, mesh, timestep, species, distribution initialization, boundary/electrode conditions, collisions if supported/configured, and run length.
- Preserve PETSc/HYPRE/MPI/compiler and EDIPIC commit provenance.
- Check statistical noise, particle counts, field convergence, energy/current balance and steady/periodic behavior as appropriate.
- Compare against WarpX/another solver only in an overlapping regime and with matched physical assumptions.
- Convert outputs to the canonical plasma data contract with explicit units and coordinates.

## Output

Reproducible run bundle, diagnostic summary, validation evidence and converted-data plan.
