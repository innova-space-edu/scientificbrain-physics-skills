# Source-grounded solver maps

The v0.2.1 skill instructions were checked against source snapshots of WarpX development, PIConGPU development, EDIPIC-2D main, Geant4 11.4.2, PhysicsNeMo 2.2.2/main and openPMD-api development.

The repository does **not** redistribute those sources. These maps tell an agent where to verify behavior in a local checkout.

## Rule

A path listed here is an anchor from an inspected snapshot, not proof that every future release retains that exact path. A skill must first resolve the installed version and then verify the path/parameter before use.

See the per-project source maps:
- WARPX_SOURCE_MAP.md
- PICONGPU_SOURCE_MAP.md
- EDIPIC2D_SOURCE_MAP.md
- GEANT4_SOURCE_MAP.md
- PHYSICSNEMO_SOURCE_MAP.md
- OPENPMD_SOURCE_MAP.md
