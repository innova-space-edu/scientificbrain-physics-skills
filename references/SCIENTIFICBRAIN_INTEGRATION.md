# ScientificBrain integration

ScientificBrain Physics Skills is consumed by the main ScientificBrain platform.

## Canonical links

- Main repository: https://github.com/innova-space-edu/ScientificBrain
- Public application: https://scientific-brain.vercel.app
- Scientific tools workspace: https://scientific-brain.vercel.app/scientific-tools
- Physics skills repository: https://github.com/innova-space-edu/scientificbrain-physics-skills

## Responsibility boundary

### scientificbrain-physics-skills

This repository defines:

- physics-model and plasma-regime/model routing;
- physics-specific literature/evidence protocol;
- FLASH / WarpX / PIConGPU / EDIPIC-2D / Geant4 / PhysicsNeMo skill instructions;
- Monte Carlo, UQ, diagnostics and multi-fidelity guidance;
- source-grounded solver maps;
- solver-specific and independent observable-level validation requirements;
- canonical scientific-data contracts;
- execution-graph planning;
- active-learning logic;
- workflow-to-skill distillation and evaluation contracts.

### ScientificBrain

The main application owns:

- user authentication and research state;
- provider credentials and NVIDIA routing;
- the /scientific-tools user interface;
- local plasma model screening;
- reproducible Monte Carlo sampling;
- typed physics job manifests;
- the server-only worker/HPC registry;
- job submission to approved workers;
- persistence, provenance and research artifacts;
- literature connectors/search services used by physics-literature.

## Current ScientificBrain API contract

The Scientific Tools workspace uses the authenticated ScientificBrain API.

Read operations:

```text
GET /api/science?op=physics_toolkit
GET /api/science?op=physics_workers
GET /api/science?op=physics_profiles
GET /api/science?op=nvidia_status
```

Physics utilities:

```text
POST /api/science?op=physics_route
POST /api/science?op=physics_monte_carlo
POST /api/science?op=physics_prepare_job
```

Remote execution:

```text
POST /api/science?op=physics_submit_job
```

NVIDIA/NIM capability invocation:

```text
POST /api/science?op=nvidia_invoke
```

Google Cloud Batch:

```text
GET  /api/science?op=gcp_setup_plan
GET  /api/science?op=gcp_batch_status
GET  /api/science?op=gcp_batch_get&job_id=...
POST /api/science?op=gcp_batch_preview
POST /api/science?op=gcp_batch_submit
POST /api/science?op=gcp_batch_delete
```

Google Cloud is an execution backend. Physics skills still determine the scientific model, solver, diagnostics and acceptance criteria. FLASH can run through this same backend using a private, licensed Artifact Registry image.

The v0.3 high-level contracts physics-model-router, physics-validator, simulation-orchestrator, physics-literature and workflow-skill-creator are skill-layer capabilities. Dedicated API bindings may be added in ScientificBrain without changing the existing plasma-route/job endpoints.

## Security boundary

The browser never chooses an arbitrary worker endpoint, shell command or provider credential.

ScientificBrain resolves:

- worker URLs;
- solver installations;
- scheduler profiles;
- executable paths;
- worker authentication;
- provider/API credentials.

Physics job manifests carry scientific parameters and resource requests, not execution secrets.

## Execution model

```text
ScientificBrain UI / research state
        ↓
physics-literature (when external evidence is needed)
        ↓
physics-model-router
        ↓
domain router (e.g. plasma-model-router)
        ↓
simulation-orchestrator
        ↓
typed physics job manifests
        ↓
ScientificBrain server
        ↓
approved worker / HPC / Google Cloud Batch
        ↓
FLASH / WarpX / PIConGPU / EDIPIC-2D / Geant4 / PhysicsNeMo
        ↓
native outputs + canonical diagnostics
        ↓
solver-specific validation
        ↓
physics-validator
        ↓
UQ / multi-fidelity / optional surrogate
        ↓
ScientificBrain research state
```

The NVIDIA API is optional for local routing, Monte Carlo sampling, job preparation and Google Cloud Batch execution. Once NVIDIA_API_KEY is configured, ScientificBrain can additionally expose approved NVIDIA/NIM capabilities from the same Scientific Tools workspace.
