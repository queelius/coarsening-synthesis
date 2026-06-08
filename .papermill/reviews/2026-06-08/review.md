# Multi-Agent Review Report

**Date**: 2026-06-08
**Paper**: One consistency theorem for coarsened-data maximum likelihood: a cross-domain synthesis of the coarsening-at-random framework
**Author**: Alexander Towell (SIUE)
**Venue target**: Statistical Science (IMS imsart, sts option)
**Recommendation**: minor-revision

## Summary

**Overall Assessment**: This is a well-built, honestly scoped synthesis whose
central mathematics is sound and whose framing is correctly calibrated for a
unity-of-the-field venue. The just-integrated sixth corollary (multiple instance
learning, cor:mil) is mathematically correct at the level of the score equation,
and "seven domains, six corollaries" is internally consistent almost everywhere.
The fold-in left two addressable MAJOR issues: (1) cor:mil is classified as a
clean regime-(A) exact reduction when it actually yields an IRLS-weighted normal
equation under a non-canonical link, which is exact but in a different sense than
the theorem's stated conclusion; and (2) one stale count ("the other four
corollaries") that contradicts the parallel five-corollary statements in the
intro and discussion. Neither is a correctness failure; both are small edits.

**Strengths**:
1. The central reductions are correct and the regime split (exponential family
   vs location family) is the right organizing axis; regime (A) is a complete
   proof and regime (B)'s Gaussian-iff boundary is correctly characterized
   (logic-checker, methodology-auditor).
2. The contribution is honestly scoped as organization, not new mathematics, and
   the seams (DP location-family branch, weak-supervision parametrization) are
   disclosed consistently in abstract, intro, the relevant corollary, and
   discussion (novelty-assessor, methodology-auditor).
3. The singleton/rank apparatus, shown to be one device across seven domains, is
   a genuine non-textbook unifying result and the strongest novelty anchor
   (novelty-assessor).
4. Build is clean and venue-correct: 12 pages, 0 substantive undefined refs, 0
   undefined citations, 0 BibTeX warnings, complete imsart frontmatter
   (format-validator, citation-verifier).
5. The prose is confident and well-paced; the opening litany and the "costume"
   metaphor land the thesis effectively, and the MIL material reads as native
   apart from two notation slips (prose-auditor).

**Weaknesses**:
1. cor:mil's "regime (A) exact" claim overstates how cleanly it instantiates the
   general theorem; the identity it derives (M^T D^{-1}(Y - p_hat) = 0) is
   IRLS-weighted, not the unweighted m(theta_hat) = bar T the theorem states
   (logic-checker, methodology-auditor, novelty-assessor).
2. A stale count: "the other four corollaries" should be "five" after the MIL
   fold-in (logic-checker, prose-auditor).
