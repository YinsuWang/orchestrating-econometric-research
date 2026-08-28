# Project Contract

## Required Root Files

- `research_config.yaml`: machine-readable research and execution settings.
- `PROJECT_STATE.yaml`: persistent workflow state.
- `RESEARCH_PROTOCOL.md`: human-readable methodological contract.
- `VARIABLE_REGISTRY.yaml`: role, source, lineage, and approval status for variables.

The initializer creates these only if absent. Existing versions are never overwritten.

## research_config.yaml Responsibilities

The configuration should identify, where applicable:

- research question and estimand;
- panel unit and time variable;
- outcome(s), treatment(s), cohort/treatment timing;
- master dataset path and immutability;
- Stata executable and orchestration settings;
- baseline estimator and comparison estimators;
- fixed effects and clustering policy;
- event-study window/reference period;
- external-data policy;
- transformation policy;
- IV approval policy;
- specification-search limits and stop rules;
- reproducibility seeds and bootstrap settings.

Do not encode unsupported facts merely to make validation pass. Mark unresolved values as `null` and set project state to `BLOCKED` only when the value is required to proceed.

## Directory Contract

The default managed subtree is `research_system/`. It may coexist with an existing project layout.

Managed purposes:

- `registry/`: variable and source registries.
- `staging/`: unapproved external datasets and transformed candidates.
- `specs/`: pending/running/completed/failed specification records.
- `results_db/`: append-only/merge-safe research result stores.
- `reviews/`: Human Gate artifacts and decisions.
- `discovery/`: literature/data discovery evidence.
- `logs/`: agent, Stata, Python, and web-discovery logs.
- `reports/`: generated IV cards, data reviews, mechanism summaries, and final synthesis.

## Master Data Rule

The master dataset is conceptually read-only. Automated runs should load it, create temporary/derived analysis frames or files, and write outputs elsewhere. Commands that save over the master path are forbidden unless the researcher explicitly authorizes a new master build.

## Variable Registry Roles

Use controlled roles:

- `outcome`
- `treatment`
- `cohort`
- `control`
- `mechanism`
- `heterogeneity`
- `iv_lead`
- `iv_candidate`
- `iv_approved`
- `auxiliary`

A variable can have multiple candidate roles only if the registry records the distinction and the research protocol explains it.
