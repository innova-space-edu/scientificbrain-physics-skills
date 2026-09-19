# Monte Carlo and uncertainty

ScientificBrain separates four concepts:

1. **MCC**: stochastic collisions of simulated charged species with a modeled/background neutral population (solver-specific).
2. **DSMC**: stochastic particle-particle collision sampling.
3. **Monte Carlo parameter/uncertainty propagation**: repeated forward-model evaluations under sampled uncertain inputs.
4. **Geant4 transport Monte Carlo**: stochastic particle interactions through matter.

For every Monte Carlo workflow preserve seed(s), RNG implementation/version where relevant, distribution definitions, correlations, rejected samples, failed simulations and sample-count convergence.

Do not report only mean ± standard deviation when the output is strongly skewed/multimodal. Include quantiles and distribution diagnostics appropriate to the question.
