"""
Numerical MLE experiments (the paper's actual route: scipy.optimize) to confirm
that the location-MLE-vs-arithmetic-mean gap is GENUINE, not optimizer tolerance.

Model: X_i = theta + Z_i, i=1..n, Z_i iid from a symmetric mean-zero kernel of
fixed scale. Fit theta_hat = argmax sum_i log p0(x_i - theta). Implied mean
m(theta_hat) = theta_hat (Z mean zero), so we compare theta_hat to xbar.

For each kernel and n we run many seeds, fit the MLE with a high-accuracy 1-D
optimizer (Brent, plus a Newton polish on the score), and report:
  - max |score(theta_hat)| over seeds  (should be ~machine eps => true optimum)
  - distribution of (theta_hat - xbar) across seeds
  - whether the gap exceeds optimizer tolerance by orders of magnitude.

Kernels (all scale 1, mean 0, symmetric):
  gaussian : psi(u) = u                      (linear)        -> expect gap == 0
  laplace  : psi(u) = sign(u)                (kinked)        -> theta_hat = median
  logistic : psi(u) = tanh(u/2)              (smooth, s-log-concave)
  student3 : Student-t, nu=3 (heavy tail, smooth, NOT log-concave)
  uniform-ish via "secant"? skip; uniform not full support.
"""
import numpy as np
from scipy import optimize, stats

rng_master = np.random.default_rng(20260603)

# ---- kernel definitions: log-density (up to const) and psi = -d/dmu log p0 ----
def make_kernel(name):
    if name == "gaussian":
        logpdf = lambda u: -0.5 * u**2
        psi = lambda u: u  # = -d/du logp0 with sign s.t. score = sum psi(x-mu)
        # NOTE: score in mu: d/dmu sum logp0(x-mu) = sum (-logp0'(x-mu)) = sum psi(x-mu)
        # with psi(u) = -logp0'(u). For gaussian logp0'(u) = -u => psi(u)=u. ok.
        return logpdf, psi
    if name == "laplace":
        logpdf = lambda u: -np.abs(u)
        psi = lambda u: np.sign(u)
        return logpdf, psi
    if name == "logistic":
        # standard logistic, scale 1: logp0(u) = -u - 2 log(1+e^{-u})
        def logpdf(u):
            return -u - 2*np.log1p(np.exp(-u))
        psi = lambda u: np.tanh(u/2)
        return logpdf, psi
    if name == "student3":
        nu = 3.0
        c = 0.0  # const dropped
        logpdf = lambda u: -((nu+1)/2)*np.log1p(u**2/nu)
        psi = lambda u: (nu+1)*u/(nu + u**2)
        return logpdf, psi
    raise ValueError(name)

def neg_ll(mu, x, logpdf):
    return -np.sum(logpdf(x - mu))

def score(mu, x, psi):
    # d/dmu sum logp0(x - mu) = sum psi(x - mu),  psi(u) = -logp0'(u)
    return np.sum(psi(x - mu))

def fit_mle(x, logpdf, psi):
    lo, hi = x.min() - 50.0, x.max() + 50.0
    # Brent on negative log-likelihood
    res = optimize.minimize_scalar(neg_ll, bounds=(lo, hi), args=(x, logpdf),
                                   method="bounded",
                                   options={"xatol": 1e-14})
    mu0 = res.x
    # Polish via Brentq on the score where applicable (score strictly monotone for
    # log-concave kernels). For non-monotone (student3) keep the Brent optimum.
    try:
        s_lo, s_hi = score(lo, x, psi), score(hi, x, psi)
        if s_lo * s_hi < 0:
            mu_polish = optimize.brentq(score, lo, hi, args=(x, psi),
                                        xtol=1e-15, rtol=1e-15, maxiter=200)
            # accept polish only if it improves or matches the objective
            if neg_ll(mu_polish, x, logpdf) <= neg_ll(mu0, x, logpdf) + 1e-12:
                mu0 = mu_polish
    except Exception:
        pass
    return mu0

def laplace_median(x):
    return np.median(x)

print(f"{'kernel':9s} {'n':>4s} {'seeds':>6s} {'max|score|':>12s} "
      f"{'mean gap':>12s} {'max|gap|':>12s} {'rms gap':>12s} {'verdict'}")
print("-" * 90)

for name in ["gaussian", "laplace", "logistic", "student3"]:
    logpdf, psi = make_kernel(name)
    for n in [1, 2, 3, 5, 10, 50, 200]:
        nseeds = 400 if n <= 50 else 200
        gaps = np.empty(nseeds)
        max_score = 0.0
        for s in range(nseeds):
            rng = np.random.default_rng((hash((name, n, s)) % (2**32)))
            theta_true = rng.normal(0, 1)
            # draw noise from the kernel
            if name == "gaussian":
                z = rng.normal(0, 1, n)
            elif name == "laplace":
                z = rng.laplace(0, 1, n)
            elif name == "logistic":
                z = rng.logistic(0, 1, n)
            elif name == "student3":
                z = stats.t.rvs(3, size=n, random_state=rng)
            x = theta_true + z
            mu_hat = fit_mle(x, logpdf, psi)
            gaps[s] = mu_hat - x.mean()
            max_score = max(max_score, abs(score(mu_hat, x, psi)) if name != "laplace" else 0.0)
        verdict = ("identity holds" if np.max(np.abs(gaps)) < 1e-9
                   else "IDENTITY FAILS")
        print(f"{name:9s} {n:>4d} {nseeds:>6d} {max_score:>12.2e} "
              f"{gaps.mean():>12.3e} {np.max(np.abs(gaps)):>12.3e} "
              f"{np.sqrt((gaps**2).mean()):>12.3e}  {verdict}")
    print()
