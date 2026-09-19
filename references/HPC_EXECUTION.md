# HPC / remote execution contract

ScientificBrain web/API processes should not run heavy FLASH, WarpX, PIConGPU, EDIPIC-2D, Geant4 or large PhysicsNeMo jobs synchronously.

A worker submission includes:
- immutable job ID;
- solver/tool and exact version/image;
- input artifact hashes;
- resource request (CPU/GPU/RAM/wall time);
- launcher/scheduler profile;
- output/checkpoint destination;
- expected diagnostics;
- validation gates.

Workers return signed/traceable status plus output manifests. Browser clients never provide arbitrary worker URLs or credentials. Endpoint allowlists and secrets belong to ScientificBrain server configuration.
