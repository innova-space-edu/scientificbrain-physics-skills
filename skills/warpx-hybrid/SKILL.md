---
name: warpx-hybrid
description: Configure and validate WarpX Hybrid-PIC where ions are kinetic and electrons are modeled as a neutralizing fluid with an Ohm-law electric-field closure.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.1
  tags:
    - physics
    - plasma
    - scientificbrain
---

# WarpX Hybrid-PIC

Use only after `kinetic-validity` supports kinetic ions with a fluid-electron treatment.

## Instructions

- Verify the current WarpX Hybrid-PIC implementation and parameters from the live version.
- Resolve ion inertial/cyclotron scales and target them in mesh/timestep design.
- Document the electron pressure/closure assumptions and generalized Ohm-law terms actually enabled.
- Define ion distribution initialization, boundaries and diagnostics.
- Compare at least one overlap case against FLASH Hall/Extended-MHD where both models should apply.
- If electron kinetics, sheaths or pressure-tensor physics control the observable, escalate to full PIC instead of stretching the hybrid model.

## Output

Hybrid closure, resolved ion scales, input configuration, diagnostics, overlap-validation plan and domain of validity.

## Source-grounded anchors

Validated against the inspected WarpX development tree. Before generating a deck, verify:
- `Docs/source/theory/models_algorithms/kinetic_fluid_hybrid_model.rst`
- `Docs/source/usage/parameters.rst`
- `Python/pywarpx/HybridPICModel.py`
- `Source/FieldSolver/FiniteDifferenceSolver/HybridPICModel/`

The inspected source documents `algo.maxwell_solver = hybrid` plus `hybrid_pic_model.elec_temp`, `n0_ref`, `gamma`, resistivity/hyper-resistivity, `n_floor`, and B-field `substeps`. It also contains optional electron-energy evolution, Joule heating and electron-ion relaxation. Do not emit these controls unless the installed checkout still contains them.

See `../../references/WARPX_SOURCE_MAP.md`.
