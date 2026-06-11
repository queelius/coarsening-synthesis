---
paper_id: coarsening-synthesis
title: "One consistency theorem for coarsened-data maximum likelihood: a cross-domain synthesis of the coarsening-at-random framework"
short_title: "Coarsening synthesis"
authors:
  - name: "Alexander Towell"
    email: "lex@metafunctor.com"
    orcid: "0000-0001-6443-9897"
    affiliation: "Department of Computer Science, Southern Illinois University Edwardsville"
paper_type: theory-synthesis
stage: submitted (Statistical Science, 2026-06-11)
created: 2026-06-03
last_updated: 2026-06-11

submission:
  venue: "Statistical Science"
  manuscript_id: "STS2606-004"
  status: under-review
  submitted: 2026-06-11
  round: null      # awaiting editor assignment (initial processing)
  decision: null
  track_url: "https://www.e-publications.org/ims/submission/STS/author/track"
  ejms_article_id: 77074
  preprint: "v0.3.0, Zenodo concept DOI 10.5281/zenodo.20533912 (version 10.5281/zenodo.20633365)"
  uploaded: "main.pdf (v0.3.0 build, 12pp, [sts] imsart); metadata, keywords, MSC2020 (in cover comments), abstract entered; no supplementary files; source held for production at acceptance"

structure:
  format: LaTeX-methods-synthesis
  main_file: main.tex
  bib_file: refs.bib
  sections_dir: sections/
  sections:
    - introduction.tex
    - framework.tex
    - consistency.tex
    - identifiability.tex
    - applications.tex
    - discussion.tex
    - conclusion.tex
  page_target: 18
  margins: 1in
  font: 11pt

build:
  paper_cmd: make paper
  base_dependencies: [pdflatex, bibtex]
  no_simulation: true
  note: "Synthesis paper. No new simulations; empirical weight is carried by the six sibling papers, which are cited."

# ============================================================================
# THESIS (papermill:thesis)
# ============================================================================

thesis:
  one_sentence: >
    One general consistency theorem for coarsened-data maximum likelihood,
    that at an interior MLE of the face-value (coarsening-at-random)
    likelihood the fitted mean of the coarsening-sufficient statistic
    equals its empirical mean, currently appears under five different
    names across five domains (cell-total consistency in scRNA-seq, the
    spot-level variant in spatial deconvolution, release consistency in
    differential privacy, agreement consistency in weak supervision, and
    code-frequency consistency in phenotyping); this paper states it once
    at the right generality, recovers each named instance as a corollary,
    and likewise states the augmented-candidate-set rank condition and the
    singleton-candidate-set restoration of identifiability once with the
    domains as instances.
  novelty: >
    Not new mathematics. The contribution is unification and
    organization: the recognition that one consistency identity and one
    rank/singleton apparatus recur across six concrete fields as
    instances of coarsening at random, plus the explicit reduction with
    an honest account of the two regimes (regular exponential family vs.
    location family) and the two seams (weak supervision reduces exactly
    only under a sufficiency-complete parametrization; differential
    privacy sits in the location-family branch, not the
    exponential-family branch).

contributions:
  - "A single abstract coarsening framework (C1/C2/C3 stated once, general DGP, the coarsening-sufficient-statistic setup)."
  - "A general consistency theorem (thm:general-consistency) in two regimes: (A) regular exponential family, complete proof via the log-partition gradient; (B) location family, proof with one labeled open step, exact for the Gaussian kernel."
  - "Five named corollaries recovering cell-total (scRNA), spot-level (spatial), code-frequency (phenotype), agreement (weak supervision), and release (DP) consistency, with explicit reduction-status flags."
  - "A general augmented-candidate-set rank condition for identifiability (thm:general-rank) and a singleton-restoration result (prop:singleton), with the per-domain singleton devices tabulated as one mechanism."
  - "A compact applications tour placing each of the six domains as an instance, citing the sibling paper for domain-specific development rather than re-deriving."

# ============================================================================
# OUTLINE (papermill:outline)
# ============================================================================

