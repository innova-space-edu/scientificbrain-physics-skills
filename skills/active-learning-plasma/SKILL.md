---
name: active-learning-plasma
description: Use PhysicsNeMo active-learning concepts to select new FLASH/PIC/hybrid/Geant4 simulations where additional labels most improve a validated plasma surrogate per unit compute cost.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.1
  tags:
    - physics
    - plasma
    - scientificbrain
---

# Active Learning for Plasma

PhysicsNeMo provides an active-learning framework with train/fine-tune, query and label phases.

## ScientificBrain loop

1. Train a baseline surrogate on validated data.
2. Define a candidate parameter pool and hard physical validity constraints.
3. Estimate uncertainty/information value with a calibrated method.
4. Query candidate points.
5. Use `plasma-model-router` and `multifidelity-plasma` to choose the **fidelity/solver**, not only the parameter point.
6. Execute/label through a configured worker.
7. Validate outputs and append them to the dataset.
8. Retrain/fine-tune and repeat until accuracy/cost/stopping criteria are reached.

## Guardrails

Do not query outside solver/model validity merely because uncertainty is high. Track failed simulations as information. Compare active learning to a non-adaptive baseline before claiming efficiency gains.

## Output

Query strategy, candidate pool, selected samples/fidelity, labeling cost, model improvement and stopping evidence.

## Source-grounded PhysicsNeMo mapping

The inspected PhysicsNeMo active-learning framework iterates **training → metrology → query → labeling**. Its protocols include QueryStrategy, LabelStrategy and MetrologyStrategy. The external-aerodynamics example shows how a domain-specific adapter sits below a generic AL loop.

For plasma, the LabelStrategy should call a ScientificBrain worker for FLASH/WarpX/PIConGPU/EDIPIC/Geant4, while plasma validation becomes the metrology/acceptance layer. Never reuse aerodynamic drag metrology directly.

See `../../references/PHYSICSNEMO_SOURCE_MAP.md`.
