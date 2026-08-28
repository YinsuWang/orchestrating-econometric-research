---
name: orchestrating-econometric-research
description: Use when conducting a multi-stage empirical econometric study involving causal identification, DID, IV, mechanisms, robustness, heterogeneity, external data discovery, or systematic specification search.
---

# Orchestrating Econometric Research

## Overview

Use this skill to run empirical econometric research as a persistent, auditable workflow rather than as isolated regressions. The default stack is **Stata for estimation** and **Python/Codex for orchestration, discovery, parsing, storage, and reporting**.

## Non-Negotiable Invariants

1. Core rule: **preserve every attempted specification**. Never delete or hide a result because it is insignificant, unstable, inconvenient, or failed.
2. Never stop specification search merely because significance has been found.
3. Treat the master dataset as immutable unless the researcher explicitly approves a replacement.
4. Newly discovered external data enters staging first; promotion requires a Human Gate.
5. IV discovery is not IV approval. Formal IV testing and promotion follow the two-stage Human Gate in `references/iv-protocol.md`.
6. Economic interpretation and identification claims remain researcher decisions.
7. Keep `PROJECT_STATE.yaml` current so work can resume across sessions.

## Start Here

1. Detect whether the project is new, existing, partial, exploratory, or replication-oriented.
2. Read project instructions and existing research artifacts before modifying anything.
3. Read `references/research-workflow.md` and `references/project-contract.md`.
4. If the project contract is absent, initialize non-destructively:

```bash
python <skill-dir>/scripts/init_project.py <project-root>
python <skill-dir>/scripts/validate_project.py <project-root>
```

5. Populate `research_config.yaml` from project evidence. Do not guess materially important research definitions.
6. Set or update `PROJECT_STATE.yaml` before executing a research phase.

## Phase-Specific References

- External data or new variables → `references/data-discovery.md`
- DID, event studies, IV-DID, mechanisms, robustness, heterogeneity → `references/econometric-chain.md`
- IV candidate work → `references/iv-protocol.md`
- Large model/specification search → `references/specification-search.md`
- Stata execution and wrappers → `references/stata-protocol.md`
- Approval boundaries → `references/human-gates.md`
- Tables, diagnostics, synthesis → `references/reporting.md`

## Default Policies

Unless the researcher specifies otherwise:

- External data: **D2 staging-only**.
- Discovery scope: **S3**, with source tiers and verification.
- Transformations: **T2 controlled transformations** with lineage.
- Search: **E2 hierarchical specification search**.
- Control variables: theory-based families/blocks, not arbitrary random subsets.
- Mechanisms: evaluate families with multiple proxies where feasible.
- Multiplicity: report nominal and multiplicity-adjusted evidence when many hypotheses/specifications are examined.

## Completion Rule

A phase is complete only when outputs, diagnostics, failed attempts, decisions, and state transitions are persisted. If a Human Gate is reached, create the review artifact, set state to `HUMAN_REVIEW_REQUIRED`, and stop that branch of the workflow.