outline:
  - section: introduction.tex
    purpose: "The family, the recurring pattern (five named consistency theorems + one rank/singleton apparatus), and the contribution: state them once. Flags the two seams up front."
  - section: framework.tex
    purpose: "C1/C2/C3 stated once for an abstract coarsening; the general data-generating process; the face-value likelihood CAR licenses; the coarsening-sufficient-statistic definition with per-domain instantiations (tab:css)."
  - section: consistency.tex
    purpose: "The GENERAL consistency theorem (thm:general-consistency) with proof (regime A complete, regime B one open step), then the five named corollaries in a few lines each, plus a reduction-status table (tab:reduction)."
  - section: identifiability.tex
    purpose: "The general augmented-candidate-set rank condition (thm:general-rank) and the singleton-restoration result (prop:singleton); per-domain singleton devices tabulated (tab:singletons); what breaks when C2 fails."
  - section: applications.tex
    purpose: "Compact tour: one short subsection per domain (reliability, scRNA, spatial, DP, weak supervision, phenotyping) showing it is an instance, citing the sibling for details and validation."
  - section: discussion.tex
    purpose: "What the unification buys (economy, shared diagnostic moral, transfer of remedies); where it is seamed (DP location-family branch, weak-supervision parametrization, spatial vector form); open per-domain problems; relation to the CAR literature."
  - section: conclusion.tex
    purpose: "Restate the one-theorem-across-domains result and the named seams; the empirical weight stays with the siblings."

narrative_arc: >
  Six fields, same problem -> one framework (C1/C2/C3 + coarsening-
  sufficient statistic) -> one consistency theorem with two regimes ->
  five named theorems fall out as corollaries (three clean, two seamed)
  -> one rank condition and one singleton device unify identifiability
  with no seams -> each domain is an instance -> what the unification
  buys and where it is honestly seamed.

# ============================================================================
# VENUE (papermill:venue)
# ============================================================================

target_venues:
  - rank: 1
    name: "Statistical Science"
    primary: true
    rationale: >
      Best fit. Statistical Science explicitly publishes unifying,
      review, and synthesis pieces, which is exactly the genre of this
      paper: one idea organized across many domains, light on new
      theorems, heavy on perspective and connection. A simulation-free
      theory-plus-worked-examples paper is squarely in scope. The
      cross-domain reach (reliability, genomics, privacy, ML weak
      supervision, clinical informatics) suits its broad readership.
  - rank: 2
    name: "Journal of the American Statistical Association (Theory & Methods)"
    rationale: >
      Strong fit if the paper leans into the general theorem as a
      methods contribution and adds a full-proofs appendix (closing the
      regime-B open step). T&M can absorb the longer derivations the
      conference-length siblings deferred. Slightly less natural than
      Statistical Science for an explicitly synthesis-framed paper.
  - rank: 3
    name: "Journal of the Royal Statistical Society Series B"
    rationale: >
      Methodology venue that values a clean general result with broad
      implication. Would require sharpening the general theorem into a
      headline methodological advance rather than a synthesis; the two
      seams (esp. the open regime-B step) may draw a harder line than at
      Statistical Science.
  - rank: 4
    name: "Biometrika"
    rationale: >
      Fits the CAR/likelihood/identifiability content and the biomedical
      anchors (phenotyping, genomics). Prefers compact, rigorous theory;
      the open regime-B step and the asymptotic weak-supervision caveat
      would need tightening for this audience.
  - rank: 5
    name: "Journal of Machine Learning Research"
    rationale: >
      Viable for the ML-leaning framing (weak supervision, differential
      privacy, the marginal-fit-is-not-unbiasedness diagnostic). JMLR
      tolerates synthesis/position work and has no page limit. Less
      natural than the statistics venues for the exponential-family /
      location-family core.
  - rank: 6
    name: "Annals of Statistics"
    aspirational: true
    rationale: >
      Aspirational only. Annals wants substantial new theory; this paper
      is a unification of existing results. Would need the regime-B open
      step closed and the rank/singleton results expanded to full,
      general proofs to even be in contention, and even then the
      synthesis framing cuts against the venue's preference.

venue_primary: "Statistical Science"
venue_strategy: >
  Submit to Statistical Science as a unifying methods/synthesis paper.
  Lead with the recurrence narrative (one idea, six fields, five names)
  and the explicit "what is new is the organization, not the math"
  statement. Keep the two seams visible: they demonstrate rigor rather
  than weakness for this venue. If Statistical Science declines on
  grounds of insufficient new theory, close the regime-B open step and
  expand the rank/singleton proofs, then redirect to JASA Theory &
  Methods with a full-proofs appendix.

# ============================================================================
# SIBLING PAPERS (cross-references; the source material)
# ============================================================================

