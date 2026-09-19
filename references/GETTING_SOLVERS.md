# Obtaining the external solvers and frameworks

This repository does not redistribute third-party solvers. Install them from their canonical upstream projects and retain license/citation information.

## FLASH
FLASH has a licensed code-request/download process. See GETTING_FLASH.md.

## WarpX
Documentation: https://warpx.readthedocs.io/
Source: https://github.com/BLAST-WarpX/warpx

Follow the installation approach for the target CPU/GPU/HPC system and preserve the exact release/commit and build options.

## PIConGPU
Documentation: https://picongpu.readthedocs.io/
Source: https://github.com/ComputationalRadiationPhysics/picongpu

Use current build documentation for the target HPC system and verify openPMD support in the actual build.

## EDIPIC-2D
Source/documentation: https://github.com/PrincetonUniversity/EDIPIC-2D

The upstream repository documents PETSc/HYPRE/MPI requirements. Validate dependency versions against the actual checkout/toolchain.

## Geant4
Official site/download: https://geant4.web.cern.ch/

Preserve the chosen release, physics list, datasets and required citations.

## openPMD
Standard: https://www.openpmd.org/
API: https://github.com/openPMD/openPMD-api

Use installed producer/consumer versions in provenance because engines and streaming support can vary.

## NVIDIA PhysicsNeMo
Documentation: https://docs.nvidia.com/physicsnemo/
Source: https://github.com/NVIDIA/physicsnemo

ScientificBrain owns NVIDIA authentication/provider routing. This skill repository never stores NVIDIA credentials.

## Security / execution
Heavy solvers should execute on trusted local/HPC/worker infrastructure. ScientificBrain web clients must never submit arbitrary execution endpoints or raw credentials.
