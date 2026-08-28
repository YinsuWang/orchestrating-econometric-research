# Econometric Research Chain

## General Principle

The exact estimator must match the estimand, assignment/treatment timing, data structure, and identification assumptions. Do not mechanically run every method. `RESEARCH_PROTOCOL.md` selects the applicable branches.

## 1. Data and Descriptive Diagnostics

Before causal estimation, document:

- unit/time coverage;
- treatment timing/cohort sizes;
- never-treated/not-yet-treated availability;
- missingness by treatment status and time;
- outcome distribution and transformations;
- control-variable balance/coverage;
- cluster counts;
- duplicate panel keys;
- changes in sample induced by each specification.

## 2. Baseline Effect

Record for every baseline model:

- estimand;
- estimator;
- treatment coding;
- comparison group;
- fixed effects;
- controls;
- clustering;
- sample restrictions;
- coefficient/ATT, SE, CI, p-value, N, clusters.

For staggered treatment, prefer estimators designed for heterogeneous treatment timing when that concern is material. TWFE may be retained as a comparison, not automatically as the principal estimator.

## 3. Event Study / Parallel Trends

Specify:

- event-time construction;
- reference period;
- lead/lag window;
- binning rule;
- comparison group;
- cohort handling;
- pointwise and, when supported, simultaneous confidence bands;
- joint test of pre-treatment coefficients;
- sparse/small-cohort diagnostics.

A non-rejection of pre-trends is not proof of parallel trends. Report effect sizes and uncertainty of leads, not only the joint p-value.

## 4. Formal IV Analysis

Only approved IVs may enter this stage. Report first stage and weak-IV diagnostics alongside second-stage estimates. Use weak-IV-robust inference when weakness is plausible. Explain how fixed effects and controls affect both relevance and exclusion arguments.

## 5. Mechanisms

Organize mechanisms into theory-based families. For each family:

- state the causal channel;
- classify each proxy as pre-treatment, contemporaneous, or post-treatment;
- report treatment→mechanism evidence;
- report outcome association/mediation strategy only when its assumptions are defensible;
- avoid calling a sequence of significant regressions a proven causal mediation effect without the required mediation assumptions;
- assess direction consistency across proxies.

When formal causal mediation is used, state sequential ignorability or alternative identification assumptions explicitly.

## 6. Robustness

Choose tests that target real threats, for example:

- alternative treatment definitions;
- alternative outcome construction;
- alternative estimators;
- alternative event windows;
- alternate comparison groups;
- sample exclusions with substantive rationale;
- alternative clustering/inference methods;
- placebo timing or placebo outcomes;
- pre-treatment falsification;
- outlier treatment/winsorization where justified;
- missing-data sensitivity;
- region×time or other richer fixed effects where conceptually justified.

Do not label arbitrary specification changes as robustness merely because they retain significance.

## 7. Heterogeneity

Predefine or theoretically motivate dimensions. Record subgroup support and sample sizes. Prefer interaction-based tests of differences over declaring heterogeneity because one subgroup is significant and another is not.

## 8. Multiplicity and Synthesis

When many outcomes, mechanisms, subgroups, IVs, or specifications are tested, report nominal p-values plus an appropriate multiplicity treatment such as Holm, BH-FDR, family-wise procedures, or simultaneous inference, depending on the question.
