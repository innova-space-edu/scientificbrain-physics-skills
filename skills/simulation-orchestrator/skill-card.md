# Skill card: simulation-orchestrator

- Status: v0.3.0
- Purpose: turn model decisions into a reproducible execution/validation DAG.
- Inputs: routing decision, observable, acceptance criteria, solver candidates, artifacts and resource constraints.
- Outputs: provider-neutral execution graph, manifests, validation gates, failure policies and lineage.
- Key dependencies: physics-model-router, physics-validator, scientificbrain-orchestration.
- Non-goal: choosing physics from compute availability.
- Security: no arbitrary commands, execution URLs or credentials in user-controlled manifests.
