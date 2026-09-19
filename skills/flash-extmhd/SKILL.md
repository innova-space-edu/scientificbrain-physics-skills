---
name: flash-extmhd
description: Configure and audit FLASH 4.8 resistive and Braginskii-style extended-MHD options including Hall, Biermann, Nernst, Seebeck, cross-field and anisotropic magnetic resistivity in the unsplit staggered-mesh solver.
license: Apache-2.0
metadata:
  author: Innova Space Education / ScientificBrain
  version: 0.1.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# FLASH Extended-MHD

This skill is tightly grounded to a live FLASH tree. Use `flash-discover` before changing parameters.

## Instructions

1. Establish the physical reason for each nonideal term from `plasma-regime`/`plasma-dimensionless`; do not enable every term simultaneously by default.
2. Verify the unsplit staggered-mesh MHD Config and compiled material-property units.
3. For resistivity, identify the actual implementation (Constant, DaviesWen, SpitzerHighZ, Multitype, etc.), resistivity convention/form, and explicit/implicit solver path. Record anisotropic components when used.
4. Verify runtime switches for Hall, Hall electron velocity, Biermann (1T/3T and source/flux formulation), Nernst, Seebeck, cross-field, cross magnetic resistivity, and flux/current limiters from the live Config/runtime docs.
5. Check timestep restrictions. Extended-MHD terms can introduce faster characteristic transport/whistler scales; inspect FLASH's live timestep implementation and logs instead of imposing a generic dt formula blindly.
6. Design term-isolation comparisons: baseline MHD, +resistive, +Hall, then additional transport terms as scientifically justified. This makes attribution possible.
7. Validate against included unit/benchmark cases where applicable (Hall waves, Biermann tests, reconnection/current-sheet cases) before trusting a new geometry.

## FLASH 4.8 note

The supplied source contains the relevant 4.8 switches listed in `../../references/FLASH48_CAPABILITIES.md`. Exact capitalization matters; verify it live.

## Output

Enabled terms and justification, implementation paths, parameter values/units, timestep/limiter considerations, and comparison matrix.
