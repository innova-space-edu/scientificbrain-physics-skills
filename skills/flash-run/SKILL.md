---
name: flash-run
description: Launch, monitor, restart, and provenance-track a configured FLASH simulation, preserving parameters, logs, checkpoints, plotfiles, executable identity, and failure diagnostics.
license: Apache-2.0
metadata:
  author: Innova Space Education / ScientificBrain
  version: 0.1.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# FLASH Run

## Instructions

1. Require an existing configured/built object directory and a reviewed runtime parameter file.
2. Create a unique run directory; copy/link the executable and runtime inputs according to local FLASH practice without modifying the source tree.
3. Record MPI launcher, rank count, host/GPU/CPU environment where relevant, executable hash, `flash.par` hash, setup command, FLASH release/revision, and start time.
4. Launch using the site's approved MPI/scheduler method. Never invent cluster scheduler directives.
5. Monitor the FLASH log for timestep collapse, NaN/abort messages, solver failures, excessive refinement, I/O errors, and checkpoint production. Do not interpret a running process as a valid solution.
6. On restart, use the checkpoint/restart semantics of the live FLASH case and preserve the lineage from the original run. Never overwrite the parent checkpoint set.
7. After completion run `../../scripts/flash_output_manifest.py` and hand results to `flash-validation`.

## Output

Run identifier, command, status, latest physical time/step when available, output files, restart lineage, and any numerical warnings.
