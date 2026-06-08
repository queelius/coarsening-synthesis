# Logic Checker Report

**Paper**: One consistency theorem for coarsened-data maximum likelihood
**Date**: 2026-06-08
**Focus**: proof correctness, logical chain integrity, claim support, with
special attention to the freshly integrated MIL corollary (cor:mil) and the
"seven domains, six corollaries" accounting.

## Summary

The mathematical spine is sound. Regime (A) is a correct, complete proof of the
exponential-family mean-value identity via the log-partition gradient. Regime
(B) is correctly characterized: the M-estimator psi-location identity is exact
finite-sample, the sample-mean form is Gaussian-iff (Teicher), and the
asymptotic variance V = Var(psi(Z)/J - Z) is the correct linearization of
hat-mu minus R-bar. The (0,1,5) Laplace example checks out (median 1, mean 2,
gap -1). The singleton/rank apparatus is stated as a sketch citing
towell2026masked and is internally consistent.

The MIL integration is mathematically correct at the level of the score
equation but introduces one classification looseness and one stale count. The
score identity M^T D^{-1}(Y - p_hat) = 0 is the *correct* normal equation for a
noisy-OR-linked Bernoulli GLM (verified below). The problem is that this
identity is NOT the conclusion eq:general-consistency (m(theta_hat) = bar T,
unweighted) that the general theorem actually states, so labeling cor:mil a
clean "regime (A) exact" corollary overstates how cleanly it instantiates the
theorem.

## Verified-correct results

### Regime (A) proof (consistency.tex:65-79). CORRECT.
For p(r|theta) = h(r) exp{eta(theta)^T T(r) - A(eta)}, the gradient
partial_eta ell = sum_i T(R_i) - n grad A(eta) = n(bar T - E_eta[T]) using
grad A = E_eta[T]. Chain rule + full-column-rank Jacobian at an interior max
gives partial_eta ell = 0, hence E_{theta_hat}[T] = bar T. This is exactly
eq:general-consistency. No gap.

### Regime (B) characterization (consistency.tex:81-110, rem:loc-sketch). CORRECT.
- Location score partial_mu log p = -p_0'(r-mu)/p_0(r-mu) = psi(r-mu), psi
  odd nondecreasing for symmetric log-concave p_0, so sum psi(R_i - hat-mu)=0
  has a unique interior root. Exact identity m(theta_hat)=hat-mu. Sound.
- Gaussian-iff-sample-mean: stationarity at R-bar for all samples forces
  psi(a)+psi(b)=psi(a+b) (Cauchy equation) at n=3, monotone solutions linear,
  log p_0 quadratic, Gaussian. This is Teicher (1961), correctly attributed.
  Sound.
- V = Var(psi(Z)/J - Z), J = E[psi'(Z)]: from hat-mu - mu_0 ~ (1/n) sum
  psi(Z_i)/J and R-bar - mu_0 = (1/n) sum Z_i, the difference linearizes to
  (1/n) sum [psi(Z_i)/J - Z_i], variance Var(psi(Z)/J - Z). Correct.
- (0,1,5) example: Laplace MLE = median = 1, mean = 2, gap -1. Correct. The
  logistic-at-strict-interior-maximum remark correctly rules out a kink
  artifact. Sound.

### cor:dp (regime B, n=1). CORRECT.
For symmetric unimodal p_conv, the single-release log-density is maximized at
mu(theta_hat) = m, and mode = mean gives E[M] = m_obs. The "does not generalize
to a sample-mean identity over several releases" caveat is consistent with the
theorem. Sound, and the seam is honestly stated.

### cor:phenotype (regime A). CORRECT.
The single-code Bernoulli law depends on (pi, sens, spec) only through
q = pi*sens + (1-pi)(1-spec), the mean parameter; eq:general-consistency reads
q(theta_hat) = bar C. The 3->1 collapse motivating the chart-review singleton
is correctly identified. The "informative regime sens+spec>1 (nonzero mean
gradient)" qualifier is the right full-rank condition. Sound.

