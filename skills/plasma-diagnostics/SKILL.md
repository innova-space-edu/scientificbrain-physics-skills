---
name: plasma-diagnostics
description: Design solver-independent field, particle, shock, energy, collision, phase-space and synthetic diagnostics with explicit definitions, units, cadence, resolution and uncertainty.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.2.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# Plasma Diagnostics

## Diagnostic families

Fields: E, B, J, charge density, potentials.
Fluid moments: density, flow, pressure/temperature tensors.
Particles: phase space, velocity/energy distributions, beams/tails, anisotropy.
Shock: front, speed, thickness, jumps, Mach numbers.
Energy: field, thermal, kinetic and source/sink budgets.
Collisions: event/reaction counts and rate estimates.
Numerical: div(B), Gauss-law/charge conservation, residuals/noise.
Synthetic: diagnostics derived to emulate a planned instrument when the forward model is explicitly defined.

## Instructions

For every diagnostic record definition, algorithm, coordinate frame, units, cadence, spatial/temporal resolution, filtering/binning and uncertainty. Avoid deriving the same named quantity differently across solvers without marking the definition.

## Output

A canonical diagnostic plan that can be mapped to FLASH, WarpX, PIConGPU, EDIPIC-2D and experiment data.
