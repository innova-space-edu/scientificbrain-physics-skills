## Description
Run PhysicsNeMo plasma surrogate inference with strict preprocessing parity, training-domain checks, rollout diagnostics, and comparison against FLASH/physical constraints before accepting predictions.

## Owner
Innova Space Education / ScientificBrain

## License / terms
Apache-2.0 for this skill text. External solvers/frameworks retain their own licenses and access terms.

## Use case
Use when an agent needs to run PhysicsNeMo plasma surrogate inference with strict preprocessing parity, training-domain checks, rollout diagnostics, and comparison against FLASH/physical constraints before accepting predictions.

## Known risks and mitigations
- Physics and solver validity are problem-dependent; the skill requires explicit assumptions and validation.
- FLASH/PhysicsNeMo APIs change; live discovery is preferred to remembered paths.
- Generated configurations can consume substantial compute; verify on small benchmark cases first.

## Output
Markdown analysis and/or reproducible configuration/script artifacts, depending on the calling agent.

## Version
0.1.0
