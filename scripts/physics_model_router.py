#!/usr/bin/env python3
"""High-level physics model router for ScientificBrain Physics Skills.

This router selects the next skill/model family to inspect. It does not replace
solver-specific validity checks or domain expertise.
"""
from __future__ import annotations

import argparse
import json
import sys
from typing import Any


def _bool(payload: dict[str, Any], key: str) -> bool:
    return bool(payload.get(key, False))


def route(payload: dict[str, Any]) -> dict[str, Any]:
    domain = str(payload.get("domain") or "unknown").strip().lower()
    observable = str(payload.get("observable") or "").strip()
    candidates: list[dict[str, str]] = []
    rejected: list[dict[str, str]] = []
    required_skills: list[str] = ["physics-model-router"]
    unresolved: list[str] = []

    if not observable:
        unresolved.append("target observable and acceptance criterion")

    particle_through_matter = _bool(payload, "particle_through_matter")
    requires_distribution = _bool(payload, "requires_distribution_function")
    requires_electron_kinetics = _bool(payload, "requires_electron_kinetics")
    use_surrogate = _bool(payload, "use_surrogate")
    has_validated_baseline = _bool(payload, "has_validated_baseline")

    plasma_domains = {
        "plasma", "mhd", "kinetic-plasma", "space-plasma", "laser-plasma",
        "high-energy-density-plasma", "low-temperature-plasma", "propulsion-plasma",
    }

    if particle_through_matter or domain in {"particle-transport", "radiation-transport"}:
        candidates.append({
            "family": "Monte Carlo particle transport",
            "solver_or_skill": "geant4-particle-transport",
            "reason": "Primary observable concerns passage/interactions of particles in matter rather than self-consistent plasma evolution.",
        })
        required_skills.append("geant4-particle-transport")
        rejected.append({
            "family": "plasma PIC as default",
            "reason": "PIC should not be selected only because particles are present; self-consistent plasma kinetics must be part of the question.",
        })
    elif domain in plasma_domains:
        candidates.append({
            "family": "plasma model hierarchy",
            "solver_or_skill": "plasma-model-router",
            "reason": "Plasma problems require scale, closure, collisionality and kinetic-validity checks before solver choice.",
        })
        required_skills.extend(["plasma-regime", "plasma-dimensionless", "kinetic-validity", "plasma-model-router"])
        if requires_distribution or requires_electron_kinetics:
            candidates.append({
                "family": "kinetic overlap candidate",
                "solver_or_skill": "pic-discover",
                "reason": "The requested observable depends explicitly on distribution-level or electron-kinetic physics.",
            })
    elif domain in {"analytic", "theory", "reduced-model"}:
        candidates.append({
            "family": "analytic / reduced model",
            "solver_or_skill": "theory-first",
            "reason": "Start from governing equations, limiting cases and dimensional analysis before numerical escalation.",
        })
    else:
        candidates.append({
            "family": "theory-first classification",
            "solver_or_skill": "physics-model-router",
            "reason": "The domain is not specific enough for a solver-level decision; define governing equations and scales first.",
        })
        unresolved.append("physics domain / governing equations")

    if use_surrogate:
        if has_validated_baseline:
            candidates.append({
                "family": "scientific surrogate",
                "solver_or_skill": "physicsnemo-plasma-discover",
                "reason": "A validated baseline exists, so a surrogate may be evaluated as an acceleration layer with held-out physics validation.",
            })
            required_skills.append("physicsnemo-plasma-discover")
        else:
            rejected.append({
                "family": "surrogate-first workflow",
                "reason": "Do not train or trust a scientific surrogate before a validated baseline/data contract exists.",
            })

    return {
        "domain": domain,
        "observable": observable or None,
        "candidate_hierarchy": candidates,
        "rejected_or_deferred": rejected,
        "required_skills": list(dict.fromkeys(required_skills)),
        "unresolved": unresolved,
        "decision_state": "blocked" if unresolved else "screened",
        "guardrail": "Choose the smallest model adequate for the target observable; higher computational fidelity is not automatically higher physical validity.",
    }


def _load_payload(path: str | None) -> dict[str, Any]:
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
    print(json.dumps(route(_load_payload(args.input)), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
