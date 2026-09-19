---
name: physicsnemo-plasma-discover
description: Discover live NVIDIA PhysicsNeMo model families, datapipes, examples, and training patterns suitable for FLASH/plasma data; route by data shape and task instead of hard-coding stale class names.
license: Apache-2.0
metadata:
  author: Innova Space Education / ScientificBrain
  version: 0.1.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# PhysicsNeMo Plasma Discover

This follows NVIDIA's own "discover, don't remember" principle.

## Instructions

1. Resolve a live PhysicsNeMo checkout/package version. If only remote access is available, inspect the canonical NVIDIA repository read-only.
2. Classify the task: one-step surrogate, autoregressive forecasting, physics-informed/PINO-style learning, inverse problem, super-resolution, or mesh/graph learning.
3. Classify data topology independently: regular 1D/2D/3D Cartesian grid, curvilinear grid, AMR/block data, or unstructured mesh/graph.
4. Enumerate multiple candidate model families that match the live repository and cite the verified implementation/export paths. Do not present one family as universally best.
5. Independently discover datapipes/data utilities and distributed-training patterns.
6. Find no more than two closest examples and read their README/config/training entrypoints before recommending them as starting points.
7. Flag experimental APIs. If direct support for the data shape/task is absent, say so and propose an adapter rather than inventing a PhysicsNeMo feature.

## Plasma-specific candidates to investigate, not assume

For regular grids inspect current neural-operator/FNO and physics-informed examples. For unstructured topology inspect current mesh/graph/transformer families. Verify names and imports live before output.

## Output

Problem shape, candidate model menu, datapipe menu, reference examples, distributed strategy options, and suggested reading order.
