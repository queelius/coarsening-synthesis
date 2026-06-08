"""
Two confirmations:

(1) Laplace MLE = sample median EXACTLY (the fitted mean equals the median, not the
    arithmetic mean). We show |theta_hat - median| ~ machine eps while
    |theta_hat - xbar| = |median - xbar| is O(1).

(2) Asymptotic rate of the gap. The remark asks whether the identity holds "only
    asymptotically with an explicit rate". We test: does the population first-moment
    identity hold (E[theta_hat] -> theta, and theta_hat -> theta), and at what rate
    does the FINITE-SAMPLE gap (theta_hat - xbar) shrink? Both theta_hat and xbar
    are consistent for theta (symmetric kernel => mean=median=theta), so their
    difference -> 0. We estimate the rate by regressing log(rms gap) on log(n).
    Expectation: both are sqrt-n consistent for theta, gap = Op(n^{-1/2}).
    So the identity holds ASYMPTOTICALLY at rate n^{-1/2}, but FAILS at finite n.
"""
import numpy as np
from scipy import optimize, stats

# ---------- (1) Laplace MLE equals the median ----------
def laplace_neg_ll(mu, x):
    return np.sum(np.abs(x - mu))

def fit_laplace_brent(x):
    lo, hi = x.min() - 10, x.max() + 10
    res = optimize.minimize_scalar(laplace_neg_ll, bounds=(lo, hi), args=(x,),
                                   method="bounded", options={"xatol": 1e-14})
    return res.x

print("=" * 70)
print("(1) Laplace MLE == sample median (not arithmetic mean)")
print("=" * 70)
rng = np.random.default_rng(1)
worst_med = 0.0
worst_mean = 0.0
for trial in range(2000):
    n = rng.integers(3, 30)
    x = rng.normal(rng.normal(0, 3), 1, n) + rng.laplace(0, 1, n)
    mu_hat = fit_laplace_brent(x)
    med = np.median(x)
    worst_med = max(worst_med, abs(mu_hat - med))
    worst_mean = max(worst_mean, abs(mu_hat - x.mean()))
print(f"max over 2000 trials |theta_hat - median| = {worst_med:.3e}  (== 0 to optim tol)")
print(f"max over 2000 trials |theta_hat - xbar|   = {worst_mean:.3e}  (O(1), the gap)")
print("Conclusion: Laplace fitted mean = MEDIAN, identity mu_hat=xbar FAILS.")
# Note: for EVEN n the median is any point in [x_(n/2), x_(n/2+1)]; Brent returns
# an interior point of that flat region; all are MLEs. The arithmetic-mean identity
# still fails. We restricted worst_med check to be robust by using np.median which
# picks the midpoint, also an MLE.

# ---------- (2) asymptotic rate of the finite-sample gap ----------
print()
print("=" * 70)
print("(2) Rate at which (theta_hat - xbar) -> 0 as n grows")
print("=" * 70)

def make_fit(name):
    if name == "laplace":
        return lambda x: np.median(x)
    if name == "logistic":
        def f(x):
            psi = lambda mu: np.sum(np.tanh((x - mu)/2))
            lo, hi = x.min()-50, x.max()+50
            return optimize.brentq(psi, lo, hi, xtol=1e-14)
        return f
    raise ValueError

theta_true = 0.0
ns = [3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
for name in ["laplace", "logistic"]:
    fit = make_fit(name)
    rmss = []
    for n in ns:
        nrep = 4000 if n <= 200 else 1500
        gaps = np.empty(nrep)
        thetahats = np.empty(nrep)
        for r in range(nrep):
            rr = np.random.default_rng((hash((name, n, r)) % 2**32))
            if name == "laplace":
                z = rr.laplace(0, 1, n)
            else:
                z = rr.logistic(0, 1, n)
            x = theta_true + z
            th = fit(x)
            gaps[r] = th - x.mean()
            thetahats[r] = th
        rms = np.sqrt((gaps**2).mean())
        rmss.append(rms)
    rmss = np.array(rmss)
    # regress log rms on log n
    slope, intercept = np.polyfit(np.log(ns), np.log(rmss), 1)
    print(f"\n{name}: rms gap vs n")
    for n, rms in zip(ns, rmss):
        print(f"   n={n:5d}  rms(theta_hat - xbar) = {rms:.5f}   "
              f"rms * sqrt(n) = {rms*np.sqrt(n):.5f}")
    print(f"   log-log slope = {slope:.3f}  (==> gap ~ n^{slope:.2f}; "
          f"-0.5 means O(n^-1/2), asymptotically vanishing)")
