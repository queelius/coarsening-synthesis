# Logic Checker Report

Date: 2026-06-03
Scope per area-chair instruction: VERIFY the clean corollaries (scRNA,
phenotype, spatial-per-coordinate) and the rank/singleton results. Do NOT
re-attempt the open location-family (regime B) step or the weak-supervision
rate; those are handled by dedicated research agents. Confirm only that the
synthesis describes those two seams faithfully.

## Verdict summary
- Regime (A) core proof: CORRECT as written. Independently re-derived.
- cor:scrna (cell-total): CLEAN. Faithful to sibling thm:cell-total.
- cor:phenotype (code-frequency): CLEAN. Faithful to sibling glass-ceiling +
  Rogan-Gladen. One sharpening recommended (scalar-family wording).
- cor:spatial (spot-level per coordinate): CLEAN per coordinate. Vector-form
  dependence on the rank theorem is correctly flagged.
- thm:general-rank: CORRECT as a restatement; proof is a sketch citing
  towell2026masked, appropriate for a synthesis. One gap noted (necessity
  scope).
- prop:singleton: CORRECT. The "adding rows can only raise rank" argument is
  valid and the six devices are genuine |c|=1 sets.
- Seam descriptions (DP regime B, weak-sup asymptotic): FAITHFUL to siblings.

## 1. Regime (A) proof, re-derived independently

The manuscript (consistency.tex, proof of thm:general-consistency) gives, for
p(r|theta) = h(r) exp{eta(theta)^T T(r) - A(eta(theta))}:
  d ell / d eta = sum_i T(R_i) - n grad A(eta) = n( Tbar - E_eta[T] ),
using grad A(eta) = E_eta[T]. Chain rule: d ell/d theta = (d eta/d theta)^T
d ell/d eta. At an interior max d ell/d theta = 0; full column rank of
d eta/d theta forces d ell/d eta = 0, hence E_hat[T] = Tbar.

Re-derivation: correct. This is the standard exponential-family score equation
(moment matching). The full-column-rank hypothesis is exactly what is needed to
pass from d ell/d theta = 0 to d ell/d eta = 0 (left-invertibility of the
Jacobian). No error. The "up to optimization tolerance" hedge is appropriate.

