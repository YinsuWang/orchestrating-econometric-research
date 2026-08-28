# Research Workflow

## Purpose

Maintain a stateful empirical research pipeline that can be resumed across Codex sessions without relying on conversation history.

## Project Classification

At entry, classify the project as one of:

- `NEW_PROJECT`: little or no empirical infrastructure exists.
- `EXISTING_PROJECT`: data/code/results already exist and must be audited before integration.
- `PARTIAL_PROJECT`: some empirical phases are complete but the chain is incomplete.
- `REPLICATION_PROJECT`: the primary objective is reproduction or extension of prior work.
- `EXPLORATORY_PROJECT`: the objective is broad specification or variable discovery; confirmatory claims require a separate locked specification.

For existing projects, do not reorganize files first. Audit before integrating.

## State Machine

Use these default phases:

1. `INITIALIZATION`
2. `PROJECT_AUDIT`
3. `DATA_AUDIT`
4. `DATA_DISCOVERY`
5. `VARIABLE_REGISTRY`
6. `BASELINE`
7. `EVENT_STUDY`
8. `IV_SCREENING`
9. `IV_HUMAN_GATE`
10. `FORMAL_IV`
11. `MECHANISMS`
12. `ROBUSTNESS`
13. `HETEROGENEITY`
14. `MULTIVERSE`
15. `FINAL_SYNTHESIS`

Allowed phase statuses:

- `PENDING`
- `RUNNING`
- `COMPLETED`
- `HUMAN_REVIEW_REQUIRED`
- `BLOCKED`
- `FAILED`

A phase may be skipped only when the project protocol explicitly states why it is inapplicable.

## Entry Procedure

1. Read repository/project instructions such as `AGENTS.md`, README, methods notes, and existing state/config files.
2. Inventory datasets, scripts, notebooks, do-files, outputs, and prior estimates.
3. Identify the current master/analysis dataset without changing it.
4. Infer what has already been completed from code and output evidence, not filenames alone.
5. Create or update `PROJECT_AUDIT.md` for existing projects.
6. Reconcile `PROJECT_STATE.yaml` with actual artifacts.
7. Execute only the current permissible phase.

## Existing Project Integration

Classify existing code as:

- `KEEP`: reproducible and callable as-is.
- `WRAP`: valid logic but needs parameterized invocation for automation.
- `REPLACE_CANDIDATE`: materially flawed, irreproducible, or impossible to parameterize. Do not replace without researcher approval.

Prefer wrappers over invasive edits.

## Resume Procedure

At the start of a later session:

1. Read `PROJECT_STATE.yaml`.
2. Validate that expected outputs for completed phases still exist.
3. Read unresolved Human Gate records.
4. Continue from `next_action` only after confirming prerequisites.
5. Update state after each meaningful transition.

## Failure Handling

Every failed run receives:

- a stable run/spec ID;
- failure class (`SYNTAX`, `DATA`, `COLLINEARITY`, `NONCONVERGENCE`, `INSUFFICIENT_SAMPLE`, `COMMAND_UNAVAILABLE`, `OTHER`);
- command/log location;
- whether retry is safe;
- corrective action if deterministic.

Do not silently rerun with changed variables to make a failure disappear.
