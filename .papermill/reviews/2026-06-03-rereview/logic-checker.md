# Logic Checker Report (re-review)

Date: 2026-06-03
Priority for this pass (per area-chair brief): the INTERNAL-CONSISTENCY
hunt. Does every section agree on the corrected regime-(B) statement and
the DP-n=1 pinning? Is there any surviving statement that the location
identity is finite-sample exact for general kernels, or that DP
release-consistency generalizes beyond n=1? The settled math is NOT to be
re-opened; flag only genuine errors.

Confidence: HIGH. Every claim below was checked against the manuscript
source directly, and the settled-result provenance in .research/ was
inspected and partially re-executed.

## Headline verdict on the consistency hunt

NO surviving false claim. Every assertion of finite-sample exactness in
the manuscript is correctly scoped to (a) regime (A), the exponential
family, or (b) the n=1 single-report case. No section claims the
location-family sample-mean identity is finite-sample exact for general
kernels. No section claims DP release-consistency generalizes beyond
n=1. The correction is integrated consistently across the abstract,
introduction, consistency.tex (theorem, proof, remark, corollaries,
reach-map table), framework.tex sec:css, applications.tex, discussion.tex,
and conclusion.tex.

### Section-by-section agreement table

- main.tex abstract (l.96-104): "In a regular exponential family the
  identity is an exact finite-sample equality; in a location family it is
  exact for a single report and a population first-moment identity
  otherwise, with the finite-sample sample-mean form holding only up to an
  n^{-1/2} remainder and exactly only for the Gaussian kernel, which
  itself sits in the exponential-family regime." CORRECT and complete.
- introduction.tex (l.88-96): two regimes, "exact in finite samples"
  (regime A) vs "exact at a single report and a population first-moment
  identity otherwise" (regime B). CORRECT.
- introduction.tex (l.82): "This half carries no caveats" refers to the
  SINGLETON/RANK half, which is genuinely seam-free. NOT a location-
  identity claim. Correct usage.
- consistency.tex theorem (l.46-57): regime (B) stated in three precise
  senses (exact at n=1; population first-moment for any n; n^{-1/2} for
  n>1), with explicit "not an exact finite-sample sample-mean identity for
  n>=3 unless p_0 is Gaussian." CORRECT.
- consistency.tex proof regime (B) (l.81-109): derives the psi-location
  first-order condition, the Gaussian-iff via linear psi, n=1 exactness,
  and the O_p(n^{-1/2}) M-estimator statement with explicit variance
  V = Var(psi(Z)/J - Z). CORRECT and complete.
- consistency.tex rem:loc-sketch (l.112-146): the Cauchy-functional-
  equation argument at n=3, Gauss's characterization, the Laplace and
  logistic counterexamples, the log-concavity-not-unimodality point.
  CORRECT and now framed as a CHARACTERIZED boundary, not an open step.
- consistency.tex cor:dp (l.226-249): "This is the single-release case,
  n=1 ... it does not generalize to a sample-mean identity over several
  releases, which would require the Gaussian kernel." CORRECT pinning.
- framework.tex sec:css (l.101-108): regime (B) "the likelihood depends on
  the full sample through the score sum psi(R_i - mu) rather than through
  Tbar alone; the fit reproduces the sample psi-location exactly and Tbar
  exactly only for a single report or for the Gaussian kernel, with an
  O_p(n^{-1/2}) remainder otherwise." CORRECT. (This is the fix to the
  prior review's Minor-3 over-claim; verified resolved.)
- applications.tex DP subsection (l.49-63): "This domain sits in regime
  (B): release consistency (cor:dp) is the location-family first-moment
  identity, not the exponential-family one." CORRECT.
- discussion.tex (l.41-57): DP-is-location-family paragraph; "Release
  consistency lives at the single release (n=1) ... for n>=3 and a
  non-Gaussian kernel the sample-mean form picks up a genuine O_p(n^{-1/2})
  remainder ... There is nothing left open here." CORRECT.
