# FLASH 4.8 capability map used by the skills

This inventory was built from the user-supplied FLASH 4.8 source distribution. Paths are relative to `FLASH_ROOT`. Agents must still verify them live because a user's tree may differ.

## Core MHD / Extended-MHD implementation

Primary solver configuration:

`source/physics/Hydro/HydroMain/unsplit/MHD_StaggeredMesh/Config`

Observed runtime switches include:

- `use_Hall`
- `hallVelocity`
- `use_Biermann`, `use_Biermann1T`, `use_Biermann3T`
- `use_Nernst`
- `use_Seebeck`
- `use_CrossFIeld` (note capitalization in FLASH 4.8 configuration)
- `useCrossMagRes`
- Hall/Nernst/cross-field/resistive limiter switches and coefficients
- constrained-transport/div(B) controls including `killdivb`

Magnetic resistivity configuration is under:

`source/physics/materialProperties/MagneticResistivity/`

Observed implementations include Constant, DaviesWen, SpitzerHighZ, Vacuum, and Multitype, with explicit/implicit solver selection and parallel/perpendicular/cross components where supported.

FLASH 4.8 release notes state that full Braginskii extended-MHD terms were added to the generalized Ohm law in the unsplit staggered-mesh solver in the 4.7 line, including anisotropic magnetic resistivity, Hall, Nernst, Seebeck, cross-field, and Biermann terms. Version 4.8 adds/updates implicit magnetic resistivity through unified HYPRE and related fixes.

## Example/test problems observed

Under `source/Simulation/SimulationMain/magnetoHD/`:

- `HallWhistlerWaves` — Hall-wave case, 1D example setup.
- `HallDriftWaves` — Hall drift case, 2D example setup.
- `GEM_challenge` — reconnection-oriented MHD/transport case.
- `Resistive` — resistive MHD test.
- `CurrentSheet` — current-sheet MHD problem with resistive configuration options.
- `OrszagTang` — standard MHD vortex benchmark.
- `BrioWu` — MHD shock tube benchmark.
- `FieldLoop`, `Rotor`, `BlastBS` — additional MHD verification/benchmark problems.
- `2DCartesianBiermannTest`, `2DCylindricalBiermannTest` — Biermann tests.
- `AnisoCond` — anisotropic conduction example, including a 3D uniform-grid parameter file.
- `AlWire`, `ZPinch` — high-energy-density / current-driven examples.

## Data / I/O

FLASH emits HDF5 checkpoint and plot files when built with HDF5 I/O. yt provides a FLASH frontend and should be preferred over handwritten HDF5 assumptions when possible because FLASH block/AMR structure and field metadata must be interpreted correctly.

## Hard rules for agents

1. Do not infer that a runtime switch is compiled merely because it exists in source; inspect the concrete setup/object directory.
2. Do not use split `MHD_8Wave` for Hall merely because Hall-named code exists there; the supplied source itself notes Hall MHD is not supported in that split implementation. Prefer the unsplit staggered-mesh path for the Extended-MHD workflows covered here.
3. Never copy a sample `flash.par` blindly. Resolve dimensionality, geometry, EOS/material model, boundaries, timestep constraints, I/O cadence, and enabled units for the actual problem.
4. Preserve the exact FLASH release and source revision in each run manifest.
