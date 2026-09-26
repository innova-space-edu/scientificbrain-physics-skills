# Google DeepMind Science Skills integration principles

ScientificBrain Physics Skills v0.3 adopts selected architectural ideas from the public Google DeepMind Science Skills project while keeping a separate, physics-specific implementation.

Upstream project: https://github.com/google-deepmind/science-skills

## Adopted principles

1. **Small composable skills** — each capability has a focused SKILL.md and supporting resources instead of one monolithic prompt.
2. **Reuse before reimplementation** — workflow skills reference existing skills and helper scripts wherever possible.
3. **Executable helpers when computation/file work is required** — deterministic tasks live in auditable scripts rather than prose-only instructions.
4. **Explicit guardrails / anti-patterns** — skills state not only what to do, but what conclusions or execution paths are not justified.
5. **Workflow distillation** — a successful, validated workflow can be converted into a draft reusable skill with dependencies and tests.
6. **Evaluation as part of the skill contract** — ScientificBrain uses unit, workflow and end-to-end capability cases rather than relying on subjective impressions.
7. **External API responsibility** — credentials, rate limits and external connectors remain in ScientificBrain; Physics Skills define scientific intent and evidence requirements.

## ScientificBrain-specific extensions

The physics implementation adds requirements that are central to computational/experimental physics:

- model hierarchy before solver choice;
- characteristic-scale and closure checks;
- observable-level validation;
- independent validator after solver-specific validation;
- cross-fidelity overlap tests;
- separation of numerical, stochastic, surrogate, measurement and model-form uncertainty;
- native solver output and fidelity identity preservation;
- provider-neutral execution graphs;
- no automatic promotion of generated skills to stable.

## Licensing and attribution

The upstream Science Skills README states that software is Apache-2.0 and other materials are CC-BY 4.0, with third-party-source terms documented separately by that project.

ScientificBrain Physics Skills does not vendor or reproduce Google DeepMind skill text in v0.3. The project uses the public architectural ideas and documents the influence here and in ACKNOWLEDGEMENTS.md/NOTICE.md. If upstream code or text is incorporated in the future, the relevant license/NOTICE obligations must be carried into the modified files.

## Independence

ScientificBrain Physics Skills is an independent project. Reference to Google DeepMind Science Skills does not imply sponsorship, endorsement, affiliation or compatibility certification.
