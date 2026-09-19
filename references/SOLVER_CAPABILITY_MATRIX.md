# Solver capability matrix

This is a routing guide, not a replacement for live version discovery.

| Solver/tool | Primary role in ScientificBrain | Canonical exchange |
|---|---|---|
| FLASH 4.8 | fluid plasma: ideal/resistive/Hall/Extended-MHD | HDF5 → yt adapter |
| WarpX | Hybrid-PIC and full kinetic PIC; MCC/DSMC where supported | openPMD |
| PIConGPU | GPU/HPC full kinetic PIC and large campaigns | openPMD |
| EDIPIC-2D | 2D low-temperature plasma PIC | adapter required |
| Geant4 | Monte Carlo particle passage through matter/radiation transport | scored-data adapter |
| PhysicsNeMo | surrogate/PINO/neural operators, distributed SciML, active learning | canonical dataset |

Routing must be based on physics scales, target observable, geometry, available diagnostics and compute—not solver popularity.

Official foundations:
- WarpX documentation: https://warpx.readthedocs.io/
- PIConGPU documentation: https://picongpu.readthedocs.io/
- EDIPIC-2D: https://github.com/PrincetonUniversity/EDIPIC-2D
- Geant4: https://geant4.web.cern.ch/
- openPMD: https://www.openpmd.org/
- PhysicsNeMo: https://docs.nvidia.com/physicsnemo/
