---
name: warpx-discover
description: Inspect the live WarpX installation/documentation for full PIC, Hybrid-PIC, MCC/DSMC, geometry, solver, GPU/MPI, diagnostics, PICMI, and openPMD capabilities needed by a specific plasma problem.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# WarpX Discover

## Instructions

1. Identify the exact WarpX release/commit and installation mode.
2. Inspect current examples and parameters for the requested geometry and physics.
3. Explicitly determine whether the task uses:
   - electromagnetic/electrostatic PIC;
   - Ampere/Ohm-law Hybrid-PIC;
   - MCC;
   - DSMC;
   - other collision/ionization modules.
4. Verify diagnostics, checkpoint/restart, openPMD output and PICMI/Python support in the installed version.
5. Record accelerator backend, MPI environment and precision/build options.
6. Select one or two closest official examples as validation anchors.

WarpX currently documents Hybrid-PIC and MCC/DSMC workflows, but exact parameters must be discovered from the installed/current release.

## Output

Version, enabled build features, relevant examples, required runtime parameters, expected outputs and unresolved dependencies.
