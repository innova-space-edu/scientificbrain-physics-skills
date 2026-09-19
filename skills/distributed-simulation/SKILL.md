---
name: distributed-simulation
description: Plan and validate MPI/GPU/multi-node execution for FLASH, WarpX and PIConGPU, separating physical convergence from parallel scaling and preserving deterministic/provenance information.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# Distributed Simulation

## Instructions

- Determine whether the solver supports the requested backend and decomposition in the live build.
- Estimate per-rank/per-GPU memory and I/O before scale-up.
- Separate **physics convergence tests** from **performance scaling tests**.
- Run a small correctness baseline before changing decomposition.
- Record nodes, ranks, GPUs, threads, accelerator backend, scheduler configuration, wall time, memory and I/O volume.
- Perform strong/weak scaling only with clearly fixed/scaled problem definitions.
- Verify checkpoint/restart across the target scheduler/storage environment.
- Do not infer identical floating-point trajectories across decompositions; compare physical observables within numerical tolerance.

## Output

Resource/decomposition plan, scheduler template requirements, scaling protocol, checkpoints and performance/provenance metrics.
