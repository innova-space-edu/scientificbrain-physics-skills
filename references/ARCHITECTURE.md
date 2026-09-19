# Architecture

## Layers

```text
ScientificBrain (later integration)
  └─ ScientificBrain Physics Skills
      ├─ Physics reasoning layer
      │   ├─ plasma-regime
      │   └─ plasma-dimensionless
      ├─ High-fidelity solver layer
      │   ├─ flash-discover / setup / run / sweep
      │   └─ flash-extmhd
      ├─ Analysis layer
      │   ├─ flash-hdf5-yt
      │   ├─ flash-shock-analysis
      │   └─ flash-validation
      └─ SciML layer
          ├─ physicsnemo-plasma-discover
          ├─ physicsnemo-flash-dataset
          ├─ physicsnemo-plasma-train
          ├─ physicsnemo-plasma-infer
          └─ flash-physicsnemo-pipeline
```

## Responsibility boundaries

FLASH remains the high-fidelity PDE solver. yt is the primary FLASH-aware data reader/analysis bridge. PhysicsNeMo supplies SciML architectures and infrastructure. This repository supplies agent routing, scientific checks, dataset contracts, reproducibility, and orchestration.

A surrogate prediction is never labeled equivalent to FLASH solely because loss decreased. Acceptance requires held-out comparisons plus physical diagnostics appropriate to the problem.
