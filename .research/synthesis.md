# Research Synthesis

## Goal

Settle the open finite-sample step in the coarsening-synthesis general consistency
theorem, regime (B) (location family), flagged in
`sections/consistency.tex` remark `rem:loc-sketch`. In the location-family regime
the report is X = theta + Z with Z symmetric, mean zero (Gaussian, Laplace,
logistic, ...) under coarsening conditions C1/C2/C3. The theorem
`thm:general-consistency` claims that at an interior maximum of the face-value
likelihood the fitted mean of the coarsening-sufficient statistic equals its
empirical mean, m(theta_hat) = T_bar, with T_bar = (1/n) sum_i T(R_i). This is
proved exact for the Gaussian kernel. The question: does the finite-sample identity
hold exactly at the interior MLE for ALL symmetric kernels, or only for a restricted
class?

## Outcome

The general-n identity is FALSE for every non-Gaussian symmetric kernel. The
finite-sample statement m(theta_hat) = T_bar holds exactly for the Gaussian kernel
at all sample sizes, holds (degenerately) for every symmetric kernel at sample sizes
n in {1, 2}, and FAILS at every finite n >= 3 for any non-Gaussian kernel as soon as
the sample is not symmetric about its own mean. I have an explicit verified
counterexample with its analytic mechanism, a complete proof of the exact
characterization (the identity holds for all samples if and only if the kernel is
Gaussian), and the precise intermediate behavior (the gap is O_p(n^{-1/2}) with an
explicit constant). The differential-privacy corollary `cor:dp` and theorem
`thm:release-consistency` are SAFE, because they are the single-release case n = 1,
where the identity is exact for any symmetric unimodal release density.

The reduction that makes the whole question elementary: in regime (B),
T(R) = R and Z has mean zero, so the model-implied mean is
m(theta) = E_theta[R] = mu(theta) + E[Z] = mu(theta). Therefore the claim
"m(theta_hat) = T_bar" is literally "mu_hat = R_bar", that is, the location MLE
equals the arithmetic sample mean. The location MLE is the M-estimator solving
sum_i psi(R_i - mu) = 0 with psi = -p0'/p0. The arithmetic mean is the M-estimator
for the linear psi only. So the entire question is the classical fact that the
maximum-likelihood location equals the sample mean exactly when the score is linear,
which forces the kernel to be Gaussian.

## Key Findings

### 1. The identity is FALSE for general symmetric kernels (explicit counterexample)

Data X = (0, 1, 5), arithmetic mean R_bar = 2.

- Laplace kernel p0(u) proportional to exp(-|u|/b): the face-value MLE minimizes
  sum_i |x_i - mu|, whose unique minimizer is the sample median = 1 (the objective
  has slope -1 on (0,1) and +1 on (1,5), a unique interior minimum at mu = 1). So
  mu_hat = 1, m(theta_hat) - T_bar = median - mean = 1 - 2 = -1, EXACTLY, and
  ell(median) - ell(mean) = 1/b > 0 confirms the median strictly beats the mean.
  This is symbolic, not numeric (sympy).
  Artifact: `findings/counterexample_laplace_n3.py`.

- Logistic kernel (smooth, strictly log-concave, psi(u) = tanh(u/2)): on the same
  data the MLE is 1.5751623946947658 (50-digit, score = 0, ell'' = -0.806 < 0 strict
  maximum, beats the mean by 0.069 in log-likelihood, and the mean is not even
  stationary: score(mean) = -0.319). Gap = -0.4248. This rules out any objection that
  the Laplace counterexample exploits the kink in psi at 0: a smooth, strictly
  log-concave kernel fails identically.

- A wider battery on the same data (generalized normal with shape beta in
  {1.5, 3, 4}, hyperbolic secant): every non-Gaussian MLE is a strictly interior,
  global maximum with a nonzero gap and ell(theta_hat) > ell(mean); the Gaussian
  alone has gap 0. The gap sign is informative: leptokurtic kernels (beta < 2:
  Laplace, gennorm-1.5, sech) pull the fit toward the median (gap < 0 here),
  platykurtic kernels (beta > 2) push it the other way (gap > 0).
  Artifact: `findings/counterexample_kernel_battery.py`.

This is a first-class result: the theorem's regime (B), read as a finite-sample
sample-mean identity, must stay restricted to the Gaussian kernel.

### 2. The genuine inequality is not optimizer noise (numerical sweep)

