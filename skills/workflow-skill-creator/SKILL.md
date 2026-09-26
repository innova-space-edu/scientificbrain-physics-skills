---
name: workflow-skill-creator
description: Distill a completed and scientifically validated physics workflow into a reviewable reusable skill that references existing skills, preserves regime limits, adds guardrails and defines unit/workflow/capability evaluations.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.3.0
  tags:
    - physics
    - skills
    - reproducibility
    - scientificbrain
---

# Physics Workflow Skill Creator

Use this skill only when a workflow has already been executed far enough to identify its real inputs, outputs, failure modes and validation requirements.

The design is inspired by the reusable-workflow pattern in Google DeepMind Science Skills, but this implementation is specific to ScientificBrain Physics Skills and does not copy upstream skill text.

## Distillation sequence

1. Reconstruct the completed workflow from artifacts, decisions and validation evidence.
2. Define the reusable scientific purpose and the regime where the workflow was demonstrated.
3. Separate strict steps from flexible steps.
4. Search the existing Physics Skills index and reuse dependencies instead of duplicating them.
5. Capture required physical inputs, units, solver/model versions, seeds, data contracts and acceptance criteria.
6. Capture failure handling and anti-patterns observed in the workflow.
7. Decide whether new helper code is genuinely required; prefer composition of existing scripts/skills.
8. Generate a draft SKILL.md plus skill-card.md and, when useful, a helper CLI.
9. Add at least:
   - one unit/routing case;
   - one multi-skill workflow case;
   - one end-to-end capability case;
   - one negative or out-of-domain case.
10. Require independent scientific review before promoting the draft to stable.

## Promotion gate

A generated skill remains draft until:

- dependencies have been reviewed;
- source/provenance requirements are explicit;
- guardrails and failure behavior are explicit;
- helper scripts compile and pass smoke tests;
- unit/workflow/capability evals exist;
- an independent reviewer confirms the skill does not generalize beyond demonstrated physics.

## Guardrails

- Do not create a new skill when an existing skill already covers the workflow.
- Do not infer undocumented API limits, solver capabilities or physics regimes.
- Do not silently change the physical model when an execution path fails.
- Do not promote a skill automatically because its source workflow succeeded once.
- Do not overwrite an existing skill without explicit review.
