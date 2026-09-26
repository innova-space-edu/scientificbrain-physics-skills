#!/usr/bin/env python3
"""Validate the three-layer evaluation case contracts."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "unit": ROOT / "evals" / "unit-cases.json",
    "workflow": ROOT / "evals" / "workflow-cases.json",
    "capability": ROOT / "evals" / "capability-cases.json",
}


def main() -> None:
    seen: set[str] = set()
    errors: list[str] = []
    counts: dict[str, int] = {}
    for level, path in FILES.items():
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT)}")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        cases = data.get("cases") if isinstance(data, dict) else None
        if not isinstance(cases, list) or not cases:
            errors.append(f"{path.name}: cases must be non-empty")
            continue
        counts[level] = len(cases)
        for case in cases:
            if not isinstance(case, dict):
                errors.append(f"{path.name}: case must be object")
                continue
            case_id = str(case.get("id") or "")
            if not case_id:
                errors.append(f"{path.name}: missing id")
            elif case_id in seen:
                errors.append(f"duplicate id {case_id}")
            seen.add(case_id)
            if case.get("level") != level:
                errors.append(f"{case_id}: level must be {level}")
            if not str(case.get("prompt") or "").strip():
                errors.append(f"{case_id}: missing prompt")
            expected = case.get("expected_skills")
            if not isinstance(expected, list):
                errors.append(f"{case_id}: expected_skills must be a list")
    print(json.dumps({"counts": counts, "errors": errors}, indent=2))
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
