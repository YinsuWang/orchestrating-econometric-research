# Human Gates

## Principle

Human Gates protect research judgments that an automated agent should not silently make. Reaching a gate pauses only the affected workflow branch; independent safe work may continue if state and dependencies make that explicit.

## Mandatory Gates

### HG-DATA-PROMOTE
Trigger: staged external data is proposed for official analysis use.

Review artifact must include source provenance, coverage, merge diagnostics, transformations, quality issues, and proposed analytic role.

### HG-IV-CANDIDATE
Trigger: a discovered IV lead is proposed for statistical screening.

Only the researcher may approve the lead as a candidate.

### HG-IV-THEORY
Trigger: an admitted IV candidate has completed statistical screening and is proposed for formal causal use.

Provide the full IV Card. Only the researcher may approve formal use.

### HG-TREATMENT-DEFINE
Trigger: a material change to treatment definition, timing, dose, or comparison group.

### HG-SAMPLE-DEFINE
Trigger: a material change to the primary sample definition rather than a clearly labeled robustness sample.

### HG-MASTER-MUTATION
Trigger: creating/replacing the official master dataset or overwriting it.

## Decision Record

Every decision records:

- gate ID/type;
- subject ID/path;
- decision: `ACCEPT`, `REJECT`, or `REVISE`;
- researcher note;
- date/time;
- version/hash when relevant.

Never infer approval from silence, prior statistical significance, or a previous approval for a different version.