The closing sentence ("any bias ... is absorbed into the part of the model
orthogonal to T") is a correct and useful interpretation, not an overclaim.

## 2. cor:scrna (cell-total consistency) -- CLEAN

Synthesis claim: ZINB observed-count law is a regular exponential family with
mean-parameterized score d_mu log g = (x - mu)/[mu(1+mu phi)], so regime (A)
applies and (1 - pi_hat) mu_hat = Xbar.

Cross-check against sibling (scrna-coarsening/sections/identifiability.tex,
thm:cell-total): states VERBATIM "(1 - pi_hat_j) mu_hat_j = Xbar_j" "at any
interior MLE ... exactly (up to optimization tolerance)." The sibling's own
remark generalizes to "any zero-inflated regular exponential family ... with a
mean-parameterized score d_mu log g = c(mu, eta)(x - mu)."

Assessment: the reduction is exact and faithful. The synthesis even uses the
sibling's own generalization mechanism. CLEAN. No issue.

Minor technical nuance (not a defect): the ZINB observed law is, strictly, a
two-component mixture; it is a regular exponential family in the
(mean, dispersion, zero-inflation) parametrization only at interior points and
modulo the boundary cases the sibling lists (pi in {0,1}, mu = 0). The
synthesis's "interior MLE" hypothesis already excludes those, so the claim is
safe. Optionally cite the boundary carve-out for completeness.

## 3. cor:phenotype (code-frequency consistency) -- CLEAN

Synthesis claim: single-code Bernoulli depends on (pi, sens, spec) only through
q = pi*sens + (1-pi)(1-spec), the natural mean parameter; regime (A) gives
q(hat) = Cbar; exact in the informative regime sens + spec > 1 (nonzero mean
gradient).

Cross-check against sibling (phenotype-coarsening/identifiability.tex):
- code frequency q = pi*sens + (1-pi)(1-spec): MATCHES (eq line 18).
- thm:glass-ceiling: "one scalar equation in three unknowns," continuum of
  triples give same q. CONFIRMS that the model is a one-dimensional
  exponential family in q (Bernoulli), with (pi,sens,spec) a 3->1
  reparametrization.
- informative condition sens + spec > 1: MATCHES VERBATIM (line 112-113,
  "well-defined whenever sens_hat + spec_hat > 1, the condition that the code
  is informative").

Assessment: CLEAN. The regime-(A) hypothesis here is the SCALAR case: a
one-parameter exponential family (Bernoulli with natural mean q), and
"full-column-rank Jacobian" degenerates correctly to grad_theta q != 0, i.e.,
sens + spec > 1. The synthesis states this exactly ("the full-rank-Jacobian
hypothesis of regime (A) specialized to the scalar mean").

Recommended sharpening (MINOR, clarity not correctness): the phrase "which is
the natural mean parameter" could add half a sentence noting that the map
(pi,sens,spec) -> q is 3-to-1, so consistency pins q but NOT the triple, which
is precisely why this domain needs the singleton (chart review). This ties
cor:phenotype to prop:singleton and is the whole point of the glass-ceiling.
Currently the reader must supply that link.

## 4. cor:spatial (spot-level consistency) -- CLEAN per coordinate

Synthesis claim: spot Poisson law with mean N_s sum_k p_sk mu_jk is a regular
exponential family, so sum_k P_hat_sk mu_hat_jk = Xbar_sj holds exactly per
coordinate; the VECTOR statement over (s,j) additionally needs the joint rank
condition (thm:general-rank), "the only place the rank condition enters a
consistency claim."

Cross-check against sibling (spatial-coarsening): cell-total consistency
theorem ported to ST; full-column-rank C / P condition present
(background.tex:58, validation full column rank K). MATCHES.

Assessment: CLEAN per coordinate. Poisson is a regular exponential family with
natural statistic = count, so the per-coordinate moment identity is exact and
needs no rank condition. The honest separation ("exact per coordinate; vector
form leans on rank") is correct and is exactly the right level of care. This is
the one place where consistency and identifiability are not cleanly separable,
and the paper says so (here and again in discussion.tex). Good.

## 5. thm:general-rank (augmented-candidate-set rank) -- CORRECT restatement

The theorem restates towell2026masked's identifiability result for the abstract
process: (a) necessity via coarsening-confounding (likelihood depends on a
confounded pair only through their sum); (b) sufficiency via full column rank
of the augmented incidence matrix C-tilde. Proof is a SKETCH that differences
the report law across candidate sets to get C-tilde g = 0, then full column
rank forces g = 0.

Assessment: the sketch is logically valid and is appropriate for a synthesis
(it cites the full proof in towell2026masked). The operator analogues (P in
spatial, A in DP linear query, agreement matrix in weak sup) are each confirmed
in their siblings (full column rank of P; A full column rank; agreement-matrix
rank-one off-diagonal under conditional independence with rank deficit r). The
unification of the rank condition is CLEAN across domains.

GAP (MINOR, scope-of-claim): the sufficiency clause carries a parenthetical
"(and, in the time-to-event instance, the mechanism assigns positive
probability to both exact and censored reports)." This is a reliability-
specific side condition smuggled into a "general" theorem. It is honest but
slightly breaks the "one clean general statement" framing. Recommend either
(i) moving it to a remark as a domain-specific regularity rider, or (ii)
abstracting it ("the mechanism is rich enough that the incidence matrix is
realized," which is what it means generally). As written it reads as a seam in
the rank result that the prose elsewhere claims is seamless.

## 6. prop:singleton (singleton restoration) -- CORRECT

Argument: a singleton {j} adds standard-basis row e_j^T to C; adding rows can
only raise rank; a set of singletons spanning the left-null directions removes
the deficit; then thm:general-rank(b) applies. Singletons satisfy C2 vacuously.

Assessment: VALID. "Adding rows can only raise (never lower) the column rank"
is correct linear algebra; covering a basis of the deficient subspace restores
full column rank. The C2-vacuousness at |c(r)| = 1 is immediate from C2's
statement (the "for all y, y' in c(r)" quantifier is vacuous on a singleton).

The six singleton devices were each verified to be genuine |c|=1 candidate sets
in their siblings (not analogies):
- reliability: diagnostic resolving the cause -> exact cause K_i (masked paper
  line 100 "when it is a singleton, the cause is exactly identified").
- scRNA: ERCC spike-in (known input).
- spatial: single-cell-resolution probe (sibling background.tex:61 "Singleton
  candidate sets |c_i|=1 are critical").
- DP: non-private (Z = 0) release (sibling: "non-private release," "singleton
  release collapses c_eff").
- weak sup: gold label (sibling background.tex:68 "Singleton candidate sets
  |c_i|=1 ... singletons restore the missing rank").
- phenotype: chart-reviewed patient -> true state.

This is the strongest part of the unification: prop:singleton is genuinely ONE
device, six costumes, with no seam. tab:singletons earns its claim "these are
not analogies."

## 7. Faithful description of the two seams (not re-derived, only audited)

- DP / regime B (cor:dp, rem:loc-sketch): synthesis says release consistency is
  a location-family first-moment identity, exact for the Gaussian kernel,
  population first-moment for a general symmetric kernel, with the
  finite-sample arbitrary-kernel case OPEN. Sibling dp-coarsening confirms
  Gaussian-convolution treatment and convolution-mean identity. FAITHFUL.
- Weak sup (cor:weaksup): synthesis says exact only when agreement indicators
  are sufficient statistics, asymptotic at n^{-1/2} for the naive-Bayes
  parametrization. Sibling weaksup-coarsening confirms n^{-1/2} rate
  (validation.tex:72,104) and rank deficit r. FAITHFUL.

The regime-B psi-function argument as written (psi = -p_0'/p_0 odd and
monotone for symmetric unimodal p_0; hat-mu is the psi-location; equals sample
mean iff psi linear) is internally correct M-estimation reasoning. The single
labeled open step (finite-n, arbitrary-kernel exactness) is correctly isolated
in rem:loc-sketch and NOT overclaimed. I did not attempt to close it (out of
scope).

## Logic-checker findings list
- MINOR (clarity): cor:phenotype should state the 3->1 reparametrization
  explicitly to link consistency to the need for the chart-review singleton.
- MINOR (scope): thm:general-rank sufficiency carries a reliability-specific
  censoring rider inside a "general" statement; abstract it or move to a
  remark.
- MINOR (completeness): cor:scrna could cite the boundary carve-out (pi in
  {0,1}, mu = 0) the sibling handles, though "interior MLE" already covers it.
- NO critical or major logic errors. The clean corollaries are genuinely
  clean; the rank/singleton results are correct; both seams are described
  faithfully.

Confidence: HIGH (re-derivations and sibling cross-references performed
directly).
