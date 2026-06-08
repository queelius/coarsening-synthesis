# Goal

Settle the open mathematical step in the coarsening-synthesis general consistency
theorem, regime (B) (location family), flagged in
`sections/consistency.tex` remark `rem:loc-sketch`.

## Source statements (verbatim pointers)

- General consistency theorem: `coarsening-synthesis/sections/consistency.tex`,
  `thm:general-consistency`. Regime (B) "Location family": coarsened report law
  p(r|theta) = p0(r - mu(theta)) for fixed symmetric unimodal density p0 with
  finite mean, and T(R)=R. Claim: at interior MLE theta_hat,
      m(theta_hat) = T_bar,  with T_bar = (1/n) sum_i T(R_i),
  i.e. in scalar form mu(theta_hat) = R_bar (arithmetic mean of reports).
- The remark `rem:loc-sketch` concedes: exact for Gaussian; for general symmetric
  kernel only a population first-moment identity, NOT a finite-sample sample-mean
  identity. Declared "the one genuinely open step".
- Framework C1/C2/C3 and the coarsening-sufficient statistic: `framework.tex`.
- DP corollary `cor:dp` uses regime (B): release consistency
  E_{theta_hat,kappa}[M] = m_obs. Its own theorem `thm:release-consistency`
  (dp-coarsening/sections/identifiability.tex) plus validation.tex assert that for
  a SINGLE symmetric release the MLE equals m exactly, any symmetric kernel.

## THE QUESTION

In the location-family regime X = theta + Z, Z symmetric mean-zero:
(a) Does the finite-sample identity m(theta_hat) = T_bar hold EXACTLY at the
    interior MLE for ALL symmetric kernels? Prove if yes.
(b) If not, explicit counterexample (e.g. Laplace, small n).
(c) If intermediate, characterize precisely (kernel class / asymptotic rate /
    bounded error with explicit bound).

## Two distinct claims to disentangle (already identified)

CLAIM-N1 (DP single release, n=1): theta_hat = m exactly for any symmetric
unimodal kernel. (location MLE of a single point.)
CLAIM-GEN (synthesis regime B, general n): mu(theta_hat) = R_bar, fitted mean
equals ARITHMETIC sample mean. This is the M-estimator-location-vs-mean question.

## Deliverable

`.research/synthesis.md`: outcome, rigorous argument, implication for BOTH the
synthesis consistency theorem and the DP release-consistency corollary, and the
exact restatement the paper should adopt. Do NOT edit any .tex.

## Conventions
No U+2014 em-dash in any written file. Rigor and honesty over tidiness.
