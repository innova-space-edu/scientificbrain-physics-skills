# FLASH → PhysicsNeMo data contract

Every exported dataset must include both tensors and provenance. A minimal dataset is not just `X.npy` and `Y.npy`.

## Required metadata

- `schema_version`
- FLASH release/revision identifier
- simulation case name and immutable run ID
- setup command and hash of setup/runtime parameter files
- geometry (`cartesian`, cylindrical, etc.)
- dimensionality (1/2/3)
- time value for every sample
- spatial bounds and spacing or mesh coordinates
- source refinement level / extraction strategy
- field map from dataset name to FLASH/yt source field
- units for every field
- input/control parameters varied in the campaign
- train/validation/test split assignment at the **run level**

## Recommended regular-grid tensor convention

For grid-based neural operators:

- 1D dynamic field: `[sample, channel, x]`
- 2D: `[sample, channel, y, x]`
- 3D: `[sample, channel, z, y, x]`
- trajectories may either add a time axis or use `(state_t → state_t+Δt)` pairs.

Store a `channels.json` (or equivalent manifest) with semantic names and units. Do not rely on channel position alone.

## Leakage prevention

Snapshots from one FLASH run are correlated. Do not randomly place neighboring snapshots from the same run across train and test sets. Split by complete simulation run or parameter-space region unless the experiment specifically studies interpolation in time within a known trajectory.

## AMR

Choose and record one of:

1. uniform covering grid at a declared level;
2. patch/block representation preserving AMR topology;
3. unstructured graph/mesh representation.

Never silently mix refinement strategies.
