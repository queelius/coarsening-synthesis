# Attempt 004: DP corollary reconciliation + final rigor

## Tried
- dp_single_release.py: fit theta from a single Normal-Laplace release; (had a
  quadrature artifact, see next).
- n1_exact_clean.py: ROUTE A analytic proof (mode-at-m) + clean numeric mode check;
  show the earlier ~1e-2 'gap' was a fixed quadrature offset (constant in m).
- interior_global_check.py: data (0,1,5), kernel battery (gaussian, laplace, logistic,
  gennorm beta=1.5/3/4, sech): theta_hat interior? global? gap? ell(th)>ell(mean)?

## Happened
- DP single release is n=1: log p_conv(m-theta) maximized at mode m-theta=0 =>
  theta_hat = m EXACTLY (any symmetric unimodal release, no scale/diff needed). Pure
  Laplace n=1 gap 8.88e-16. cor:dp / thm:release-consistency SAFE (n=1 first-moment).
- Kernel battery: every non-Gaussian theta_hat strictly interior, global max, gap !=0,
  ell(th)>ell(mean). Gaussian alone gap 0. Gap sign: leptokurtic negative (toward
  median), platykurtic positive.

## Interpretation
The DP corollary is correct because it is the n=1 case. The synthesis general-n
regime (B) sample-mean statement is the false part. Counterexample is a bona fide
interior global MLE.
