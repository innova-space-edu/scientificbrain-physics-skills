---
name: scientificbrain-orchestration
description: Orchestrate end-to-end physics workflows in ScientificBrain: model/solver routing, remote execution, diagnostics, validation, UQ, multi-fidelity datasets, PhysicsNeMo training, active learning, and provenance.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# Direct ScientificBrain Physics Orchestration

This is the top-level skill for the expanded toolkit.

## Workflow

1. Parse the scientific question, observable, geometry and uncertainty target.
2. Run regime/model routing.
3. Create a solver hierarchy and validation/overlap plan.
4. Select execution backend:
   - FLASH worker;
   - WarpX Hybrid/PIC worker;
   - PIConGPU HPC worker;
   - EDIPIC-2D worker;
   - Geant4 worker;
   - local analytical/Monte Carlo utility;
   - PhysicsNeMo training worker.
5. Emit a provider-neutral job specification with immutable inputs, solver/version, resource request, expected outputs and acceptance criteria.
6. Monitor job state; ingest HDF5/openPMD/output manifests.
7. Run canonical diagnostics and solver validation.
8. Update UQ/multi-fidelity state.
9. Train/evaluate surrogate when useful.
10. If active learning is enabled, select the next simulation/fidelity and loop.
11. Store every accepted/rejected artifact and decision in ScientificBrain research state.

## Security

ScientificBrain holds credentials and endpoint allowlists. Skills never accept arbitrary execution URLs or secrets from a browser request.

## Output

A complete execution graph, job manifests, validation decisions, dataset lineage, uncertainty state and next-action rationale.