siblings:
  - key: towell2026masked
    role: "Foundational theory; C1/C2/C3, the face-value likelihood, the augmented-candidate-set rank/identifiability theorem, Appendix A regularity. Source of thm:general-rank."
    doi: "10.5281/zenodo.18725577"
  - key: towell2026mdrelax
    role: "Sensitivity to C2 violations; robustness bands. Source for the 'what breaks when C2 fails' material."
    doi: "10.5281/zenodo.20414727"
  - key: towell2026scrnacoarsening
    role: "scRNA-seq dropout; cell-total consistency (regime A, ZINB); spike-ins as singletons; bias bound. The proof template the other consistency theorems cite."
    doi: "10.5281/zenodo.20414734"
  - key: towell2026spatialcoarsening
    role: "Spatial deconvolution; spot-level consistency (regime A, Poisson); single-cell-resolution probes as singletons; rank condition on P."
    doi: "10.5281/zenodo.20422883"
  - key: towell2026dpcoarsening
    role: "Differential privacy; release consistency (regime B, location-family score, NOT exponential family); non-private release as singleton; compositional calculus."
    doi: "10.5281/zenodo.20422885"
  - key: towell2026weaksupcoarsening
    role: "Weak supervision; agreement consistency (regime A under sufficiency-complete parametrization, asymptotic for naive-Bayes); gold labels as singletons; rank deficit r."
    doi: "10.5281/zenodo.20422888"
  - key: towell2026phenotypecoarsening
    role: "EHR phenotyping; code-frequency consistency (regime A, Bernoulli); chart review as singleton; Rogan-Gladen connection."
    doi: "10.5281/zenodo.20422890"

# ============================================================================
# THEOREMS / REDUCTION AUDIT (the honest core)
# ============================================================================

results:
  general_consistency:
    label: thm:general-consistency
    statement: "At an interior MLE of the face-value likelihood, m(theta_hat) = T_bar (fitted mean of the coarsening-sufficient statistic = empirical mean)."
    regime_A: "Regular exponential family. COMPLETE PROOF via log-partition gradient (mean-value identity) + full-column-rank natural-parameter Jacobian."
    regime_B: "Location family. PROOF WITH ONE OPEN STEP. Location-family score identity. Exact for the Gaussian kernel; population first-moment statement for a general symmetric kernel. Finite-sample arbitrary-kernel version is OPEN (rem:loc-sketch)."
  reduction_audit:
    - corollary: cor:scrna
      named: "cell-total consistency"
      regime: A
      status: "EXACT. ZINB observed-count law is a regular exponential family with mean-parameterized score."
    - corollary: cor:spatial
      named: "spot-level / cell-total consistency"
      regime: A
      status: "EXACT per coordinate (Poisson). Vector form additionally needs the joint rank condition (thm:general-rank)."
    - corollary: cor:phenotype
      named: "code-frequency consistency"
      regime: A
      status: "EXACT in the informative regime sens+spec > 1 (nonzero mean gradient)."
    - corollary: cor:weaksup
      named: "agreement consistency"
      regime: A
      status: "SEAM. Exact only when agreement indicators are sufficient statistics; ASYMPTOTIC (n^-1/2) for the naive-Bayes parametrization practitioners use."
    - corollary: cor:dp
      named: "release consistency"
      regime: B
      status: "SEAM. NOT recovered from regime A. Location-family first-moment identity; exact for the Gaussian kernel."
  rank_and_singleton:
    - "thm:general-rank: augmented-candidate-set full-column-rank condition. Unifies with NO seams (finite incidence matrix C-tilde; operator analogues P in spatial, A in DP linear query, agreement matrix in weak sup)."
    - "prop:singleton: a |c(r)|=1 report restores identifiability. Unifies with NO seams; six singleton devices (diagnostic resolution, ERCC spike-in, single-cell probe, non-private release, gold label, chart review) are literally singleton candidate sets."

honest_assessment: >
  The synthesis holds at the level of MLE-stationarity forcing the
  fitted mean of the coarsening-sufficient statistic to match its
  empirical mean. The rank condition and singleton device unify cleanly
  across all six domains. The consistency theorem is where the seams
  are: three domains (scRNA, spatial, phenotype) reduce exactly through
  the exponential-family regime; weak supervision reduces exactly only
  under a parametrization practitioners do not use and asymptotically
  otherwise; differential privacy does not live in the
  exponential-family regime at all and is recovered through a separate
  location-family branch whose general (kernel-arbitrary, finite-sample)
  proof has one open step. These seams are named in the paper, not
  hidden. No domain resists unification outright; DP is the one that
  required a second regime to absorb.

