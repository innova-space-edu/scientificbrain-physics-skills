---
name: distributed-training
description: Plan PhysicsNeMo/PyTorch distributed scientific-ML training and inference using current distributed utilities, matching strategy to 2D/3D meshes, graphs, model size and memory rather than copying LLM parallelism.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# Distributed PhysicsNeMo Training

## Instructions

1. Discover the current PhysicsNeMo distributed API and recommended launch pattern.
2. Profile single-device memory/throughput first.
3. Prefer data parallelism for models that fit per device; inspect PhysicsNeMo domain parallelism/ShardTensor for high-resolution spatial data when appropriate.
4. Record world size, precision, batch/global batch, gradient accumulation, seeds and data sharding.
5. Check that validation/test sampling is invariant to distributed partitioning.
6. Measure throughput/scaling separately from scientific accuracy.
7. Ensure checkpoints can resume with the intended topology or document topology constraints.

## Output

Parallel strategy, launch configuration, memory estimate, scaling benchmark and reproducibility record.
