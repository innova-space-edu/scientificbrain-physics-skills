# Geant4 source map — inspected v11.4.2 snapshot

## Basic application anchor

- `examples/basic/B1/README.md`

B1 demonstrates geometry/material definition, a reference physics list (QBBC in that example), primary generation, scoring of energy deposition/dose, multithreaded accumulation and batch macro execution.

ScientificBrain should use B1 as a structural tutorial, not as a physics-list recommendation for unrelated problems.

## Space-radiation anchor

- `examples/advanced/gorad/README`
- `examples/advanced/gorad/`

GORAD is an advanced Geant4 application for radiation analysis and spacecraft design. The inspected example uses GDML geometry, UI/macro configuration, dose/flux scorers and demonstrates large-event Monte Carlo workflows.

## Electromagnetic validation anchors

- `examples/extended/electromagnetic/TestEm0/`
- `examples/extended/electromagnetic/TestEm1/`

These provide electromagnetic-process examples and validation patterns.

## Routing rule

Geant4 is for transport/interactions of particles in matter, detector response, shielding and radiation analysis. It is not a replacement for self-consistent plasma PIC.

Always resolve the exact installed version, datasets, reference/custom physics list, production cuts, random-engine/seed policy, geometry/material definitions and scoring before a production run.
