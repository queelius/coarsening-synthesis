"""
The characterization reduces to a functional equation. The location MLE equals the
arithmetic mean for EVERY sample of size n (>=3) iff

    (FE)   sum_{i=1}^n psi(r_i) = 0   for all (r_1,...,r_n) with sum_i r_i = 0,

where psi = -p0'/p0 is continuous and odd (p0 symmetric). We prove psi must be
LINEAR. Here we (a) verify the reduction, (b) test the key two-point lemma that
cracks it, and (c) sanity-check the final form on candidate kernels.

KEY LEMMA (n=3 already suffices). Put r_3 = -(r_1+r_2), free r_1,r_2. (FE) becomes
    psi(r1) + psi(r2) + psi(-(r1+r2)) = 0,  i.e. (psi odd)
    psi(r1) + psi(r2) = psi(r1 + r2)   for all r1, r2 in R.            (CAUCHY)
That is exactly Cauchy's functional equation for psi. A continuous (even: monotone,
or measurable) solution of Cauchy's equation is LINEAR: psi(u) = c*u. Done.

Then c>0 (psi increasing for a proper density / log-concave max), and
psi(u) = -p0'(u)/p0(u) = c u  =>  (log p0)' = -c u  =>  log p0 = -c u^2/2 + const
=>  p0 Gaussian with variance 1/c. So the ONLY symmetric kernel for which the
finite-sample arithmetic-mean identity holds for all samples is the Gaussian.

We verify each algebraic step with sympy.
"""
import sympy as sp

r1, r2, u, v, c = sp.symbols('r1 r2 u v c', real=True)
psi = sp.Function('psi')

print("STEP 1: reduce (FE) at n=3 to Cauchy's equation.")
print("  Set r3 = -(r1+r2). (FE): psi(r1)+psi(r2)+psi(r3) = 0.")
print("  psi odd => psi(r3) = psi(-(r1+r2)) = -psi(r1+r2).")
print("  So (FE) <=> psi(r1)+psi(r2) = psi(r1+r2).   [Cauchy]")
print()

print("STEP 2: continuous solutions of Cauchy are linear: psi(u)=c*u.")
print("  (Standard. Continuity OR monotonicity OR measurability suffices;")
print("   psi = -p0'/p0 is continuous for a C^1 positive density.)")
# demonstrate that psi(u)=c*u satisfies Cauchy and that, e.g., quadratic-in-odd
# corrections cannot (any odd analytic psi = sum a_k u^{2k+1}; plug in):
print()
print("STEP 3: which odd polynomials solve Cauchy? Test psi(u)=a1*u + a3*u^3.")
a1, a3 = sp.symbols('a1 a3', real=True)
cand = lambda t: a1*t + a3*t**3
lhs = cand(r1) + cand(r2)
rhs = cand(r1 + r2)
diff = sp.expand(rhs - lhs)
print("  psi(r1+r2) - psi(r1) - psi(r2) =", diff)
print("  Vanishes for all r1,r2 iff coefficient of each monomial = 0:")
poly = sp.Poly(diff, r1, r2)
for monom, coeff in poly.terms():
    print(f"    r1^{monom[0]} r2^{monom[1]} : {coeff} = 0")
print("  => a3 = 0. Only the linear term survives. (Same kills every odd power>1.)")
print()

print("STEP 4: psi(u)=c*u  =>  p0 is Gaussian.")
p0 = sp.Function('p0')
# (log p0)'(u) = -psi(u) = -c u  => p0(u) = A exp(-c u^2/2)
x = sp.symbols('x', real=True)
A = sp.symbols('A', positive=True)
p0_gauss = A*sp.exp(-c*x**2/2)
logder = sp.simplify(sp.diff(sp.log(p0_gauss), x))
print("  Take p0(u) = A exp(-c u^2/2). Then (log p0)'(u) =", logder)
print("  so -p0'/p0 =", sp.simplify(-sp.diff(p0_gauss, x)/p0_gauss), "= c*u = psi. consistent.")
print("  Normalizing: c = 1/sigma^2, A = 1/sqrt(2 pi sigma^2). p0 = N(0, sigma^2).")
print()
print("CONCLUSION: arithmetic-mean identity holds for ALL samples (n>=3)")
print("  <=> psi affine (linear, since odd) <=> p0 Gaussian.")
print()

# ---- numerical cross-check of the Cauchy reduction for n=3,4,5 ----
print("=" * 60)
print("Numerical cross-check: for non-Gaussian psi, (FE) fails on H.")
import numpy as np
rng = np.random.default_rng(7)
def check_FE(psi_func, n, trials=5000):
    worst = 0.0
    for _ in range(trials):
        r = rng.normal(0, 1, n)
        r = r - r.mean()  # project onto sum-zero hyperplane H
        val = np.sum(psi_func(r))
        worst = max(worst, abs(val))
    return worst
psis = {
    "linear c=1 (Gauss)": lambda u: u,
    "sign (Laplace)":      lambda u: np.sign(u),
    "tanh(u/2) (logistic)":lambda u: np.tanh(u/2),
    "u^3 (toy odd)":       lambda u: u**3,
}
for n in (3, 4, 5):
    print(f"  n={n}:")
    for name, f in psis.items():
        w = check_FE(f, n)
        flag = "FE holds" if w < 1e-12 else "FE FAILS"
        print(f"    {name:24s} sup|sum psi(r_i)| on H = {w:.3e}  {flag}")
