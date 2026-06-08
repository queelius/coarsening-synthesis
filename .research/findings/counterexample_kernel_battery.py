"""
Final rigor checks on the counterexample, to forestall objections:

(1) The counterexample theta_hat is a GENUINE GLOBAL INTERIOR maximum of the
    face-value log-likelihood (not boundary, not merely local). For log-concave
    kernels the log-likelihood is concave so any stationary point is the unique
    global max. We verify by exhaustive fine grid that ell(theta_hat) is the global
    max and theta_hat lies strictly inside R (it is finite, between min and max
    report), and that ell(theta_hat) > ell(xbar) strictly.

(2) Wider symmetric-kernel battery at n=3 with the SAME asymmetric data (0,1,5):
    report theta_hat and the gap to the mean for many symmetric log-concave kernels,
    showing the gap is generic and only Gaussian gives 0.
"""
import numpy as np
from scipy import optimize

x = np.array([0.0, 1.0, 5.0])
xbar = x.mean()
print(f"data = {x}, arithmetic mean = {xbar}")
print()

# kernel: name -> log p0(u) up to const  (all symmetric, mean 0)
def kernels():
    K = {}
    K["gaussian"]   = lambda u: -0.5*u**2
    K["laplace"]    = lambda u: -np.abs(u)
    K["logistic"]   = lambda u: -u - 2*np.log1p(np.exp(-u))
    # generalized normal (Subbotin) shape beta: exp(-|u|^beta); beta=2 gaussian,
    # beta=1 laplace, beta=4 platykurtic, beta=1.5 between
    for beta in (1.5, 3.0, 4.0):
        K[f"gennorm_b{beta}"] = (lambda b: (lambda u: -np.abs(u)**b))(beta)
    # hyperbolic secant: log p0 = log sech(pi u/2) = -log cosh(pi u /2) + const
    K["sech"]       = lambda u: -np.log(np.cosh(np.pi*u/2))
    return K

print(f"{'kernel':14s} {'theta_hat':>11s} {'gap to mean':>13s} "
      f"{'ell(th)-ell(mean)':>18s} {'interior?':>10s} {'global?':>8s}")
print("-"*80)
for name, logp0 in kernels().items():
    ell = lambda th: np.sum(logp0(x - th))
    negll = lambda th: -ell(th)
    res = optimize.minimize_scalar(negll, bounds=(x.min()-30, x.max()+30),
                                   method="bounded", options={"xatol":1e-13})
    th = res.x
    # exhaustive grid for global check
    grid = np.linspace(x.min()-30, x.max()+30, 2000001)
    ell_grid = np.array([ell(g) for g in grid[::1]]) if False else None
    # cheaper: coarse + refine
    g1 = np.linspace(x.min()-30, x.max()+30, 60001)
    e1 = logp0(x[:,None]-g1[None,:]).sum(axis=0)
    g_star = g1[np.argmax(e1)]
    g2 = np.linspace(g_star-0.01, g_star+0.01, 200001)
    e2 = logp0(x[:,None]-g2[None,:]).sum(axis=0)
    th_global = g2[np.argmax(e2)]
    interior = (x.min() < th < x.max())  # strictly inside data range => interior of R
    is_global = abs(th - th_global) < 1e-3
    gap = th - xbar
    print(f"{name:14s} {th:>11.6f} {gap:>13.6f} {ell(th)-ell(xbar):>18.6e} "
          f"{str(interior):>10s} {str(is_global):>8s}")

print()
print("All non-Gaussian kernels: theta_hat strictly interior, global max, gap != 0,")
print("and ell(theta_hat) > ell(mean). Gaussian alone has gap = 0.")
