# Research State

## Sub-problems
1. Pin down the EXACT model in regime (B). RESOLVED: model is X_i = theta + Z_i,
   i=1..n, common scalar location theta, Z_i iid symmetric mean-zero, scale fixed.
   m(theta)=E[X]=theta, so claim "m(theta_hat)=T_bar" <=> "mu_hat = xbar".
   - status: resolved
2. CLAIM-N1: single report n=1, theta_hat = m exactly for any symmetric unimodal
   kernel. CONFIRMED exact (sympy + 50-digit mpmath + scipy 400 seeds, gap ~1e-15).
   - status: resolved (TRUE, exact)
3. CLAIM-GEN: general n, mu(theta_hat) = R_bar. FALSE for n>=3, any non-Gaussian
   symmetric kernel. (Laplace, logistic, student-t all fail with gap O(0.1-1) while
   score(theta_hat) ~ 1e-15.) - status: resolved (FALSE)
4. Explicit counterexample. DONE: Laplace data (0,1,5) -> MLE=median=1, mean=2,
   gap=-1 EXACT (sympy). Logistic same data -> 1.5752 vs 2, gap -0.4248 (smooth,
   strict log-concave; rules out kink objection). - status: resolved
5. Kernel-class characterization: identity holds for ALL data (all n) iff psi affine
   iff kernel Gaussian. Need rigorous proof. - status: in-progress
6. Implication for DP cor:dp / thm:release-consistency: DP single-release case is
   n=1 (one release M), where identity is EXACT. SAFE. But the synthesis general-n
   regime (B) statement is wrong as written. - status: in-progress (verify n meaning)
7. NEW: asymptotic rate. Gap = Op(n^{-1/2}); log-log slope -0.482 ~ -1/2;
   rms*sqrt(n) -> const (1.0 Laplace, 0.53 logistic). So identity holds
   ASYMPTOTICALLY at n^{-1/2}, fails at finite n>=3. - status: in-progress (get const)
8. NEW: student-t (nu=3, not log-concave) fails even at n=2 (bimodal likelihood,
   gap up to 7). Unimodality of p0 does NOT save it; need log-concavity for unique
   MLE, and even then identity fails for n>=3. - status: noted

## Hypotheses
1. CLAIM-N1 TRUE and exact (n=1 location MLE = the point). - status: CONFIRMED
   (sympy + mpmath 50-digit + scipy 400 seeds; analytic mode-at-m proof).
2. CLAIM-GEN FALSE for non-Gaussian symmetric kernels; mu_hat = psi-location,
   = arithmetic mean iff psi affine iff Gaussian; Laplace gives MEDIAN.
   - status: CONFIRMED (symbolic counterexample + Cauchy-eqn proof + sweep).
3. Correct statement = n=1/population first-moment identity, OR psi-location, OR
   asymptotic n^{-1/2}. - status: CONFIRMED (all three are the honest options;
   asymptotic constant V derived and verified).

## Current focus
ALL sub-problems resolved. Writing synthesis.md. Findings to promote:
- 001-symbolic-small-n (Laplace exact counterexample, n=1/2 degeneracy)
- 002-scipy-mle-sweep (genuine-gap sweep + n^{-1/2} rate)
- 003-characterization-proof (Cauchy reduction => Gaussian iff; asymptotic constant)
- 004-dp-reconciliation (DP n=1 exact; counterexample interior+global; kernel battery)

FINAL ANSWER:
(a) NO. The finite-sample identity m(theta_hat)=T_bar does NOT hold for all symmetric
    kernels at n>=3.
(b) Counterexample (verified, with mechanism): Laplace, data (0,1,5), MLE=median=1,
    mean=2, gap=-1 EXACT; logistic same data gap=-0.4248 (smooth, rules out kink);
    wide log-concave battery all nonzero, interior, global. Mechanism: location MLE
    is the M-estimator/psi-location, = arithmetic mean iff psi affine.
(c) Precise characterization (proved): identity holds for ALL samples at some/every
    n>=3 IFF psi=-p0'/p0 is affine IFF p0 Gaussian. For non-Gaussian kernels it holds
    EXACTLY at n in {1,2} (degenerate symmetric configs) and only ASYMPTOTICALLY for
    n>=3, with gap sqrt(n)(theta_hat-xbar) -> N(0,V), V=Var(psi(Z)/J - Z),
    J=E[psi'(Z)] (Laplace V=1, logistic V=0.290). Op(n^{-1/2}).

Implications:
- DP cor:dp / thm:release-consistency: SAFE. Single release => n=1 => theta_hat=m
  EXACT for any symmetric unimodal release density (mode-at-m argument, no scale
  needed). The DP first-moment identity E[M]=m_obs is the n=1 case. No over-claim
  there, BUT the synthesis cor:dp inherits its truth ONLY because n=1; it must not be
  read as a general-n sample-mean identity.
- Synthesis thm:general-consistency regime (B): the general-n sample-mean form is
  FALSE for non-Gaussian kernels. Must be restated (options in synthesis.md):
  restrict to Gaussian; OR replace T_bar by the psi-location; OR state as the n=1 /
  population first-moment identity + n^{-1/2} asymptotic; OR fold (B) into (A) since
  Gaussian-location is also exponential-family.
- Hypotheses: regime (B) should require LOG-CONCAVE p0 (not merely unimodal) for the
  MLE to be unique/well-defined (student-t nu=2 gives bimodal likelihood, mean is a
  valley).

## Sub-problem statuses (final)
1 resolved, 2 resolved (TRUE n=1), 3 resolved (FALSE n>=3), 4 resolved, 5 resolved
(iff Gaussian, proved), 6 resolved (DP safe via n=1), 7 resolved (n^{-1/2}, constant
V), 8 resolved (need log-concavity).
