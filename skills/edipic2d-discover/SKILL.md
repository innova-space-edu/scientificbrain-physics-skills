---
name: edipic2d-discover
description: Inspect EDIPIC-2D for low-temperature 2D particle-in-cell applications, current build dependencies, input parameters, diagnostics, output analysis, and problem suitability.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# EDIPIC-2D Discover

EDIPIC-2D is a 2D PIC code developed for low-temperature plasma applications.

## Instructions

1. Resolve the exact upstream commit/local version.
2. Read the repository installation, input-parameter, execution and analysis documentation.
3. Verify the local PETSc/HYPRE/MPI/compiler combination; do not assume old recommended dependency versions are mandatory for a newer checkout without testing.
4. Determine whether the requested discharge/sheath/electrostatic problem fits EDIPIC-2D's model and available diagnostics.
5. Record output format and conversion needs for the canonical data layer.

## Output

Suitability assessment, version/dependencies, relevant inputs, diagnostics and adapter requirements.
