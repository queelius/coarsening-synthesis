# Research Log

## Goal
Settle the open finite-sample step in coarsening-synthesis general consistency
theorem regime (B) (location family): does m(theta_hat) = T_bar (arithmetic mean)
hold exactly at the interior MLE for ALL symmetric kernels, or only for a
restricted class (Gaussian / exponential-family)?

## Eval
Self-evaluation against goal (no eval script). Success = rigorous proof OR verified
explicit counterexample (numeric + analytic) OR precise characterization with proof.

---

### Cycle 0 (2026-06-03) DECOMPOSE
**Phase:** decompose / read sources
**Notes:** Read consistency.tex, framework.tex, dp-coarsening identifiability.tex,
methodology.tex, translation.tex, validation.tex.

Key reading result: there are TWO distinct claims conflated by the goal text.

- CLAIM-N1 (DP, single release): proof sketch in thm:release-consistency and the
  validation section assert that for ONE symmetric release M the MLE theta_hat = m
  exactly, for any symmetric kernel. This is the n=1 location MLE. Plausibly exact:
  at n=1 the score sum is psi(m - mu); psi odd => zero at mu = m.

- CLAIM-GEN (synthesis regime B, general n): thm:general-consistency claims
  mu(theta_hat) = R_bar, the ARITHMETIC sample mean. The remark concedes this is
  only the population first-moment identity for non-Gaussian kernels, since the
  psi-location of the sample equals the arithmetic mean only when psi is linear.

The location-family MLE for n>1 is an M-estimator: solve sum_i psi(R_i - mu)=0 with
psi = -p0'/p0. For Gaussian psi(u)=u/sigma^2 (linear) => mu_hat = R_bar. For Laplace
psi(u) = sign(u)/b => mu_hat = sample MEDIAN. Median != mean in general => CLAIM-GEN
should FAIL for Laplace at n>=3. This is the prime counterexample.

Subtlety to verify: m(theta) = E_theta[T(R)] = E_theta[R] = mu(theta) + E[Z] =
mu(theta) since Z mean zero. So m(theta_hat) = mu(theta_hat) = mu_hat. The claim
m(theta_hat) = T_bar is literally mu_hat = R_bar. So the question reduces exactly to:
is the location M-estimator equal to the arithmetic mean? Known answer: iff psi
affine (Gauss). Need to make rigorous + confirm interior + handle unimodality
carefully (Laplace psi has a kink at 0; is theta_hat still an "interior maximum"?).

**Reflection:** Strong prior that CLAIM-GEN is FALSE in general and TRUE iff
Gaussian, while CLAIM-N1 is TRUE for all symmetric kernels. Next: confirm both with
sympy (n=1,2,3) and scipy numerics, then assemble the proof of the
characterization. Set up state.md, goal.md.

---

### Cycle 1 (2026-06-03) ATTEMPT symbolic small-n
**Phase:** hypothesize + attempt
**Hypothesis:** CLAIM-N1 true for all symmetric kernels; CLAIM-GEN false in general,
fitted mu_hat = psi-location (M-estimator), = xbar iff psi affine (Gaussian).
**Modality:** symbolic (sympy) + high-precision root (mpmath)
**Attempt:** attempts/001-symbolic-small-n/
**Result:**
- n=1: mu_hat = x0 EXACTLY for Gaussian, logistic, Cauchy (any odd psi). CLAIM-N1
  CONFIRMED symbolically (and trivially: score = psi(x0 - mu), psi odd => root at
  mu=x0).
- n=2: mu_hat = (x0+x1)/2 = xbar for Gaussian, logistic, Cauchy. n=2 is DEGENERATE:
  the midpoint is the unique symmetric center, odd psi vanishes there. So n=2 never
  distinguishes kernels. (Cauchy n=2 additionally has 2 spurious non-mean stationary
  pts when |x0-x1|>2: redescending psi => multimodal likelihood.)
