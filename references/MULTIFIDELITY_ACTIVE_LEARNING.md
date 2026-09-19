# Multi-fidelity + active learning

ScientificBrain treats solver fidelity as a decision variable.

Example hierarchy:
FLASH MHD → FLASH Extended-MHD → WarpX Hybrid-PIC → WarpX/PIConGPU full PIC.

Geant4 belongs to a different transport branch and may couple to plasma results through source/material conditions rather than being a simple higher fidelity.

An active-learning iteration should select:
1. parameter point;
2. governing-model fidelity;
3. numerical resolution;
4. expected information value;
5. compute cost.

The loop is accepted only if it improves held-out scientific metrics relative to a non-adaptive baseline and does not hide failed solver regions.
