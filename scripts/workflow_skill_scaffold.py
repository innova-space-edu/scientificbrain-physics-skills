#!/usr/bin/env python3
"""Create a reviewable skill scaffold from a validated workflow description.

This helper deliberately does not register, publish or overwrite a skill.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def build_files(name: str, description: str, dependencies: list[str]) -> dict[str, str]:
    if not NAME_RE.fullmatch(name) or len(name) > 64:
        raise ValueError("name must be lowercase kebab-case and at most 64 characters")
    if not description.strip() or len(description) > 1024:
        raise ValueError("description must be 1..1024 characters")
    dep_lines = "\n".join(f"- {d}" for d in dependencies) or "- None yet; verify existing skills before implementation."
    skill = f"""---
name: {name}
description: {description.strip()}
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.1.0-draft
  tags:
    - physics
    - scientificbrain
    - draft
---

# {name}

## Scope

Distill only a workflow that has already been executed and validated. Define the reusable scientific purpose here.

## Dependencies

{dep_lines}

## Inputs

- Define required physical quantities, artifacts, units, versions and provenance.

## Workflow

1. Reconstruct the validated workflow and identify strict versus flexible steps.
2. Reuse existing skills instead of reimplementing them.
3. Preserve solver/model versions, parameters, seeds and acceptance criteria.
4. Route failures explicitly; never silently substitute a different physical model.
5. Run unit, workflow and capability evaluations before promotion.

## Outputs

- Define structured outputs and provenance.

## Guardrails

- Do not promote this draft to stable without independent review and evaluation evidence.
- Do not generalize beyond the physical regime demonstrated by the source workflow.
- Do not fabricate missing parameters, citations, benchmark results or validation evidence.

## Evaluation

Add at least one positive case, one negative-routing case and one end-to-end capability case.
"""
    card = f"""# Skill card: {name}

- Status: draft
- Purpose: {description.strip()}
- Dependencies: {", ".join(dependencies) if dependencies else "to be reviewed"}
- Promotion gate: independent scientific review + unit/workflow/capability evaluations
- Non-goal: automatic self-registration or silent replacement of existing skills
"""
    return {"SKILL.md": skill, "skill-card.md": card}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--depends-on", action="append", default=[])
    parser.add_argument("--output-root", default="skills")
    parser.add_argument("--write", action="store_true", help="write files; default is dry-run JSON")
    args = parser.parse_args()
    files = build_files(args.name, args.description, args.depends_on)
    target = Path(args.output_root) / args.name
    if not args.write:
        print(json.dumps({"target": str(target), "files": sorted(files), "status": "dry-run"}, indent=2))
        return
    if target.exists():
        raise SystemExit(f"refusing to overwrite existing path: {target}")
    target.mkdir(parents=True)
    for filename, content in files.items():
        (target / filename).write_text(content, encoding="utf-8")
    print(json.dumps({"target": str(target), "files": sorted(files), "status": "created"}, indent=2))


if __name__ == "__main__":
    main()
