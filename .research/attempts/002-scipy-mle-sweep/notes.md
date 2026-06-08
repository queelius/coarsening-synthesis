# Attempt 002: scipy MLE sweep (paper's actual route) + asymptotic rate

## Tried
- mle_sweep.py: fit location MLE via scipy minimize_scalar (Brent) + Brentq score
  polish, 4 kernels (gaussian, laplace, logistic, student-t nu=3) x n in
  {1,2,3,5,10,50,200}, 200-400 seeds each. Report max|score(theta_hat)|, gap stats.
- laplace_is_median_and_rate.py: (1) Laplace MLE == median over 2000 trials; (2) rms
  gap vs n for laplace & logistic, log-log slope.

## Happened
- Gaussian: gap ~1e-15 (machine eps) at ALL n. Identity exact.
- Laplace/logistic/student-t: n=1 gap ~1e-15; n=2 ~1e-15 (log-concave, degenerate);
  n>=3 gap O(0.1-1) while max|score(theta_hat)| ~1e-15. Genuine, 8-14 orders above tol.
  (student-t n=2 fails: bimodal likelihood.)
- Laplace MLE = median exactly. Gap = median - mean = Op(1).
- log-log slope of rms gap vs n = -0.482 ~ -1/2 (both kernels). rms*sqrt(n) -> const
  (1.0 Laplace, 0.53 logistic).

## Interpretation
The gap is a real inequality, not optimizer noise (the score is ~0 at theta_hat yet
the gap is O(0.1-1)). Identity fails at every finite n>=3 for non-Gaussian kernels but
the gap is Op(n^{-1/2}), so it holds asymptotically.
