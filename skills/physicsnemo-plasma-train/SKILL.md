---
name: physicsnemo-plasma-train
description: Train and evaluate PhysicsNeMo plasma surrogate models from FLASH datasets, with live API verification, held-out runs, physics-aware losses where justified, reproducible configs, and rollout/convergence diagnostics.
license: Apache-2.0
metadata:
  author: Innova Space Education / ScientificBrain
  version: 0.1.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# PhysicsNeMo Plasma Train

## Instructions

1. Run `physicsnemo-plasma-discover` and freeze the live PhysicsNeMo version/commit used by the experiment.
2. Load a validated dataset manifest from `physicsnemo-flash-dataset`. Refuse ambiguous channel ordering or mixed units.
3. Define target task and metrics before model construction. Keep a pure data baseline before adding physics-loss complexity when practical.
4. Configure the chosen live model family without inventing imports. Record architecture, resolution, optimizer, scheduler, precision, seed, distributed strategy, and checkpoint policy.
5. For PINO/physics-informed losses, derive residuals for the exact modeled equations/normalization and test the residual implementation on known fields. Do not paste ideal-MHD residuals onto an Extended-MHD target.
6. Evaluate on held-out FLASH runs at each model-selection checkpoint. For temporal models include multi-step rollout error, not only one-step loss.
7. Preserve training curves, best/last checkpoints, config, code revision, dataset hash, and hardware/runtime metadata.
8. Hand the best candidate to `physicsnemo-plasma-infer` and physical-validation checks.

## Output

Reproducible training configuration, metrics by field/run/parameter region, checkpoint references, observed failure modes, and whether the model is ready for held-out physical validation.
