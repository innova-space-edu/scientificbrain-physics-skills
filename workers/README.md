# Solver image / worker contract

These files describe how external solver images should integrate with ScientificBrain.

The main ScientificBrain repository owns job submission, authentication, Google Cloud Batch integration and the public web UI.

A solver image is intentionally **not** allowed to receive an arbitrary shell command from the browser. Its default ENTRYPOINT should be fixed by the image and should:

1. decode and validate `SCIBRAIN_JOB_JSON_B64`;
2. verify the solver identity expected by that image;
3. fetch the input artifact from `SCIBRAIN_INPUT_URI`;
4. generate or select a solver input using the job's validated scientific parameters;
5. run the solver;
6. preserve logs/checkpoints/native output;
7. run required diagnostics/validation;
8. upload results to `SCIBRAIN_OUTPUT_URI`;
9. write `scientificbrain-output.json`.

See `SOLVER_CONTAINER_CONTRACT.md`.

FLASH is excluded from public image recipes because the FLASH source has separate access/license terms.
