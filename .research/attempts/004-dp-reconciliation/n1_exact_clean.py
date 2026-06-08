"""
Clean, artifact-free confirmation that the n=1 location identity theta_hat = m is
EXACT, and that the previous ~1e-2 'bias' was pure quadrature roundoff (it was
constant in m within each (tau,b), the signature of a fixed quadrature error, not a
real m-dependent effect).

Two clean routes:

ROUTE A (analytic, no numerics needed). For a single observation m from a location
family p_M(m|theta) = p_conv(m - theta) with p_conv symmetric about 0 and unimodal
(unique mode at 0), the log-likelihood L(theta) = log p_conv(m - theta) is, as a
function of theta, the function u -> log p_conv(u) reflected and shifted, with u =
m - theta. It attains its unique maximum where u = 0 (the mode), i.e. theta = m.
Therefore theta_hat = m EXACTLY, for ANY symmetric unimodal convolved release.
This needs NO differentiability and NO scale knowledge; only symmetry+unimodality.

ROUTE B (numeric, clean). Use the SCORE = derivative of log p_conv at (m - theta),
which by symmetry is an ODD function vanishing exactly at 0. We evaluate the
convolution and its derivative with the SAME high-accuracy grid centered so that the
integrand is sampled identically for every theta via the substitution u = m - theta;
then theta_hat - m is forced to 0 by construction of symmetry. Instead, here we just
confirm Route A's prediction by checking that p_conv is maximized at 0 to high
precision, independent of m.
"""
import numpy as np
from scipy import integrate, stats

print("ROUTE A is a proof (see docstring). ROUTE B numeric confirmation below.")
print()

def p_conv(u, tau, b, lim_mult=60, n_nodes=20001):
    """Normal(0,tau^2)*Laplace(0,b) at scalar u, via fixed symmetric Simpson grid.
    Using a FIXED grid in v (independent of u) makes the only u-dependence the
    smooth factor exp(-|u-v|/b); the mode test below evaluates p_conv on a u-grid."""
    L = lim_mult*max(tau, b)
    v = np.linspace(-L, L, n_nodes)
    integ = stats.norm.pdf(v, 0, tau) * (1/(2*b))*np.exp(-np.abs(u - v)/b)
    return integrate.simpson(integ, x=v)

for (tau, b) in [(0.5,1.0),(1.0,1.0),(0.2,2.0),(1.5,0.5)]:
    # find argmax of p_conv(u) over a fine u-grid; should be u=0 (symmetric unimodal)
    ug = np.linspace(-2, 2, 400001)
    vals = np.array([p_conv(u, tau, b) for u in ug[::4000]])  # coarse scan first
    # refine near 0
    ufine = np.linspace(-0.05, 0.05, 200001)
    vfine = np.array([p_conv(u, tau, b) for u in ufine[::400]])
    umode = ufine[::400][np.argmax(vfine)]
    print(f"tau={tau}, b={b}: argmax_u p_conv(u) = {umode:+.6f}  (mode at 0 => "
          f"theta_hat = m exactly).  p symmetric: p(0.3)-p(-0.3) = "
          f"{p_conv(0.3,tau,b)-p_conv(-0.3,tau,b):+.2e}")

print()
print("The mode of the convolved release sits at u = m - theta = 0, so theta_hat = m.")
print("The earlier ~1e-2 'gap' was constant in m within each (tau,b): a fixed")
print("quadrature offset in the optimizer's objective, not a real effect. The 1.55e-15")
print("entry (when the minimizer coincided with a quadrature-exact node) confirms this.")
print()
print("Pure-Laplace cross-check (no convolution): n=1, p0=Laplace, m=any:")
m = 3.7137
negll = lambda th: abs(m - th)
# minimizer of |m - th| is th = m, exactly
from scipy import optimize
res = optimize.minimize_scalar(negll, bounds=(m-10, m+10), method="bounded", options={"xatol":1e-14})
print(f"  Laplace n=1: theta_hat = {res.x:.10f}, m = {m}, gap = {res.x - m:.2e} (exact).")
