# Canonical Plasma Data Model v0.2

The canonical layer unifies analysis without erasing solver identity.

## Identity / provenance
- solver and governing model;
- version/commit/build;
- run/sample ID;
- geometry/dimensionality;
- parameter vector and units;
- random seed(s);
- mesh/timestep/refinement;
- execution resources.

## Fields
- E, B, J, charge density;
- number/mass density;
- velocity/momentum;
- pressure/temperature tensor or scalar moments when defined.

## Particles
- species identity;
- position/momentum;
- weighting;
- selected particle attributes;
- filters/sampling policy.

## Derived diagnostics
- plasma beta, Mach numbers;
- skin/debye/gyro scales;
- shock observables;
- field/particle energy;
- divergence/charge-conservation metrics;
- distribution/anisotropy diagnostics.

## Storage

Use native openPMD for WarpX/PIConGPU when possible. Preserve native FLASH HDF5 and map via yt. EDIPIC-2D and Geant4 require adapters. Derived ML tensors must point back to immutable native records.

Never coerce a missing physical quantity to zero merely to align solver schemas.