# ============================================================================
# BUILD STATUS (papermill:status)
# ============================================================================

build_status:
  main_pdf: "13 pages, clean build"
  undefined_count: 0
  label_changed_warning: "resolved after settling pass"
  em_dash_check: "PASS (no U+2014 in any source file)"
  vanity_count_check: "PASS (enumeration of corollaries only; no achievement-scale framing)"
  simulation: "n/a (synthesis paper, no new simulations by design)"

# ============================================================================
# STAGE TIMELINE
# ============================================================================

stage_timeline:
  - date: 2026-06-03
    event: "Scaffold v0.1: repo created mirroring dp-coarsening LaTeX setup; seven sections written; refs.bib with six sibling Zenodo DOIs + CAR lineage + domain anchors; build verified (13 pp, 0 undefined). Papermill init+thesis+outline+venue+status recorded."

# ============================================================================
# REVIEW HISTORY (papermill multi-agent editorial passes; append-only)
# ============================================================================

review_history:
  - date: 2026-06-03
    dir: ".papermill/reviews/2026-06-03"
    note: "Initial multi-agent review pass."
  - date: 2026-06-03
    dir: ".papermill/reviews/2026-06-03-rereview"
    note: "Re-review pass."
  - date: 2026-06-04
    dir: ".papermill/reviews/2026-06-04"
    note: "Multi-agent review pass."
  - date: 2026-06-08
    dir: ".papermill/reviews/2026-06-08"
    recommendation: minor-revision
    focus: "Post-MIL-fold-in integrity (cor:mil math, seven-domains/six-corollaries counts, regime-A classification)."
    findings: "Critical 0, Major 3, Minor 7, Suggestions 4."
    top_item: "cor:mil is classified as a clean regime-(A) exact reduction, but its identity M^T D^{-1}(Y - p_hat) = 0 is IRLS-weighted under a non-canonical noisy-OR link, not the unweighted m(theta_hat) = bar T the general theorem states; re-state regime (A) in score-equation form (collapsing to m=bar T for canonical links) so cor:mil is a true corollary, and mark the MIL row of tab:reduction as exact-but-weighted."
    other_major: "Stale count at consistency.tex:276 (the other four corollaries should be five; intro and discussion already say five). MUSK1/MUSK2 named in applications.tex with no citation to Dietterich et al. (1997); MIL is the only domain lacking an external anchor (sibling is URL-only). Build verified clean at 12 pages."
---

# State: coarsening-synthesis

## Stage: scaffold-v0.1

The flagship synthesis paper of the masked-data / coarsening-at-random
paper family. States the one consistency theorem, the one rank
condition, and the one singleton device that recur across six sibling
domains, and recovers each domain's named result as a corollary.

## Dashboard

- **Thesis**: recorded (one-theorem-across-domains unification). See
  `thesis` above.
- **Outline**: 7 sections, one-line purpose each. See `outline` above.
- **Venue**: primary **Statistical Science** (the synthesis/review
  venue); ranked shortlist of 6 with rationale. See `target_venues`.
- **Build**: `make paper` clean, 13 pages, 0 undefined references.
- **Proof status**: regime (A) of the general consistency theorem is a
  complete proof; regime (B) has one labeled open step (kernel-general
  finite-sample identity); the rank and singleton results are sketches
  citing `towell2026masked`.
- **Honesty**: two seams named (weak-supervision parametrization,
  differential-privacy location-family branch). See `honest_assessment`.

## Next action

Close or formally bound the regime-(B) open step (restrict to Gaussian
kernel, or replace the empirical mean with the kernel psi-location for
the arbitrary-kernel finite-sample case). Then expand the rank/singleton
sketches to full proofs if targeting a proofs-bearing venue, and run
`papermill:prior-art` to position against the broader CAR/unification
literature beyond the siblings.


# Venue analysis (2026-06-03)

Researched 2026-06-04 against live publisher/society pages (curl fetch, HTML
stripped). Sources are noted inline. Where a publisher CDN blocked automated
fetch (OUP, Taylor and Francis, Annual Reviews all returned HTTP 403), the
society page or a secondary source is cited and the item is flagged
"publisher-standard, not live-verified" rather than guessed. This pass
CONFIRMS Statistical Science as primary on scope grounds and, importantly,
overturns the earlier worry that it is invited-only: its manuscript-submission
page runs an open author-driven system (EJMS). It also DROPS JMLR entirely
(it refuses unsolicited surveys) and downgrades Annual Review of Statistics
(invited/commissioned only).

