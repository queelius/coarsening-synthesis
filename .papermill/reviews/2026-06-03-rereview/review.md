# Multi-Agent Re-Review Report

Date: 2026-06-03 (re-review of a materially revised manuscript)
Paper: One consistency theorem for coarsened-data maximum likelihood: a
cross-domain synthesis of the coarsening-at-random framework
Target venue: Statistical Science (primary); JASA T&M, JRSS-B (backups)
Recommendation: minor-revision (one short citation away from ready)

Orchestration note: the Task fan-out tool is unavailable in this
environment (confirmed by direct probe; consistent with the prior review's
note that this orchestrator cannot spawn subagents). All eight specialist
lenses were executed inline by the area chair in a single context, with
every finding checked against the manuscript source, the build, and the
settled-result provenance in .research/. Build, formula spot-checks, grep-
based consistency hunt, and sibling cross-references are HIGH confidence.
Absolute prior-art is MEDIUM (no live web search); a live papermill:prior-
art pass remains advisable but the field position is stable.

## Headline answer to the brief

Does any section still assert the OLD false finite-sample-exact location
claim, or an over-general DP claim? NO. Verified by a full grep-based hunt
plus section-by-section reading. Every "exact finite-sample" assertion is
correctly scoped to regime (A) (exponential family) or to the n=1 single-
report case. No section claims the location-family sample-mean identity is
finite-sample exact for general kernels. No section claims DP release-
consistency generalizes beyond n=1. The correction is integrated
consistently across the abstract, introduction, consistency.tex (theorem,
proof, remark, corollaries, reach-map table), framework.tex sec:css,
applications.tex, discussion.tex, and conclusion.tex.

All three of the prior review's framing items are also resolved: M1 (the
exponential-family-moment-matching rebuttal, now introduction.tex
l.119-139), M2 (the reach-map reframe with glyph column, now tab:reduction
consistency.tex l.259-284), M3 (abstract/intro reordered to lead with the
seam-free singleton/rank result, now main.tex l.78-85). The prior review's
one methodology defect (the regime-(B) over-claim in sec:css) is fixed.

## Summary

