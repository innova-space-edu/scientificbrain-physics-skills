# PhysicsNeMo source map — inspected 2.2.2 and main snapshots

## MHD PINO

Verified anchor:
- `examples/cfd/mhd_pino/`
- `examples/cfd/mhd_pino/README.md`
- `examples/cfd/mhd_pino/losses/mhd_pde.py`
- `examples/cfd/mhd_pino/train_mhd.py`
- `examples/cfd/mhd_pino/train_mhd_vec_pot.py`
- `examples/cfd/mhd_pino/train_mhd_vec_pot_tfno.py`

The inspected example implements incompressible MHD PINO with FNO/TFNO, data loss plus equation residuals, and optionally evolves magnetic vector potential to enforce div(B)=0 structurally.

It uses `physicsnemo.sym` PDE tooling in the current explicit-training-loop style.

## Active learning

Verified anchors:
- `examples/active_learning/`
- `examples/cfd/external_aerodynamics/active_learning_aero/`
- `physicsnemo.active_learning`

The inspected active-learning framework is organized around repeated training, metrology, query and labeling phases. Strategy protocols include QueryStrategy, LabelStrategy and MetrologyStrategy.

The aerodynamic example demonstrates uncertainty-aware querying and DDP, but plasma must replace the CFD-specific physics/metrology adapter.

## Distributed

Verified anchor:
- `docs/api/physicsnemo.distributed.rst`

The inspected API uses `physicsnemo.distributed.DistributedManager`, built on torch.distributed. Documented launch modes include torchrun, OpenMPI/mpirun and SLURM/srun.

Use DDP when the model fits per device; inspect model/domain parallel mechanisms for larger spatial models instead of copying LLM parallelism.
