# Architecture

## Layers

```text
ScientificBrain
  └─ ScientificBrain Physics Skills
      ├─ Evidence layer
      │   └─ physics-literature
      ├─ Physics reasoning layer
      │   ├─ physics-model-router
      │   ├─ plasma-regime
      │   ├─ plasma-dimensionless
      │   ├─ kinetic-validity
      │   └─ plasma-model-router
      ├─ Execution-planning layer
      │   ├─ simulation-orchestrator
      │   ├─ distributed-simulation
      │   └─ scientificbrain-orchestration
      ├─ Solver layer
      │   ├─ FLASH
      │   ├─ WarpX Hybrid/full PIC
      │   ├─ PIConGPU
      │   ├─ EDIPIC-2D
      │   └─ Geant4
      ├─ Analysis / data layer
      │   ├─ flash-hdf5-yt
      │   ├─ openpmd-analysis
      │   ├─ plasma-diagnostics
      │   └─ uncertainty-quantification
      ├─ Independent validation layer
      │   ├─ flash-validation
      │   ├─ pic-validation
      │   └─ physics-validator
      ├─ SciML layer
      │   ├─ multifidelity-plasma
      │   ├─ PhysicsNeMo skills
      │   └─ active-learning-plasma
      └─ Reusable-workflow layer
          └─ workflow-skill-creator
```

## Decision flow

```text
question
  ↓
physics-literature (when external evidence is required)
  ↓
observable + acceptance criterion
  ↓
physics-model-router
  ↓
domain-specific router (e.g. plasma-model-router)
  ↓
simulation-orchestrator
  ↓
solver-specific execution + diagnostics
  ↓
solver-specific validation
  ↓
physics-validator
  ↓
UQ / multi-fidelity / surrogate (optional)
  ↓
ScientificBrain research state
```

## Responsibility boundaries

Solvers remain responsible for their numerical implementations. ScientificBrain Physics Skills is responsible for model/solver routing, scientific checks, reproducible execution contracts, dataset contracts, uncertainty separation and validation requirements. ScientificBrain owns credentials, provider/worker routing, research state and persistence.

A surrogate prediction is never labeled equivalent to a reference solver solely because loss decreased. Acceptance requires held-out comparisons plus physical diagnostics appropriate to the target observable.

A completed solver job is never equivalent to a validated scientific result. physics-validator operates after solver-specific validation and assigns status to explicit observables/claims.

## Skill architecture

The repository uses focused skill directories with SKILL.md and skill-card.md plus deterministic helper scripts where programmatic work is needed. From v0.3, workflow-skill-creator can distill validated workflows into draft skills, but generated skills are never self-promoted to stable.

See SCIENCE_SKILLS_INTEGRATION.md for the architectural influence from Google DeepMind Science Skills and the project-specific differences.
