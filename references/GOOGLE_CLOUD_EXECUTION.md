# Google Cloud execution

ScientificBrain can use **Google Cloud Batch** as a compute backend for approved physics jobs.

## Responsibility split

```text
ScientificBrain Physics Skills
        ↓
scientific model / solver / validation contract
        ↓
ScientificBrain
        ↓
typed PhysicsJob
        ↓
Google Cloud Batch adapter
        ↓
Compute Engine CPU/GPU VM(s)
        ↓
approved solver image
        ↓
native outputs + validation artifacts
```

This repository does not contain Google credentials and does not select arbitrary machine images.

## Google Batch profile

ScientificBrain stores server-only profiles that map a solver to:

- approved container image;
- machine type;
- optional NVIDIA accelerator type;
- maximum GPUs per node;
- GPU driver installation policy;
- retry policy;
- optional Spot provisioning.

The browser cannot override these values.

## Input/output contract

A solver image receives:

- `SCIBRAIN_JOB_JSON_B64`
- `SCIBRAIN_INPUT_URI`
- `SCIBRAIN_OUTPUT_URI`
- `SCIBRAIN_SOLVER`
- `SCIBRAIN_ACTION`
- `SCIBRAIN_JOB_ID`
- `SCIBRAIN_MPI_RANKS`

For multi-node Batch jobs, the image may also use `BATCH_HOSTS_FILE`.

The image must emit a machine-readable output manifest plus native scientific files.

## Recommended images

Separate images should be built for:

- WarpX;
- PIConGPU;
- EDIPIC-2D;
- Geant4;
- PhysicsNeMo;
- FLASH 4.8 as a **private licensed image**.

FLASH is fully compatible with the ScientificBrain → Google Cloud Batch execution model. The difference is distribution: the image must be built privately from an authorized FLASH checkout, stored in a private Artifact Registry repository, and never published with FLASH source bundled.

## Storage

ScientificBrain maps logical input artifacts to a configured Cloud Storage bucket and writes each job under a unique output prefix.

Native data must remain available:
- FLASH HDF5;
- WarpX/PIConGPU openPMD;
- EDIPIC native outputs;
- Geant4 scoring outputs;
- PhysicsNeMo checkpoints/metrics.

Derived canonical datasets should reference those native artifacts.

## Authentication

Google authentication belongs to ScientificBrain, not to the skills.

Preferred production approaches:
- attached least-privilege service account on Google Cloud;
- Workload Identity Federation when ScientificBrain runs outside Google Cloud.

Long-lived service-account keys should be treated as fallback credentials only.
