"""
Logistic location MLE at n=3: a SMOOTH (analytic, strictly log-concave) kernel
counterexample. This rules out the objection that the Laplace counterexample
exploits the kink in psi at 0.

Logistic p0(u) = e^{-u}/(1+e^{-u})^2 (standard logistic, symmetric, smooth,
strictly log-concave, unimodal). psi(u) = -p0'/p0 = tanh(u/2), which is smooth,
odd, strictly increasing, bounded => unique MLE root (strict log-concavity).

MLE first-order condition: sum_i tanh((x_i - mu)/2) = 0. We solve numerically
with mpmath at high precision and compare to the arithmetic mean.

Data x = (0, 1, 5): arithmetic mean = 2. We compute mu_hat and the gap, and
verify the second-order condition (strict max) and that it is the UNIQUE root.
"""
import mpmath as mp
mp.mp.dps = 50  # 50 decimal digits

xs = [mp.mpf(0), mp.mpf(1), mp.mpf(5)]
n = len(xs)
xbar = sum(xs)/n

def psi(u):
    return mp.tanh(u/2)

def score(mu):
    return sum(psi(x - mu) for x in xs)

def ell(mu):
    # log-likelihood up to additive const: sum log p0(x_i - mu)
    # log p0(u) = -u - 2 log(1+e^{-u}) ; symmetric so fine
    s = mp.mpf(0)
    for x in xs:
        u = x - mu
        s += -u - 2*mp.log(1 + mp.e**(-u))
    return s

# Solve score(mu) = 0. score is strictly decreasing in mu (since psi increasing in
# its arg, and -mu inside), so unique root. Bracket and use findroot.
mu_hat = mp.findroot(score, xbar)  # start at mean
print("data x =", [float(x) for x in xs])
print("arithmetic mean xbar =", mp.nstr(xbar, 20))
print("logistic MLE mu_hat   =", mp.nstr(mu_hat, 20))
print("score(mu_hat)         =", mp.nstr(score(mu_hat), 5), "(should be ~0)")
gap = mu_hat - xbar
print("GAP m(theta_hat) - T_bar = mu_hat - xbar =", mp.nstr(gap, 20))

# Confirm uniqueness: score strictly monotone -> derivative sign constant
dscore = lambda mu: mp.diff(score, mu)
print("\nscore'(mu_hat) =", mp.nstr(dscore(mu_hat), 8), "(nonzero, strict => unique root)")

# Confirm it is a MAXIMUM of ell: ell''(mu_hat) < 0
ell2 = mp.diff(ell, mu_hat, 2)
print("ell''(mu_hat)  =", mp.nstr(ell2, 8), "(<0 => strict local max)")
print("ell(mu_hat)    =", mp.nstr(ell(mu_hat), 12))
print("ell(xbar)      =", mp.nstr(ell(xbar), 12))
print("ell(mu_hat) - ell(xbar) =", mp.nstr(ell(mu_hat) - ell(xbar), 12),
      "(>0 => MLE strictly beats the mean)")

# Sanity: at the mean, the score is NOT zero (so mean is not stationary)
print("\nscore(xbar) =", mp.nstr(score(xbar), 12), "(nonzero => mean is NOT the MLE)")
