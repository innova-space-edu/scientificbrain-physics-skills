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

- physical-regime and model routing;
- FLASH / WarpX / PIConGPU / EDIPIC-2D / Geant4 / PhysicsNeMo skill instructions;
- Monte Carlo, UQ, diagnostics and multi-fidelity guidance;
- source-grounded solver maps;
- validation requirements;
- canonical scientific-data contracts;
- active-learning and orchestration logic.

### ScientificBrain

The main application owns:

- user authentication and research state;
- provider credentials and NVIDIA routing;
- the `/scientific-tools` user interface;
- local plasma model screening;
- reproducible Monte Carlo sampling;
- typed physics job manifests;
- the server-only worker/HPC registry;
- job submission to approved workers;
- persistence, provenance and research artifacts.

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

## Security boundary

The browser never chooses an arbitrary worker endpoint, shell command or provider credential.

ScientificBrain resolves:

- worker URLs;
- solver installations;
- scheduler profiles;
- executable paths;
- worker authentication;
- NVIDIA/API credentials.

Physics job manifests carry scientific parameters and resource requests, not execution secrets.

## Execution model

```text
ScientificBrain UI
        ↓
physics skill / model router
        ↓
typed physics job manifest
        ↓
ScientificBrain server
        ↓
approved worker / HPC
        ↓
FLASH / WarpX / PIConGPU / EDIPIC-2D / Geant4 / PhysicsNeMo
        ↓
HDF5 / openPMD / native outputs
        ↓
validation + canonical diagnostics
        ↓
ScientificBrain research state
```

The NVIDIA API is optional for the local router, Monte Carlo sampling and job preparation. Once `NVIDIA_API_KEY` is configured, ScientificBrain can additionally expose approved NVIDIA/NIM capabilities from the same Scientific Tools workspace.
