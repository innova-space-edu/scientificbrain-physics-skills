---
name: picongpu-discover
description: Inspect the current PIConGPU installation/documentation for 2D3V/3D3V kinetic PIC, accelerator/HPC configuration, plugins, checkpointing, diagnostics, and openPMD output.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.1
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

## Source-grounded anchors

Validated against the inspected PIConGPU development tree:
- `docs/source/usage/plugins/openPMD.rst`
- `docs/source/usage/plugins/chargeConservation.rst`
- `docs/source/usage/plugins/energyFields.rst`
- `docs/source/usage/plugins/energyParticles.rst`
- `docs/source/usage/plugins/phaseSpace.rst`
- `docs/source/models/binary_collisions.rst`

The source exposes concrete openPMD controls such as `--openPMD.period`, `--openPMD.source`, `--openPMD.ext`, backend JSON/TOML configuration and data-preparation strategy. Energy plugins warn about reduction precision/non-determinism; treat them as diagnostics, not exact conservation proofs.

See `../../references/PICONGPU_SOURCE_MAP.md`.
