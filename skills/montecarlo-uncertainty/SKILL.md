---
name: montecarlo-uncertainty
description: Propagate input and model uncertainty through analytical models, FLASH/PIC simulations, or surrogates using reproducible Monte Carlo sampling and statistically explicit outputs.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# Monte Carlo Uncertainty Propagation

## Instructions

1. Define uncertain inputs and distinguish measurement uncertainty, manufacturing variation, nuisance parameters and epistemic/model uncertainty.
2. Assign distributions only when justified by evidence; otherwise use bounded/scenario analysis and label assumptions.
3. Preserve correlations. Do not independently sample variables known to covary.
4. Generate samples with a recorded seed and scheme using `../../scripts/monte_carlo_sampling.py` or an equivalent validated sampler.
5. Evaluate the chosen forward model: analytical, FLASH, PIC/hybrid, Geant4 or a validated surrogate.
6. Report distributions/quantiles/confidence intervals for target observables, convergence with sample count, and failed-run policy.
7. If a surrogate is used, include surrogate error/model-form uncertainty rather than treating it as exact.

## Output

Input distribution table, correlation assumptions, sample manifest, observable distribution, convergence assessment and uncertainty decomposition.
