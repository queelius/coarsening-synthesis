# Methodology Auditor Report

**Paper**: One consistency theorem for coarsened-data maximum likelihood
**Date**: 2026-06-08
**Note**: this is a simulation-free synthesis paper by design; the empirical
weight is carried by the cited siblings. So "methodology" here means the
soundness of the reduction methodology (does each named theorem actually follow
from the general theorem?), the honesty of the regime classification, and
reproducibility of the derivations, not experimental design.

## Summary

The reduction methodology is principled: state one theorem, instantiate per
domain via a coarsening-sufficient statistic, flag where the reduction is exact
vs asymptotic vs single-release. The two-regime split (exponential family vs
location family) is the right organizing axis and the seams are disclosed rather
than hidden, which is methodologically commendable for a synthesis. The audit
finds one genuine overstatement in the regime classification (MIL), confirming
the logic-checker's MAJOR finding by independent derivation, plus a
reproducibility-of-claim gap: several reductions assert exponential-family
membership that the reader cannot verify from the paper alone and must take from
the (in one case URL-only) sibling.

## Cross-verification of the logic-checker MIL finding (independent reproduction)

I re-derived the MIL normal equation from scratch without consulting the
logic-checker's algebra. Bernoulli bag log-likelihood with eta_i = m_i^T s,
p_i = 1 - exp(-eta_i):
- 1 - p_i = exp(-eta_i); dp_i/deta_i = exp(-eta_i) = 1 - p_i.
- gradient wrt s: sum_i (Y_i - p_i)/(p_i(1-p_i)) * (1-p_i) * m_i
  = sum_i (Y_i - p_i)/p_i * m_i = M^T diag(p)^{-1} (Y - p).
Setting to zero: M^T D^{-1}(Y - p_hat) = 0. CONFIRMED identical to cor:mil and
to the logic-checker. The equation is the exact noisy-OR (complementary
log-survival) GLM normal equation.

I AGREE with the logic-checker: this is methodologically *not* the same object
as the theorem's eq:general-consistency (m(theta_hat) = bar T). The D^{-1} is
the IRLS weight forced by the non-canonical link; the theorem's stripped
identity holds only for canonical-link members. Putting MIL in the same
`bullet` "exact finite-sample identity" bucket as scrna/spatial/phenotype in
tab:reduction conflates two methodologically distinct strengths: unweighted
moment-matching vs IRLS-weighted moment-matching. The corollary's own prose is
honest about the weighting, so the fix is presentational (distinguish the
buckets), not a retraction. Severity: MAJOR, concurring with logic-checker.

## Findings

### [MAJOR, concurs with logic-checker] Regime (A) bucket conflates weighted and unweighted exact identities
**Location**: tab:reduction (consistency.tex:290-316), cor:mil
(consistency.tex:225-229).
**Quoted text (table caption)**: "$\bullet$ exact finite-sample identity
through the exponential-family regime (A)".
**Quoted text (corollary)**: "the moment matching is IRLS-weighted rather than
unweighted."
**Problem**: the table's `bullet` legend asserts a single notion of "exact
finite-sample identity," but four of the five regime-(A) rows are unweighted
mean-matches (m=bar T) while MIL is an IRLS-weighted normal equation. A reader
using tab:reduction as the at-a-glance summary will read MIL as the same kind of
clean identity as cell-total consistency. It is exact, but in a different sense.
**Suggestion**: split the legend or add a sub-mark, e.g., `bullet` = exact
unweighted m=bar T; `bullet*` (or a footnote) = exact but IRLS-weighted
(non-canonical link). Apply `bullet*` to the MIL row. Pair this with the
theorem-statement fix the logic-checker proposes (state regime (A) in
score-equation form, collapsing to m=bar T for canonical links).

### [MAJOR] Reproducibility of the exponential-family claims rests on siblings the reader cannot all reach
**Location**: cor:scrna (consistency.tex:172-175, "ZINB ... is a regular
exponential family"); cor:mil (consistency.tex:225, "The bag label is
Bernoulli, a regular exponential family"); both cite siblings for the precise
development.
**Problem**: a self-contained synthesis should let the reader verify each
reduction's regime hypothesis from the paper. Two of the six corollaries assert
exponential-family membership that is either imprecise (ZINB is a mixture, see
logic-checker MINOR) or link-subtle (MIL noisy-OR is non-canonical), and the
authority for the precise statement is deferred to the sibling. For MIL that
sibling (towell2026milcoarsening) is cited only by GitHub URL with no Zenodo DOI
(refs.bib:130-137), so the deferral target is the least citable reference in the
paper. The reduction methodology is sound, but its *checkability* is uneven
across domains.
**Why it matters**: for Statistical Science the "technical results inside a
review frame" must still be self-verifiable to the level claimed. The strongest
corollaries (phenotype, dp) are fully checkable in-paper; the two flagged are
not, and they are the two with the loosest exponential-family wording.
**Suggestion**: add one sentence per flagged corollary giving the precise family
statement in-paper (for scrna: NB-at-fixed-dispersion exponential family plus
the (1-pi) mean factor; for MIL: per-bag Bernoulli exponential family with a
non-canonical noisy-OR link), so the regime hypothesis is verifiable without the
sibling. This also de-risks the URL-only MIL citation.

### [MINOR] tab:css MIL implied mean is given without the IRLS caveat
**Location**: tab:css (framework.tex:138-140).
**Quoted text**: "Multiple instance learning ... $1 - \exp(-\bm m_b^\top \bm
s)$ (noisy-OR bag prevalence)".
**Problem**: tab:css presents "implied mean m(theta) = E[T]" uniformly across
domains, with the consistency identity stated as "the single identity
m(theta_hat) = bar T, read in each row's coordinates" (framework.tex:144-146).
For MIL that single identity is the *weighted* one, so the table's unifying
caption m(theta_hat)=bar T is, for the MIL row, only true in the weighted sense.
Same root cause as the MAJOR findings; noting it here because tab:css is where
the "one identity, read per row" promise is made and the MIL row is the one row
where it needs an asterisk.
**Suggestion**: a footnote on the MIL row, or amend the tab:css caption to
"m(theta_hat) = bar T (exactly, or IRLS-weighted for the noisy-OR link)."

## What is methodologically strong (for the record)
- The decision to carry the candidate set as a weighted/continuum object
  (framework.tex:26-30) so that discrete reliability and continuous DP are one
  construction is a clean, non-ad-hoc unification device.
- The reduction-status table (tab:reduction) is exactly the right artifact for a
  synthesis: it makes the boundary auditable. The fix above sharpens it; it does
  not replace it.
- The seams (DP location-family, weak-supervision parametrization) are disclosed
  in abstract, intro, the relevant corollary, and discussion, consistently. That
  four-way consistency is good methodology; the count slip at consistency.tex:276
  is the only place the four-way consistency breaks.
