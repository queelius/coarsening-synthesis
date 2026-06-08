# Prose Auditor Report

**Paper**: One consistency theorem for coarsened-data maximum likelihood
**Date**: 2026-06-08
**Focus**: writing quality, narrative arc, notation consistency, with attention
to whether the MIL fold-in reads as a native part of the prose or a bolt-on.

## Summary

The writing is strong: confident, precise, well-paced, with a clear narrative
arc (one problem across fields -> one framework -> one consistency theorem in
two regimes -> corollaries -> one rank/singleton device -> what the unification
buys and where it is seamed). The register is exactly right for a synthesis. The
MIL integration is mostly seamless at the prose level, but it left two notation
slips and inherited the count slip the logic-checker flagged. The chief
stylistic risk is sentence length: several sentences run very long with stacked
appositives, which a Statistical Science copyeditor will want trimmed.

## Findings

### [MINOR] Notation: bag-composition vector is m_b in one place, m_i in another
**Location**: tab:css (framework.tex:140) vs cor:mil (consistency.tex:217).
**Quoted text (framework)**: "$1 - \exp(-\bm m_b^\top \bm s)$".
**Quoted text (consistency)**: "$\hat p_i = 1 - \exp(-\bm m_i^\top \hat{\bm
s})$".
**Problem**: the same bag-composition row vector is subscripted b in tab:css and
i in cor:mil. A reader matching the table to the corollary has to infer they are
the same object. Trivial but exactly the kind of inconsistency a fresh-domain
fold-in produces.
**Suggestion**: pick one subscript (i is used elsewhere for the generic unit;
use m_i in both, or b in both consistently with "bag").

### [MINOR] Symbol overload: M is the DP release scalar and the MIL composition matrix in the same section
**Location**: consistency.tex. cor:dp uses "the additive-noise release $M = q(D)
+ Z$" (consistency.tex:259) and tab:css row "The release $M = R$ itself"
(framework.tex:131); cor:mil uses "$M^\top D^{-1}(\bm Y - \hat{\bm p}) = \bm 0$,
with $M$ the composition matrix" (consistency.tex:220-221).
**Problem**: within one section the capital M denotes both a scalar random
release (DP) and a fixed composition matrix (MIL), in adjacent corollaries.
Lowercase m(theta) is also in play as the implied mean, and bold m_i as the bag
row. The case/boldface partly disambiguate, but M-scalar vs M-matrix is a real
collision. Context resolves it, but a careful reader will pause.
**Suggestion**: rename the MIL composition matrix (e.g., to B for "bag
composition," or keep M but rename the DP release to A or use only "the release"
in prose without the symbol where possible). Even a footnote acknowledging the
local reuse would help. Low effort, removes a genuine reading speed bump.

### [MINOR, prose echo of the logic MAJOR] "the other four corollaries" reads wrong against the prose elsewhere
**Location**: consistency.tex:276.
**Quoted text**: "the exponential-family mean-value identity that serves the
other four corollaries."
**Problem**: purely as prose, this sentence contradicts introduction.tex:126
("the other five domains") and discussion.tex:42 ("The other five consistency
theorems"). A reader who has read the intro arrives at this line and trips.
**Suggestion**: "five corollaries" (substantive fix owned by logic-checker;
noted here because it is a prose-consistency break a reader will catch).

### [SUGGESTION] Long stacked-appositive sentences
**Location**: e.g., main.tex:117-128 (abstract, the "Its boundary is the more
nuanced part..." sentence and the following), introduction.tex:111-117 (the
"The count is seven domains but six named consistency corollaries: reliability
... is the source ... so it appears among the seven domains and contributes a
singleton device ... which is why the consistency corollaries number six"
sentence), consistency.tex:282-288 (the tab:reduction lead-in "A unification
whose boundary is located exactly, here is where it is an exact finite-sample
identity, here a per-coordinate one, here an $n = 1$ identity, here an asymptotic
one, is stronger...").
**Problem**: these sentences are correct and even elegant, but they stack three
or more appositive clauses and run long enough that the main verb is hard to
locate on first read. Statistical Science prose tends to be cleaner.
**Suggestion**: split the worst offenders into two sentences each. The
introduction.tex:111-117 "count" sentence in particular would read better as a
short claim ("Seven domains, six named consistency corollaries.") followed by the
one-sentence reason.

### [SUGGESTION] The "not a list of apologies" / "not a list of apologies" defensiveness
**Location**: consistency.tex:286-288 ("the map below is the demonstrated reach
... not a list of apologies"); discussion.tex:36 ("located exactly, not
asserted").
**Problem**: the paper several times preempts the reader's skepticism about the
seams by insisting the boundary is a strength ("not a list of apologies,"
"demonstrated reach," "rigor rather than weakness"). Once is persuasive; the
repetition can read as protesting too much. For the synthesis venue the seams
genuinely are a strength and need less defending.
**Suggestion**: keep the strongest single statement (the tab:reduction lead-in)
and soften or cut the repeated reassurances.

## What is strong (for the record)
- The opening litany (introduction.tex:4-15: failed component, transcript count,
  spot of tissue, sensitive statistic, label, billing code) is an excellent
  hook and lands the "same object, different vocabulary" thesis immediately.
- The costume metaphor ("the singleton wears a different costume in each field")
  is used consistently and aids retention without becoming twee.
- Section-to-section transitions are clean; each section opens by stating what it
  does in one sentence.
- No em-dashes (U+2014) anywhere in source; the convention is respected.
- The MIL material in applications.tex:93-109 and discussion.tex:102-108 reads as
  a native part of the paper, not a bolt-on, apart from the notation slips above.
