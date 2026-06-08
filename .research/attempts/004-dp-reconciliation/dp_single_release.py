"""
DP reconciliation. The DP release-consistency theorem (thm:release-consistency,
cor:dp) concerns a SINGLE release M = q(D) + Z. The analyst fits theta from the
marginal release density (a convolution), which is a LOCATION family in theta:
    p_M(m | theta) = p_conv(m - theta),
with p_conv = g0 * kappa the convolution of the (centered) query sampling density
g0 and the noise kernel kappa. Both g0 and kappa symmetric about 0 => p_conv
symmetric about 0. If additionally unimodal, the n=1 location MLE of a single m is
theta_hat = m EXACTLY (the mode-at-m argument): the unique maximizer of
log p_conv(m - theta) over theta is theta = m.

We verify for the ACTUAL DP release density used in the paper: Normal-Laplace
convolution (Gaussian sample mean of variance tau^2, Laplace mechanism noise).
We show theta_hat = m to optimizer tolerance for many m, for several (tau, b).

This confirms cor:dp / thm:release-consistency are SAFE: they are the n=1
first-moment identity E_{theta_hat,kappa}[M] = m, which holds EXACTLY for any
symmetric unimodal convolved release density. The synthesis's cor:dp invokes
regime (B) in its FIRST-MOMENT form at n=1, which is exactly the regime where the
identity is true.
"""
import numpy as np
from scipy import optimize, integrate, stats

def normal_laplace_logpdf(x, tau, b):
    """log density of N(0,tau^2) * Laplace(0,b) evaluated at x (vectorized scalar)."""
    # convolution integral; do it numerically with a fixed fine grid (symmetric)
    # p(x) = int phi(v; 0,tau) * (1/2b) exp(-|x-v|/b) dv
    f = lambda v: stats.norm.pdf(v, 0, tau) * (1/(2*b))*np.exp(-np.abs(x - v)/b)
    val, _ = integrate.quad(f, -40*max(tau,b), 40*max(tau,b), limit=200)
    return np.log(val)

def fit_theta_single(m, tau, b):
    # maximize log p_conv(m - theta) over theta  <=>  minimize -log p_conv(m-theta)
    negll = lambda th: -normal_laplace_logpdf(m - th, tau, b)
    res = optimize.minimize_scalar(negll, bounds=(m-20, m+20), method="bounded",
                                   options={"xatol": 1e-10})
    return res.x

print("Normal-Laplace convolved release (single release, n=1):")
print(f"{'tau':>6s} {'b':>6s} {'m':>8s} {'theta_hat':>12s} {'theta_hat-m':>14s}")
rng = np.random.default_rng(11)
worst = 0.0
for (tau, b) in [(0.5, 1.0), (1.0, 1.0), (0.2, 2.0), (1.5, 0.5)]:
    for _ in range(8):
        m = rng.normal(0, 3)
        th = fit_theta_single(m, tau, b)
        worst = max(worst, abs(th - m))
        print(f"{tau:>6.2f} {b:>6.2f} {m:>8.3f} {th:>12.6f} {th-m:>14.2e}")
print(f"\nmax |theta_hat - m| over all = {worst:.2e}  (=> theta_hat = m exactly)")
print("CONCLUSION: single-release DP consistency (cor:dp, thm:release-consistency)")
print("is the n=1 identity and is EXACT for the symmetric unimodal convolved release.")
print("The DP corollary is SAFE; it does not invoke the false general-n statement.")
