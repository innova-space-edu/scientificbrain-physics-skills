---
name: multifidelity-plasma
description: Combine FLASH, Hybrid-PIC, full PIC, Geant4/transport, experiment, and validated surrogate data without pretending different fidelities are interchangeable; learn or quantify cross-fidelity discrepancy.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# Multi-Fidelity Plasma Modeling

## Instructions

1. Define fidelity levels by governing model and numerical resolution, not by vague labels such as low/high.
2. Identify overlapping inputs/observables and harmonize definitions/units.
3. Design paired/overlap runs where discrepancy can be measured.
4. Treat `u_high - u_low` (or another discrepancy representation) as a modeled quantity only after alignment and validation.
5. Preserve fidelity as an explicit feature/metadata field.
6. Prevent train/test leakage across paired runs and parameter neighborhoods.
7. Quantify bias and uncertainty by fidelity; do not let a large low-fidelity dataset dominate a small high-fidelity correction without diagnostics.
8. Route sample allocation to active learning when the value of another high-fidelity run can be estimated.

## Output

Fidelity graph, overlap design, discrepancy metrics/model, combined-data schema and acceptance limits.
