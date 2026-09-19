---
name: plasma-dimensionless
description: Calculate and sanity-check dimensionless numbers and characteristic plasma scales for MHD/extended-MHD simulation planning and dataset metadata.
license: Apache-2.0
metadata:
  author: Innova Space Education / ScientificBrain
  version: 0.1.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# Plasma Dimensionless Numbers

Use for quantitative scale analysis before simulation or when annotating a campaign.

## Instructions

- Normalize all supplied quantities to explicit SI (or document another consistent system before calculation).
- Compute only quantities supported by the provided inputs. Typical values: plasma beta, Alfvén speed/Mach, ion inertial length, ion/electron gyro radii, `d_i/L`, `rho_i/L`, magnetic Reynolds number, Lundquist number, and Knudsen number when mean-free-path information exists.
- Use `../../scripts/plasma_regime.py` for the implemented SI subset, and independently sanity-check orders of magnitude.
- Preserve both raw values and the definitions/inputs used. Dimensionless numbers are useless for reproducibility if their characteristic `L`, `U`, or resistivity convention is omitted.
- When comparing FLASH and literature values, check whether magnetic diffusivity [m²/s] or electrical resistivity [ohm m] is being denoted by eta; convert rather than silently equating them.

## Output

Produce a compact table of value, definition, inputs, and interpretation. Mark unavailable quantities rather than inventing them.
