# Logic Checker Report

Date: 2026-06-04 (final pre-submission pass)
Priority (per brief): (1) verify the corrected regime-(B) statement is
internally consistent and the Gauss-iff boundary is correctly supported by
Teicher 1961; (2) the five corollaries still follow from the corrected
general theorem, esp. the phenotype 3-to-1 edit and the dp n=1 pinning;
(3) the general rank + singleton result after the censoring rider was moved
to a remark. The already-settled location-family correction is NOT
re-litigated. Confidence: HIGH. Every claim was checked against the
manuscript source, the clean build, and the on-disk proof provenance, two
scripts of which were re-executed this pass.

## 1. Regime (B) internal consistency and the Teicher-supported Gauss-iff boundary

VERDICT: internally consistent, and the Gauss-iff boundary is correctly
cited. The Teicher (1961) characterization says exactly what the paper uses
it for.

The theorem (consistency.tex l.46-62) states regime (B) in three precise,
mutually consistent senses: exact at n=1; population first-moment
E[M]=m_obs for any n; and finite-sample sample-mean form up to O_p(n^{-1/2})
for n>1, with sqrt(n)(mu_hat - Rbar) asymptotically normal. It then states
the negative half cleanly: "It is not an exact finite-sample sample-mean
identity for n>=3 unless p_0 is Gaussian (in which case the report law is
already an exponential family and the exact identity is the regime-(A)
statement)." What regime (B) reproduces exactly is the sample psi-location,
m(theta_hat)=mu_hat with sum_i psi(R_i-mu_hat)=0, psi=-p_0'/p_0. This is
correct and non-contradictory: the exact finite-sample object is the
psi-location, the sample-mean form is the n=1/population/asymptotic reading,
and the only kernel collapsing the two at all n is the Gaussian.

