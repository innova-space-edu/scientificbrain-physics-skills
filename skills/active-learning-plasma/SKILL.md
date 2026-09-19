---
name: active-learning-plasma
description: Use PhysicsNeMo active-learning concepts to select new FLASH/PIC/hybrid/Geant4 simulations where additional labels most improve a validated plasma surrogate per unit compute cost.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
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
