# PhysicsNeMo integration guidance

PhysicsNeMo changes rapidly. Do not hard-code a class/import path from memory. The `physicsnemo-plasma-discover` skill must inspect the live NVIDIA repository/package before emitting model or datapipe paths.

For plasma/FLASH tasks, data shape provides the first routing axis:

- regular Cartesian 2D/3D grids: neural-operator families such as FNO-style models are natural candidates;
- PDE-constrained regular-grid learning: inspect current PINO/physics-informed examples;
- unstructured mesh/block/graph data: inspect current mesh/graph/transformer families;
- temporal forecasting: inspect autoregressive/time-series examples that match the field topology.

A model family is a candidate, not a winner. Final selection depends on resolution, boundary representation, temporal formulation, memory, accuracy targets, conservation constraints, and training-data volume.

Official sources:

- https://github.com/NVIDIA/physicsnemo
- https://docs.nvidia.com/physicsnemo/
- https://github.com/NVIDIA/skills/tree/main/skills/physicsnemo-discover