scipy.optimize MLE fits (Brent on the negative log-likelihood, Brentq polish on the
score), four kernels (Gaussian, Laplace, logistic, Student-t nu = 3), n in
{1, 2, 3, 5, 10, 50, 200}, 200 to 400 seeds each. The decisive column is
max|score(theta_hat)| over seeds, which is ~1e-15 (machine epsilon) for the smooth
kernels, certifying a true stationary point, while the gap to the arithmetic mean is
O(0.1 to 1) for n >= 3, that is 8 to 14 orders of magnitude above optimizer
tolerance. Gaussian: gap ~1e-15 at all n (identity exact). Laplace/logistic/Student:
gap ~1e-15 at n = 1 and (for log-concave kernels) n = 2, then O(0.1 to 1) at n >= 3.
Artifact: `findings/numerical_sweep_all_kernels.py`.

### 3. Exact characterization: the identity holds for all samples IFF the kernel is Gaussian (proof)

Write the residuals r_i = x_i - R_bar; they satisfy sum_i r_i = 0 and otherwise
range freely over the sum-zero hyperplane H. The arithmetic mean is the MLE for
every sample of size n if and only if R_bar is a stationary point of the
log-likelihood for every sample, that is

    (FE)   sum_{i=1}^n psi(r_i) = 0   for all r in H,

where psi = -p0'/p0 is odd (p0 symmetric). Specialize to n = 3 and set
r_3 = -(r_1 + r_2) (free r_1, r_2). Using oddness, (FE) becomes Cauchy's functional
equation

    psi(r_1) + psi(r_2) = psi(r_1 + r_2)   for all r_1, r_2 in R.

For a C^1 positive symmetric density psi is continuous; a continuous solution of
Cauchy's equation is linear, psi(u) = c u. (Continuity is the cleanest sufficient
regularity; monotonicity, which holds whenever p0 is log-concave, or mere
measurability, also forces linearity, so the conclusion is robust to how one phrases
the smoothness of the kernel.) Linearity of psi gives (log p0)'(u) = -c u, hence
log p0(u) = -c u^2 / 2 + const, that is p0 is Gaussian with variance 1/c (and c > 0
for a proper density). Conversely, for the Gaussian the score is exactly linear and
the log-likelihood -(1/2 sigma^2) sum (x_i - mu)^2 is strictly concave with unique
interior maximizer R_bar, so the identity holds exactly at every n. A sympy check
confirms the Cauchy reduction and that any odd polynomial correction a_3 u^3 is
killed (its Cauchy defect is 3 a_3 (r_1^2 r_2 + r_1 r_2^2), forcing a_3 = 0); a
numerical check confirms (FE) holds on H only for the linear psi at n = 3, 4, 5.
Artifact: `findings/proof_gaussian_iff.py`.

The sample sizes n = 1 and n = 2 are degenerate and do not test the kernel: at n = 1
the score psi(x_0 - mu) is odd with unique zero at mu = x_0 = R_bar; at n = 2 the
midpoint satisfies x_0 - mid = -(x_1 - mid), so psi(d) + psi(-d) = 0 for any odd psi,
making the midpoint stationary (and, for a log-concave kernel, the unique maximizer)
for every symmetric kernel. The first asymmetric residual pattern on H appears at
n = 3, which is exactly where the constraint bites.

### 4. Precise intermediate behavior: the gap is O_p(n^{-1/2}) with an explicit constant

Both the location MLE and the arithmetic mean are consistent for theta (for a
symmetric kernel the population mean and the psi-location coincide at theta), so the
gap vanishes asymptotically. Standard M-estimator theory gives the joint expansion

    sqrt(n)(theta_hat - theta) = (1/J) n^{-1/2} sum_i psi(Z_i) + o_p(1),
    sqrt(n)(R_bar    - theta) =          n^{-1/2} sum_i Z_i,

