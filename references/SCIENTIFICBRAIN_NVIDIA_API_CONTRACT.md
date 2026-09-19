# ScientificBrain ↔ NVIDIA API integration contract

The NVIDIA API/NIM client belongs to the **ScientificBrain core**, not to this skill repository.

## Why

A skill should describe scientific intent and execution requirements. It should not own provider secrets, authentication refresh, endpoint policy, billing controls, rate-limit handling, or organization-wide telemetry.

```text
Physics skill
   │
   │ structured capability request
   ▼
ScientificBrain provider router
   │
   ├── NVIDIA hosted endpoint
   ├── NVIDIA NIM deployed by ScientificBrain
   └── local PhysicsNeMo execution
```

## Responsibility split

### scientificbrain-physics-skills

- defines the requested capability;
- defines scientific inputs/outputs;
- validates units, geometry, data schema, and physical assumptions;
- validates returned results against solver/physics criteria;
- never stores API keys.

### ScientificBrain core

- stores/retrieves secrets;
- selects hosted NVIDIA API vs local NIM vs local PhysicsNeMo;
- resolves model/service identifiers;
- performs authentication;
- invokes endpoints/containers;
- implements retries, timeout, quota and cost policies;
- records provider/model/version provenance;
- normalizes the response for the calling skill.

## Credential policy

For NGC/NIM services that require authentication, NVIDIA currently recommends scoped Personal or Service API keys rather than legacy keys. Personal/service keys can be used directly as bearer tokens for supported NGC APIs. NVIDIA documentation also uses `NGC_API_KEY` for authenticated NIM/model access.

ScientificBrain should keep the actual secret in its secret store or deployment environment. Never write real values into:

- `.env.example`;
- skill files;
- run manifests;
- logs;
- GitHub issues;
- generated datasets.

A placeholder contract may refer to:

```text
NGC_API_KEY=<managed by ScientificBrain secret provider>
```

but the skills should receive only an authenticated client/capability handle whenever possible.

## Proposed capability request

A physics skill can emit a provider-neutral request such as:

```json
{
  "provider": "nvidia",
  "domain": "physics",
  "capability": "physicsnemo",
  "execution_mode": "auto",
  "task": "train_surrogate",
  "provenance_required": true
}
```

ScientificBrain resolves `execution_mode=auto` according to available hardware, allowed endpoints, configured credentials, model availability, privacy rules, and cost policy.

## BioNeMo

BioNeMo follows the same provider boundary. ScientificBrain may expose BioNeMo/NIM capabilities to life-science agents, while the physics toolkit requests PhysicsNeMo/NVIDIA compute capabilities. Shared NVIDIA authentication and routing remain centralized.

## Next implementation step

When ScientificBrain integration begins, implement one provider adapter in the core:

```text
providers/nvidia/
  auth
  catalog/discovery
  hosted_nim
  local_nim
  physicsnemo_runtime
  provenance
```

Then expose it to skills through ScientificBrain's tool/capability router rather than importing provider SDK code into each `SKILL.md`.