- conclusion.tex (l.19-34): regime (A) "exact finite-sample mean-value
  identity"; regime (B) "exact at a single report and a population
  first-moment identity"; DP "exact single-release identity," Gaussian-iff.
  CORRECT.

The n=2 boundary is handled correctly by stating the genuine-failure
threshold as n>=3 (n in {1,2} is degenerate: the sample is symmetric about
its mean, so every symmetric kernel matches there). The "for any n" of the
population first-moment identity and the "n>1" of the O_p(n^{-1/2})
statement are mutually consistent.

## Settled-math spot check (not a re-derivation)

I ran .research/findings/counterexample_laplace_n3.py: on data (0,1,5) the
Laplace MLE is the median 1 against the mean 2, exact gap -1, with the
log-likelihood strictly favoring the median. This confirms the n=3
non-Gaussian failure the theorem now claims. The synthesis.md documents
the full kernel battery (logistic MLE 1.575..., generalized-normal and
sech kernels), the Gaussian-iff proof, and the O_p(n^{-1/2}) constant. The
math is correct and independently checkable. No error.

## Regime-(A) proof

Re-derived: log-partition gradient nabla A(eta) = E_eta[T], score in eta
is n(Tbar - E_eta[T]), full-column-rank Jacobian passes the stationarity
d_theta ell = 0 to d_eta ell = 0, hence E_hat[T] = Tbar. CORRECT. The
full-column-rank hypothesis is exactly the ingredient that licenses the
pass-through. No error.

## Clean corollaries still follow after the restructure

- cor:scrna (ZINB, regime A): m(theta) = (1-pi_j)mu_j = Xbar_j. Exact;
  ZINB observed-count law is a regular exponential family with mean-
  parameterized score. Faithful to the scRNA sibling. CORRECT.
- cor:spatial (Poisson, regime A): per-coordinate exact, vector form uses
  the joint rank condition (thm:general-rank). The dependence is correctly
  flagged as "the only place the rank condition enters a consistency
  claim." CORRECT.
- cor:phenotype (Bernoulli, regime A): q(pi,sens,spec) = Cbar, exact in
  the informative regime sens+spec>1 (nonzero mean gradient). CORRECT. The
  prior review's Minor-1 (state the 3->1 reparametrization explicitly) is
  partially addressed: cor:phenotype names the code frequency q as the
  natural mean parameter, which is the reparametrization; making the
  3-parameter-to-1 collapse fully explicit would still help the reader see
  why the chart-review singleton is needed. Carry as MINOR.
- cor:weaksup (regime A, seam): exact under sufficiency-complete
  parametrization, asymptotic n^{-1/2} for naive-Bayes. CORRECT and
  faithful.
- cor:dp (regime B, seam): single-release n=1 first-moment identity.
  CORRECT (see consistency hunt above).

## Residual logic items (all MINOR, all pre-existing, none introduced by the revision)

1. thm:general-rank(b) sufficiency still carries the reliability-specific
   parenthetical "(and, in the time-to-event instance, the mechanism
   assigns positive probability to both exact and censored reports)"
   inside a statement the prose calls seamless. This is a small domain-
   specific rider in a "general" theorem. Recommend moving to a remark or
   abstracting it. Pre-existing (prior review Minor-2); not yet addressed.
   Severity MINOR.
2. cor:phenotype reparametrization explicitness (above). MINOR.

## What I did NOT find (the things a botched revision usually leaves behind)

- No section asserts "fitted mean = empirical mean" as finite-sample exact
  for a general location kernel.
- No "exact for all/any/every kernel" claim survives.
- No DP statement generalizes release-consistency past n=1.
- The regularity hypothesis is uniformly "symmetric, log-concave" in the
  theorem and proof; "unimodal" survives only in the n=1 single-release
  context, where exactness for any symmetric unimodal density is correct.
- The weak-sup rate is Theta(r/gap^2) for L2/total recovery everywhere it
  appears (tab:reduction and discussion.tex open-problems), with
  Theta(log r/gap^2) correctly tagged as the per-direction (different-loss)
  rate.

No critical or major logic errors. The correction landed cleanly.