- n=3 LAPLACE, data (0,1,5): MLE = median = 1 (unique global max on R, interior;
  ell(1)-ell(2)=1/b>0). Arithmetic mean = 2. m(theta_hat) - T_bar = -1 EXACTLY.
  Gaussian on same data gives 2 = mean. CLEAN SYMBOLIC COUNTEREXAMPLE.
- n=3 LOGISTIC (smooth, strictly log-concave), data (0,1,5): MLE = 1.5752 (50-digit,
  score=0, ell''<0 strict max, beats mean by 0.069). mean=2. GAP = -0.4248. Rules
  out the "kink" objection: smooth kernel ALSO fails.

**Reflection:** CLAIM-GEN is FALSE. The identity mu_hat = xbar holds at n=1 and n=2
for ALL symmetric kernels (degenerate symmetric configs), but breaks at n>=3 for any
NON-Gaussian kernel as soon as the sample is asymmetric. This pins the mechanism:
the location MLE is the M-estimator (psi-location), which equals the arithmetic mean
identically in the data iff psi is affine. Next: (1) confirm with scipy MLE pipeline
many seeds (the paper's actual route) that gap is real not optimizer tol; (2) prove
the iff-affine characterization rigorously; (3) re-examine DP n=1 claim (SAFE) vs the
DP validation "n=500" claim which may be conflating sample-mean-as-query with the
n=1 release. Update state.

---

### Cycle 2 (2026-06-03) ATTEMPT scipy sweep + characterization proof
**Phase:** attempt + evaluate
**Hypothesis:** gap genuine (not optim tol); identity holds for all samples iff psi
affine iff Gaussian; gap = Op(n^{-1/2}) with explicit constant.
**Modality:** code+tests (scipy MLE, 400 seeds x 7 n x 4 kernels), symbolic (sympy
Cauchy reduction), numeric integration (asymptotic constant).
**Attempt:** attempts/002-scipy-mle-sweep/, attempts/003-characterization-proof/
**Result:**
- SWEEP: Gaussian gap ~1e-15 all n (identity holds). Laplace/logistic/student-t:
  n=1 gap ~1e-15 (holds), n=2 ~1e-15 for log-concave (degenerate), n>=3 gap O(0.1-1)
  while max|score(theta_hat)| ~ 1e-15. GENUINE inequality, 8-14 orders above optim
  tol. CLAIM-GEN decisively FALSE.
- Laplace MLE = sample MEDIAN exactly (worst |theta_hat - median| is even-n flat-
  region artifact; all points in the flat interval are MLEs; mean identity still
  fails). gap = median - mean = Op(1) at finite n.
- CHARACTERIZATION PROOF (sympy-verified): identity holds for ALL samples at some
  n>=3 <=> (FE) sum psi(r_i)=0 on sum-zero hyperplane H <=> (set r3=-(r1+r2), psi
  odd) Cauchy eqn psi(r1)+psi(r2)=psi(r1+r2) <=> psi linear (continuous/monotone/
  measurable Cauchy) <=> p0 Gaussian. Odd-polynomial test: a3 u^3 killed (3 a3=0).
  Numeric: FE holds only for linear psi at n=3,4,5; fails sign/tanh/cubic.
- BOUNDARY CASES: (I) Laplace via objective (not score) => median, robust to kink.
  (II) student-t nu=2 (unimodal NOT log-concave): likelihood BIMODAL, mean is a
  local MIN, two global maxima away from mean => MLE not unique, identity ill-posed.
  So need LOG-CONCAVITY (not mere unimodality) for a well-defined unique MLE.
  (III) Gaussian: unique max at xbar by strict concavity, exact all n.
- ASYMPTOTIC CONSTANT: sqrt(n)(theta_hat - xbar) -> N(0,V), V=Var(psi(Z)/J - Z),
  J=E[psi'(Z)]. Laplace V=1 (sqrt=1.000, MC 1.004). Logistic sqrt(V)=0.538 (MC
  0.530). Gap = Op(n^{-1/2}): vanishes asymptotically, nonzero every finite n>=3.

**Eval (self):** Goal achieved: the open step is SETTLED. Outcome = verified
counterexample (numeric + analytic mechanism) + precise characterization with proof
+ explicit asymptotic rate/constant. Three regimes fully mapped.
**Reflection:** CLAIM-GEN false; CLAIM-N1 (DP single release, n=1) true and exact.
Remaining: confirm DP "n" = #releases so cor:dp/thm:release-consistency are SAFE as
the n=1 first-moment identity; check DP validation prose for over-claim; then write
synthesis with the exact restatement. Update state.

---

### Cycle 3 (2026-06-03) ATTEMPT DP reconciliation + final rigor
**Phase:** attempt + evaluate + reflect (toward conclusion)
**Hypothesis:** DP single-release is n=1 (exact); counterexample is interior+global;
n=1,2 degeneracy explains why the gap only appears at n>=3.
**Modality:** code+tests (scipy, convolution), symbolic (sympy n=2 oddness).
**Attempt:** attempts/004-dp-reconciliation/
**Result:**
- DP single release: marginal release p_M(m|theta) = p_conv(m-theta), p_conv =
  g0 * kappa symmetric+unimodal. ROUTE A PROOF: log p_conv(m-theta) maximized at the
  mode m-theta=0 => theta_hat = m EXACTLY (no scale, no differentiability needed).
  Numeric Normal-Laplace confirmed mode at u=0 (symmetry diff ~1e-17). The earlier
  ~1e-2 'gap' was a FIXED quadrature offset (constant in m; 1.55e-15 when minimizer
  hit an exact node) - ruled out as artifact. Pure-Laplace n=1 gap = 8.88e-16.
  => cor:dp / thm:release-consistency SAFE: they are the n=1 first-moment identity
  E_{theta_hat,kappa}[M]=m_obs, exact for symmetric unimodal release. mode=mean for
  symmetric unimodal => E[M]=theta_hat=m.
- INTERIOR+GLOBAL: data (0,1,5), kernel battery (gaussian, laplace, logistic,
  gennorm beta=1.5/3/4, sech): every non-Gaussian theta_hat strictly interior
  (min<th<max), global max, ell(th)>ell(mean). Gaussian alone gap=0. Gap sign varies:
  leptokurtic (beta<2) negative (toward median), platykurtic (beta>2) positive.
- n=1,2 DEGENERACY (sympy): n=1 score psi(x0-mu) odd => unique zero at x0=xbar.
  n=2 midpoint: x0-mid = -(x1-mid) => psi(d)+psi(-d)=0 for ANY odd psi => midpoint
  always stationary (= unique max for log-concave) = xbar. So identity is
  degenerately true for n<=2; n>=3 is the first asymmetric residual pattern on the
  sum-zero hyperplane, where Cauchy forces psi linear.

**Eval (self):** SUCCESS on all counts. The open step is fully settled with: a
verified explicit counterexample (numeric + analytic mechanism), a complete proof of
the exact characterization (Gaussian iff), the precise intermediate/asymptotic story
(n=1,2 exact; n>=3 only asymptotic at n^{-1/2} with explicit constant V), and the DP
corollary reconciliation (safe via n=1). 
**Reflection:** Concluding. Writing synthesis.md with the exact restatement options
for thm:general-consistency regime (B) and confirmation that cor:dp is safe. All four
attempt dirs contain runnable scripts + this analysis. CONCLUDE.

---

### Cycle 4 (2026-06-03) CONCLUDE
**Phase:** conclude
**Decision:** Goal achieved on every success criterion. Outcome: verified explicit
counterexample (numeric + analytic mechanism) + complete proof of the exact
characterization (finite-sample sample-mean identity holds iff Gaussian) + precise
intermediate behavior (exact at n in {1,2}; n^{-1/2} asymptotic with explicit
constant V=Var(psi(Z)/J - Z) for n>=3) + DP corollary reconciliation (safe, n=1
exact).
**Deliverable:** synthesis.md written. Findings promoted (5 runnable scripts). All
attempt notes.md written. No U+2014/U+2013 in any file. Findings scripts re-run
clean end-to-end.
**Final statuses:** all 8 sub-problems resolved; all 3 hypotheses confirmed.
Pointer: see .research/synthesis.md.
