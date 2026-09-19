---
name: flash-hdf5-yt
description: Load, inspect, visualize, and convert FLASH HDF5 plot/checkpoint data with yt while respecting AMR/block topology, field units, geometry, and extraction level.
license: Apache-2.0
metadata:
  author: Innova Space Education / ScientificBrain
  version: 0.1.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# FLASH HDF5 + yt

## Instructions

1. Prefer `yt.load()` for FLASH plotfiles/checkpoints. Do not assume raw HDF5 dataset names encode the physical topology correctly.
2. Inspect `ds.field_list`, derived fields, geometry, dimensionality, domain bounds, current time, units, and refinement structure before analysis.
3. Resolve requested physical fields by verified yt field identifiers. Keep the mapping in metadata.
4. For neural operators on regular grids, explicitly choose a covering-grid level and record interpolation/refinement policy. Use `../../scripts/flash_to_npz.py` as a minimal exporter.
5. For AMR-aware/mesh models, preserve block/mesh connectivity instead of flattening to a uniform grid.
6. Visualizations must state slice/projection direction, coordinate, time, units, and color normalization. Avoid comparing images with inconsistent normalization as if quantitative.
7. Never use checkpoint files as interchangeable with plotfiles without inspecting contained variables.

## Output

Dataset summary, verified field map, geometry/refinement information, requested plots/statistics, and exported dataset/metadata paths.
