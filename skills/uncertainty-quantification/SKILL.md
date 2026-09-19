---
name: uncertainty-quantification
description: Build a complete uncertainty-quantification workflow combining measurement, parameter, numerical, stochastic/PIC noise, surrogate, and model-form uncertainty with explicit propagation and attribution.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# Uncertainty Quantification

## Sources

- input/measurement uncertainty;
- parameter uncertainty;
- numerical discretization/convergence error;
- stochastic Monte Carlo/PIC sampling error;
- surrogate approximation/calibration error;
- model-form/fidelity discrepancy;
- diagnostic extraction uncertainty.

## Instructions

Create an uncertainty budget before propagation. Route stochastic propagation to `montecarlo-uncertainty`, numerical error to solver validation, and model discrepancy to `multifidelity-plasma`. Preserve correlations and report conditional vs marginal intervals clearly.

Use `../../scripts/uq_summary.py` for simple scalar-sample summaries; use more advanced methods only when justified and validated.

## Output

Uncertainty budget, propagation method, convergence/effective sample information, intervals/quantiles and dominant sources.
