# Skill card: physics-model-router

- Status: v0.3.0
- Purpose: choose a defensible model hierarchy before choosing a solver.
- Inputs: target observable, governing physics, characteristic scales, geometry, closures, uncertainty target and compute constraints.
- Outputs: candidate hierarchy, rejected/deferred models, unresolved quantities, overlap tests and downstream skills.
- Key dependency: plasma-model-router for plasma-specific routing.
- Non-goal: declaring a universally correct solver from a single scale ratio.
- Validation expectation: every solver escalation must be tied to an observable-level need and an overlap/benchmark plan.
