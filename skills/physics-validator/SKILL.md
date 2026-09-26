---
name: physics-validator
description: Independently validate physics calculations, simulations and surrogate outputs at the observable/claim level using dimensions, regime validity, conservation, convergence, benchmarks, uncertainty and provenance.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.3.0
  tags:
    - physics
    - validation
    - verification
    - scientificbrain
---

# Physics Validator

Use this skill as an independent gate after theory, numerical simulation, transport calculation or surrogate inference and before scientific claims are accepted.

## Dependencies

- flash-validation — solver-specific validation for FLASH.
- pic-validation — solver-specific validation for PIC/hybrid calculations.
- uncertainty-quantification — uncertainty propagation and uncertainty decomposition.
- plasma-dimensionless — regime/scale checks for plasma observables.

## Validation sequence

1. State the exact observable or claim being validated.
2. Audit dimensions, units, normalizations and coordinate/sign conventions.
3. Check governing assumptions, closures and regime boundaries.
4. Check limiting cases and analytic/reduced-model expectations where available.
5. Check conservation laws and boundary/source accounting appropriate to the model.
6. Check numerical convergence: mesh, timestep, particles/sample count, solver tolerances and restart behavior as applicable.
7. Run or cite an appropriate benchmark and document version/configuration.
8. Quantify measurement, numerical, stochastic, surrogate and model-form uncertainty separately where they matter.
9. Compare adjacent fidelities or independent formulations when the claim crosses a model boundary.
10. Verify provenance: code/solver version, parameters, seeds, input artifacts and processing lineage.

## Decision states

Assign a state per observable/claim:

- accepted — all required checks have evidence and meet project-defined criteria;
- conditional — evidence exists but warnings/limitations restrict the claim;
- rejected — at least one required criterion fails;
- blocked — required evidence or inputs are missing.

Never label an entire simulation valid simply because one observable passes.

## Output contract

Return a validation matrix with check, evidence, criterion, result, uncertainty contribution, accepted claim scope, failed/blocked items and required next tests.

## Guardrails

- Solver completion is not scientific validation.
- Visual plausibility is not a convergence test.
- Do not invent universal numerical tolerances where the project has not defined them.
- Missing evidence remains missing; never promote it to pass.
- Do not let the same generated explanation substitute for an independent check.
- Validation applies to specified observables and regimes, not to the code globally.
