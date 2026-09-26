#!/usr/bin/env python3
"""Deterministic observable-level validation gate.

The script never upgrades missing evidence to a pass. It aggregates explicit
check results into accepted/conditional/rejected/blocked states.
"""
from __future__ import annotations

import argparse
import json
import sys
from typing import Any

DEFAULT_REQUIRED = [
    "dimensions",
    "regime",
    "convergence",
    "conservation",
    "benchmark",
    "uncertainty",
    "provenance",
]
ALLOWED = {"pass", "warn", "fail", "blocked", "not_applicable"}


def validate_observable(item: dict[str, Any]) -> dict[str, Any]:
    name = str(item.get("name") or "observable").strip()
    required = item.get("required_checks", DEFAULT_REQUIRED)
    if not isinstance(required, list) or not all(isinstance(x, str) for x in required):
        raise ValueError(f"{name}: required_checks must be a list of strings")
    checks = item.get("checks", {})
    if not isinstance(checks, dict):
        raise ValueError(f"{name}: checks must be an object")

    normalized: dict[str, dict[str, Any]] = {}
    missing: list[str] = []
    for check_name in required:
        record = checks.get(check_name)
        if not isinstance(record, dict):
            missing.append(check_name)
            continue
        status = str(record.get("status") or "").strip().lower()
        if status not in ALLOWED:
            raise ValueError(f"{name}.{check_name}: invalid status {status!r}")
        normalized[check_name] = {
            "status": status,
            "evidence": record.get("evidence"),
            "note": record.get("note"),
        }

    statuses = [record["status"] for record in normalized.values()]
    if missing or "blocked" in statuses:
        decision = "blocked"
    elif "fail" in statuses:
        decision = "rejected"
    elif "warn" in statuses:
        decision = "conditional"
    else:
        decision = "accepted"

    return {
        "name": name,
        "decision": decision,
        "missing_required_checks": missing,
        "checks": normalized,
        "claim_scope": item.get("claim_scope"),
        "note": "Validation applies to this observable/claim only, not to the simulation globally.",
    }


def evaluate(payload: dict[str, Any]) -> dict[str, Any]:
    observables = payload.get("observables")
    if not isinstance(observables, list) or not observables:
        raise ValueError("observables must be a non-empty list")
    results = [validate_observable(item) for item in observables if isinstance(item, dict)]
    if len(results) != len(observables):
        raise ValueError("every observable must be an object")
    summary = {
        state: sum(r["decision"] == state for r in results)
        for state in ["accepted", "conditional", "rejected", "blocked"]
    }
    return {
        "schema_version": "0.3",
        "results": results,
        "summary": summary,
        "global_validity_claim": False,
    }


def _load(path: str | None) -> dict[str, Any]:
    if path:
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    else:
        data = json.load(sys.stdin)
    if not isinstance(data, dict):
        raise ValueError("input JSON must be an object")
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="JSON input file; reads stdin when omitted")
    args = parser.parse_args()
    print(json.dumps(evaluate(_load(args.input)), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
