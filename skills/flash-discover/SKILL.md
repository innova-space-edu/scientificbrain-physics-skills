---
name: flash-discover
description: Inspect a live FLASH source/object tree to find the exact units, example problems, runtime parameters, and version-specific capabilities needed for plasma/MHD work; never name a FLASH path from memory when it can be verified.
license: Apache-2.0
metadata:
  author: Innova Space Education / ScientificBrain
  version: 0.1.0
  tags:
    - physics
    - plasma
    - scientificbrain
---

# FLASH Discover

FLASH is version- and setup-dependent. Discover from the live tree.

## Instructions

1. Resolve `FLASH_ROOT`; verify `RELEASE`, the setup entry point, `source/`, and site configuration.
2. Run `python ../../scripts/flash_inventory.py --flash-root "$FLASH_ROOT"` as a quick inventory.
3. For MHD/Extended-MHD inspect the live unsplit staggered-mesh Config and relevant material-property/Diffuse units. Search runtime parameter documentation generated in the tree if available.
4. Inspect the exact simulation `Config` and `flash.par` closest to the intended benchmark, but do not copy it wholesale.
5. Report whether each required capability is merely present in source, requested by a simulation Config, or actually present in the built object directory. These are different states.
6. Prefer self-documentation (`Config`, release notes, runtime parameter docs, example setup comments) over remembered syntax.

## FLASH 4.8 anchor

The supplied 4.8 tree used to develop this toolkit is summarized in `../../references/FLASH48_CAPABILITIES.md`. Treat it as a map, not proof about another installation.

## Output

Return verified version, paths inspected, candidate benchmark/example, required units/setup flags, and unresolved dependencies.