with J = E[psi'(Z)], hence

    sqrt(n)(theta_hat - R_bar) -> Normal(0, V),
    V = Var( psi(Z)/J - Z ).

For the Laplace kernel V = 1 exactly (influence function sign(Z)/(2 f(0)) = sign(Z),
so V = Var(sign(Z) - Z) = 1 - 2 E|Z| + Var(Z) = 1 - 2 + 2 = 1 at b = 1). For the
logistic kernel V = 0.28987, sqrt(V) = 0.538. Monte-Carlo at n = 20000 gives
sd(sqrt(n) gap) = 1.004 (Laplace) and 0.530 (logistic), and the log-log slope of the
rms gap against n is -0.482, all confirming the n^{-1/2} law and the constants.
Artifact: `findings/asymptotic_rate_constant.py`.

So the honest intermediate statement is: for a non-Gaussian symmetric (log-concave)
kernel, m(theta_hat) - T_bar is zero at n in {1, 2}, nonzero at every finite n >= 3,
and equals O_p(n^{-1/2}) with leading standard deviation sqrt(V)/sqrt(n),
V = Var(psi(Z)/J - Z). The population first-moment identity that the DP sibling
proves is the n -> infinity (or n = 1) limit of this.

### 5. Regularity: regime (B) needs log-concavity, not mere unimodality

The theorem as written assumes p0 "symmetric, unimodal". Unimodality of the density
is not enough for the MLE to be well defined. For Student-t with nu = 2 (symmetric,
unimodal, but not log-concave) and data (-4, 4), the log-likelihood is bimodal with
two global maxima at +-3.74 and the arithmetic mean (0) sits at a local MINIMUM (a
valley). With a non-unique MLE the identity is not even well posed. The right
hypothesis for a unique interior MLE is that p0 is log-concave (equivalently psi
nondecreasing), which holds for Gaussian, Laplace, logistic, hyperbolic secant, and
generalized-normal with shape >= 1, but not for Student-t or Cauchy.
Artifact: `attempts/003-characterization-proof/rigor_boundary_cases.py`.

### 6. The single-release case n = 1 is exact (so the DP corollary is safe)

For one observation m from a location family p_M(m | theta) = p_conv(m - theta) with
p_conv symmetric about 0 and unimodal, the log-likelihood log p_conv(m - theta), as a
function of theta, attains its unique maximum where m - theta = 0 (the mode of the
symmetric unimodal p_conv), so theta_hat = m EXACTLY. This needs no differentiability
and no knowledge of the kernel scale, only symmetry and unimodality. For the actual
DP release density (Normal-Laplace convolution) the mode sits at u = 0 to ~1e-17 and
the pure-Laplace n = 1 fit returns m to machine epsilon. Because p_conv is symmetric
unimodal, mode = mean, so E_{theta_hat, kappa}[M] = theta_hat = m, which is exactly
`eq:release-consistency`. (An earlier convolution-quadrature run showed a spurious
~1e-2 offset that was constant in m and collapsed to 1.5e-15 when the optimizer
landed on a quadrature-exact node, the signature of a fixed numerical artifact, not a
real effect.) Artifact: `attempts/004-dp-reconciliation/n1_exact_clean.py`.

## What it implies for the two papers

### coarsening-synthesis `thm:general-consistency` regime (B)

The general-n form "mu(theta_hat) = R_bar" is the false part and must be restated.
The remark `rem:loc-sketch` already concedes this honestly and was correct to call it
the one genuinely open step. The investigation removes the "open" status: the step is
not merely unproved, it is FALSE for every non-Gaussian kernel, with the clean
Gaussian-iff characterization above. Four honest restatements, any of which is
defensible (in rough order of how little they give up):

1. Fold regime (B) into regime (A) for the exact finite-sample claim. The only
   kernel for which the finite-sample sample-mean identity holds is the Gaussian, and
   the Gaussian location family is also a regular exponential family with natural
   sufficient statistic T(R) = R. So the exact finite-sample identity is entirely
   covered by regime (A); regime (B)'s distinct content is the n = 1 / population /
   asymptotic first-moment identity, not a finite-sample sample-mean identity.

2. Keep regime (B) but replace T_bar by the kernel's psi-location. The exact
   finite-sample statement for any symmetric log-concave kernel is
   m(theta_hat) = (psi-location of the sample), where the psi-location is the
   M-estimator solving sum_i psi(R_i - mu) = 0 (the median for Laplace, the
   tanh-location for logistic, the sample mean for Gaussian). This is exact at every
   n and degenerates to R_bar exactly when psi is linear.

3. Keep R_bar but downgrade the claim to its true scope: exact at n in {1, 2} for any
   symmetric kernel and at all n for the Gaussian; for n >= 3 and a non-Gaussian
   kernel it is the population first-moment identity E_{theta_hat, kappa}[T] = m_obs
   and a finite-sample approximation with error O_p(n^{-1/2}), leading standard
   deviation sqrt(Var(psi(Z)/J - Z) / n). This is the reading the DP sibling already
   uses.

4. State regime (B) only at n = 1 (the single coarse report per latent value), where
   theta_hat = R_1 exactly for any symmetric unimodal kernel. This is the cleanest
   true statement and is exactly what the DP corollary needs.

Recommended: combine (1) and (3). Say that the exact finite-sample sample-mean
identity is the Gaussian case (hence an instance of regime (A) with T(R) = R), and
that regime (B)'s genuinely distinct content is the population first-moment identity
E_{theta_hat, kappa}[T] = m_obs (exact at n = 1, asymptotic at rate n^{-1/2} for
n >= 3). Also tighten the hypothesis from "symmetric unimodal" to "symmetric
log-concave" so the MLE is a unique interior point (item 5).

Concretely, the sentence in `rem:loc-sketch` that currently reads "would require
either restricting to the Gaussian family or replacing R_bar with the kernel's
psi-location; we leave this as the one genuinely open step" should change to a
settled statement: the finite-sample sample-mean identity holds if and only if the
kernel is Gaussian (proof: the stationarity condition at R_bar for all samples is
Cauchy's equation for psi, whose continuous solutions are linear, forcing a Gaussian
kernel); for a general symmetric log-concave kernel the exact finite-sample identity
is m(theta_hat) = psi-location of the sample, and the sample-mean form holds only at
n in {1, 2}, in the population limit, or asymptotically at rate n^{-1/2}.

### dp-coarsening `cor:dp` / `thm:release-consistency`

SAFE as stated. The release-consistency theorem is the single-release case: the
analyst observes one release M = q(D) + Z and fits theta from the marginal release
density. That is n = 1 in the location-family sense, where theta_hat = m exactly for
any symmetric unimodal release density and E_{theta_hat, kappa}[M] = m_obs is exact.
The proof sketch's chain ("MLE first-order condition equivalent to m being a
stationary point of the log-density in m; for symmetric unimodal p_M that maximum
lies at E_{theta_hat, kappa}[M]") is correct for n = 1. The validation prose ("n = 500
iid draws") refers to the database size feeding the single query q(D); the
release-consistency check is on the one release, not on 500 reports, so there is no
hidden general-n claim and no over-claim. One sentence of insurance is worth adding:
state explicitly that release consistency is the single-release (n = 1) first-moment
identity, so a reader does not generalize it to a sample-mean identity over many
releases (where it would fail for non-Gaussian kernels by the synthesis result). For
the compositional case (`thm:composition`, k releases) the relevant object is the
combined Fisher information and the stacked score, not an arithmetic mean of reports,
so the n >= 3 failure does not touch it.

## Failed approaches

None of the analytic routes failed; the question turned out to have a clean
elementary answer once reduced to mu_hat versus R_bar. The only false start was
numerical: a convolution-quadrature MLE for the DP single release showed a spurious
~1e-2 offset. It was caught and dismissed because the offset was constant in m within
each (tau, b) and collapsed to machine epsilon when the optimizer happened to land on
a quadrature-exact node, the signature of a fixed numerical artifact. The clean
mode-at-m argument (no quadrature) confirmed the exact n = 1 identity.

## Open questions

The mathematics is settled. Residual modeling choices for the authors, not open
problems:

- Whether to adopt restatement (1)+(3) or one of the alternatives is an expository
  decision, not a mathematical one.
- The exact constant V = Var(psi(Z)/J - Z) is available in closed form for Laplace
  (V = 1) and by one integral for any other kernel; the paper could tabulate it for
  the standard DP kernels if it wants a finite-sample correction, but this is
  optional.

## Recommendations

1. Replace the "open step" language in `rem:loc-sketch` with the settled
   characterization: the finite-sample sample-mean identity holds iff the kernel is
   Gaussian; otherwise the exact statement uses the psi-location, and the sample-mean
   form is n = 1 / population / asymptotic at n^{-1/2}.
2. In `thm:general-consistency`, either fold the exact finite-sample regime (B) into
   regime (A) (Gaussian-location is exponential-family) and keep regime (B) as the
   population/asymptotic first-moment identity, or restate regime (B)'s conclusion as
   m(theta_hat) = psi-location of the sample.
3. Tighten regime (B)'s hypothesis from "symmetric, unimodal" to "symmetric,
   log-concave" so the MLE is a unique interior maximizer (the Student-t nu = 2
   bimodality shows unimodality is insufficient).
4. In dp-coarsening, add one sentence pinning release consistency to the
   single-release n = 1 first-moment identity, to prevent a reader from generalizing
   it to a many-release sample-mean identity.
5. Optionally cite the standard fact behind the characterization: that the sample
   mean is the maximum-likelihood location estimator only for the Gaussian (Gauss's
   own characterization of the normal law via the arithmetic mean as the most
   probable value), which is precisely the Cauchy-equation argument above.

## Reproducibility

All scripts are runnable with the environment's Python (sympy 1.13.3, scipy 1.16.1,
numpy 2.2.6, mpmath). Key artifacts in `findings/`:
- `counterexample_laplace_n3.py` (exact symbolic Laplace counterexample)
- `counterexample_kernel_battery.py` (interior/global gap over many kernels)
- `numerical_sweep_all_kernels.py` (genuine-gap sweep, score ~1e-15 vs gap O(1))
- `proof_gaussian_iff.py` (Cauchy reduction, Gaussian-iff)
- `asymptotic_rate_constant.py` (n^{-1/2} law and explicit constant V)
Full working notes in `attempts/001..004/notes.md`; cycle history in `log.md`.