## Most important single fact

Statistical Science is NOT invited-only for this genre. Its stated central
purpose (imstat.org Statistical Science page, fetched 2026-06-04) is "to
convey the richness, breadth and unity of the field by presenting the full
range of contemporary statistical thought at a moderate technical level,
accessible to the wide community of practitioners, researchers and students of
statistics and probability." It runs an open Electronic Journal Management
System submission (e-publications.org/ims/submission), the cover letter must
state the paper is being submitted to STS, and authors "are encouraged to
suggest up to five suitable referees." There is no invited-only gate. The real
gate at STS is genre, not access: "A paper that follows the usual theory and
methods format and focuses on publishing a slew of new results is not suitable
for STS," but "the journal does allow technical results (and often publishes
such) provided they are placed in a larger review context." A cross-domain
unification with the math placed inside a review frame is squarely in scope.
Current editor: Lutz Dumbgen (2026-2028).

## Preprint-policy verdict (primary)

PASS for Statistical Science. The IMS "IMS Journals on arXiv" page
(imstat.org, fetched 2026-06-04) states plainly: "The IMS encourages all
members to post their articles on arXiv. Please be sure to check your copyright
transfer agreements before posting." STS is an IMS journal, so a paper already
public as a Zenodo preprint with a DOI is fine; the only obligation is the
standard prior-dissemination disclosure in the cover letter and respecting the
copyright-transfer terms at acceptance. A Zenodo DOI (not arXiv) is the same
class of prior public posting and is covered by the same policy. Action:
disclose the Zenodo concept DOI (10.5281/zenodo.20533912) in the cover letter
and cite it in the paper as the prior version. No hard preprint gate is
tripped at the primary or at either IMS backup.

## Format gap (primary: Statistical Science)

- Current draft: 16 pages, single-column, 11pt article class, 1in margins
  (main.tex, verified).
- STS requirement (STS Manuscript Preparation page, fetched 2026-06-04):
  "Manuscripts must be written in LaTeX using STS's template," which is the
  IMS imsart class (imsart.cls/imsart.sty, the same class Statistics Surveys
  documents on its preparation page). The template sets margins and font.
- Gap: a class swap from article to imsart, not a rewrite. imsart is a
  single-column journal class; expect the recompiled length to differ from the
  current 16 article-class pages (imsart typically runs a touch denser).
  No hard page cap applies to a regular STS article. The only explicit STS
  page cap is the 10-page bound on Short Communications, a separate track that
  does not apply here.
- Other STS structural notes: abstract present (have one), suggest up to five
  referees (prepare the list), cover letter naming STS as the target.
- Effort: low. One LaTeX class migration plus a referee list and cover letter.

## Ranked shortlist

### Primary: Statistical Science (IMS)
Best fit and access-clear. Scope explicitly prizes unity-of-the-field,
review-framed work at moderate technical level for a broad audience, which is
exactly this paper's genre (one idea, six fields, five names, stated once).
The "technical results inside a larger review context" clause licenses the
general consistency theorem and the rank/singleton apparatus precisely because
they are wrapped in a synthesis. Open unsolicited submission via EJMS,
IMS-wide arXiv/preprint encouragement covers the Zenodo prior posting, and the
cross-domain readership (reliability, genomics, privacy, weak supervision,
clinical informatics) matches STS's stated wide community. Risk: STS will
bounce anything that reads as plain theory-and-methods, so the framing must
lead with synthesis, not theorems. Format cost is a single imsart class swap.
(All facts: imstat.org STS pages + IMS arXiv page, fetched 2026-06-04.)

### Backup 1: Statistics Surveys (IMS, co-sponsored, open access)
The cleanest fallback and arguably co-primary. Its stated scope (imstat.org
Statistics Surveys page, fetched 2026-06-04): "Statistics Surveys publishes
survey articles in theoretical, computational, and applied statistics. The
style of articles may range from current research to graduate textbook
exposition. Articles may be broad or narrow in scope. The essential
requirements are a well specified topic and target audience, together with
clear exposition." A cross-domain synthesis of CAR-coarsening with worked
domain instances is a textbook fit for "survey article, broad scope, well
specified topic." Same imsart.cls template (its Preparation of Manuscripts
page documents imsart.cls/sty), same IMS arXiv/preprint encouragement (Zenodo
preprint fine), free open access. Lower selectivity-prestige than STS but a
higher genre-fit certainty: STS can reject on "too much new theory / not
enough review"; Statistics Surveys cannot, because survey IS the mandate. Use
this if STS declines on genre, or run it as the primary if certainty of fit
is valued over the STS imprimatur.

