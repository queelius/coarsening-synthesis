# Methodology Auditor Report (re-review)

Date: 2026-06-03
Confidence: HIGH for build/reproducibility and for the regime-(B)
definition fix (checked directly); the empirical validation is delegated
to the siblings by design, which is legitimate for this venue.

## Synthesis method

The method (state the shared result once at the right generality, recover
each named instance as a corollary, delegate empirical weight to the
siblings) is sound and is the correct method for a Statistical Science
synthesis. No new simulations are expected or required.

## The regime-(B) definition over-claim is FIXED

The prior review's Minor-3 (escalating toward MAJOR for a proofs-bearing
venue) was that framework.tex sec:css asserted the coarsening-sufficient
statistic makes "the face-value log-likelihood depend on the data only
through the empirical mean Tbar," which is false for general location
families at finite n. The revision splits the definition by regime
(framework.tex l.97-108): regime (A) depends on the data through Tbar and
reproduces it exactly; regime (B) "depends on the full sample through the
score sum psi(R_i - mu) rather than through Tbar alone," reproduces the
sample psi-location exactly, and reproduces Tbar exactly only at n=1 or
for the Gaussian kernel, with an O_p(n^{-1/2}) remainder otherwise. This
is now methodologically correct and consistent with the corrected theorem.
RESOLVED.

## Two-regime partition

The partition into (A) regular exponential family and (B) location family
is correctly argued as NON-NESTED (consistency.tex rem:loc-sketch l.143-145:
"(A) is a curved constraint on a discrete or count report, (B) is a
location shift of a continuous report"). This is methodologically honest:
the Gaussian location family is the one overlap and is correctly assigned
to (A) because Gaussian-location is exponential-family. The non-nesting is
presented as a structural fact, not a defect. Sound.

## Boundary characterization is now a result, not an open step

The old draft carried regime (B) as a proof with one open finite-sample
step. The revision closes it: the boundary is exactly characterized
(Gaussian-iff, via Cauchy's functional equation at n=3), with explicit
counterexamples (Laplace median vs mean on (0,1,5); logistic strict
interior maximum) and the O_p(n^{-1/2}) rate with an explicit asymptotic
variance V = Var(psi(Z)/J - Z). I inspected the provenance in
.research/findings/ (the Laplace n=3 script runs and confirms the exact
gap of -1; synthesis.md documents the kernel battery and the numerical
sweep certifying true stationary points 8 to 14 orders of magnitude above
optimizer noise). The methodology behind the settled result is rigorous.
What discussion.tex correctly labels as remaining OPTIONAL (not open) is
tabulating the leading constant V for standard release kernels if a
multi-release finite-sample correction is ever wanted. Correctly scoped.

## Reproducibility

- make paper: exit 0.
- 15 pages, 0 undefined references, bibtex clean (0 warnings in main.blg).
- No new simulation to reproduce (by design); the empirical base lives in
  the six cited siblings.

## Delegation of empirical validation

Legitimate for Statistical Science. Each named identity is empirically
confirmed in its sibling (three exactly via exponential family, weak-sup
at the predicted n^{-1/2} rate, DP for the Gaussian kernel / single
release). RECOMMENDATION (carried from prior review, still open): add one
global sentence making the delegated empirical base visible at a glance,
rather than leaving it scattered across the per-domain applications
subsections. Severity SUGGESTION.

## Residual methodology items

1. SUGGESTION: one-line global empirical-validation statement (above).
2. MINOR: the spatial vector-form caveat (consistency and identifiability
   not cleanly separable there) is correctly disclosed in discussion.tex
   as the "third, milder boundary." No action needed beyond what is there;
   noted for completeness.

No critical or major methodology issues. The one methodology defect from
the prior review (regime-B definition over-claim) is resolved.
