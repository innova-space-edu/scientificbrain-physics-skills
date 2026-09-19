# Physical and numerical validation

Validation is problem-dependent. The following is a minimum checklist, not a universal acceptance certificate.

## FLASH run validation

- demonstrate resolution sensitivity / convergence for the target observable;
- monitor CFL/timestep behavior and solver failures;
- inspect `∇·B` relative to an appropriate magnetic-field gradient scale;
- check conserved quantities when the selected physics and boundaries imply conservation;
- validate known benchmarks when introducing a new numerical configuration;
- separate numerical diffusion from physical resistivity/conductivity;
- verify that selected transport/Extended-MHD terms are actually compiled and enabled;
- record boundary conditions and AMR refinement criteria.

## Shock observables

For shock studies, candidates include:

- front location `R_s(t)` or `x_s(t)`;
- shock speed `v_s(t)`;
- shock thickness `L_shock` with a stated operational definition;
- upstream/downstream density, pressure, temperature, flow and magnetic jumps;
- current density and electric-field terms where available;
- Alfvénic/sonic Mach numbers and plasma beta;
- ratios of nonideal terms such as Hall vs resistive contributions when they can be computed consistently.

## Surrogate validation

At minimum compare held-out FLASH data using per-field RMSE/NRMSE plus physics diagnostics. For MHD fields also evaluate divergence error. For trajectory models measure error growth with rollout horizon. Report performance across the parameter domain, not only an aggregate mean.

Never interpret a low data loss as evidence that the learned solution obeys a PDE unless residuals/conservation constraints were explicitly evaluated.
