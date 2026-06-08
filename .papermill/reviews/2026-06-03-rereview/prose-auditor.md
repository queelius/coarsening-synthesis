# Prose Auditor Report (re-review)

Date: 2026-06-03
Confidence: HIGH (read all seven sections and the abstract directly).

## Did the revision read cleanly, and did it introduce prose damage?

Yes to the first, mostly no to the second. The restructured abstract,
the new intro rebuttal paragraph, the reach-map recaption, and the
corrected regime-(B) prose are all well written and consistent in voice
with the rest of the paper. The prose is confident, precise, and
venue-suited. The narrative arc is intact and arguably improved: leading
the abstract with the seam-free result is a stronger opening.

## Notation consistency

The synthesis successfully reconciles symbols across domains that natively
use different notation (the load-bearing virtue of a real synthesis). I
checked the regime-(B) symbols specifically, since that is where the
revision concentrated: T(R)=R, mu(theta), psi = -p0'/p0, the sample
psi-location hat-mu, the kernel p0, the convolution density p_conv, and
m(theta)=E_theta[T]. These are used consistently in framework.tex sec:css,
the theorem, the proof, rem:loc-sketch, and cor:dp. The relation
m(theta)=mu(theta) in regime (B) (because E[Z]=0 for the symmetric kernel)
is stated where it is used (consistency.tex l.92-93). Good.

## The reach map reads well

tab:reduction now has a glyph column and a legend; the visual
"three exact, one parametrization-dependent, one single-release" lands at
a glance. The caption and lead-in prose are calibrated to "demonstrated
reach, not apologies." This is exactly the tonal correction the prior
review recommended, and the prose executes it cleanly.

## Residual prose items (mostly carried from the prior review)

1. MINOR (carried, check if still present): the marginal-fit-is-not-
   unbiasedness moral appears in consistency.tex (l.148-154, the closing
   paragraph of the theorem subsection) and again in discussion.tex
   (l.16-24, "a shared diagnostic moral"). The two statements are now
   differentiated enough that the repetition reads as deliberate
   reinforcement rather than accidental duplication (the consistency.tex
   instance states the moral, the discussion.tex instance frames it as a
   property of coarsened-data MLE in general). Acceptable as is; if
   trimming for length, have one reference the other. Severity MINOR,
   borderline cosmetic.
2. MINOR (carried): applications.tex reliability subsection uses c_i for
   the candidate set (l.13-15) while the rest of the paper uses c(r) /
   c(R) (framework.tex eq:fw-candidate). One stray notation. Trivial fix.
3. MINOR: the n=1 vs n>1 vs n>=3 boundary is stated correctly but appears
   in several places (theorem, remark, discussion). The phrasing is
   consistent and each occurrence earns its place (theorem states it,
   remark explains the mechanism, discussion situates it), so this is not
   redundancy to cut, but a careful reader should confirm the three
   thresholds stay aligned in any future edit. No action now.
4. SUGGESTION: abstract is 322 words. Statistical Science does not impose a
   hard abstract limit, but 322 is on the long side; if trimming, the
   regime-(B) sentence (l.97-104) is precise and should stay, while the
   final empirical-weight sentence could shorten. Low priority.

## Convention check

No em-dash (U+2014) anywhere in the source (verified). No vanity counts
(the enumerations are of corollaries and contributions, not achievement
framing). Conventions pass.

No critical or major prose issues. The revision is well written and did
not introduce new prose problems; the residuals are minor and largely
predate the revision.