The proof (l.65-110) is sound. Regime (A): for a regular exponential family
the score in the natural parameter is n(Tbar - E_eta[T]) by the
log-partition gradient nabla A(eta)=E_eta[T]; full-column-rank
partial-eta/partial-theta passes stationarity partial_theta ell=0 to
partial_eta ell=0, hence E_hat[T]=Tbar. Re-derived independently; correct.
Regime (B): T(R)=R and E[Z]=0 give m(theta)=mu(theta); symmetric log-concave
p_0 makes psi odd and nondecreasing, so the score sum is strictly decreasing
in mu_hat with a unique interior root; n=1 gives mu_hat=R; the sample-mean
form requires psi linear, the only symmetric kernel with linear score is
Gaussian; M-estimator theory gives sqrt(n)(mu_hat-Rbar)->N(0,V),
V=Var(psi(Z)/J - Z), J=E[psi'(Z)]. All steps correct.

The boundary remark rem:loc-sketch (l.112-150) cites
\citep{teicher1961maximum} for "the location MLE equals the arithmetic
sample mean for every sample if and only if the kernel is Gaussian"
(l.119-121) and again at l.132 ("made precise as the maximum-likelihood
characterization of the normal by \citet{teicher1961maximum}"), with
\citet{kagan1973characterization} for the broader placement (l.133).

CITATION ACCURACY: Teicher (1961, "Maximum Likelihood Characterization of
Distributions," Ann. Math. Statist. 32(4):1214-1222) characterizes
distributions by the property that a prescribed statistic is their MLE; the
governing special case is that the arithmetic sample mean is the
maximum-likelihood estimator of a location parameter if and only if the
density is normal. The paper uses the citation for precisely this statement.
It is correctly characterized and correctly load-bearing. Note Teicher
covers the location-mean case the paper needs; if a referee wants the origin
of the idea, Gauss (1809) is the classical source and the paper already
names "Gauss's characterization of the normal law as the unique location
family whose most probable value is the arithmetic mean" in prose (l.129-131)
without a Gauss bib entry, which is acceptable since Teicher is the rigorous
modern citation.

PROVENANCE RE-RUN (this pass, not a re-derivation): I re-executed
.research/findings/proof_gaussian_iff.py: the n=3 functional equation
reduces to Cauchy psi(r1)+psi(r2)=psi(r1+r2); the odd cubic correction is
killed (coefficient 3*a3=0); numerically sup|sum psi(r_i)| on the sum-zero
hyperplane is ~1e-15 for the linear (Gaussian) score and O(1) for sign
(Laplace), tanh/2 (logistic), and u^3 at n=3,4,5. I re-ran
.research/findings/counterexample_laplace_n3.py: on data (0,1,5) the Laplace
MLE is the median 1 vs mean 2, exact gap -1, with ell(median)-ell(mean)=1/b>0.
Both confirm the boundary the citation supports. The (0,1,5) numbers in
rem:loc-sketch (l.137-138, "the Laplace MLE is the median 1 against the mean
2, an exact gap of -1") match the script output exactly.

The "first appears at n=3" claim is correct: n in {1,2} are degenerate (a
2-point sample is symmetric about its mean, so every symmetric kernel
matches), and the "for any n" population identity and the "n>1"
O_p(n^{-1/2}) statement are mutually consistent. The log-concavity (not mere
unimodality) hypothesis is correctly justified by the Student-t_2 bimodality
remark (l.143-146).

## 2. The five named corollaries -- all still follow

- cor:scrna (l.166-176, regime A, ZINB): m(theta)=(1-pi_j)mu_j=Xbar_j. The
  ZINB observed-count law is a regular exponential family with mean-
  parameterized score (x-mu)/[mu(1+mu phi)]. Exact. CORRECT.
- cor:spatial (l.178-191, regime A, Poisson): sum_k P_sk mu_jk = Xbar_sj,
  per-coordinate exact; the vector form over (s,j) uses the joint rank
  condition (thm:general-rank), correctly flagged as "the only place the
  rank condition enters a consistency claim." CORRECT.
- cor:phenotype (l.193-211, regime A, Bernoulli): EDIT VERIFIED. The
  corollary now makes the 3-to-1 reparametrization explicit: "The single-code
  likelihood depends on the three parameters (pi, sens, spec) only through
  the scalar q, so consistency pins q but not the triple: the 3 -> 1 collapse
  is exactly why the chart-review singleton ... is needed" (l.206-210). q is
  correctly identified as the natural mean parameter; the informative regime
  sens+spec>1 (nonzero mean gradient) is the full-rank-Jacobian hypothesis of
  regime (A) specialized to the scalar mean. The edit is mathematically
  correct and tightens the link to the identifiability section. CORRECT.
- cor:weaksup (l.213-232, regime A, seam): exact when the agreement
  indicators are sufficient statistics; asymptotic at n^{-1/2} for the
  naive-Bayes parametrization practitioners use (ratner2016data). The seam is
  stated faithfully. CORRECT.
- cor:dp (l.234-257, regime B, seam): PINNING VERIFIED. "This is the
  single-release case, n=1" (l.236); "it does not generalize to a sample-mean
  identity over several releases, which would require the Gaussian kernel"
  (l.248-249); recovered through branch (B) using the location-family score,
  "not a corollary of regime (A)" (l.256). The n=1 exactness for any
  symmetric unimodal kernel (mode=mean) is correct. CORRECT.

The reach-map table tab:reduction (l.267-292) is consistent with all five
corollaries: three bullet (exact via A), one circle (weak-sup,
exact-or-asymptotic), one triangle (DP, regime B, n=1). No mismatch.

## 3. The general rank + singleton result after the censoring-rider move

VERDICT: the move strengthened the general statement; it did not weaken or
break it.

thm:general-rank (identifiability.tex l.19-34) now reads cleanly: necessity
(coarsening-confounded pair not separately identifiable) and sufficiency
(full column rank of tilde-C implies identifiability), with NO
domain-specific censoring condition inside the theorem body. I confirmed by
extracting the theorem environment: no "censor"/"time-to-event"/"exact and
censored" text survives inside it. The reliability-specific condition (the
mechanism assigns positive probability to both exact and censored reports,
so the all-ones augmenting row is realized) now lives in the new
rem:rank-instantiation (l.36-48), correctly framed as an instantiation
detail of the one rank condition, not a hypothesis of the general theorem.
This is exactly the right move: the general sufficiency hypothesis is the
column-rank condition on tilde-C alone, and each domain supplies its own
support condition to realize a full-rank incidence. The remark's
generalization to the continuous-report operator analogues (P in spatial, A
in DP) is consistent with the proof sketch (l.50-74). The seam-free billing
of the identifiability half (introduction.tex l.79-83) is now accurate: with
the rider relocated, the general statement carries no domain-specific rider.
CORRECT, and the prior review's m3 is resolved.

prop:singleton (l.81-103) is unchanged and correct: a |c(r)|=1 report adds a
standard basis row e_j^T to C, raising column rank; a basis-covering set of
singletons removes the rank deficit; C2 holds vacuously at a singleton. The
six singleton devices (tab:singletons l.109-141) are genuine |c(r)|=1 sets.
CORRECT.

## Residual logic items

None at critical or major severity. The two prior-review minors that touched
logic (cor:phenotype reparametrization explicitness; thm:general-rank
censoring rider) are BOTH now resolved in source. I find no new logic defect
introduced by the six minors or by the imsart reformat.

## What I did NOT find (botched-revision signatures)

- No section asserts the location identity as finite-sample exact for a
  general kernel (grep + section read).
- No DP statement generalizes release-consistency past n=1.
- The censoring rider does not survive anywhere inside a "general" theorem
  body.
- The Teicher citation is not misattributed: it supports the exact claim made.
- Theorem/corollary numbering is internally consistent in the aux (Theorem 1
  general-consistency, Theorem 2 general-rank, Corollaries 1-5, Proposition
  1, Remarks 1-2, Conditions 1-3); no duplicate or dangling result number.

No critical or major logic errors. The six minors and the imsart reformat
are logically sound.
