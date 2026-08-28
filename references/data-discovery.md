# External Data Discovery Protocol

## Default Mode: D2 + S3 + T2

### D2 — Automatic Staging

The agent may autonomously search, download, parse, standardize, and quality-check candidate external data. It may not promote those data into the master/official analysis panel without Human Gate approval.

### S3 — Full-Web Discovery with Source Tiers

Rank evidence sources:

1. **Tier 1:** official statistical agencies, governments, central banks, international organizations.
2. **Tier 2:** established academic/research databases with methodology documentation.
3. **Tier 3:** journal replication packages, Dataverse, Zenodo, institutional repositories.
4. **Tier 4:** author GitHub repositories, working-paper supplements, other research-hosted files.
5. **Tier 5:** web pages, forums, community posts, news, or informal discussions — discovery leads only unless independently verified.

Prefer the highest-tier source that measures the intended construct adequately.

## Candidate Discovery Record

For each candidate variable/dataset record:

- canonical name and proposed role;
- construct measured;
- source organization;
- exact dataset/indicator identifier;
- retrieval page/API/file reference;
- retrieval date;
- units and scale;
- temporal coverage;
- geographic coverage;
- license/access constraints when known;
- missingness;
- duplicate-key diagnostics;
- merge keys and country-code mapping;
- likely post-treatment status;
- known revisions/breaks;
- source tier;
- proposed transformations;
- theoretical rationale.

## Quality Gate Before Human Review

A staged dataset should receive a `data_review.md` artifact covering:

- raw vs expected row counts;
- uniqueness of merge keys;
- unmatched country/unit shares;
- missingness before/after merge simulation;
- impossible/extreme values;
- unit consistency;
- temporal alignment;
- whether interpolation/imputation occurred;
- whether the variable may be downstream of treatment.

No silent imputation or interpolation.

## T2 Controlled Transformations

Allowed by default when substantively justified and lineage is recorded:

- log;
- lags 1–3;
- growth rates;
- per-capita scaling;
- GDP/share scaling;
- regional/peer mean;
- neighbor exposure;
- leave-one-out aggregates;
- historically predetermined × time-varying interactions;
- moving averages;
- winsorization;
- standardization.

For each derived variable record exact formula, source variables, timing, missing-value behavior, and rationale.

## Promotion

Promotion from staging requires an explicit Human Gate decision. The approved record should state which exact staged version/checksum is promoted and for what analytic role.
