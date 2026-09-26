---
name: simulation-orchestrator
description: Convert an accepted physics model hierarchy into a reproducible execution graph with baseline, overlap, solver jobs, diagnostics, validation, UQ and optional surrogate stages.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.3.0
  tags:
    - physics
    - simulation
    - orchestration
    - scientificbrain
---

# Simulation Orchestrator

Use this skill after physics-model-router or plasma-model-router has produced a defensible model hierarchy.

## Dependencies

- physics-model-router — model-family decision.
- scientificbrain-orchestration — ScientificBrain job/state/provider integration.
- distributed-simulation — multi-run/HPC campaign planning.
- physics-validator — independent acceptance gate.
- uncertainty-quantification — uncertainty state and propagation.
- solver-specific run/analysis skills selected by the router.

## Workflow

1. Freeze the scientific question, observable and acceptance criteria.
2. Record the routing decision and unresolved assumptions.
3. Build a directed execution graph:
   - analytic/reduced baseline where available;
   - lowest-fidelity numerical baseline;
   - adjacent-fidelity overlap cases;
   - production runs only after baseline/overlap gates;
   - canonical diagnostics and data conversion;
   - solver-specific validation;
   - independent physics-validator gate;
   - uncertainty propagation;
   - optional surrogate training/inference after validated data exist.
4. Emit provider-neutral job manifests with immutable input artifacts, solver/model version, resources, seed, expected outputs and validation requirements.
5. Preserve native solver output and fidelity identity.
6. Stop or downgrade the claim when a validation gate fails.
7. Store accepted and rejected artifacts with lineage in ScientificBrain.

## Output contract

Return an execution DAG containing nodes, dependencies, skill, model/solver, input artifact, version, resources, outputs, validation gate, retry/failure policy and provenance fields.

## Guardrails

- Do not execute an expensive production sweep before a minimal benchmark/overlap case.
- Do not allow browser/user input to inject arbitrary commands, endpoints, credentials or solver binaries.
- Do not skip validation because a job completed successfully.
- Do not merge outputs from different fidelities without retaining fidelity/model identity.
- Do not train a surrogate on unvalidated or provenance-free data.
