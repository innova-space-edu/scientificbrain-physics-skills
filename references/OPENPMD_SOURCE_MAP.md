# openPMD-api source map — inspected development snapshot

Verified anchors:
- `include/openPMD/Series.hpp`
- `include/openPMD/Iteration.hpp`
- `include/openPMD/Streaming.hpp`
- `src/binding/python/openpmd_api/`
- `docs/source/usage/streaming.rst`
- `docs/source/usage/10_streaming_read.py`
- `docs/source/usage/10_streaming_write.py`
- `docs/source/backends/adios2.rst`
- `docs/source/backends/hdf5.rst`

The inspected API supports C++ and Python bindings and file-based or streaming-aware workflows.

For streaming, the inspected documentation uses linear access modes and `Series.snapshots()`; ADIOS2 is the streaming-enabled backend called out in the snapshot. Closed streaming iterations generally cannot be reopened.

ScientificBrain must preserve Series/Iteration metadata and should not flatten native openPMD into anonymous arrays before provenance is captured.
