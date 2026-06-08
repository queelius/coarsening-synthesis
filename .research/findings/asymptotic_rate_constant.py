"""
Explicit asymptotic constant for the finite-sample gap (theta_hat - xbar).

General M-estimator theory (van der Vaart, Asymptotic Statistics, Thm 5.21):
for psi odd with E[psi'(Z)] = J and E[psi(Z)^2] = K, the location M-estimator
satisfies sqrt(n)(theta_hat - theta) -> N(0, K/J^2).
The sample mean satisfies sqrt(n)(xbar - theta) -> N(0, sigma^2), sigma^2=Var(Z).
They are JOINTLY asymptotically normal (both are sums/quasi-sums of iid terms):
  sqrt(n)(theta_hat - theta) = (1/J) (1/sqrt n) sum psi(Z_i) + o_p(1),
  sqrt(n)(xbar    - theta) =          (1/sqrt n) sum Z_i.
Hence sqrt(n)(theta_hat - xbar) -> N(0, V) with
  V = Var( psi(Z)/J - Z ) = K/J^2 - 2 Cov(psi(Z),Z)/J + sigma^2.
This is the EXPLICIT constant. The gap is Op(n^{-1/2}): identity holds
asymptotically at rate n^{-1/2}, with leading constant sqrt(V).

We compute V in closed form per kernel and compare to the simulated rms*sqrt(n).

LAPLACE (b=1): Z has Var = 2. psi(u)=sign(u). theta_hat = median.
  Asymptotic var of median: 1/(4 f(0)^2), f(0)=1/2 => 1/(4*1/4)=1. So K/J^2 = 1.
  Joint: median - theta = (1/(2 f(0))) * (1/sqrt n) sum (1/2 - 1{Z_i<0})... use
  the influence function IF_med(z) = sign(z)/(2 f(0)) = sign(z) (since 2 f(0)=1).
  IF_mean(z) = z. So V = Var(sign(Z) - Z).
  E[sign(Z)]=0,E[Z]=0. Var(sign Z)=1. Var(Z)=2. Cov(sign Z,Z)=E[|Z|]=b=1.
  V = 1 - 2*1 + 2 = 1.  => sqrt(V)=1.  matches rms*sqrt(n)->1.0 observed.

LOGISTIC (scale 1): handled numerically (J,K via integrals).
"""
import numpy as np
from scipy import integrate, stats

def kernel_constants(name):
    if name == "laplace":
        f = lambda z: 0.5*np.exp(-np.abs(z))
        psi = lambda z: np.sign(z)
        psip = None  # kink; use median influence function directly
        var_Z = 2.0
        # influence functions
        IF_est = lambda z: np.sign(z) / (2*f(0.0))  # = sign(z)/1 = sign(z)
        IF_mean = lambda z: z
        return f, psi, var_Z, IF_est, IF_mean
    if name == "logistic":
        f = lambda z: np.exp(-z)/(1+np.exp(-z))**2
        psi = lambda z: np.tanh(z/2)
        psip = lambda z: 0.5*(1 - np.tanh(z/2)**2)  # = 0.5 sech^2(z/2)
        var_Z = (np.pi**2)/3.0
        # J = E[psi'(Z)], compute by integration; IF_est = psi(z)/J
        J = integrate.quad(lambda z: psip(z)*f(z), -60, 60)[0]
        IF_est = lambda z: psi(z)/J
        IF_mean = lambda z: z
        return f, psi, var_Z, IF_est, IF_mean
    raise ValueError

for name in ["laplace", "logistic"]:
    f, psi, var_Z, IF_est, IF_mean = kernel_constants(name)
    # V = Var(IF_est(Z) - IF_mean(Z)) = E[(IF_est - IF_mean)^2] (both mean zero by oddness)
    integrand = lambda z: (IF_est(z) - IF_mean(z))**2 * f(z)
    V = integrate.quad(integrand, -200, 200, limit=400)[0]
    print(f"{name}: asymptotic Var of sqrt(n)(theta_hat - xbar) = V = {V:.5f}")
    print(f"        => leading constant sqrt(V) = {np.sqrt(V):.5f}")
    print(f"        (compare simulated rms*sqrt(n): "
          f"{'~1.00' if name=='laplace' else '~0.53'})")

# Monte-Carlo confirmation of the joint CLT constant at large n:
print()
print("Monte-Carlo: sqrt(n)*(theta_hat - xbar) sd at n=20000")
for name in ["laplace", "logistic"]:
    n = 20000
    nrep = 3000
    g = np.empty(nrep)
    for r in range(nrep):
        rr = np.random.default_rng((hash((name, "asym", r)) % 2**32))
        if name == "laplace":
            z = rr.laplace(0,1,n); th = np.median(z)
        else:
            z = rr.logistic(0,1,n)
            from scipy import optimize
            th = optimize.brentq(lambda m: np.sum(np.tanh((z-m)/2)), z.min()-50, z.max()+50, xtol=1e-12)
        g[r] = np.sqrt(n)*(th - z.mean())
    print(f"  {name}: empirical sd(sqrt(n)*gap) = {g.std():.5f}")
