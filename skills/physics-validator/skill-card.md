# Skill card: physics-validator

- Status: v0.3.0
- Purpose: independent observable-level verification and validation.
- Inputs: claim/observable, model, run/calculation artifacts, benchmarks, convergence evidence, uncertainty and provenance.
- Outputs: accepted/conditional/rejected/blocked status with a quantitative evidence matrix.
- Delegates: FLASH checks to flash-validation; PIC/hybrid checks to pic-validation.
- Non-goal: certifying an entire solver or simulation from visual agreement.
- Critical rule: missing validation evidence produces blocked, not pass.