Overall Assessment: The revision landed cleanly. The single correction
that motivated this re-review (regime (B): exact at n=1, population first-
moment for any n, n^{-1/2} for finite n>1, not exact for n>=3 unless
Gaussian, log-concave regularity, DP pinned to n=1) is now stated
correctly in the theorem and propagated consistently to every section that
touches it. The boundary that was an open step in the prior draft is now a
fully characterized result (Gaussian-iff via Cauchy's functional equation),
with verified counterexamples in the provenance. The clean corollaries
(scRNA cell-total, phenotype code-frequency, spatial spot-level per
coordinate) still follow exactly after the restructure. The reach map reads
as control, not apology. The paper is submission-grade for Statistical
Science; the only substantive remaining item is a single missing classical
citation that the revision itself created by promoting the Gauss
characterization from an open step to a stated result.

Strengths:
1. The regime-(B) correction is internally consistent across all sections;
   no surviving old/false claim (logic-checker, full consistency hunt).
2. The regime-(B) boundary is now a sharp characterized result with
   verified provenance (the Laplace n=3 counterexample runs and confirms
   median 1 vs mean 2, exact gap -1; logistic and kernel-battery
   counterexamples documented), turning a former liability into an asset
   (logic-checker, methodology-auditor).
3. The seam-free singleton/rank unification remains correct and is now
   correctly billed as the stronger, less attackable claim (novelty-
   assessor, prop:singleton + tab:singletons).
4. The exponential-family-moment-matching objection is now named and
   answered in a dedicated paragraph, converting the easiest rejection
   into a stated strength (novelty-assessor).
5. The reach map (glyph column, "boundary located precisely rather than
   asserted" legend) reads as mastery of the boundary (prose-auditor,
   novelty-assessor).
6. Build is production-clean: exit 0, 15 pages, 0 undefined refs, 0 bibtex
   warnings, 28 labels resolve, conventions pass (format-validator).

Weaknesses:
1. The Gauss-characterization classical result, now load-bearing in regime
   (B), is stated without a primary citation (citation-verifier). NEW this
   pass; the single most important remaining item.
2. Two carried minor items unaddressed since the prior review: the unused
   dwork2006calibrating entry, and two bib-metadata malformations
   (citation-verifier, format-validator).
3. Two carried minor presentation items: the 5-consistency-vs-6-singleton
   asymmetry needs one clause (novelty-assessor), and thm:general-rank(b)
   still carries a reliability-specific censoring rider inside a "general"
   statement (logic-checker).

Finding Counts: Critical: 0 | Major: 0 | Minor: 6 | Suggestions: 3

## Critical Issues

None.

## Major Issues

None. The prior review's three major framing issues (M1, M2, M3) are all
resolved, and the regime-(B) correction is integrated consistently. No new
major issue was introduced by the revision.

## Minor Issues

### m1. The Gauss characterization is now load-bearing but uncited (source: citation-verifier; the top remaining item)
- Location: consistency.tex l.119-129 (rem:loc-sketch), discussion.tex
  l.47-50, conclusion.tex l.31-33.
- Quoted text: "The classical face of this is Gauss's characterization of
  the normal law as the unique location family whose most probable value is
  the arithmetic mean." (consistency.tex l.128-129)
- Problem: the revision promoted "the location MLE equals the arithmetic
  sample mean for every sample iff Gaussian" from an open step to a stated
  result that now carries regime (B). It is stated without a primary
  citation. For Statistical Science this is a known fact, but it should be
  attributed; for the proofs-bearing backups (JASA T&M, Biometrika) an
  uncited classical characterization invites a referee note.
- Suggestion: cite Teicher (1961, Ann. Math. Statist. 32, "Maximum
  likelihood characterization of distributions") or Kagan-Linnik-Rao
  (1973, Characterization Problems in Mathematical Statistics), optionally
  Gauss (1809, Theoria Motus) for the origin. One line in refs.bib and one
  \citep in rem:loc-sketch.
- Cross-verified: yes, against the manuscript text directly.

### m2. cor:phenotype reparametrization not fully explicit (source: logic-checker)
- Location: consistency.tex cor:phenotype (l.189-203).
- Problem: the corollary names the code frequency q as the natural mean
  parameter (correct) but does not spell out that the three parameters
  (pi, sens, spec) collapse to the one-dimensional q, which is exactly why
  the chart-review singleton is needed for identifiability. Making the
  3->1 collapse explicit links consistency to the identifiability section.
- Suggestion: one clause noting q is a single function of three parameters,
  so consistency pins q but not the triple, motivating the singleton.

### m3. thm:general-rank carries a domain-specific rider in a general statement (source: logic-checker; carried from prior review)
- Location: identifiability.tex thm:general-rank(b) (l.31-34).
- Quoted text: "(and, in the time-to-event instance, the mechanism assigns
  positive probability to both exact and censored reports)".
- Problem: a reliability-specific censoring condition sits inside a theorem
  the prose calls seamless. Small seam in the seam-free half.
- Suggestion: abstract it or move to a remark.

### m4. The 5-vs-6 asymmetry (source: novelty-assessor; carried)
- Location: introduction.tex / abstract (six domains listed) vs five named
  consistency theorems.
- Problem: reliability supplies the framework and the singleton/rank
  apparatus but contributes no named consistency theorem; a reader may
  stumble on "six domains, five names."
- Suggestion: one clause stating reliability is the framework source.

### m5. Unused bibliography entry (source: citation-verifier, format-validator; carried)
- Location: refs.bib dwork2006calibrating (cited 0 times).
- Suggestion: cite in the DP subsection (natural reference for calibrated
  noise / the Laplace mechanism that regime (B) is about) or remove.

### m6. Bib-metadata malformations (source: citation-verifier; carried)
- Location: refs.bib. tsiatis2006semiparametric is a @book with a journal
  field (use series=); gill1997coarsening is a @article for a proceedings
  volume (better as @incollection with booktitle=).
- Suggestion: cosmetic; fix for cleanliness.

## Suggestions

1. One global sentence making the delegated empirical base visible at a
   glance (each named identity is confirmed in its sibling: three exactly,
   weak-sup at the predicted n^{-1/2} rate, DP for the single release /
   Gaussian kernel) (methodology-auditor).
2. Add an M-estimation anchor (Huber 1964) at first use of psi in regime
   (B); van der Vaart already carries the asymptotics, so this is optional
   (citation-verifier).
3. One-sentence acknowledgment of the broader measurement-error /
   misclassification-correction umbrella (Rogan-Gladen is a special case)
   to situate the synthesis among kindred unifications (novelty-assessor,
   literature-context).

## Detailed Notes by Domain

### Logic and Proofs (logic-checker)
Internal-consistency hunt is the priority and the result is clean: no
section asserts the old finite-sample-exact location claim and none over-
generalizes DP past n=1. A section-by-section agreement table (abstract,
intro, theorem, proof, remark, corollaries, reach-map, sec:css,
applications, discussion, conclusion) shows uniform agreement on the
corrected regime-(B) statement, the n=1 DP pinning, and the symmetric/log-
concave regularity. The n=2 boundary is handled correctly (genuine-failure
threshold stated as n>=3). Regime-(A) proof re-derived and correct. The
three clean corollaries still follow exactly. The settled math was spot-
checked against the .research provenance (Laplace n=3 script run). Residual
items are two minors (cor:phenotype reparametrization explicitness;
thm:general-rank censoring rider), both pre-existing. No critical or major
logic error.

### Novelty and Contribution (novelty-assessor)
All three prior framing fixes (M1 rebuttal, M2 reach map, M3 abstract
reorder) landed and are well executed. The unification is real, the
novelty-as-organization framing is correct and now well defended, and the
DP-forces-regime-(B) discovery is now an asset (sharp boundary) rather than
a liability (open step). One carried minor (5-vs-6 asymmetry) and one
suggestion (measurement-error umbrella).

### Methodology (methodology-auditor)
The synthesis method is sound and the empirical delegation is legitimate
for the venue. The prior review's regime-(B) definition over-claim in
sec:css is fixed (the definition is now split by regime and is correct).
The two-regime partition is correctly argued as non-nested. The boundary is
a rigorous characterized result with verified provenance. Build fully
reproducible. One suggestion (global empirical-validation sentence).

### Writing and Presentation (prose-auditor)
The revision reads cleanly and introduced no prose damage; the restructured
abstract and the reach-map recaption are well written and in voice.
Notation is consistent, including the regime-(B) symbols where the revision
concentrated. Residuals are minor and largely predate the revision (one
stray c_i in the reliability subsection; the diagnostic moral stated in two
places, now differentiated enough to read as deliberate; abstract on the
long side at 322 words). Conventions pass.

### Citations and References (citation-verifier)
Internal integrity perfect (0 undefined). The revision orphaned no
reference. The one NEW item is the missing Gauss-characterization primary
citation now that the characterization is load-bearing (top remaining
item). Carried items: unused dwork2006, two bib-metadata fixes, optional
M-estimation anchor. CAR backbone and domain anchors complete.

### Formatting and Production (format-validator)
Build exit 0, 15 pages, 0 undefined refs, 0 bibtex warnings, all labels
resolve, 0 "??". The glyph column renders correctly and added no warnings.
Conventions pass. Generic article class is submittable; page count now
comfortable for the venue. Two carried cosmetic bib items; no build-blocker.

## Literature Context Summary
The paper sits in the CAR / missing-data-ignorability tradition and anchors
it correctly. No prior work unifies these specific six domains under CAR,
so the novelty-as-organization claim stands. The kindred umbrellas
(measurement-error correction, latent-class crowdsourcing, semiparametric
missing-data theory) do not subsume the claim. The clearest scholarly
addition the literature suggests is the Gauss-characterization primary
citation; an M-estimation anchor and a measurement-error umbrella
acknowledgment are optional. (Live prior-art pass still advisable.)

## Review Metadata
- Agents used (inline, single-context, Task fan-out unavailable):
  literature-scout-broad, literature-scout-targeted (merged into
  literature-context.md), logic-checker, novelty-assessor,
  methodology-auditor, prose-auditor, citation-verifier, format-validator.
- Cross-verifications performed: the consistency hunt itself is the
  cross-cut (logic-checker findings checked against citation-verifier on
  the new citation gap and against methodology-auditor on the sec:css fix);
  all converged.
- Disagreements noted: 0.
- Verified directly by area chair: full build (exit 0, 15 pp, 0 undefined),
  grep-based consistency hunt over all sections, the Laplace n=3
  counterexample script, all three framing fixes against source, the
  corrected regime-(B) statement in every section, all quoted text against
  the manuscript.
