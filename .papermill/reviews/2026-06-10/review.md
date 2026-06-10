# Comprehensive Review: coarsening-synthesis

**Date**: 2026-06-10
**Paper**: One consistency theorem for coarsened-data maximum likelihood: a cross-domain synthesis of the coarsening-at-random framework
**Author**: Alexander Towell (SIUE, ORCID 0000-0001-6443-9897)
**Target venue**: Statistical Science (synthesis / unifying article)
**Reviewer**: single deep pass (Fable 5, max effort), with independent numerical
verification (Python/scipy), live Zenodo metadata checks, and web citation
verification. Not a multi-agent papermill pass.
**Build**: `make paper` clean, 12 pp, 0 undefined references/citations (the 3
"undefined" in the log are benign T1/ptm font-shape substitutions).
**Recommendation**: **minor-to-moderate revision.** One operational blocker (three
sibling DOIs do not resolve); two correctness-of-exposition items worth fixing for
a top venue; the rest are polish. The mathematics is sound and the central claims
verify.

---

## Summary

This is a strong synthesis. Its signature move, stating one consistency identity
and one rank/singleton apparatus once and recovering six domain theorems as
corollaries, is executed cleanly, and its main credibility asset, the honest
location of the two "seams" (differential privacy in the location-family branch;
weak supervision exact only under a sufficiency-complete parametrization), holds up
under scrutiny. I independently verified the load-bearing mathematics and the
citations; almost everything checks out. The findings below are about precision of
exposition and one operational citation problem, not about the validity of the
synthesis.

### What I verified (evidence)

1. **The scRNA cell-total identity is exact.** Simulated ZINB data (pi=0.30,
   mu=5, dispersion r=2, n=4000), fit by MLE, and confirmed
   `(1-pi_hat)*mu_hat = Xbar` to ~1e-7 with dispersion known and to ~3e-9 with
   dispersion free. The corollary's *conclusion* is correct. (Its *justification*
   is imprecise; see M1.)
2. **Regime-(B) constants are correct.** Numerically, the standard logistic kernel
   gives `J = 1/3`, `V = Var(psi(Z)/J - Z) = 0.28987`, `sqrt(V) = 0.5384`, matching
   the paper's "V ~ 0.290, sqrt(V) ~ 0.538". Laplace `V = 1` confirmed analytically
   (influence function `sign(Z) - Z`, `1 - 2E|Z| + Var = 1 - 2 + 2`). The
   Gaussian-iff-sample-mean characterization (Teicher 1961 / Cauchy equation at
   n=3) is correctly stated and correctly attributed.
