## Description
Plan PhysicsNeMo/PyTorch distributed scientific-ML training and inference using current distributed utilities, matching strategy to 2D/3D meshes, graphs, model size and memory rather than copying LLM parallelism.

## Owner
Innova Space Edu SpA / ScientificBrain

## License / terms
Apache-2.0 for this skill text. External solvers, data and frameworks retain their own licenses, citations and access terms.

## Use case
Use when ScientificBrain needs this capability as part of a reproducible computational-physics workflow.

## Known risks and mitigations
- Scientific/numerical validity is problem-dependent; require explicit acceptance criteria.
- Remote/HPC execution must use server-configured endpoints and credentials.
- Stochastic results require seed/sample-count/statistical convergence records.
- Cross-fidelity data must retain model identity and discrepancy.

## Version
0.2.0
