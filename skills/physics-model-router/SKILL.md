---
name: physics-model-router
description: Route physics problems to the smallest adequate model family and downstream skill before selecting a solver; covers analytic/reduced models, plasma fluid/kinetic hierarchies, particle transport, and validated scientific surrogates.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.3.0
  tags:
    - physics
    - modeling
    - routing
    - scientificbrain
---

# Physics Model Router

Use this skill before solver selection when the question is broader than one plasma solver.

## Dependencies

- plasma-regime — classify plasma regimes when plasma physics is involved.
- plasma-dimensionless — compute/interpret scale-separation and dimensionless evidence.
- kinetic-validity — decide whether distribution-level or particle kinetics are required.
- plasma-model-router — route plasma cases across fluid, hybrid and full-kinetic models.
- geant4-particle-transport — route particle-through-matter problems.
- physicsnemo-plasma-discover — consider surrogates only after a validated baseline exists.

## Routing sequence

1. Define the target observable, uncertainty target and acceptance criterion.
2. Identify the governing equations, closures, characteristic scales and geometry.
3. Start from the smallest model that can represent the observable; do not start from the most expensive solver.
4. For plasma problems, delegate detailed scale/closure routing to plasma-model-router.
5. For particle passage through matter or radiation transport, inspect Geant4 before plasma PIC.
6. For analytic or reduced-model questions, preserve an analytic/semi-analytic baseline before numerical escalation.
7. Consider PhysicsNeMo or another surrogate only when validated reference data, fidelity identity and an out-of-distribution policy exist.
8. When adjacent model families remain plausible, require overlap cases and compare the requested observable.
9. Route the accepted model hierarchy to simulation-orchestrator.

## Output contract

Return:

- scientific question and target observable;
- candidate model hierarchy ordered from lowest adequate complexity upward;
- rejected/deferred model families with explicit reasons;
- scale/closure evidence used in the decision;
- unresolved quantities that block a decision;
- overlap/benchmark cases required;
- downstream skills and expected data formats;
- compute constraints without allowing hardware availability to determine physics.

## Guardrails

- Higher computational fidelity is not automatically higher physical validity.
- Do not select full PIC merely because it is available.
- Do not select a surrogate before a validated baseline/data contract exists.
- Do not select a solver solely from hardware, popularity or familiarity.
- Do not turn a heuristic scale threshold into a universal validity theorem.
- Do not hide missing physical inputs by silently assuming values.
