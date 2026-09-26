# Evaluations

ScientificBrain Physics Skills v0.3 uses three evaluation layers.

## 1. Unit cases

evals/unit-cases.json checks focused routing/skill behavior. These cases ask whether the correct skill(s) are selected and whether key contract elements are present.

## 2. Workflow cases

evals/workflow-cases.json checks multi-skill scientific workflows such as model routing → execution planning → validation/UQ.

## 3. Capability cases

evals/capability-cases.json describes end-to-end research tasks. These are intended for scored agent runs that verify scientific reasoning, evidence handling, model hierarchy, validation and provenance together.

## Compatibility routing set

evals/routing-cases.json remains a compact positive/negative routing set for backward compatibility and quick smoke checks.

## Structural gate

scripts/validate_repo.py checks the skill structure and required v0.3 skills. scripts/eval_contracts.py validates the three evaluation JSON contracts. GitHub Actions also compiles all helper scripts and runs deterministic smoke tests.

The JSON cases are evaluation specifications, not proof that an LLM has passed them. A future scored runner should record model/version, prompt, tool availability, outputs, rubric results and failure category for every execution.
