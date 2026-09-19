# ScientificBrain Solver Container Contract v0.1

## Required environment

The ScientificBrain dispatcher provides:

| Variable | Meaning |
|---|---|
| `SCIBRAIN_JOB_JSON_B64` | Base64-encoded validated PhysicsJob |
| `SCIBRAIN_INPUT_URI` | Authorized input artifact prefix |
| `SCIBRAIN_OUTPUT_URI` | Unique output prefix |
| `SCIBRAIN_SOLVER` | Solver ID |
| `SCIBRAIN_ACTION` | run / validate / sweep / train / infer / analyze |
| `SCIBRAIN_JOB_ID` | ScientificBrain UUID |
| `SCIBRAIN_MPI_RANKS` | Requested MPI ranks |

Google Batch also supplies task variables such as `BATCH_TASK_INDEX`; multi-node jobs can supply `BATCH_HOSTS_FILE`.

## Mandatory security behavior

The container must not:
- eval a command contained in PhysicsJob;
- accept executable paths from the client;
- pull a second unapproved image based on job data;
- echo secrets;
- upload outside the assigned output prefix.

The image defines its own solver executable and launch wrapper.

## Mandatory provenance

`scientificbrain-output.json` should include:

```json
{
  "schema_version": "0.1",
  "job_id": "...",
  "solver": "warpx",
  "solver_version": "...",
  "source_commit": "...",
  "status": "succeeded",
  "started_utc": "...",
  "completed_utc": "...",
  "input_uri": "...",
  "output_uri": "...",
  "native_artifacts": [],
  "diagnostics": [],
  "validation": {},
  "resources_observed": {},
  "warnings": []
}
```

## Solver-specific expectations

### WarpX
Preserve input/PICMI configuration, openPMD diagnostics, checkpoints and collision cross-section provenance.

### PIConGPU
Preserve parameter/template revision, plugin configuration, openPMD output, checkpoints and accelerator/MPI topology.

### EDIPIC-2D
Preserve complete input directory, PETSc/HYPRE/MPI provenance and native output/diagnostic files.

### Geant4
Preserve application commit, macro, GDML/materials, physics list, datasets, seeds and scoring output.

### PhysicsNeMo
Preserve dataset version, model/config, git/package version, distributed topology, seed, checkpoints, metrics and held-out validation.

### FLASH
A private image/worker may implement the same contract, but FLASH source must not be redistributed through this public repository.
