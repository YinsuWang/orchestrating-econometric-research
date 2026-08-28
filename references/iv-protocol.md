# Instrumental Variable Protocol

## Core Rule

**The researcher controls IV admissibility. Statistical strength cannot establish the exclusion restriction.**

There are two Human Gates.

## Gate 1 — Candidate Admission

The agent may discover potential IV ideas from literature or data and record them only as `iv_lead`. It may explain why a lead could be relevant, but must not run it as a formal candidate until the researcher marks it `APPROVED_FOR_STATISTICAL_SCREENING`.

Store approved candidates in a researcher-controlled candidate registry.

## Statistical Screening

For every admitted candidate, report as applicable:

- first-stage coefficient and standard error;
- first-stage p-value;
- conventional first-stage F statistic;
- heteroskedasticity/cluster-robust weak-IV statistic such as Kleibergen–Paap when appropriate;
- partial R²;
- Sanderson–Windmeijer conditional F for multiple endogenous regressors when applicable;
- underidentification tests when applicable;
- weak-IV-robust Anderson–Rubin or comparable inference when feasible;
- overidentification tests only when overidentified, with the warning that they do not prove validity;
- sample size and effective clusters;
- sign and magnitude stability across pre-specified reasonable controls/samples.

Do not promote solely because `p < 0.05` or `F > 10`. Thresholds are diagnostics, not validity proofs.

## IV Card

For each statistically viable candidate, generate the template `iv_card.md`. It must include both supporting and adversarial analysis:

1. construction and timing;
2. relevance mechanism;
3. empirical relevance diagnostics;
4. exclusion-restriction argument;
5. plausible direct pathways to the outcome;
6. common causes of IV and outcome;
7. reverse causality/treatment contamination;
8. literature precedent and differences from precedent;
9. placebo/falsification opportunities;
10. controls or fixed effects that address specific threats;
11. threats those controls cannot solve;
12. overall assessment: `PLAUSIBLE`, `FRAGILE`, or `UNSUPPORTED`, never `VALIDATED`.

## Gate 2 — Theoretical Approval

After the IV Card, set status to `HUMAN_REVIEW_REQUIRED`. Only the researcher may mark:

- `ACCEPTED_FOR_FORMAL_IV`
- `REJECTED`
- `REVISE_AND_REVIEW`

Only `ACCEPTED_FOR_FORMAL_IV` candidates may enter formal IV-DID/2SLS research chains.

## Multiple IVs

When multiple approved instruments are used jointly, retain instrument-specific relevance diagnostics where possible and assess whether adding instruments changes the identifying assumptions. More instruments are not automatically better.
