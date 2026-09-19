---
name: openpmd-analysis
description: Use openPMD as the canonical exchange layer for particle/mesh simulation data from WarpX/PIConGPU and adapters, preserving SI units, species, coordinates, iterations and provenance.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# openPMD Analysis

## Instructions

1. Verify that the producing solver was built/configured with openPMD support.
2. Inspect series, iterations, mesh records, particle species/components, units and geometry with the current openPMD API.
3. Keep native openPMD metadata intact; add ScientificBrain provenance externally or in compatible attributes rather than renaming physical records ad hoc.
4. Map fields/particles to `../../references/CANONICAL_PLASMA_DATA.md`.
5. For streaming workflows, confirm producer/consumer engine and lifecycle rather than assuming file-based access.
6. Normalize or resample only in derived datasets; preserve original data references.
7. Record filters/binning used when a solver outputs only selected particles or diagnostics.

## Output

Series inventory, field/species map, units, iteration/time map, conversion manifest and quality warnings.
