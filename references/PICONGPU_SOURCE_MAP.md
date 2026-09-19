# PIConGPU source map — inspected development snapshot

## openPMD

Verified anchor:
- `docs/source/usage/plugins/openPMD.rst`

The openPMD plugin is available when openPMD-api is compiled in. The inspected source documents:
- `--openPMD.period`
- `--openPMD.source`
- `--openPMD.range`
- `--openPMD.file`
- `--openPMD.ext`
- `--openPMD.infix`
- `--openPMD.backendConfig`
- `--checkpoint.openPMD.backendConfigRestart`
- `--openPMD.dataPreparationStrategy`
- `--openPMD.pluginConfig`
- `--openPMD.particleIOChunkSize`
- `--openPMD.writeAccess`

The inspected plugin documents ADIOS2 BP5/BP4, HDF5 and SST streaming choices through file extension/backend settings. It also documents double-buffer vs mapped-memory data preparation and asynchronous/streaming workflows.

## Validation/diagnostic plugins

Verified anchors:
- `docs/source/usage/plugins/chargeConservation.rst`
- `docs/source/usage/plugins/energyFields.rst`
- `docs/source/usage/plugins/energyParticles.rst`
- `docs/source/usage/plugins/phaseSpace.rst`
- `docs/source/usage/plugins/checkpoint.rst`
- `docs/source/usage/plugins/binningPlugin.rst`

Examples of verified command-line controls:
- `--chargeConservation.period`
- `--fields_energy.period`
- `--<species>_energy.period`
- phase-space period/filter/space/momentum/range/openPMD extension options.

Important source note: energy-reduction plugins explicitly warn that floating-point reductions can be non-deterministic and only accurate to a few percent in some configurations. ScientificBrain must not use them as exact conservation certificates.

## Collisions

Verified anchors:
- `docs/source/models/binary_collisions.rst`
- `include/picongpu/particles/collision/`
- `include/picongpu/param/collision.param`

The inspected tree contains relativistic binary collision implementations with constant or dynamically calculated Coulomb logarithms and support for collision pipelines/particle filters.
