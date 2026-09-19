---
name: physicsnemo-flash-dataset
description: Build reproducible PhysicsNeMo-ready datasets from validated FLASH runs, preserving fields, units, geometry, time, parameter vectors, run-level splits, AMR extraction policy, and solver provenance.
license: Apache-2.0
metadata:
  author: Innova Space Education / ScientificBrain
  version: 0.1.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# PhysicsNeMo FLASH Dataset

## Instructions

1. Accept only FLASH runs that have passed the campaign's minimum integrity checks; retain failed runs separately for diagnostics.
2. Use `flash-hdf5-yt` to inspect and extract data. Decide regular covering grid vs AMR/mesh representation before conversion.
3. Follow `../../references/DATA_CONTRACT.md`. Every tensor must be traceable to run ID, time, source field and units.
4. Build control/conditioning vectors from the campaign parameters and physical nondimensional metadata where appropriate.
5. Define the learning pair: static parameter→field, state→next-state, history→future, coordinates→solution, etc. Avoid accidental target leakage.
6. Split by complete runs or parameter-space regions. Do not randomly split snapshots from the same run across train/test.
7. Compute normalization statistics from the training split only and save them separately.
8. Validate tensor shapes, NaN/Inf counts, time ordering, field units, duplicate samples, and parameter coverage before training.

## Output

Dataset manifest, schema version, shape/channel map, split manifest, normalization statistics, parameter ranges, and provenance summary.
