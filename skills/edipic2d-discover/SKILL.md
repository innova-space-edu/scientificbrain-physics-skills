---
name: edipic2d-discover
description: Inspect EDIPIC-2D for low-temperature 2D particle-in-cell applications, current build dependencies, input parameters, diagnostics, output analysis, and problem suitability.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.1
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

## Source-grounded anchors

Validated against EDIPIC-2D main:
- `Instructions/installing_edipic2d.md`
- `Instructions/running_edipic2d.md`
- `Doc/EDIPIC2D_input_data_description_*.pdf`
- `Doc/EDIPIC2D_output_data_description_*.pdf`
- complete `input_data_*/` examples.

The inspected build requires Fortran, MPI, PETSc, HYPRE and BLAS/LAPACK. The solver executable is built under `src` and run directories contain structured `init_*.dat` files plus `petsc.rc`. Prefer cloning/modifying a complete example directory.

See `../../references/EDIPIC2D_SOURCE_MAP.md`.
