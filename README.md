# ScientificBrain Physics Skills

Agent skills for computational physics, centered on plasma physics and a multi-fidelity stack spanning theory/reduced models, fluid, hybrid, kinetic/PIC, Monte Carlo transport, diagnostics, uncertainty quantification, scientific machine learning, validation and reproducible workflow orchestration.

**Developed in collaboration with Innova Space Edu SpA — 2026.** Agent-assisted design, implementation, review, and documentation used OpenAI models.

The repository follows a modular agent-skill pattern influenced by the public NVIDIA Agent Skills ecosystem and, from v0.3, selected architectural principles from Google DeepMind Science Skills: focused SKILL.md capabilities, helper scripts for deterministic work, dependency reuse, explicit guardrails and evaluation as part of the skill contract. External solvers are referenced, not redistributed.

See references/SCIENCE_SKILLS_INTEGRATION.md for the exact scope of that influence.

## Used by ScientificBrain

This toolkit is the physics capability layer used by the main **ScientificBrain** project.

- ScientificBrain repository: https://github.com/innova-space-edu/ScientificBrain
- Public ScientificBrain application: https://scientific-brain.vercel.app
- Scientific tools workspace: https://scientific-brain.vercel.app/scientific-tools

ScientificBrain provides the user-facing orchestration layer, authentication, provider routing, safe job manifests, research state and remote/HPC/Google Cloud Batch dispatch. FLASH can use the same Google Cloud backend through a private licensed image. This repository provides scientific routing, solver-specific skills, diagnostics, validation rules, source-grounded references, multi-fidelity logic and reusable physics workflow contracts.

See references/SCIENTIFICBRAIN_INTEGRATION.md for the current integration contract and references/GOOGLE_CLOUD_EXECUTION.md for the Google Cloud Batch execution path.

## v0.3.0 — 44 skills

v0.3 adds five high-level skills:

- physics-model-router — choose the smallest adequate model family before selecting a solver;
- physics-validator — independent observable-level validation gate;
- simulation-orchestrator — turn an accepted model hierarchy into a benchmark/overlap/production/validation DAG;
- workflow-skill-creator — distill completed validated workflows into draft reusable skills;
- physics-literature — physics-specific arXiv/OpenAlex/DOI evidence mapping through ScientificBrain.

The toolkit routes across:

Scientific question
→ literature / evidence map
→ target observable + acceptance criterion
→ physics model hierarchy
→ plasma scale / closure / kinetic assessment when applicable
→ FLASH fluid MHD/Extended-MHD
→ WarpX Hybrid-PIC
→ WarpX / PIConGPU full kinetic PIC
→ EDIPIC-2D for low-temperature 2D cases
→ Geant4 for particle-through-matter transport
→ diagnostics + uncertainty
→ independent observable-level validation
→ optional PhysicsNeMo surrogate / active learning
→ reusable validated workflow skill when appropriate

See skills/README.md for all 44 skills.

## Core design

### Model routing before solver routing

ScientificBrain evaluates the target observable, governing equations, closure assumptions, characteristic scales, collisionality, distribution-function requirements, geometry, uncertainty target and computational budget before selecting a solver.

For plasma problems the detailed hierarchy remains:

- FLASH — ideal/resistive/Hall/Extended-MHD fluid plasma.
- WarpX Hybrid-PIC — kinetic ions with fluid electrons where justified.
- WarpX full PIC — full kinetic PIC and MCC/DSMC workflows.
- PIConGPU — GPU/HPC-scale kinetic PIC campaigns.
- EDIPIC-2D — low-temperature 2D PIC applications.
- Geant4 — Monte Carlo particle/radiation transport through matter.
- PhysicsNeMo — surrogate/SciML acceleration only after validated reference data exist.

### Independent validation

Solver-specific validation is followed by physics-validator. Acceptance is attached to an observable/claim and regime, never to a simulation globally. Missing required evidence yields blocked, not pass.

### Three-layer evaluation

The repository now carries:

1. unit cases — local routing/skill behavior;
2. workflow cases — multi-skill scientific workflows;
3. capability cases — end-to-end research tasks.

The older routing-cases.json remains as a compact compatibility set. scripts/eval_contracts.py validates the three-layer case contracts in CI.

### Canonical data layer

WarpX and PIConGPU can exchange particle/mesh data using openPMD. FLASH remains in native HDF5 and is interpreted through yt. EDIPIC-2D and Geant4 use explicit adapters. Native output is preserved; ML tensors never become the only copy.

### Monte Carlo and uncertainty

The toolkit distinguishes MCC, DSMC, Monte Carlo parameter sampling, Monte Carlo uncertainty propagation, Geant4 transport Monte Carlo, stochastic/PIC noise, numerical error, surrogate error and model-form/fidelity discrepancy.

### Multi-fidelity and active learning

ScientificBrain can choose both the next parameter point and the next fidelity level. A campaign may use many FLASH runs, fewer Hybrid-PIC runs, a smaller number of full-PIC runs, and experimental/transport data where appropriate. PhysicsNeMo active learning can propose new expensive labels subject to physical validity and cost.

## Helper scripts

Helpers include:

- scripts/plasma_regime.py
- scripts/plasma_model_router.py
- scripts/physics_model_router.py
- scripts/validation_gate.py
- scripts/workflow_skill_scaffold.py
- scripts/eval_contracts.py
- scripts/canonical_run_manifest.py
- scripts/monte_carlo_sampling.py
- scripts/uq_summary.py
- scripts/flash_inventory.py
- scripts/flash_to_npz.py
- scripts/validate_surrogate.py

## External software

See references/GETTING_SOLVERS.md, references/GETTING_FLASH.md, references/SOLVER_CAPABILITY_MATRIX.md, references/CANONICAL_PLASMA_DATA.md, references/MONTE_CARLO_UQ.md, references/MULTIFIDELITY_ACTIVE_LEARNING.md and references/HPC_EXECUTION.md.

## ScientificBrain boundary

ScientificBrain owns credentials, allowed endpoints, remote/HPC worker routing, job state, telemetry and provenance. Skills express scientific intent, model selection and validation requirements. The browser never receives solver/provider secrets.

## Design rules

1. Physics before compute.
2. Observable and acceptance criterion before model selection.
3. Smallest adequate model before fidelity escalation.
4. Discover live solver/version capabilities instead of guessing.
5. Benchmark and overlap before scale-up.
6. Separate solver completion from scientific validation.
7. Validate claims/observables, not simulations globally.
8. Separate native solver output from derived ML datasets.
9. Keep stochastic seeds and sample manifests.
10. Preserve solver/fidelity identity in every combined dataset.
11. No silent surrogate extrapolation.
12. No credentials or arbitrary execution URLs in skills.
13. Reuse existing skills before creating new ones.
14. Generated workflow skills remain draft until independently reviewed and evaluated.

## Acknowledgements

This project acknowledges the Flash Center, WarpX/BLAST collaboration, PIConGPU community, EDIPIC developers, Geant4 Collaboration, openPMD community, NVIDIA PhysicsNeMo/Agent Skills teams, Google DeepMind Science Skills, yt Project, OpenAI, and the broader scientific-computing community. See ACKNOWLEDGEMENTS.md.

These acknowledgements do not imply endorsement or sponsorship.

## Status

v0.3.0 adds the high-level physics model router, independent validator, simulation execution-graph layer, physics literature protocol, workflow-to-skill distillation and three-level evaluation contracts.

Next work is deeper automated execution evaluation: solver benchmark bundles, cross-solver regression artifacts, richer synthetic diagnostics and scored agent runs over the unit/workflow/capability cases.
