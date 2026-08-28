# Hierarchical Specification Search

## Objective

Explore a defensible specification universe efficiently while preserving the complete search record. The system may rank or filter views, but the underlying database remains complete.

## Default E2 Search

Use stages rather than a single Cartesian-product explosion:

1. data/coverage eligibility;
2. baseline estimator and minimal controls;
3. control-family expansions;
4. event-study diagnostics;
5. admitted IV statistical screening;
6. formal IV models for human-approved IVs;
7. mechanism families;
8. robustness variants;
9. heterogeneity variants;
10. multiverse/specification-curve synthesis.

Poor statistical significance is never a hard-elimination reason. Hard elimination may use deterministic technical or identification criteria such as impossible merge, no identifying variation, severe collinearity, inadequate sample support, or an IV rejected by Human Gate.

## Control Families

Group controls by theory, for example:

- economic development;
- demographics;
- trade/external exposure;
- finance;
- institutions;
- infrastructure;
- industrial structure;
- environment/energy;
- geography/history.

Search family/block additions before arbitrary individual-variable subsets. Log the theory for every family.

## Mechanism Families

A mechanism family may contain multiple proxies for the same channel. Summaries should report:

- number of valid proxies;
- sign consistency;
- effect-size range;
- nominal significance count;
- multiplicity-adjusted significance count;
- sample/estimator stability.

## Specification Record

Every attempted specification receives an immutable `spec_id` and stores:

- hypothesis family;
- outcome/treatment;
- estimator;
- controls/control families;
- IV(s);
- mechanism/subgroup;
- transformations;
- sample rule;
- fixed effects;
- clustering/inference;
- event-study settings;
- N/clusters;
- estimate, SE, CI, p-value;
- diagnostic statistics;
- run status/failure reason;
- code/data version identifiers;
- timestamp.

## Result Views

It is permissible to create views such as `nominal_full_chain_success`, but label them as search-derived. Always display the numerator and denominator, e.g. `137 / 18,463 attempted specifications`.

Never present a search-selected specification as if it had been chosen ex ante.

## Multiplicity

Define hypothesis families before adjustment where possible. Depending on purpose, compute:

- Bonferroni/Holm for strong family-wise control;
- BH-FDR for discovery-oriented families;
- Romano–Wolf or simultaneous inference when implementation/design supports it.

Specification search creates dependence across tests; corrections do not magically convert post-selection estimates into pre-specified confirmatory inference. Use holdout/validation designs or a locked confirmatory specification when confirmatory inference is required.

## Stop Rule

Default stop is saturation/computational budget, never significance. Example conditions:

- maximum specification budget reached;
- planned control/mechanism/IV families have required coverage;
- no new high-quality data candidates in N discovery rounds;
- no new substantively distinct specification family in N rounds;
- all pending Human Gates resolved or explicitly blocked.

Persist the exact stop reason.
