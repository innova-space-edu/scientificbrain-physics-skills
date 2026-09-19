# EDIPIC-2D source map — inspected main snapshot

Verified root README states that EDIPIC-2D is a 2D particle-in-cell code for low-temperature plasma applications.

## Build/runtime anchors

- `README.md`
- `Instructions/installing_edipic2d.md`
- `Instructions/running_edipic2d.md`
- `Instructions/installing_PETSc.md`
- `src/`

The inspected installation guide requires:
- Fortran compiler (Intel or GNU paths are documented)
- MPI
- PETSc
- HYPRE
- BLAS/LAPACK.

The distributed field equations are described as using HYPRE multigrid as a preconditioner and GMRES through PETSc.

Build pattern in the inspected tree:
- set `PETSC_DIR`
- add `PETSC_DIR/lib` to `LD_LIBRARY_PATH`
- run `make` under `src`
- executable: `edipic2d`.

## Input structure

The inspected repository contains multiple complete input directories. Common files include:
- `init_configuration.dat`
- `init_extfields.dat`
- `init_particles.dat`
- `init_neutrals.dat`
- `init_simcontrol.dat`
- `init_snapshots.dat`
- `init_probes.dat`
- material/boundary object files
- neutral cross-section files such as `init_neutral_*_crsect_*.dat`
- `petsc.rc`.

The run guide recommends copying a complete example directory, then adapting parameters, rather than inventing a run directory from scratch.

## HPC

The inspected run guide provides SLURM and direct MPI examples and notes that EDIPIC-2D is an MPI code. Resource counts are examples, not universal defaults.
