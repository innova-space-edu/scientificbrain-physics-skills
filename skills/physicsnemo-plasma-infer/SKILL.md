---
name: physicsnemo-plasma-infer
description: Run PhysicsNeMo plasma surrogate inference with strict preprocessing parity, training-domain checks, rollout diagnostics, and comparison against FLASH/physical constraints before accepting predictions.
license: Apache-2.0
metadata:
  author: Innova Space Education / ScientificBrain
  version: 0.1.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# PhysicsNeMo Plasma Inference

## Instructions

1. Load checkpoint, model config, channel map, normalization statistics, dataset schema and PhysicsNeMo revision as one versioned bundle.
2. Verify input geometry/resolution/fields/units and parameter vector against the model contract.
3. Compare requested parameters with the training envelope. Mark extrapolation explicitly; do not silently clip to the training range.
4. Apply exactly the training preprocessing/normalization; invert transforms on outputs before physical evaluation.
5. For autoregressive models report error/instability signals as rollout horizon grows.
6. When FLASH truth exists, run `../../scripts/validate_surrogate.py` or stronger project diagnostics. At minimum use per-field error and MHD divergence checks; add conservation/PDE residuals appropriate to the modeled equations.
7. Return uncertainty indicators based on validated methods (ensemble, calibration, distance-to-training data, etc.) only if the trained bundle actually supports them.

## Output

Prediction artifact, domain-of-validity status, parameter-distance/extrapolation notes, quantitative validation metrics, and explicit limitations.