3. Two corollaries (cor:scrna, cor:mil) assert exponential-family membership
   loosely (ZINB is a mixture; MIL's noisy-OR link is non-canonical) and defer
   the precise statement to siblings, one of which is cited only by URL
   (logic-checker, methodology-auditor).
4. MIL is the thinnest-anchored domain: MUSK1/MUSK2 is named with no citation to
   Dietterich et al. (1997), and the sibling has no DOI (citation-verifier,
   novelty-assessor, literature context).
5. Minor notation friction from the fold-in: m_b vs m_i for the bag vector, and
   M overloaded as DP release scalar and MIL composition matrix (prose-auditor).

**Finding Counts**: Critical: 0 | Major: 3 | Minor: 7 | Suggestions: 4

## Critical Issues

None. No proof is broken, no theorem is false, and the central unification claim
is supported. The MIL score equation is correctly derived and independently
reproduced; the count and classification issues below are real but
edit-level.

## Major Issues

### MIL corollary is classified as clean regime-(A) exact, but its identity is IRLS-weighted (sources: logic-checker, methodology-auditor, novelty-assessor)
- **Location**: cor:mil (consistency.tex:213-234) against the theorem statement
  (consistency.tex:38-45, eq:general-consistency) and the tab:reduction MIL row
  `bullet` (consistency.tex:300); echoed in tab:css (framework.tex:138-140) and
  the abstract (main.tex:109-111).
- **Quoted text (theorem)**: "In regime (A) the fitted mean of the
  coarsening-sufficient statistic equals its empirical mean as an exact
  finite-sample identity, in every coordinate of $\T$, $m(\hat\theta) = \bar\T$".
- **Quoted text (corollary)**: "Then \eqref{eq:general-consistency} reads
  $M^\top D^{-1}(\bm Y - \hat{\bm p}) = \bm 0$ ... the inverse-fitted-rate
  weighting $D^{-1}$ is the only wrinkle ... so the moment matching is
  IRLS-weighted rather than unweighted."
- **Problem**: eq:general-consistency is the UNWEIGHTED identity m(theta_hat) =
  bar T (for MIL that would be p_hat = bar Y, sum_i (Y_i - p_i) = 0). What the
  corollary actually derives, correctly, is the WEIGHTED equation
  M^T D^{-1}(Y - p_hat) = 0, which holds precisely because the noisy-OR link is
  non-canonical. So "eq:general-consistency reads M^T D^{-1}(Y - p_hat) = 0" is
  not a reading of eq:general-consistency; it is a reading of the score equation
  (partial eta/partial theta)^T (bar T - E[T]) = 0 before the full-column-rank
  step strips the Jacobian. cor:scrna and cor:phenotype genuinely satisfy
  m(theta_hat) = bar T (canonical mean parameter); cor:mil does not. The reach
  symbol `bullet` ("exact finite-sample identity") in tab:reduction puts MIL in
  the same clean bucket as the unweighted rows, overstating the fit. This is
  exactly the regime-(A) classification question the brief flagged: as written,
  MIL is regime (A) in the GLM/score-equation sense, not the stripped
  m = bar T sense.
- **Suggestion**: state the theorem's regime-(A) conclusion once in
  score-equation form, (partial eta/partial theta)^T (bar T - E[T]) = 0, noting
  it collapses to m(theta_hat) = bar T for canonical-link members (scrna,
  phenotype, spatial-Poisson) and carries the IRLS weight D^{-1} for
  non-canonical links (MIL noisy-OR). Then cor:mil becomes a true corollary.
  Add a distinguishing mark to the MIL row of tab:reduction (e.g., "exact,
  IRLS-weighted") and a matching half-clause in the abstract. The novelty-
  assessor notes the honest framing (the single principle reaching a
  non-canonical-link member) is a STRONGER synthesis point than the current
  tidy-but-loose claim.
- **Cross-verified**: YES. methodology-auditor re-derived M^T D^{-1}(Y - p_hat)
  = 0 from scratch and obtained the identical equation, concurring that it is the
  noisy-OR GLM normal equation and that the `bullet` bucket conflates weighted
  and unweighted exact identities. novelty-assessor concurs from the framing
  side. No disagreement among specialists.

### Stale count: "the other four corollaries" contradicts the five-corollary statements elsewhere (sources: logic-checker, prose-auditor)
- **Location**: consistency.tex:276 (inside cor:dp).
- **Quoted text**: "its proof uses the location-family score identity, not the
  exponential-family mean-value identity that serves the other four
  corollaries."
- **Problem**: DP is contrasted against the regime-(A) corollaries. After the
  MIL fold-in those are scrna, spatial, phenotype, mil, weaksup = FIVE. The two
  parallel sentences already say five: introduction.tex:126 ("the
  exponential-family branch that serves the other five domains") and
  discussion.tex:42 ("The other five consistency theorems"). The conclusion
  (conclusion.tex:24-29) also correctly enumerates five regime-A corollaries
  plus release. So consistency.tex:276 is the lone location the MIL integration
  missed, still carrying the pre-MIL count of four. A reader cross-checking the
  central accounting of a "state it once" paper finds 4 / 5 / 5.
- **Suggestion**: change "the other four corollaries" to "the other five
  corollaries" at consistency.tex:276.
- **Cross-verified**: YES. All three parallel sentences quoted verbatim from
  source (sed-confirmed). The five-count is correct; the four-count is the
  error. prose-auditor independently flagged the same line as a prose-
  consistency break.

### MIL domain anchor missing: MUSK named without citing Dietterich et al. (1997) (sources: citation-verifier, novelty-assessor, literature context)
- **Location**: applications.tex:108 ("a MUSK1/MUSK2 application"); cor:mil and
  the MIL subsection cite only towell2026milcoarsening.
- **Quoted text**: "a MUSK1/MUSK2 application; it identifies the confound between
  intrinsic instance positivity and the noisy-OR firing rate as the
  discrete-label analogue of the spike-in capture-efficiency gap in scRNA-seq."
- **Problem**: the MUSK datasets and the multiple-instance problem originate with
  Dietterich, Lathrop & Lozano-Perez (1997), Artificial Intelligence
  89(1-2):31-71. MIL is the only one of the seven domains with no external
  anchor citation (every other domain cites a classical source). Naming MUSK
  without its source is a gap a MIL referee will catch, and it weakens the
  "seven established fields that do not cite one another" breadth claim for the
  newest domain.
- **Suggestion**: add Dietterich et al. (1997) and cite it where MUSK is named;
  optionally add one noisy-OR-MIL reference (Viola-Platt-Zhang 2005 or
  Zhang-Goldman 2001) where the model is introduced.
- **Cross-verified**: YES. citation-verifier confirmed via the cite-key/bib
  diff that MIL has no external anchor; literature context confirmed Dietterich
  et al. (1997) is the MUSK source.

## Minor Issues

### "ZINB ... is a regular exponential family" is imprecise (source: logic-checker)
- **Location**: cor:scrna (consistency.tex:172-175).
- **Quoted text**: "the ZINB observed-count law is a regular exponential family
  with the mean-parameterized score $\partial_\mu \log g(x; \mu, \phi) = (x -
  \mu)/[\mu(1+\mu\phi)]$, which is the regime-(A) hypothesis."
- **Problem**: ZINB with free zero-inflation is a two-component mixture, not a
  regular exponential family, and the displayed score is the NB (not ZINB)
  mean-score. The consistency identity (1-pi_hat)mu_hat = X_bar is correct; the
  exponential-family justification is loose. Same family of looseness as the MIL
  "Bernoulli ... regular exponential family" claim.
- **Suggestion**: rephrase to the NB-at-fixed-dispersion exponential family plus
  the (1-pi) mean factor, or cite the sibling for the precise family statement.

### Exponential-family claims defer checkability to siblings unevenly (source: methodology-auditor)
- **Location**: cor:scrna (consistency.tex:172), cor:mil (consistency.tex:225).
- **Problem**: a self-contained synthesis should let the reader verify each
  regime hypothesis in-paper; phenotype and dp are fully checkable, but scrna and
  mil defer the precise family statement to siblings, and the MIL sibling is
  URL-only.
- **Suggestion**: add one sentence per corollary giving the precise family/link
  statement in-paper.

### Abstract states the identity in unweighted form without the MIL caveat (source: logic-checker)
- **Location**: main.tex:109-111.
- **Quoted text**: "the fit reproduces the empirical mean of a
  coarsening-sufficient statistic at the optimum."
- **Problem**: for MIL this holds only in the IRLS-weighted sense. The abstract
  qualifies the boundary immediately, so minor; track whichever MIL fix is
  chosen.
- **Suggestion**: "reproduces the empirical mean ..., exactly or in an
  IRLS-weighted sense, at the optimum."

### tab:css MIL row presents the implied mean without the IRLS caveat (source: methodology-auditor)
- **Location**: framework.tex:138-140, caption framework.tex:144-146.
- **Problem**: tab:css promises "the single identity m(theta_hat) = bar T, read
  in each row's coordinates," which for the MIL row is true only weighted.
- **Suggestion**: footnote the MIL row or amend the caption.

### Notation: bag vector is m_b in tab:css, m_i in cor:mil (source: prose-auditor)
- **Location**: framework.tex:140 ($\bm m_b$) vs consistency.tex:217-218
  ($\bm m_i$).
- **Suggestion**: use one subscript in both.

### Symbol overload: M is the DP release scalar and the MIL composition matrix in the same section (source: prose-auditor)
- **Location**: consistency.tex:259 / framework.tex:131 (release $M$) vs
  consistency.tex:220-221 (composition matrix $M$).
- **Suggestion**: rename the MIL matrix (e.g., B), or note the local reuse.

### State file / CLAUDE.md page count stale (13 vs build 12) (source: format-validator)
- **Location**: .papermill/state.md, CLAUDE.md.
- **Suggestion**: update to 12 at the next state edit (done in this pass's
  review-history update; the body counts can be refreshed when next editing).

## Suggestions

1. Split the longest stacked-appositive sentences (abstract 117-128; the "count"
   sentence introduction.tex:111-117; the tab:reduction lead-in
   consistency.tex:282-288) into shorter sentences (prose-auditor).
2. Soften the repeated "not a list of apologies" / "located exactly, not
   asserted" reassurances; once is enough for the synthesis venue (prose-auditor).
3. Add one or two sentences distinguishing this synthesis from EM-as-unifier
   (Dempster-Laird-Rubin) and influence-function unifications (Tsiatis, van der
   Vaart): those unify estimation machinery, this unifies a diagnostic identity
   and its identifiability remedy (novelty-assessor, literature context).
4. Optional citations: a continuous-CAR reference (Jacobsen-Keiding 1995 or
   Nielsen 2000) where the continuum candidate set is introduced, and an
   exponential-family-foundations reference (Brown 1986 or Barndorff-Nielsen
   1978) for regime (A) (citation-verifier, literature context).

## Detailed Notes by Domain

### Logic and Proofs
Regime (A) proof is complete and correct (log-partition gradient + full-column-
rank Jacobian -> m(theta_hat)=bar T). Regime (B) is correctly characterized: the
psi-location identity is exact finite-sample, the Gaussian-iff-sample-mean result
is Teicher (1961) via the Cauchy equation at n=3, the (0,1,5) Laplace example is
correct (gap -1), and V = Var(psi(Z)/J - Z) is the correct linearization. cor:dp
(n=1, mode=mean), cor:phenotype (q the mean parameter), and cor:weaksup
(sufficiency vs naive-Bayes asymptotic seam) are correct and honest. The MIL
score equation is correctly derived. The two logic-level defects are the
classification of cor:mil relative to the theorem's stated conclusion (MAJOR) and
the stale count at consistency.tex:276 (MAJOR), plus the ZINB exponential-family
imprecision (MINOR).

### Novelty and Contribution
Correctly scoped as organization, not new mathematics; the framing preemptively
answers the "isn't this the textbook score equation" objection well, and the
singleton/rank apparatus is the genuine non-textbook anchor. No prior work
unifies CAR across this seven-domain span. The only novelty risk is upward: the
MIL reduction is presented as cleaner (a fifth clean regime-(A) exact reduction)
than it is; fixing the regime-(A) framing converts the overstatement into a
stronger, truthful reach result.

### Methodology
The reduction methodology is principled and the seams are disclosed
consistently. Independent re-derivation confirms the MIL normal equation and
confirms the regime-(A) bucket conflates unweighted (m=bar T) and IRLS-weighted
exact identities. Checkability of the exponential-family hypotheses is uneven
across corollaries; the two loosest (scrna, mil) defer to siblings.

### Writing and Presentation
Strong, confident, well-paced; clean transitions; no em-dashes. The MIL fold-in
reads as native apart from two notation slips (m_b/m_i, M overload) and the count
line. Some sentences run long with stacked appositives; the seam-defense phrasing
is slightly over-repeated.

### Citations and References
Bibliography integrity clean: 27 cited keys = 27 defined keys, zero orphans, zero
undefined, zero BibTeX warnings. Classical references spot-checked correct. The
substantive gap is the missing Dietterich et al. (1997) where MUSK is named
(MAJOR); the URL-only MIL sibling is deliberate and disclosed (MINOR); a
continuous-CAR and an exponential-family-foundations cite are optional.

### Formatting and Production
Build clean: `make paper` exit 0, 12 pages, 0 substantive undefined refs, 0
undefined citations, no multiply-defined labels, complete imsart sts frontmatter.
Five overfull hboxes, largest 13.9pt in tab:reduction (cosmetic, below the
visible-protrusion threshold). State/CLAUDE page count is stale (13 vs 12).

## Literature Context Summary
No direct prior-art threat to the central unification claim: nobody has published
this seven-domain CAR synthesis, and the "marginal fit is not evidence of
unbiasedness" diagnostic is not packaged under a single canonical name, which
supports the organizing contribution. The two citation soft-spots a domain
referee is most likely to name are the MIL domain (no Dietterich 1997 despite
naming MUSK; sibling URL-only) and the continuous-CAR lineage (Jacobsen-Keiding /
Nielsen) given the discrete-to-continuous candidate-set move. Teicher (1961) is
the correct primary cite for the Gaussian characterization and is correctly
attributed. van der Vaart suffices for regime (A); Brown (1986) / Barndorff-
Nielsen (1978) would strengthen it.

## Review Metadata
- Specialist roles executed: literature scout (broad + targeted, merged),
  logic-checker, novelty-assessor, methodology-auditor, prose-auditor,
  citation-verifier, format-validator. (The Task tool for spawning sub-agents was
  unavailable in this environment; the area chair executed each specialist role
  directly and verified every quoted manuscript string verbatim against source.)
- Cross-verifications performed: 3 (MIL regime-(A) classification re-derived
  independently by methodology-auditor and reframed by novelty-assessor; count
  slip confirmed verbatim across all three parallel sentences; MUSK citation gap
  confirmed via cite-key/bib diff).
- Disagreements noted: 0. All specialists concur on the MIL classification and
  the count slip.
- Hallucination check: PASS. Every Critical/Major/Minor quoted string was
  re-confirmed verbatim in the source files (grep/sed). No finding rests on text
  absent from the manuscript.
