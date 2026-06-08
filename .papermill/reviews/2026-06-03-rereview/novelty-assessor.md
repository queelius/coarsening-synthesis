# Novelty Assessor Report (re-review)

Date: 2026-06-03
Confidence: HIGH for the internal framing assessment; MEDIUM for absolute
prior-art (no live search; see literature-context.md).

## The three framing fixes from the prior review landed

The prior review raised three framing items (M1, M2, M3). All three are
now addressed in the source.

### M1 (RESOLVED): the exponential-family-moment-matching objection is now answered

The introduction adds a dedicated rebuttal paragraph (introduction.tex
l.119-139) that names the objection verbatim ("in its exponential-family
regime the consistency identity is the textbook score equation sum T(R_i)
= n E[T] at the MLE, so is the contribution merely that several papers
reused an elementary fact?") and answers it with three reasons: (i) the
content is what the COARSENING does to the identity (observed marginal is
an exponential family while the bias lives in the LATENT parameter, the
diagnostic moral), (ii) the singleton/rank half is not elementary moment-
matching, (iii) the discovery that DP forces a structurally distinct
location-family regime with a located boundary is itself a result about
the reach of the principle. This is exactly the defense the prior review
said existed in pieces but was never assembled. It is now assembled and
well placed. The easiest rejection is converted into a stated strength.

### M2 (RESOLVED): the seam table is now a reach map, not a failure ledger

tab:reduction (consistency.tex l.259-284) is recaptioned "How far
Theorem reaches in each domain," has a glyph "Reach" column (filled
circle = exact via regime A, open circle = exact under the right
parametrization / asymptotic otherwise, triangle = location-family
single-release), and a legend that reads "The boundary is located
precisely rather than asserted." The "caveats / recorded honestly /
what does not fit" language is gone. The lead-in sentence (l.251-257)
frames it as "the demonstrated reach ... not a list of apologies." The
connotation has flipped from apology to mastery, which is precisely what
Statistical Science rewards. This was the highest-value, lowest-effort
fix and it was executed well.

### M3 (RESOLVED): the seam-free singleton/rank half now leads

The abstract (main.tex l.78-85) now opens the two-results contrast with
"The first is seam-free across all six domains: an augmented-candidate-set
rank condition ... and a singleton candidate set ... restores
identifiability," BEFORE introducing the seamed consistency identity. The
introduction's contribution list (introduction.tex l.76-83) likewise
gives the identifiability result as item (ii) and explicitly labels it
"the seam-free half of the synthesis ... This half carries no caveats and
is not reducible to a textbook identity." The paper now leads with its
robust half. RESOLVED.

## Novelty verdict (unchanged in substance, strengthened in presentation)

The unification is real and the novelty-as-organization framing is
correct and now well defended. Three independent novelty pillars:

1. The recurrence itself: one MLE-stationarity identity under five names
   across five domains, plus one rank/singleton apparatus across six. No
   prior work unifies these specific domains under CAR (see
   literature-context.md). SAFE.
2. The singleton/rank half is genuinely non-trivial and seam-free, and is
   now correctly billed as the stronger claim. This is the part least
   vulnerable to a "textbook" dismissal.
3. The DP-forces-regime-(B) discovery, now with a fully characterized
   boundary (Gaussian-iff), is a real result about the limits of the
   principle, not a restatement. The revision turned this from a liability
   (an open step) into an asset (a sharp characterization).

## Residual novelty/framing items

1. MINOR (carried, partially open): the 5-consistency-vs-6-singleton
   asymmetry. Reliability supplies the framework and the singleton/rank
   apparatus but contributes no named consistency theorem (it has five
   named consistency theorems across the OTHER domains but six singleton
   devices including reliability). The abstract and intro now both list
   six domains; a single clause explaining why reliability is the
   framework source rather than a sixth named consistency theorem would
   remove a reader stumble. Low effort.
2. SUGGESTION: a one-sentence acknowledgment of the broader measurement-
   error / misclassification-correction umbrella (Rogan-Gladen is itself a
   special case of it) would situate the synthesis among kindred
   unifications and preempt a referee asking "how does this relate to
   measurement-error correction." See literature-context.md.

No critical or major novelty issues. The three framing risks the prior
review flagged are resolved. The contribution reads, after revision, as a
controlled and well-defended unification.
