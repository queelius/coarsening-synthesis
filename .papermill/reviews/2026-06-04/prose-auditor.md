# Prose Auditor Report

Date: 2026-06-04 (final pre-submission pass)
Priority: did the six minors or the imsart reformat introduce prose damage,
notation drift, or narrative breaks? Confidence: HIGH (checked against
source, build, and rendered PDF).

## Reformat: no prose damage

The article-to-imsart migration is format-only. The abstract block is
byte-identical between main.tex and main.tex.article-bak (verified by diff);
the section inputs are unchanged since the re-review date. The only frontmatter
additions are imsart-required (`\runtitle`, `\runauthor`, `\begin{aug}`
author markup, ORCID via `\orcid`), which are markup, not prose. The title
text is identical. No narrative or sentence-level change.

## The six minors: prose quality

- Teicher/Kagan-Linnik-Rao insertion (consistency.tex rem:loc-sketch
  l.119-133): the new sentences read cleanly and in voice. "The sample-mean
  form mu(theta_hat) = Rbar is exactly characterized [teicher1961maximum]:
  the location MLE equals the arithmetic sample mean for every sample if and
  only if the kernel is Gaussian" is crisp. The follow-on "The classical face
  of this is Gauss's characterization ... made precise as the
  maximum-likelihood characterization of the normal by [teicher1961maximum]
  and placed in the broader characterization theory of [kagan1973...]" is
  well constructed and attributes correctly without overloading. Good.
- phenotype 3-to-1 (cor:phenotype l.206-210): the added clause "the 3 -> 1
  collapse is exactly why the chart-review singleton ... is needed to recover
  the individual parameters" is a clean motivational bridge to the
  identifiability section. Reads naturally.
- censoring rider relocation: the new rem:rank-instantiation
  (identifiability.tex l.36-48) is well written and correctly frames the
  domain support conditions as "instantiation details of one rank condition,
  not separate hypotheses of the general theorem." The theorem body now reads
  as a clean general statement. Improvement.
- 5-vs-6 clause (introduction.tex l.107-113): the inserted explanation is
  slightly long (a single sentence running several lines) but clear and not
  awkward. Acceptable.
- bib removal and metadata: no prose effect.

## Notation consistency

Consistent. The regime-(B) symbols (psi=-p_0'/p_0, mu_hat, the psi-location,
V, J) are used uniformly across the theorem, proof, remark, sec:css, and
discussion. m(theta) and mu(theta) coincidence in regime (B) is stated where
needed (proof l.92-93, sec:css). T, R, c(r), tilde-C are consistent. The
cleveref output renders results in lowercase ("theorem 1", "corollary 1") per
imsart's crefname convention, which is consistent throughout the rendered
PDF (verified).

## Narrative arc

Intact and strong. Six fields -> one framework -> one consistency theorem
(two regimes) -> five corollaries (three clean, two seamed) -> one rank +
singleton device (seam-free) -> domains as instances -> what the unification
buys and where it is seamed. The abstract leads with the seam-free half, the
reach-map reads as control rather than apology, and the conclusion restates
the result with the boundary located. No break introduced by the edits.

## Residual prose items (all MINOR/SUGGESTION, mostly carried)

1. (MINOR, carried) Stray `c_i` in the reliability applications subsection
   (applications.tex l.13-14, "candidate set c_i of suspect components")
   where the rest of the paper uses c(r). Cosmetic; the reliability sibling
   uses c_i natively, so this reads as a deliberate nod, but for one-paper
   uniformity it could be c(r) or footnoted. Severity MINOR.
2. (MINOR, carried) The marginal-fit-is-not-unbiasedness moral appears in
   both consistency.tex (l.152-158) and discussion.tex (l.16-24). The two are
   now differentiated enough (one states it as the corollary's moral, the
   other as a discussion theme) to read as deliberate emphasis rather than
   accidental duplication. Borderline; leave or have one reference the other.
3. (MINOR) Abstract is 322 words. Statistical Science does not impose a hard
   abstract cap, so this is acceptable, but if trimmed toward ~250 the lead
   would sharpen. Optional.

No critical or major prose defects. The edits and the reformat introduced no
writing damage; the manuscript reads as a polished synthesis.
