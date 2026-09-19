---
name: flash-physicsnemo-pipeline
description: Orchestrate the complete validated plasma workflow: regime assessment → FLASH setup/run/sweep → HDF5/yt → PhysicsNeMo dataset → 2D/3D surrogate training/inference → comparison against held-out FLASH and physical constraints.
license: Apache-2.0
metadata:
  author: Innova Space Education / ScientificBrain
  version: 0.1.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# FLASH → PhysicsNeMo Plasma Pipeline

Use this as the top-level workflow skill.

## Pipeline

1. **Question and observable** — define the scientific question, geometry, target fields and acceptance observable.
2. **Regime** — invoke `plasma-regime` + `plasma-dimensionless`; establish the model hierarchy that must be tested.
3. **High-fidelity configuration** — `flash-discover` → `flash-setup` → `flash-extmhd` as needed.
4. **Verification runs** — `flash-run` + `flash-validation` on baseline/benchmark/resolution cases before campaign generation.
5. **Campaign** — `flash-sweep` with immutable run manifests and run-level validation flags.
6. **Data** — `flash-hdf5-yt` → `physicsnemo-flash-dataset`, following the shared data contract.
7. **Model discovery** — `physicsnemo-plasma-discover` using the live PhysicsNeMo repository.
8. **Training** — `physicsnemo-plasma-train` on train/validation runs only.
9. **Held-out test** — `physicsnemo-plasma-infer` on untouched FLASH runs.
10. **Physical acceptance** — compare target observables, per-field error, divergence/conservation/PDE diagnostics and rollout behavior. Do not promote the surrogate if it only passes aggregate ML metrics.
11. **2D → 3D** — treat 3D as a new validation/training regime; do not claim a 2D surrogate generalizes to 3D. Choose FNO/mesh/transformer families from the live model discovery based on the 3D representation.
12. **Iteration/active learning** — only after the base loop is validated, use error/uncertainty maps to propose additional FLASH runs in poorly covered parameter regions.

## Artifacts

A completed campaign should emit: regime assessment, FLASH build/run manifests, validated HDF5 inventory, dataset manifest/splits, model/training bundle, held-out metrics, physical-validation report, and a machine-readable domain-of-validity record.

## Stop conditions

Stop and report instead of continuing when: fluid closure is unsupported; FLASH configuration cannot represent requested physics; output fields/units are ambiguous; validation runs fail; train/test leakage is detected; or inference is materially outside the documented training domain.
