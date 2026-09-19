---
name: flash-sweep
description: Design and execute reproducible FLASH parameter campaigns for sensitivity studies and PhysicsNeMo datasets while changing declared variables only and preserving one manifest per run.
license: Apache-2.0
metadata:
  author: Innova Space Education / ScientificBrain
  version: 0.1.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# FLASH Parameter Sweep

## Instructions

1. Define scientific factors, ranges/distributions, constants, and the target observables before generating runs.
2. Prefer a small verification matrix first. Do not launch a large Cartesian product until representative corner/center cases run successfully.
3. Generate one immutable run directory per parameter vector. Store a machine-readable campaign manifest mapping run ID → parameters → parameter-file hash → status.
4. Change runtime parameters when possible; rebuild FLASH only when the changed quantity is compile/setup-time.
5. Include baseline/benchmark cases and resolution variants so surrogate data are not detached from numerical verification.
6. Split future ML datasets by run/parameter region, not randomly by snapshot.
7. Detect duplicate parameter vectors and failed/incomplete runs before dataset export.

## Output

Campaign design, number of unique runs, rebuild groups, parameter table/manifest path, validation subset, and storage estimate when known.
