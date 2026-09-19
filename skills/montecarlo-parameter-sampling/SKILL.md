---
name: montecarlo-parameter-sampling
description: Design reproducible random, stratified, Latin-hypercube, or quasi-random parameter campaigns for solver sweeps and surrogate training without confusing space-filling design with uncertainty distributions.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# Monte Carlo Parameter Sampling

## Instructions

- Clarify whether the goal is probabilistic uncertainty propagation or space-filling exploration. They are not the same.
- Define bounds/distributions, transforms, correlations, constraints and invalid regions.
- Select random/stratified/LHS/quasi-random design based on objective and available implementation.
- Record seed and generated parameter vectors before launching solvers.
- Detect duplicate/invalid samples and preserve rejected vectors with reasons.
- For expensive solvers, begin with a pilot and route to `active-learning-plasma` when adaptive sampling is beneficial.
- Split ML datasets by simulation/sample group with leakage controls.

## Output

Sampling design, seed, parameter manifest, validity constraints, solver mapping and stopping rule.
