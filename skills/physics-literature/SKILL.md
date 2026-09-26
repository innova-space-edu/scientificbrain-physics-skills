---
name: physics-literature
description: Build source-grounded physics literature maps through ScientificBrain using arXiv, OpenAlex, DOI/publisher metadata and project sources while preserving versions, regimes, contradictory evidence and claim provenance.
license: Apache-2.0
metadata:
  author: Innova Space Edu SpA / ScientificBrain
  version: 0.3.0
  tags:
    - physics
    - literature
    - evidence
    - scientificbrain
---

# Physics Literature

Use this skill for physics-specific literature discovery and evidence mapping. ScientificBrain owns external search connectors and credentials; this skill defines the physics search and evidence protocol.

## Search sequence

1. Translate the research question into multiple query families: phenomenon, governing model, diagnostic/observable, solver/method and key parameter/regime.
2. Search complementary sources through ScientificBrain:
   - arXiv for current physics preprints;
   - OpenAlex for broad scholarly metadata/citation graph discovery;
   - DOI/publisher or other authoritative metadata when resolving the published record;
   - project-provided papers and institutional sources.
3. Deduplicate preprint/published versions and retain identifiers for both when useful.
4. Record publication/preprint date, version, authors, venue, DOI/arXiv identifier and retrieval source.
5. Extract claims with explicit evidence pointers; do not use title/abstract alone when the claim requires methods/results.
6. Tag the physical regime, geometry, dimensionality, parameter range, diagnostic and model assumptions.
7. Preserve contradictory results and explain regime differences before treating them as disagreement.
8. Separate foundational references from recent state-of-the-art work.
9. Pass accepted evidence into ScientificBrain's literature/evidence agents and research state.

## Output contract

Return literature map, query log, canonical identifiers, version relationships, regime tags, evidence records, contradictions, unresolved gaps and recommended next searches.

## Guardrails

- Never invent a DOI, arXiv identifier, author, quotation or bibliographic field.
- Citation count is not a correctness score.
- Do not collapse preprint and peer-reviewed versions without recording the relationship.
- Do not treat an abstract as sufficient evidence for a detailed quantitative claim.
- Do not flatten incompatible physical regimes into one conclusion.
- Respect API/source rate limits and terms through ScientificBrain's connector layer.
