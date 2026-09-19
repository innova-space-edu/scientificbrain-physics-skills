# WarpX source map — inspected development snapshot

## Hybrid-PIC

Verified anchors:
- `Docs/source/theory/models_algorithms/kinetic_fluid_hybrid_model.rst`
- `Python/pywarpx/HybridPICModel.py`
- `Source/FieldSolver/FiniteDifferenceSolver/HybridPICModel/`
- `Source/FieldSolver/FiniteDifferenceSolver/HybridPICSolveE.cpp`
- `Source/FieldSolver/WarpXPushFieldsHybridPIC.cpp`
- `Docs/source/usage/parameters.rst`

The inspected implementation documents `algo.maxwell_solver = hybrid` and an Ohm-law electric field with kinetic ions and fluid electrons.

Verified runtime parameters include:
- `hybrid_pic_model.elec_temp` [eV]
- `hybrid_pic_model.n0_ref` [m^-3]
- `hybrid_pic_model.gamma`, default 5/3
- `hybrid_pic_model.plasma_resistivity(rho,J,t)` [ohm m]
- `hybrid_pic_model.plasma_hyper_resistivity(rho,B)` [ohm m^3]
- per-species `hybrid_pic_model.plasma_resistivity_<species>(...)`
- `hybrid_pic_model.solve_electron_energy_equation`
- `hybrid_pic_model.include_joule_heating`
- `hybrid_pic_model.joule_redirect_Te_threshold`
- `hybrid_pic_model.electron_ion_relaxation_rate(...)`
- `hybrid_pic_model.n_floor` [m^-3]
- `hybrid_pic_model.substeps`, default 10, with even-substep handling.

The theory document states that the B field advances with Faraday's law while E is obtained from generalized Ohm's law. Electron pressure can use a polytropic closure or the electron energy equation.

## MCC / DSMC

Verified anchors:
- `Docs/source/theory/multiphysics/collisions.rst`
- `Docs/source/usage/parameters.rst`
- `Examples/Physics_applications/capacitive_discharge/`
- `Examples/Tests/collision/`
- `Examples/Tests/ionization_dsmc/`
- `Source/Particles/Collision/`

Verified collision types include `background_mcc` and `dsmc`.

For MCC/DSMC the inspected parameters include:
- `collisions.collision_names`
- `<collision_name>.type`
- `<collision_name>.background_density` [m^-3] for background MCC
- `<collision_name>.background_temperature` [K]
- `<collision_name>.background_mass` [kg]
- `<collision_name>.scattering_processes`
- `<collision_name>.<process>_cross_section`
- `<collision_name>.<process>_energy` [eV]
- per-process scattering-angle model.

Cross-section files are documented as two-column energy [eV] vs cross-section [m^2] tables with strictly increasing energy.

Verified process names include elastic/excitation channels, electron ionization, ion charge exchange and two-product reactions depending on collision mode/species.

## openPMD

Verified anchors:
- `Docs/source/dataanalysis/openpmd.rst`
- `Docs/source/dataanalysis/openpmdapi.rst`
- `Docs/source/dataanalysis/openpmdviewer.rst`

WarpX documents openPMD output and analysis with openPMD-api/openPMD-viewer. Use the live diagnostics parameter documentation to configure actual output.