### Backup 2: JASA Theory and Methods (ASA, Taylor and Francis)
Viable if the paper is repositioned as a methods contribution (lead with the
general theorem and a full-proofs appendix that closes the regime-B open step)
rather than as a synthesis. JASA "covers work primarily focused on the
application of statistics, statistical theory and methods... also includes
reviews" (Wikipedia summary of JASA, fetched 2026-06-04; T and F author page
was 403-blocked). Two-section structure; Theory and Methods is the target.
Preprint: T and F / ASA permit prior preprints (publisher-standard for this
field; not live-verified because the T and F page blocked automated fetch, so
confirm on the submission portal). Weaker than STS/Statistics Surveys for an
explicitly synthesis-framed paper, and the open regime-B finite-sample step
would draw harder scrutiny here than in a review venue.

### Backup 3: JRSS-B, Statistical Methodology (RSS, OUP)
A reach for this paper as written. RSS society page (rss.org.uk Series B,
fetched 2026-06-04): Series B "publishes work at the leading edge of
methodological development, with a strong emphasis on relevance to statistical
practice," scope broad enough to embrace computational methods and
foundations, with a discussion-paper tradition. The bar is leading-edge new
methodology, not unification of existing results, so the paper would need to
be sharpened into a headline methodological advance and the two seams (esp.
the regime-B open step) closed. Preprint: OUP permits the original-submission
preprint (publisher-standard; OUP page 403-blocked, so not live-verified).
Keep as a stretch target only if the theorem is upgraded.

## Explicitly demoted / excluded

- JMLR: EXCLUDED. JMLR author page (jmlr.org/author-info.html, fetched
  2026-06-04) states: "JMLR occasionally publishes surveys by invitation from
  the editorial board; we do not consider unsolicited survey papers,"
  and separately "Currently, JMLR does not publish review articles." This
  paper is an unsolicited survey/synthesis, so JMLR is a hard no despite its
  preprint-friendliness and ML-adjacent content. Remove from the shortlist.
- Annual Review of Statistics and Its Application: EXCLUDED for direct
  submission. Annual Reviews articles are "usually peer-invited solicited
  submissions" with topics planned one to two years ahead by an editorial
  committee (Wikipedia, Annual Reviews publisher, fetched 2026-06-04; the
  Annual Reviews author/FAQ pages were 403-blocked). Editor: Nancy Reid. One
  may suggest a topic to the editorial committee but cannot submit unsolicited.
  Not a primary path; a topic suggestion is the only realistic move and is
  slow.
- Biometrika: not recommended for a synthesis. Its principal focus is
  theoretical statistics with "emphasis placed on papers containing original
  theoretical contributions" (Wikipedia Biometrika, fetched 2026-06-04; OUP
  Biometrika instructions 403-blocked). Wants original theory, not
  organization of existing theory.
- Annals of Statistics: aspirational only, unchanged from the prior pass.
  Editorial policy (imstat.org AOS Editorial Policy, fetched 2026-06-04):
  "aim to publish research papers of highest quality... Primary emphasis is
  placed on... theoretical advances... at the forefront of mathematical
  statistics." A unification of existing results is against the grain.

## Submission strategy (concrete)

1. Reformat for the primary: migrate main.tex from article 11pt to the IMS
   imsart class (imsart.cls/imsart.sty) used by STS and Statistics Surveys.
   This is a class swap, not a content edit; do it once and it serves both the
   primary and backup 1. Recheck length after recompile (no hard cap at STS;
   imsart may shift the 16-page figure).

2. Cover-letter angle (STS): lead with the synthesis, not the theorems. Open
   with the recurrence claim, one statistical identity surfacing under five
   different names across six fields, then state that the contribution is
   organization at the right generality, not new mathematics, and quote the
   paper's own "the claim is unification, not new mathematics" line. Tie this
   directly to the STS scope phrase "richness, breadth and unity of the field"
   and to the "technical results placed in a larger review context" clause.
   Disclose the Zenodo concept DOI (10.5281/zenodo.20533912) as prior public
   posting and confirm it is cited in the paper. Pre-empt the one objection
   the intro already answers (is this just the textbook score equation) by
   pointing the editor to that paragraph.

