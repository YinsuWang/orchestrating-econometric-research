# Reporting and Synthesis

## Reporting Layers

Maintain separate layers:

1. **Run-level database:** every attempt, including failures.
2. **Diagnostic views:** weak-IV, pretrend, sample support, convergence, missingness.
3. **Specification views:** baseline, robustness families, mechanism families, heterogeneity, search-selected views.
4. **Research synthesis:** claims tied to identification assumptions and robustness evidence.

## Core Tables

Where applicable, produce:

- sample/descriptive statistics;
- treatment/cohort composition;
- baseline estimates;
- event-study coefficients and pretrend diagnostics;
- first-stage/weak-IV diagnostics;
- formal IV estimates;
- mechanism-family evidence;
- robustness matrix;
- heterogeneity interaction tests;
- specification/multiverse summary;
- multiplicity-adjusted results.

## Specification Curve

A specification-curve or multiverse report should show:

- effect estimates ordered by magnitude or predefined grouping;
- confidence intervals;
- key specification choices;
- number of attempted vs successfully estimated models;
- distribution of effect signs/magnitudes;
- sample-size variation;
- clearly separated confirmatory vs exploratory specifications when applicable.

## Claim Discipline

Distinguish:

- `ESTIMATED_ASSOCIATION`;
- `CAUSAL_ESTIMATE_UNDER_ASSUMPTIONS`;
- `MECHANISM_CONSISTENT_EVIDENCE`;
- `EXPLORATORY_SIGNAL`;
- `ROBUST_TO_LISTED_VARIANTS`.

Do not upgrade a claim merely because many searched specifications are significant.

## Final Evidence Assessment

For each major claim summarize:

- estimand and baseline estimate;
- core identifying assumptions;
- evidence supporting assumptions;
- unresolved threats;
- result stability across defensible specifications;
- multiplicity/post-selection context;
- whether evidence is confirmatory, exploratory, or mixed.
