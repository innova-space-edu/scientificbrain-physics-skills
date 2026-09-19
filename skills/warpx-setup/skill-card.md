## Description
Build reproducible WarpX input/PICMI configurations with explicit geometry, resolution, timestep, particles-per-cell, boundaries, field solver, collisions, diagnostics, restart, and provenance.

## Owner
Innova Space Edu SpA / ScientificBrain

## License / terms
Apache-2.0 for this skill text. External solvers, data and frameworks retain their own licenses, citations and access terms.

## Use case
Use when ScientificBrain needs this capability as part of a reproducible computational-physics workflow.

## Known risks and mitigations
- Solver validity is regime- and observable-dependent; require explicit scale/closure checks.
- Solver APIs and input syntax change; inspect the live installed version.
- Expensive simulations require benchmark and reduced-size validation before scale-up.
- Never treat a successful run as physical validation.

## Version
0.2.0