3. Suggested-reviewer guidance (STS encourages up to five): pick reviewers who
   each own one of the unified domains plus the CAR lineage, so the editor can
   triangulate the cross-domain claim. Cover the CAR/coarsening foundations
   (the Heitjan-Rubin / Gill-van der Laan-Robins ignorability tradition), one
   single-cell or spatial genomics methodologist, one differential-privacy
   statistician, one weak-supervision / data-programming researcher, and one
   reliability or missing-data theorist. Avoid anyone co-authored with the
   author. Spread across the domains is the point: a single-domain panel will
   undervalue a synthesis.

4. Reject-then-resubmit chain. Note the STS-specific hazard: the STS editorial
   policy explicitly says papers "previously submitted to such journals
   [theory-and-methods journals] and rejected should not be resubmitted to STS
   directly, since such papers are likely to be quickly rejected." Therefore
   do NOT route a JASA/JRSS-B/Biometrika rejection into STS afterward, that
   ordering is penalized. Submit STS FIRST while the paper is in synthesis
   form. Chain:
   - STS (synthesis framing, imsart) ->
   - if STS declines on genre or theory-depth: Statistics Surveys (same
     imsart file, reframed as a survey; genre fit is near-certain here) ->
   - in parallel or after, if a methods home is wanted instead: close the
     regime-B finite-sample open step (restrict to the Gaussian kernel or
     state the result via the kernel psi-location) and expand the
     rank/singleton sketches to full proofs, then submit to JASA Theory and
     Methods with a full-proofs appendix ->
   - JRSS-B only if the theorem is further sharpened into a leading-edge
     methodological headline.
   The synthesis-first ordering protects the STS option, which the
   theory-venue-first ordering would forfeit.

5. Pre-submission cleanup carried over from Next action: closing or formally
   bounding the regime-B open step strengthens every option and is required
   before JASA/JRSS-B; it is optional but helpful for STS and Statistics
   Surveys, where the located boundary already reads as rigor rather than a
   gap.

## Verdict on the preliminary pick

CONFIRMED, with a sharpened access finding and a strong co-primary added. The
earlier worry that Statistical Science is invited-only does not hold: STS takes
unsolicited submissions through EJMS, so it remains the primary. The one change
is to elevate Statistics Surveys to backup 1 (near-certain genre fit, same
template, same preprint policy) as the safety net if STS bounces on genre, and
to drop JMLR and Annual Review of Statistics from the viable-direct-submission
list for the reasons above.

# Review log: 2026-06-08 (multi-agent editorial pass)

Recommendation: **minor-revision**. Build verified clean: `make paper` exit 0,
12 pages, 0 substantive undefined refs, 0 undefined citations, 0 BibTeX
warnings, no em-dashes. (The Dashboard/build_status above are the point-in-time
scaffold-v0.1 snapshot and say 13 pages; current build is 12. Snapshots left
intact per the append-only convention.)

Focus of this pass was the just-folded-in sixth corollary (cor:mil, multiple
instance learning) and the seven-domains/six-corollaries accounting.

Findings: Critical 0, Major 3, Minor 7, Suggestions 4. Full report and
per-specialist files in `.papermill/reviews/2026-06-08/` (review.md plus
logic-checker, methodology-auditor, novelty-assessor, prose-auditor,
citation-verifier, format-validator, literature-context).

Single most-important remaining item: cor:mil is presented as a clean
regime-(A) exact reduction, but the identity it derives, M^T D^{-1}(Y - p_hat)
= 0, is IRLS-weighted under the non-canonical noisy-OR link, not the unweighted
m(theta_hat) = bar T that thm:general-consistency states; re-state regime (A)
in score-equation form so it collapses to m=bar T for canonical-link members
(scrna, phenotype, spatial-Poisson) and carries the D^{-1} weight for MIL,
making cor:mil a true corollary, and mark the MIL row of tab:reduction as
exact-but-IRLS-weighted. Other majors: fix the stale count
'the other four corollaries' -> 'five' at consistency.tex:276 (intro and
discussion already say five); cite Dietterich et al. (1997) where MUSK1/MUSK2
is named.