### cor:weaksup (regime A under sufficiency, asymptotic otherwise). CORRECT and honest.
The corollary is explicit that agreement indicators are sufficient statistics
only under a sufficiency-complete parametrization, and that the naive-Bayes
data-programming model gives only an n^-1/2 asymptotic identity. This seam is
stated correctly and matches the discussion and abstract. Sound.

### MIL score equation M^T D^{-1}(Y - p_hat) = 0 (cor:mil). DERIVATION CORRECT.
With eta_i = m_i^T s, p_i = 1 - exp(-eta_i), so 1 - p_i = exp(-eta_i) and
dp_i/deta_i = exp(-eta_i) = 1 - p_i. Bernoulli score:
d ell/d s = sum_i [Y_i/p_i - (1-Y_i)/(1-p_i)] (dp_i/deta_i) m_i
         = sum_i [(Y_i - p_i)/(p_i(1-p_i))] (1-p_i) m_i
         = sum_i [(Y_i - p_i)/p_i] m_i
         = M^T D^{-1}(Y - p), D = diag(p).
Setting to zero gives exactly M^T D^{-1}(Y - p_hat) = 0. The "variance-link
factor of the log-survival (noisy-OR) link" description is accurate: the
1/p_i = 1/(p_i(1-p_i)) * (1-p_i) factor is precisely the non-canonical-link IRLS
weight. The math is right.

## Findings

### [MAJOR] cor:mil is not a special case of the theorem's stated conclusion
**Location**: consistency.tex:213-234 (cor:mil), against the theorem
statement consistency.tex:38-45 (eq:general-consistency) and tab:reduction
row "Bag-prevalence (MIL) ... (A) ... exact finite-sample identity"
(consistency.tex:300).
**Quoted text (theorem)**: "In regime (A) the fitted mean of the
coarsening-sufficient statistic equals its empirical mean as an exact
finite-sample identity, in every coordinate of $\T$, $m(\hat\theta) = \bar\T$".
**Quoted text (corollary)**: "Then \eqref{eq:general-consistency} reads
$M^\top D^{-1}(\bm Y - \hat{\bm p}) = \bm 0$ ... the inverse-fitted-rate
weighting $D^{-1}$ is the only wrinkle ... so the moment matching is
IRLS-weighted rather than unweighted."
**Problem**: eq:general-consistency is the UNWEIGHTED identity m(theta_hat) =
bar T. For MIL that would be p_hat = bar Y coordinatewise (sum_i (Y_i - p_i) =
0). What the corollary actually derives is the *weighted* equation
M^T D^{-1}(Y - p_hat) = 0, which is a different statement, true precisely
because the noisy-OR link is non-canonical (the corollary says so). So when the
corollary writes "eq:general-consistency reads M^T D^{-1}(Y - p_hat) = 0," that
is not a reading of eq:general-consistency; it is a reading of the *score
equation* (partial eta/partial theta)^T (bar T - E[T]) = 0 BEFORE the
full-column-rank step strips the Jacobian. cor:scrna and cor:phenotype genuinely
satisfy m(theta_hat)=bar T (canonical mean parameter); cor:mil does not. The
reach symbol `bullet` ("Exact finite-sample identity") in tab:reduction puts MIL
in the same clean bucket, which overstates the fit.
**Why it matters**: the user specifically asked whether the MIL regime-(A)
classification is correct. As written it is looser than the theorem licenses:
MIL is regime (A) in the GLM/score-equation sense, not the stripped
m(theta_hat)=bar T sense. This is the same family of subtlety the paper handles
correctly for spatial (vector form needs the rank condition) but here it bites
at the *scalar/per-coordinate* level via the link weighting.
**Suggestion**: one of two small fixes. (a) Add a clause to cor:mil noting that
the noisy-OR link is non-canonical, so the corollary instantiates the
*score-equation form* (partial eta/partial theta)^T(bar T - E[T]) = 0 of regime
(A) rather than the stripped identity m(theta_hat)=bar T, the D^{-1} being the
Jacobian/IRLS weight; OR (b) state the theorem's regime (A) conclusion in its
score-equation form once and note that for canonical-link members it collapses
to m(theta_hat)=bar T (scrna, phenotype, spatial-Poisson) while for
non-canonical links (MIL noisy-OR) it carries the IRLS weight. Option (b) is
cleaner and makes cor:mil a true corollary. Either way, the tab:reduction
legend for MIL should distinguish "exact, IRLS-weighted" from the unweighted
exact rows.

