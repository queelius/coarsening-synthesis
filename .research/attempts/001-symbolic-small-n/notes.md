# Attempt 001: symbolic small-n analysis

## Tried
- sympy: location-MLE stationarity score sum_i psi(x_i - mu) for Gaussian (psi=u),
  logistic (psi=tanh(u/2)), Cauchy (psi=2u/(1+u^2)) at n=1,2,3 (symbolic.py).
- sympy: Laplace n=3 with explicit data (0,1,5): minimize sum|x_i-mu| (laplace_n3.py).
- mpmath 50-digit: logistic n=3 data (0,1,5) root + 2nd-order check (logistic_n3.py).

## Happened
- n=1: mu_hat = x0 for every kernel (psi odd => unique zero at x0). EXACT.
- n=2: mu_hat = midpoint = xbar for every symmetric kernel (oddness at midpoint).
- Laplace n=3 (0,1,5): MLE = median = 1, mean = 2, gap = -1 EXACT; ell(1)-ell(2)=1/b>0.
- Logistic n=3 (0,1,5): MLE = 1.5752, mean = 2, gap = -0.4248; ell''<0 strict max,
  beats mean by 0.069; score(mean) = -0.319 != 0 (mean not stationary).

## Interpretation
n<=2 are degenerate (always xbar). n>=3 breaks the arithmetic-mean identity for every
non-Gaussian kernel. The logistic case (smooth, strictly log-concave) shows the
failure is not an artifact of the Laplace kink. Mechanism: MLE = psi-location.
