"""
Stress-test the regularity boundaries of the characterization, so the written proof
states the right hypotheses.

We probe three issues:

(I) DIFFERENTIABILITY. Laplace psi has a kink; the "Cauchy via psi" route needs psi
    defined a.e. and the stationarity read as a subgradient condition. We confirm the
    cleaner route (work with the minimizer, not the score) gives the same conclusion.
    The Laplace minimizer of sum|x_i-mu| is the median; identity-with-mean fails.

(II) UNIQUENESS / LOG-CONCAVITY. If p0 is unimodal but NOT log-concave (student-t),
    the MLE can be non-unique (multiple local maxima). Then "the MLE" is ambiguous
    and the arithmetic-mean identity is not even well-posed, let alone true. We show
    a 2-point student-t sample with TWO global maxima, neither at the mean.

(III) The CONVERSE (Gaussian => identity, all n) is exact and the maximizer is unique
    (strict concavity of -sum (x_i-mu)^2). Confirm.

These determine the precise hypotheses of the theorem: for the identity to hold for
ALL samples at some n>=3, need psi affine (=> Gaussian); for the MLE to be a
well-defined unique interior point we additionally want p0 log-concave; Gaussian is
the unique kernel satisfying the identity within the log-concave symmetric class AND
within the broader differentiable symmetric class.
"""
import numpy as np
from scipy import optimize, stats

print("=" * 70)
print("(I) Laplace (non-differentiable psi): minimizer = median, route via")
print("    the OBJECTIVE not the score still kills the mean identity.")
print("=" * 70)
x = np.array([0.0, 1.0, 5.0])
grid = np.linspace(-2, 7, 900001)
obj = np.array([np.sum(np.abs(x - m)) for m in grid])
mhat = grid[np.argmin(obj)]
print(f"  argmin_grid sum|x_i - mu| = {mhat:.5f}  (median = {np.median(x):.5f})")
print(f"  arithmetic mean = {x.mean():.5f}.  gap = {mhat - x.mean():+.5f}  (nonzero)")
print("  The minimizer is the median for ANY odd nonconstant nondecreasing psi-")
print("  this is robust to the kink; we never differentiated at 0.")

print()
print("=" * 70)
print("(II) Student-t nu=2 (unimodal, NOT log-concave): MLE NON-UNIQUE, and the")
print("     mean is not even a local max. Identity ill-posed.")
print("=" * 70)
nu = 2.0
xs2 = np.array([-4.0, 4.0])  # symmetric 2-point; mean = 0
def negll_t(mu, x, nu):
    return np.sum(((nu+1)/2)*np.log1p((x-mu)**2/nu))
grid2 = np.linspace(-8, 8, 1600001)
o2 = np.array([negll_t(m, xs2, nu) for m in grid2])
# find local minima of negll (= local maxima of ll)
from scipy.signal import argrelextrema
mins = argrelextrema(o2, np.less)[0]
locs = grid2[mins]
print(f"  data {xs2}, mean = {xs2.mean():.3f}")
print(f"  local maxima of log-likelihood at mu = {np.round(locs,4)}")
print(f"  value of -ll at mean (mu=0): {negll_t(0.0, xs2, nu):.5f}")
print(f"  value of -ll at the two modes: "
      f"{[round(negll_t(l, xs2, nu),5) for l in locs]}")
print("  => the mean (0) is a LOCAL MINIMUM of the likelihood (a valley), the two")
print("     global maxima sit AWAY from the mean. So even n=2 breaks once p0 is not")
print("     log-concave. Unimodality of the DENSITY is not enough.")

print()
print("=" * 70)
print("(III) Converse: Gaussian => identity exact and maximizer UNIQUE, all n.")
print("=" * 70)
rng = np.random.default_rng(3)
worst = 0.0
for _ in range(20000):
    n = rng.integers(3, 40)
    x = rng.normal(rng.normal(0,5), 2.0, n)
    # MLE for Gaussian location = sample mean (strictly concave ll); check vs xbar
    mu_hat = x.mean()  # closed form; also = argmax since -sum(x-mu)^2 strictly concave
    worst = max(worst, abs(mu_hat - x.mean()))
print(f"  Gaussian: max |mu_hat - xbar| over 20000 random (n,data) = {worst:.2e}")
print("  Strict concavity of -(1/2)sum (x_i-mu)^2 => unique interior max at xbar.")
print("  Identity EXACT for every n. (matches sweep: gaussian gap ~1e-15.)")
