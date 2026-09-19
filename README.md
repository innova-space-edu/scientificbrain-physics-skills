# ScientificBrain Physics Skills

Agent skills for computational physics, centered on plasma physics and a multi-fidelity stack spanning fluid, hybrid, kinetic/PIC, Monte Carlo transport, diagnostics, uncertainty quantification, and scientific machine learning.

**Developed in collaboration with Innova Space Edu SpA — 2026.** Agent-assisted design, implementation, review, and documentation used OpenAI models.

The repository follows the public NVIDIA Agent Skills pattern: each skill contains a SKILL.md instruction/routing file plus a skill-card.md. External solvers are referenced, not redistributed.

## Used by ScientificBrain

This toolkit is the physics capability layer used by the main **ScientificBrain** project.

- ScientificBrain repository: https://github.com/innova-space-edu/ScientificBrain
- Public ScientificBrain application: https://scientific-brain.vercel.app
- Scientific tools workspace: https://scientific-brain.vercel.app/scientific-tools

ScientificBrain provides the user-facing orchestration layer, authentication, NVIDIA/provider routing, Monte Carlo utilities, safe job manifests, and remote/HPC/Google Cloud Batch dispatch. FLASH can use the same Google Cloud backend through a private licensed image. This repository provides the scientific routing, solver-specific skills, diagnostics, validation rules, source-grounded references, and multi-fidelity logic.

See `references/SCIENTIFICBRAIN_INTEGRATION.md` for the current integration contract and `references/GOOGLE_CLOUD_EXECUTION.md` for the Google Cloud Batch execution path.

## v0.2.1 — 39 skills

The toolkit now routes across:

Scientific question
→ physics / scale / closure assessment
→ FLASH fluid MHD/Extended-MHD
→ WarpX Hybrid-PIC
→ WarpX / PIConGPU full kinetic PIC
→ EDIPIC-2D for low-temperature 2D cases when appropriate

Parallel branches add WarpX MCC/DSMC, Monte Carlo parameter and uncertainty propagation, and Geant4 particle-through-matter transport.

All solver output then flows through HDF5/yt, openPMD or explicit adapters into canonical diagnostics, validation, multi-fidelity datasets, PhysicsNeMo surrogate training, uncertainty quantification and active learning. ScientificBrain can then choose the next parameter point, fidelity and solver.

See skills/README.md for all 39 skills.

## Core design

### Model routing before solver routing

ScientificBrain evaluates target observable, closure assumptions, Debye/skin/gyro scales, collisionality, distribution-function requirements, geometry and computational budget before selecting a solver.

Candidate hierarchy:

- FLASH — ideal/resistive/Hall/Extended-MHD fluid plasma.
- WarpX Hybrid-PIC — kinetic ions with fluid electrons where justified.
- WarpX full PIC — general full kinetic PIC and MCC/DSMC workflows.
- PIConGPU — GPU/HPC-scale kinetic PIC campaigns.
- EDIPIC-2D — low-temperature 2D PIC applications.
- Geant4 — Monte Carlo passage of particles through matter/radiation transport.
- PhysicsNeMo — surrogate models, SciML, distributed training and active learning.

### Canonical data layer

WarpX and PIConGPU can exchange particle/mesh data using openPMD. FLASH remains in native HDF5 and is interpreted through yt. EDIPIC-2D and Geant4 use explicit adapters. Native output is preserved; ML tensors never become the only copy.

### Monte Carlo and uncertainty

The toolkit distinguishes MCC, DSMC, Monte Carlo parameter sampling, Monte Carlo uncertainty propagation, Geant4 transport Monte Carlo, stochastic/PIC noise, numerical error, surrogate error and model-form/fidelity discrepancy.

### Multi-fidelity and active learning

ScientificBrain can choose both the next parameter point and the next fidelity level. A campaign may use many FLASH runs, fewer Hybrid-PIC runs, a smaller number of full-PIC runs, and experimental/transport data where appropriate. PhysicsNeMo active learning can propose new expensive labels subject to physical validity and cost.

## Helper scripts

Existing and new helpers include:
- scripts/plasma_regime.py
- scripts/plasma_model_router.py
- scripts/canonical_run_manifest.py
- scripts/monte_carlo_sampling.py
- scripts/uq_summary.py
- scripts/flash_inventory.py
- scripts/flash_to_npz.py
- scripts/validate_surrogate.py

## External software

See references/GETTING_SOLVERS.md, references/GETTING_FLASH.md, references/SOLVER_CAPABILITY_MATRIX.md, references/CANONICAL_PLASMA_DATA.md, references/MONTE_CARLO_UQ.md, references/MULTIFIDELITY_ACTIVE_LEARNING.md and references/HPC_EXECUTION.md.

## ScientificBrain / NVIDIA boundary

ScientificBrain owns credentials, allowed endpoints, remote/HPC worker routing, job state, telemetry and provenance. Skills express scientific intent and validation requirements. The browser never receives solver/provider secrets.

## Design rules

1. Physics before compute.
2. Discover live solver/version capabilities instead of guessing.
3. Model hierarchy before fidelity escalation.
4. Benchmark before scale-up.
5. Separate native solver output from derived ML datasets.
6. Keep stochastic seeds and sample manifests.
7. Do not confuse space-filling sampling with probabilistic uncertainty.
8. Preserve solver/fidelity identity in every combined dataset.
9. No silent surrogate extrapolation.
10. No credentials or arbitrary execution URLs in skills.

## Acknowledgements

This project acknowledges the Flash Center, WarpX/BLAST collaboration, PIConGPU community, Princeton/PPPL EDIPIC developers, Geant4 Collaboration, openPMD community, NVIDIA PhysicsNeMo/Agent Skills teams, yt Project, OpenAI, and the broader scientific-computing community. See ACKNOWLEDGEMENTS.md.

These acknowledgements do not imply endorsement or sponsorship.

## Status

v0.2.1 implements the previous roadmap items: PIC/hybrid routing, additional diagnostics, distributed simulation/training, active learning and direct ScientificBrain orchestration. It additionally introduces Monte Carlo/MCC/DSMC, Geant4 transport, uncertainty quantification, canonical openPMD data handling and multi-fidelity modeling.

Next work is execution infrastructure: concrete worker/HPC adapters, solver-specific benchmark bundles, richer synthetic diagnostics and automated cross-solver regression suites.
