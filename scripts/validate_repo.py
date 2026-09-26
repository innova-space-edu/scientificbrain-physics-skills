#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
skills = root / "skills"
errors: list[str] = []

dirs = sorted(p for p in skills.iterdir() if p.is_dir())
for directory in dirs:
    skill_file = directory / "SKILL.md"
    card = directory / "skill-card.md"
    if not skill_file.exists():
        errors.append(f"{directory.name}: missing SKILL.md")
        continue
    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{directory.name}: missing YAML frontmatter")
    if f"name: {directory.name}" not in text:
        errors.append(f"{directory.name}: frontmatter name mismatch")
    if "description:" not in text:
        errors.append(f"{directory.name}: missing description")
    if not card.exists():
        errors.append(f"{directory.name}: missing skill-card.md")

required_v03 = {
    "physics-model-router",
    "physics-validator",
    "simulation-orchestrator",
    "workflow-skill-creator",
    "physics-literature",
}
missing_v03 = sorted(required_v03 - {d.name for d in dirs})
if missing_v03:
    errors.append("missing v0.3 skills: " + ", ".join(missing_v03))

if len(dirs) < 44:
    errors.append(f"expected at least 44 skills, found {len(dirs)}")

for filename in [
    "routing-cases.json",
    "unit-cases.json",
    "workflow-cases.json",
    "capability-cases.json",
]:
    path = root / "evals" / filename
    if not path.exists():
        errors.append(f"missing evals/{filename}")
        continue
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"evals/{filename}: invalid JSON: {exc}")

print(f"skills={len(dirs)} errors={len(errors)}")
for error in errors:
    print("ERROR", error)
sys.exit(1 if errors else 0)
