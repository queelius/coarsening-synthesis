"""
Laplace location MLE at n=3: the cleanest counterexample to CLAIM-GEN.

Laplace p0(u) = (1/2b) exp(-|u|/b). log-likelihood for reports x_1..x_n:
    ell(mu) = -n log(2b) - (1/b) sum_i |x_i - mu|.
Maximizing ell <=> MINIMIZING sum_i |x_i - mu|, whose minimizer is the SAMPLE
MEDIAN. For odd n the median is the middle order statistic, unique.

So mu_hat = median(x). m(theta_hat) = mu_hat = median. The claimed identity says
mu_hat = xbar (arithmetic mean). These differ whenever median != mean.

Take x = (0, 1, 5). median = 1, mean = 2. Gap = -1. EXACT, not optimizer noise.

We also confirm:
  (i) mu_hat = 1 is a genuine global maximum of ell (interior point of Theta=R),
  (ii) the gap m(theta_hat) - T_bar = median - mean = 1 - 2 = -1 exactly,
  (iii) the Gaussian fit on the SAME data gives mu_hat = mean = 2 (identity holds).
"""
import sympy as sp

mu = sp.symbols('mu', real=True)
b = sp.symbols('b', positive=True)

xs = [sp.Integer(0), sp.Integer(1), sp.Integer(5)]
n = len(xs)
xbar = sp.Rational(sum(xs), n)
print("data x =", xs)
print("arithmetic mean xbar =", xbar)

# Laplace negative log-likelihood (drop constants): f(mu) = sum |x_i - mu|
f = sum(sp.Abs(x - mu) for x in xs)
print("\nLaplace objective to minimize  f(mu) = sum |x_i - mu| =", f)

# Evaluate f on a grid of candidate points and around the median
for val in [-1, 0, sp.Rational(1,2), 1, sp.Rational(3,2), 2, 3, 5, 6]:
    print(f"  f({val}) = {f.subs(mu, val)}")

# The minimizer of sum|x_i-mu| for sorted x is the median = middle value = 1.
# Confirm via piecewise derivative: for mu in (0,1), f = (mu-0)+(1-mu)+(5-mu)=6-mu, slope -1 (decreasing)
#                                   for mu in (1,5), f = mu + mu-1 + 5-mu = mu+4, slope +1 (increasing)
# so min at mu=1.
print("\nslope of f on (0,1): d/dmu of (6 - mu) =", sp.diff(6 - mu, mu), "(decreasing)")
print("slope of f on (1,5): d/dmu of (mu + 4) =", sp.diff(mu + 4, mu), "(increasing)")
print("=> unique minimizer mu_hat = 1 = median")

median = sp.Integer(1)
print("\nLaplace MLE  mu_hat = median =", median)
print("m(theta_hat) - T_bar = median - mean =", median - xbar, "  (EXACT, nonzero)")

# Gaussian comparison on the SAME data: minimize sum (x_i - mu)^2 -> mean
g = sum((x - mu)**2 for x in xs)
mu_g = sp.solve(sp.diff(g, mu), mu)[0]
print("\nGaussian MLE on same data: mu_hat =", mu_g, " == xbar:", sp.simplify(mu_g - xbar) == 0)

# Full ell value comparison (with b) to confirm global max, not just stationary:
ell = -n*sp.log(2*b) - (1/b)*f
print("\nLaplace ell(mu) =", ell)
print("ell at median mu=1:", sp.simplify(ell.subs(mu, 1)))
print("ell at mean   mu=2:", sp.simplify(ell.subs(mu, 2)))
print("ell(1) - ell(2) =", sp.simplify(ell.subs(mu,1) - ell.subs(mu,2)),
      "(positive => median strictly better, b>0)")
