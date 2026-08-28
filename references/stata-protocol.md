# Stata Execution Protocol

## Architecture

Use Stata as the estimation engine and Python/Codex as the orchestrator.

Preferred flow:

`spec record → Stata parameter/wrapper → Stata run → machine-readable result → parser → results database`

Avoid embedding the entire search universe in deeply nested Stata `foreach` loops when Python can generate and audit specifications more transparently.

## Existing Code

For existing projects:

1. audit existing do-files;
2. preserve reproducible logic;
3. add wrappers that pass macros/arguments;
4. only refactor original do-files when necessary and approved.

## Stata Executable

Never guess an executable path. Discover non-destructively when possible; otherwise store a required path in `research_config.yaml` and block execution until resolved.

## Reproducibility

Record:

- Stata version/edition when available;
- community commands and versions when available;
- seeds for bootstrap/random procedures;
- input dataset hash or version marker;
- exact do-file/wrapper and arguments;
- log file;
- return code.

## Output Contract

Each run should emit machine-readable output with at least:

- `spec_id`;
- estimation status;
- coefficient/ATT of interest;
- SE/CI/p-value;
- N and cluster count when available;
- diagnostic test values;
- estimator-specific metadata.

Prefer explicit `postfile`, `collect`, frames, CSV/JSON intermediates, or other deterministic export patterns over parsing visually formatted console tables.

## Error Handling

A Stata error is a stored result, not a vanished run. Capture the return code and log. Classify failures and retry only when the correction does not alter the specification's substantive meaning.

Examples of safe corrections:

- missing package installation after approval/availability;
- corrected file path;
- transient file lock.

Examples requiring a new specification ID:

- dropping a control;
- changing sample restrictions;
- changing clustering;
- changing estimator;
- changing event window.
