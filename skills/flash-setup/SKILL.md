---
name: flash-setup
description: Construct and preflight reproducible FLASH setup/build configurations for plasma, MHD, resistive, Hall, or extended-MHD simulations while grounding every flag in the live FLASH tree.
license: Apache-2.0
metadata:
  author: Innova Space Education / ScientificBrain
  version: 0.1.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# FLASH Setup

Use after the physical regime and target benchmark are defined.

## Instructions

1. Invoke `flash-discover` logic first. Resolve FLASH version, site, compiler/MPI/HDF5 availability, grid backend, dimensionality, geometry, block size, species/EOS/material models, and target simulation unit.
2. Start from the closest verified setup command embedded in the chosen FLASH example and change only justified options. Never fabricate setup shortcuts.
3. Prefer unsplit staggered-mesh MHD for the Extended-MHD workflows covered by this toolkit; verify the required `Config` dependencies.
4. Run setup as a dry/preflight step where supported, preserve the complete command, generated setup/runtime defaults, compiler/site configuration, and FLASH revision.
5. Build in a dedicated object directory. Do not alter the source distribution to make one campaign work unless the change is intentional, version-controlled, and documented.
6. Before execution verify that the generated object configuration contains the requested physics units and runtime parameters.

## Output

Provide the exact setup command, build command, assumptions, expected object directory, dependency checks, and a reproducibility record. Do not launch an expensive run unless requested by the parent workflow.
