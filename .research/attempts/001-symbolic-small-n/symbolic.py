"""
Symbolic analysis of the location-family MLE identity m(theta_hat) = T_bar.

Model (regime B): reports X_i = theta + Z_i, i = 1..n, Z_i iid from a fixed
symmetric mean-zero density p0 (scale fixed/known). The face-value log-likelihood
in the location mu = mu(theta) is
    ell(mu) = sum_i log p0(x_i - mu).
The implied mean m(theta) = E_theta[X] = mu + E[Z] = mu (Z mean zero), so the
claimed identity m(theta_hat) = T_bar is literally
    mu_hat = xbar  (arithmetic sample mean).
The MLE first-order condition is sum_i psi(x_i - mu) = 0 with psi = -p0'/p0.

We test three kernels: Gaussian (psi linear), Laplace (psi = sign), logistic
(psi = tanh-like). For each we examine whether the stationary mu_hat equals xbar
for n = 1, 2, 3 symbolically.
"""
import sympy as sp

print("=" * 70)
print("SYMBOLIC: location MLE stationarity, m(theta_hat)=mu_hat vs xbar")
print("=" * 70)

mu = sp.symbols('mu', real=True)

def report_case(name, psi_func, xs):
    """xs: list of sympy symbols/values for the reports. psi_func: u -> psi(u)."""
    n = len(xs)
    score = sum(psi_func(x - mu) for x in xs)
    xbar = sp.Rational(1, n) * sum(xs)
    print(f"\n--- {name}, n={n} ---")
    print("  score sum_i psi(x_i - mu) =", sp.simplify(score))
    # Solve score = 0 for mu
    try:
        sols = sp.solve(sp.Eq(score, 0), mu, dict=False)
    except Exception as e:
        sols = None
        print("  solve failed:", e)
    print("  stationary mu solving score=0:", sols)
    print("  arithmetic mean xbar =", sp.simplify(xbar))
    if sols:
        for s in sols:
            diff = sp.simplify(s - xbar)
            print(f"    mu_hat={s}  ->  mu_hat - xbar = {diff}")
    return score, xbar

# ---------------------------------------------------------------------------
# Gaussian: p0(u) = exp(-u^2/2)/sqrt(2pi), psi(u) = u  (scale 1)
# ---------------------------------------------------------------------------
print("\n" + "#" * 70)
print("# GAUSSIAN kernel: psi(u) = u (linear)")
print("#" * 70)
psi_gauss = lambda u: u
for n in (1, 2, 3):
    xs = sp.symbols(f'x0:{n}', real=True)
    report_case("Gaussian", psi_gauss, list(xs))

# ---------------------------------------------------------------------------
# Logistic: p0(u) = e^{-u}/(1+e^{-u})^2, psi(u) = -p0'/p0.
# log p0 = -u - 2 log(1+e^{-u}); d/du log p0 = -1 + 2 e^{-u}/(1+e^{-u})
#        = -1 + 2/(1+e^{u}) = (1 - e^{u})/(1+e^{u}) = -tanh(u/2).
# psi(u) = -d/du log p0 = tanh(u/2).
# ---------------------------------------------------------------------------
print("\n" + "#" * 70)
print("# LOGISTIC kernel: psi(u) = tanh(u/2)")
print("#" * 70)
psi_logistic = lambda u: sp.tanh(u/2)
for n in (1, 2, 3):
    xs = sp.symbols(f'x0:{n}', real=True)
    report_case("Logistic", psi_logistic, list(xs))

# ---------------------------------------------------------------------------
# Student-t (nu=1, Cauchy): p0(u) ~ 1/(1+u^2). log p0 = -log(1+u^2)+c.
# psi(u) = -d/du log p0 = 2u/(1+u^2).  (NOT monotone: redescending.)
# Cauchy is symmetric, NOT unimodal-log-concave but density IS unimodal.
# ---------------------------------------------------------------------------
print("\n" + "#" * 70)
print("# CAUCHY (Student-t nu=1) kernel: psi(u) = 2u/(1+u^2) (redescending)")
print("#" * 70)
psi_cauchy = lambda u: 2*u/(1+u**2)
for n in (1, 2):
    xs = sp.symbols(f'x0:{n}', real=True)
    report_case("Cauchy", psi_cauchy, list(xs))

print("\n(Cauchy n=3 with symbolic xi is a degree-5 polynomial; do numeric later.)")