### [MAJOR] Stale count: "the other four corollaries" should be "five"
**Location**: consistency.tex:276 (inside cor:dp).
**Quoted text**: "its proof uses the location-family score identity, not the
exponential-family mean-value identity that serves the other four corollaries."
**Problem**: DP is being contrasted against the regime-(A) corollaries. After
the MIL fold-in those are cor:scrna, cor:spatial, cor:phenotype, cor:mil,
cor:weaksup = FIVE, not four. The parallel sentence in the introduction
(introduction.tex:126) already says "the exponential-family branch that serves
the other five domains," and the discussion (discussion.tex:42) says "The other
five consistency theorems." So consistency.tex:276 is the one location the MIL
integration missed; it still carries the pre-MIL count of four.
**Why it matters**: this is the flagship paper's own accounting of its central
claim. A reader cross-checking the three parallel sentences finds 5 / 4 / 5 and
will not know which is right. Self-consistency of the count is load-bearing for
a "state it once" synthesis.
**Suggestion**: change "the other four corollaries" to "the other five
corollaries" at consistency.tex:276.

### [MINOR] "ZINB ... is a regular exponential family" is imprecise
**Location**: consistency.tex:172-175 (cor:scrna).
**Quoted text**: "The reduction is exact: the ZINB observed-count law is a
regular exponential family with the mean-parameterized score $\partial_\mu \log
g(x; \mu, \phi) = (x - \mu)/[\mu(1+\mu\phi)]$, which is the regime-(A)
hypothesis."
**Problem**: a zero-inflated negative binomial with a free zero-inflation
parameter pi_j is a two-component mixture (point mass at 0 plus NB), which is
generically NOT a regular exponential family. Moreover the score displayed,
(x-mu)/[mu(1+mu phi)], is the *negative-binomial* mean-score at fixed
dispersion, not the ZINB score (the ZINB score in mu carries the zero-inflation
weight). The consistency *identity* (1-pi_hat)mu_hat = X_bar is correct and is
genuinely what regime (A) would give if the observed-count law were exp-family
with T=X and mean (1-pi)mu; the defect is the *justification*, which conflates
ZINB with NB and overstates exponential-family membership.
**Suggestion**: rephrase to "the observed-count mean is (1-pi)mu and the NB
component is a one-parameter exponential family at fixed dispersion; the
identity is the mean-match (1-pi_hat)mu_hat = X_bar," or cite the sibling for
the precise family statement rather than asserting ZINB is a regular exponential
family. This is the same loose move as the MIL "Bernoulli ... regular
exponential family" claim; tightening both would make the regime-(A) hypothesis
applications uniform.

### [MINOR] Abstract states the identity in unweighted form without the MIL caveat
**Location**: main.tex:109-111 (abstract).
**Quoted text**: "the face-value likelihood can be maximized without modeling
the coarsening, and the fit reproduces the empirical mean of a
coarsening-sufficient statistic at the optimum."
**Problem**: for MIL the fit reproduces the empirical mean only in the
IRLS-weighted (column-space-of-M, D^{-1}) sense, not the flat
"reproduces the empirical mean" sense. Same looseness as the MAJOR MIL finding,
surfacing in the abstract. The abstract does immediately qualify the boundary,
so this is minor, but if the MAJOR finding is fixed by adopting the
score-equation framing, the abstract sentence should track it (e.g., "reproduces
the empirical mean of a coarsening-sufficient statistic, exactly or in an
IRLS-weighted sense, at the optimum").
**Suggestion**: align with whichever fix is chosen for the MIL classification.

## Cross-check requests for other specialists
- methodology-auditor: independently reproduce the MIL score derivation and
  confirm M^T D^{-1}(Y - p_hat) = 0 is the noisy-OR GLM normal equation, and
  judge whether calling it "regime (A) exact" is a methodology overstatement.
- prose-auditor: the symbol M is overloaded (DP release scalar vs MIL
  composition matrix) within consistency.tex; flag for clarity.
