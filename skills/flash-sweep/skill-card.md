## Description
Design and execute reproducible FLASH parameter campaigns for sensitivity studies and PhysicsNeMo datasets while changing declared variables only and preserving one manifest per run.

## Owner
Innova Space Education / ScientificBrain

## License / terms
Apache-2.0 for this skill text. External solvers/frameworks retain their own licenses and access terms.

## Use case
Use when an agent needs to design and execute reproducible FLASH parameter campaigns for sensitivity studies and PhysicsNeMo datasets while changing declared variables only and preserving one manifest per run.

## Known risks and mitigations
- Physics and solver validity are problem-dependent; the skill requires explicit assumptions and validation.
- FLASH/PhysicsNeMo APIs change; live discovery is preferred to remembered paths.
- Generated configurations can consume substantial compute; verify on small benchmark cases first.

## Output
Markdown analysis and/or reproducible configuration/script artifacts, depending on the calling agent.

## Version
0.1.0
