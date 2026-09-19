# ScientificBrain Physics Skills

Agent skills for computational physics, initially focused on plasma physics, FLASH 4.8, scientific data analysis, and NVIDIA PhysicsNeMo.

**Developed in collaboration with Innova Space Edu SpA — 2026.** Agent-assisted design, implementation, review, and documentation used OpenAI models.

This repository follows the public NVIDIA Agent Skills pattern: each skill has a `SKILL.md` routing/instruction file and a `skill-card.md` governance card, with shared `references/`, `scripts/`, and evaluation cases. The repository deliberately does **not** redistribute FLASH source code. A local FLASH installation is supplied separately through `FLASH_ROOT`.

## Scope of v0.1.0

The initial toolkit contains 15 skills:

| Skill | Purpose |
|---|---|
| `plasma-regime` | Decide which physical description should be examined before simulation. |
| `plasma-dimensionless` | Calculate plasma/MHD dimensionless and scale-separation quantities. |
| `flash-discover` | Inspect a live FLASH tree instead of guessing units, tests, or runtime parameters. |
| `flash-setup` | Build reproducible FLASH setup commands and preflight dependencies. |
| `flash-run` | Launch, monitor, restart, and preserve provenance for a FLASH run. |
| `flash-sweep` | Generate controlled parameter sweeps without losing run provenance. |
| `flash-hdf5-yt` | Inspect FLASH HDF5 outputs and load/convert them with yt. |
| `flash-shock-analysis` | Extract shock position, speed, thickness, jumps, and field profiles. |
| `flash-extmhd` | Configure and audit resistive/Hall/Biermann/Nernst/Seebeck/cross-field physics. |
| `flash-validation` | Validate numerical convergence, div(B), conservation, and benchmark behavior. |
| `physicsnemo-plasma-discover` | Discover suitable PhysicsNeMo models/examples for plasma data shape and task. |
| `physicsnemo-flash-dataset` | Convert FLASH runs into ML-ready datasets with explicit metadata. |
| `physicsnemo-plasma-train` | Train physics-informed or data-driven surrogate models. |
| `physicsnemo-plasma-infer` | Run surrogate inference and quantify domain-of-validity/uncertainty signals. |
| `flash-physicsnemo-pipeline` | Orchestrate FLASH → HDF5 → yt → PhysicsNeMo → physical validation. |

## Core pipeline

```text
Scientific question
      ↓
plasma-regime + plasma-dimensionless
      ↓
FLASH setup / run / sweep
      ↓
FLASH HDF5 plotfiles + checkpoints
      ↓
yt analysis / uniform-grid extraction
      ↓
PhysicsNeMo dataset
      ↓
2D/3D surrogate
      ↓
physical + numerical validation against held-out FLASH runs
```

The surrogate never replaces the high-fidelity solver by assumption. It is accepted only inside a documented validation domain.

## Obtain FLASH

FLASH is distributed by the Flash Center for Computational Science and is **not redistributed by this repository**.

1. Go to the official FLASH Code Request page:
   https://flash.rochester.edu/site/flashcode/coderequest.html
2. Submit the requested registration/research information and accept the FLASH license agreement.
3. After approval, use the official download page with the credentials provided by the Flash Center:
   https://flash.rochester.edu/site/flashcode/download/
4. Extract the official source archive locally.
5. Point this toolkit to the installation:

```bash
export FLASH_ROOT=/path/to/FLASH4.8
python scripts/flash_inventory.py --flash-root "$FLASH_ROOT"
```

The Flash Center license controls access, use, redistribution, and publication acknowledgment requirements. Users must follow the current official license. For publications based on FLASH, consult the Code Request/license page for the exact acknowledgment requested by the Flash Center.

See `references/GETTING_FLASH.md` for the complete workflow.

## NVIDIA API integration

The NVIDIA API credential and runtime client belong to the **ScientificBrain core project**, not this skill repository.

```text
scientificbrain-physics-skills
          │ capability request
          ▼
     ScientificBrain
          │
          ├── NVIDIA hosted API / NIM
          ├── locally hosted NVIDIA NIM
          └── local PhysicsNeMo runtime
```

Skills describe the scientific operation and required capability. ScientificBrain will own authentication, secrets, endpoint selection, retries, telemetry, provider routing, and response normalization.

See `references/SCIENTIFICBRAIN_NVIDIA_API_CONTRACT.md`.

## Quick start

```bash
export FLASH_ROOT=/path/to/FLASH4.8
python scripts/flash_inventory.py --flash-root "$FLASH_ROOT"
python scripts/plasma_regime.py --ne 1e24 --B 2 --Te-ev 100 --Ti-ev 100 --A 1 --Z 1 --L 1e-3 --U 1e5
python scripts/validate_repo.py
```

## Design rules

1. **Discover, do not guess.** FLASH and PhysicsNeMo versions change.
2. **Physics before compute.** Estimate scales before choosing the model hierarchy.
3. **Separate solver truth from surrogate prediction.**
4. **2D and 3D are first-class.**
5. **No silent extrapolation.**
6. **No FLASH redistribution.**
7. **No provider secrets in skills.** NVIDIA/API credentials belong to ScientificBrain.

## Acknowledgements

This project gratefully acknowledges:

- the **Flash Center for Computational Science** for developing and maintaining FLASH;
- **NVIDIA** and the PhysicsNeMo/Agent Skills teams for the public scientific-ML frameworks and skill architecture that informed this project;
- the **yt Project** and broader scientific Python ecosystem for analysis and data tooling;
- **OpenAI**, whose models were used as agent-assisted tools during the design, implementation, review, and documentation of this toolkit;
- **Innova Space Edu SpA**, collaborating organization in the development of ScientificBrain Physics Skills during 2026.

These acknowledgements do not imply endorsement, sponsorship, or affiliation unless separately stated by the respective organization.

## External foundations

- NVIDIA Agent Skills: https://github.com/NVIDIA/skills
- NVIDIA PhysicsNeMo: https://github.com/NVIDIA/physicsnemo
- PhysicsNeMo documentation: https://docs.nvidia.com/physicsnemo/
- FLASH Center: https://flash.rochester.edu/site/flashcode/
- yt: https://yt-project.org/

## Status

`v0.1.0` is the plasma/FLASH foundation. Planned later extensions include PIC/hybrid routing, additional diagnostics, distributed simulation/training, active learning, and direct ScientificBrain orchestration.