3. **Citations are overwhelmingly accurate.** `domke2020moment` (arXiv:2001.09771),
   `fotakis2021efficient` (COLT 2021, PMLR 134:2060-2079, arXiv:2108.09805),
   `teicher1961maximum`, and `molenberghs2008every` all exist and are described
   correctly. The inline `arXiv:2602.23341` is real ("Mean Estimation from Coarse
   Data: Characterizations and Efficient Algorithms," Feb 2026). Sibling DOIs for
   masked, mdrelax, scrna, weaksup, mil all match their live Zenodo records.

### Finding counts
Major: 1 | Medium: 2 | Minor: 4 | Notes: 2 | Critical: 0

---

## Major

### J1. Three sibling citations point to Zenodo DOIs that do not resolve (operational, pre-submission blocker)
- **Where**: `refs.bib` entries `towell2026spatialcoarsening` (10.5281/zenodo.20422883),
  `towell2026dpcoarsening` (20422885), `towell2026phenotypecoarsening` (20422890),
  cited throughout (intro, framework table, corollaries, applications, identifiability).
- **Problem**: All three return **404** on both the Zenodo records API and doi.org;
  they are unpublished Zenodo *drafts* (the umbrella README lists spatial/dp/phenotype
  as "draft"). A Statistical Science referee who clicks any of these three references
  reaches a dead DOI. Since the empirical weight of the synthesis is explicitly
  delegated to the siblings ("the empirical validation of each named identity lives
  in the corresponding sibling, which we cite"), three unreachable siblings is a real
  credibility liability, not a cosmetic one. (weaksup 20422888 resolves to records/20422889;
  masked, mdrelax, scrna, mil all resolve.)
- **Fix (preferred)**: publish the spatial, dp, and phenotype Zenodo drafts so their
  concept DOIs resolve, exactly as mil and synthesis-v0.2.0 were just published. This
  is the family convention (cite by concept DOI; publish the preprint). One authorized
  one-click publish each.
- **Fix (fallback)**: if those three are not ready to be public, change their bib
  entries to a "manuscript in preparation / available from the author" form without a
  DOI, so the reference list does not advertise a DOI that 404s.

---

## Medium (fix for a top venue: correctness of exposition)

### M1. `cor:scrna` mischaracterizes the ZINB family and shows the wrong score
- **Where**: `sections/consistency.tex`, `cor:scrna` (lines ~178-181).
- **Quoted**: "the ZINB observed-count law is a regular exponential family with the
  mean-parameterized score `d_mu log g(x; mu, phi) = (x - mu)/[mu(1 + mu phi)]`,
  which is the regime-(A) hypothesis."
- **Problem**: Two inaccuracies, though the corollary's *conclusion* is correct
  (verified exact, above).
  (a) The displayed score `(x-mu)/[mu(1+mu phi)]` is the **negative-binomial** score,
  not the ZINB score; the ZINB score in `mu` carries an additional zero-inflation
  term from the point mass at 0. As written it scores NB, not ZINB.
  (b) ZINB is **not** a one-dimensional exponential family with sufficient statistic
  `T(X)=X`. A zero-inflated NB with known dispersion is a regular exponential family
  with the **two-dimensional** sufficient statistic `(X, 1{X=0})` (its density is the
  NB base reweighted only at zero). Cell-total consistency is the `X`-coordinate of the
  exact two-moment matching `E[X]=Xbar`, `E[1{X=0}] = `(zero fraction)`. A referee who
  tries to verify "ZINB is an exponential family with sufficient statistic X" will
  reject the sentence as stated, even though the identity it supports is true.
- **Fix**: one or two clauses, e.g. "the ZINB law (dispersion known) is a regular
  exponential family with sufficient statistic `(X, 1{X=0})`; cell-total consistency
  is the `X`-coordinate of the mean-matching identity," and drop or relabel the NB
  score (or present it as the NB component's score). Optionally note that with
  dispersion estimated the clean exponential-family story is lost but the `X`-moment
  identity persists (verified numerically).

### M2. The general theorem is stated/proved for i.i.d. reports but applied to GLMs
- **Where**: `thm:general-consistency` regime (A) and its proof (`sections/consistency.tex`
  lines ~66-79); used in `cor:spatial` and `cor:mil`.
- **Problem**: Regime (A) is stated for "the coarsened report law `p(r|theta)`" as a
  single exponential family with a common natural parameter `eta(theta)`, and the proof
  writes `l(theta) = sum_i [eta(theta)^T T(R_i) - A(eta(theta))]` with `eta` shared
  across `i` (the i.i.d. case), yielding the coordinatewise `m(theta_hat)=Tbar`. But
  `cor:spatial` (per-spot mean `sum_k p_{s,k} mu_{j,k}`) and `cor:mil` (per-bag
  `1 - exp(-m_i^T s)`) are **regression** exponential families: the reports are
  independent but not identically distributed, with a unit-indexed natural parameter
  `eta_i(theta)`. There the stationarity identity is the **aggregate score**
  `sum_i (d eta_i/d theta)^T (T(R_i) - m_i(theta_hat)) = 0` (which `cor:mil` correctly
  writes as `M^T D^{-1}(Y - p_hat)=0`), not a coordinatewise `m=Tbar`. The proof's
  chain-rule step extends verbatim, but the theorem as stated does not literally cover
  the GLM case its own corollaries use.
- **Why it matters**: at Statistical Science a careful reader will notice that four of
  the five regime-(A) corollaries are GLMs and ask where the theorem authorizes the
  unit-indexed `eta`. Right now the paper half-bridges this (it flags the "vector
  statement ... requires the joint rank condition" in cor:spatial/cor:mil) but never
  states the regression generalization.
- **Fix**: add one sentence or a short remark generalizing regime (A) to independent,
  non-identically-distributed exponential-family reports with `eta_i(theta)` (the
  aggregate-score identity, with `d eta/d theta` full column rank the rank condition).
  Then the four GLM corollaries are literal instances rather than re-derivations.

---

## Minor

### m1. `cor:spatial` calls its own identity "cell-total" (should be "spot-level")
- **Where**: `sections/consistency.tex` line 190: "`sum_k P_sk mu_{j,k} = Xbar_{sj}`,
  the **cell-total** consistency theorem of `\citet{towell2026spatialcoarsening}`."
- **Problem**: copy-paste slip; spatial's identity is **spot-level** consistency
  (the corollary is even titled "Spot-level consistency"). "cell-total" is the scRNA
  name (correctly used at line 177).
- **Fix**: "cell-total" -> "spot-level" at line 190.

### m2. weaksup bib title does not match the published Zenodo record
- **Where**: `refs.bib` `towell2026weaksupcoarsening`.
- **Problem**: bib title is "Coarsening at random for programmatic weak supervision:
  identifiability and bias bounds under heterogeneous labeling functions"; the live
  record (10.5281/zenodo.20422888 -> records/20422889) is titled "**Programmatic weak
  supervision as masked-cause inference: identifiability of label models without gold
  data**." The reference list will show a title that does not match the landing page.
- **Fix**: update the bib title to the record's title. (Aside: the masked and mdrelax
  bib titles here *do* match their Zenodo records, but differ from the titles used in
  the mil paper's bib and the umbrella README for the same DOIs; that is a
  family-wide harmonization issue, out of scope for this manuscript, which is correct.)

### m3. The 2026 coarse-data paper is cited as an inline string and mislabeled a "follow-up"
- **Where**: `sections/discussion.tex` lines ~139-145.
- **Quoted**: "`\citet{fotakis2021efficient}`, with a 2026 follow-up
  (`\texttt{arXiv:2602.23341}`) that characterizes when a coarse-label partition is
  information-preserving."
- **Problem**: (a) `arXiv:2602.23341` is typeset as a literal string, not a `\cite`,
  so it is absent from the reference list, unverified by BibTeX, and gives the reader
  no authors/title. (b) It is called a "follow-up" to Fotakis et al. 2021, but the
  author set differs (2602.23341 = Kalavasis, Mehrotra, Zampetakis, Zhou, Zhu; only
  Kalavasis is shared), so it is a thematically related later paper, not a direct
  follow-up. The paper is real and genuinely relevant (Gaussian mean estimation from
  partition-coarsened data, an identifiability characterization close to this paper's
  own regime-(B) content).
- **Fix**: add a proper `@misc`/`@article` bib entry and `\cite` it; replace "follow-up"
  with "a closely related 2026 paper" or similar.

### m4. `cor:spatial` implied mean includes a library-size factor the table omits
- **Where**: `cor:spatial` text ("Poisson report law of mean `N_s sum_k p_{s,k} mu_{j,k}`")
  vs `tab:css` spatial row (`sum_k P_sk mu_{j,k}`, no `N_s`).
- **Problem**: minor inconsistency in whether the spot library size `N_s` appears in
  the implied mean. Presumably `N_s` is a known offset absorbed into the identity, but
  the table and corollary should agree.
- **Fix**: state `N_s` as a known offset in both places, or drop it from the corollary
  text for consistency with the table and the displayed identity.

---

## Notes (optional, non-blocking)

### N1. Regime-(B) V constants are at each kernel's standard scale, not a common variance
The tabulated `V = 1` (Laplace) and `V ~ 0.290` (logistic) are computed at each
kernel's **scale-1** parametrization (standard Laplace, variance 2; standard logistic,
variance pi^2/3), not standardized to a common variance. Because `V = Var(psi(Z)/J - Z)`
contains the `-Z` term, it is scale-dependent, so the two numbers are not on a common
footing. This is fine for a per-kernel constant table, but one clause stating the scale
convention ("each kernel at unit scale parameter") would prevent a reader from
comparing 1 vs 0.290 as if they were standardized. (Both values are otherwise correct.)

### N2. Strengths worth preserving
The two-seam honesty is the paper's best feature and should not be softened in
revision: it is what makes the unification credible rather than glib, and it is
mathematically correct (verified). The preemptive "isn't this just moment matching?"
paragraph in the introduction is well-judged and now correctly anchored to
`domke2020moment`. The singleton-and-rank half is genuinely the stronger, seam-free
contribution and is framed as such.

---

## Disposition for submission

The paper is intellectually ready. The only true pre-submission blocker is **J1**
(publish the three draft siblings so their DOIs resolve, or de-DOI them). **M1** and
**m1** are cheap correctness fixes that a top-venue referee would otherwise flag;
**M2** is a one-remark rigor improvement; **m2/m3/m4/N1** are polish.

Because the repository HEAD already diverges from the published v0.2.0 (the
`[ht]->[tb]` float fix, commit abf67ed), a **v0.3.0 re-version** is already implied
if the submitted PDF is to match the public preprint. The efficient path is to fold
M1, M2, m1-m4, N1 into that same v0.3.0, publish once, and submit. None of these
changes touch the results; they sharpen exposition, fix one typo, and repair
citations.
