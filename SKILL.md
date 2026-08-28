---
name: orchestrating-econometric-research
description: Use when conducting a multi-stage empirical econometric study involving causal identification, DID, IV, mechanisms, robustness, heterogeneous effects, external data discovery, or systematic specification search.
---

# Orchestrating Econometric Research

## Overview

Run empirical econometric research as a persistent, auditable state machine. Stata is the default estimation engine; Python/Codex handles orchestration, discovery, registries, result parsing, search, and reporting.

## Core invariants

- NEVER overwrite the authoritative/master dataset.
- NEVER discard a specification because it is insignificant, inconvenient, or failed.
- NEVER promote an IV from statistical strength alone.
- NEVER merge externally discovered data into the authoritative panel without Human Gate approval.
- ALWAYS persist specifications, diagnostics, failures, transformations, and agent decisions.
- Significance is a view over the specification universe, never the stopping rule.

## Default policy

Use the project contract when present; otherwise default to:

- **D2 data governance:** discover/download/clean into staging; human approval before promotion.
- **S3 discovery:** official sources, academic databases, replication repositories, then weaker sources as leads only.
- **T2 transformations:** controlled lags, logs, growth/rates, per-capita/scales, moving averages, leave-one-out, geographic exposure, historical interactions, winsorization, standardization; record lineage.
- **E2 search:** hierarchical specification search with a finite computation budget and saturation stopping.
- **Two IV Human Gates:** researcher approves candidates before statistical screening and approves theoretically defensible IVs after IV Cards.

## Workflow

1. **Detect project state.** Classify as new, existing, partially completed, replication, or exploratory.
2. **Read local authority first.** Read `AGENTS.md`, research protocols, configs, code, results, and data metadata before changing anything.
3. **Create or validate the project contract.** Use `references/project-contract.md` and templates. Never replace existing project rules silently.
4. **Audit before estimating.** Map data lineage, estimands, code dependencies, completed analyses, failures, and irreversible operations.
5. **Advance through the research state machine** in `references/research-workflow.md` and `references/econometric-chain.md`.
6. **Use Human Gates** exactly as defined in `references/human-gates.md` and `references/iv-protocol.md`.
7. **Run Stata through a parameterized execution layer** according to `references/stata-protocol.md`.
8. **Search specifications hierarchically**, preserve the denominator, and use saturation—not significance—to stop. Read `references/specification-search.md`.
9. **Report the complete evidence surface** according to `references/reporting.md`.
10. Update `PROJECT_STATE.yaml` after every material state transition.

## Required references

Read only what the current phase needs:

- Project setup/audit: `references/project-contract.md`, `references/research-workflow.md`
- Data discovery: `references/data-discovery.md`
- DID/IV/mechanisms/robustness: `references/econometric-chain.md`
- IV work: `references/iv-protocol.md`, `references/human-gates.md`
- Stata execution: `references/stata-protocol.md`
- Specification search: `references/specification-search.md`
- Final synthesis: `references/reporting.md`

## Project initialization

For a project that does not yet have the contract files, run:

```bash
python <skill-dir>/scripts/init_project.py <project-root>
python <skill-dir>/scripts/validate_project.py <project-root>
```

The initializer is non-destructive: it creates only missing files/directories.

## Stop conditions

Stop the affected branch and request researcher action when:

- staging data is ready for promotion;
- a discovered IV lead requires candidate approval;
- a statistically viable IV requires theoretical review;
- the treatment/estimand definition would materially change;
- the primary sample would materially change;
- an irreversible change to authoritative data is proposed;
- required software/data/credentials are unavailable.

Do not replace a Human Gate with an automated heuristic.
