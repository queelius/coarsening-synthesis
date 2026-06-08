# Prose Auditor Report

Date: 2026-06-03
Focus per area chair: narrative arc, prose quality, NOTATION CONSISTENCY across
synthesized domains, and whether the seam table reads as a credibility strength
or a list of failures.

## Verdict summary
- Narrative arc: STRONG. The "six fields, same problem -> state it once ->
  corollaries -> what it buys / where seamed" arc is clear and well-paced.
- Prose quality: high. Confident, economical, suited to Statistical Science.
- Notation: CONSISTENT and well-reconciled across domains. The synthesis
  successfully unifies the siblings' divergent symbols. One residual.
- Seam table (tab:reduction): currently reads MORE as a list of caveats than as
  a credibility instrument. This is the highest-value prose fix and is
  addressed in detail below.

## 1. Narrative arc

The opening (introduction.tex) is excellent: six one-sentence vignettes (failed
component, dropout, tissue spot, noised statistic, vote, billing code) that
collapse to "the statistical object is the same." This is the right hook for a
broad-readership venue and it lands. The arc then proceeds cleanly: framework
(state once) -> consistency theorem + corollaries -> identifiability
(rank/singleton) -> applications tour -> discussion (buys/seams) -> conclusion.

The conclusion's "six fields that do not cite one another" is a strong closer
that re-states the thesis without mere repetition.

One structural observation: the abstract leads with the consistency theorem and
treats the singleton/rank result as secondary ("the companion structural
results recur in the same way"). Per the novelty-assessor, the singleton result
is the stronger, seam-free half; consider rebalancing the abstract so the
seam-free unification is not subordinated to the seamed one. This is a framing
call shared with novelty-assessor.

## 2. Notation consistency across domains (the load-bearing check)

The siblings use different notation (scRNA: mu_j, pi_j; spatial: P_sk, mu_jk;
DP: M, q(D), Z; weak sup: lambda_j, A_jk; phenotype: pi, sens, spec). The
synthesis reconciles these into one system:
- Latent variable: Y (macro \Y) uniformly. Verified: 9 uses, consistent.
- Coarsening-sufficient statistic: T (macro \T), Tbar for empirical mean.
  Verified: 30 uses of \T, 7 of \bar\T, all consistent. No stray T vs t.
- Candidate set: c(r). Verified: 9 uses of c(r), 2 of c(R...), 1 stray c_i.
- Report: R in the abstract framework; M reserved for the DP release; both used
  deliberately and consistently (M is introduced as "the release M = R").
- Implied mean: m(theta) = E_theta[T]. Consistent throughout.

The per-domain symbols (mu_j, P_sk, sens, spec, lambda_j) appear ONLY inside
the relevant corollary/subsection, mapped back to the general T/m(theta) via
tab:css. This is exactly right: the synthesis keeps one global system and
localizes each domain's native notation under the umbrella. The reconciliation
is the kind of thing that distinguishes a real synthesis from stapled results,
and it is done well.

Residual (MINOR): one stray c_i in the reliability applications subsection
(applications.tex) where the rest of the paper uses c(r). Since the reliability
sibling's native notation is c_i, this is defensible, but for a paper whose
whole point is one notation, normalize to c(R_i) or add a one-time note "we
write c_i for the candidate set of unit i." Trivial fix.

Residual (MINOR): the consistency theorem uses both "mu(theta)" (regime B
scalar functional) and "m(theta)" (general implied mean). These are different
objects (mu is the location parameter; m is E[T]) and in regime B they
coincide, but a reader can briefly conflate m and mu. One clarifying clause at
first co-occurrence ("in regime (B) the implied mean m(theta) is the location
mu(theta)") would prevent the stumble.

## 3. The seam table (tab:reduction): strength or list of failures?

THIS IS THE KEY PRESENTATION ISSUE. Verdict: as currently presented,
tab:reduction reads closer to a list of caveats than to a credibility
instrument, and the surrounding prose reinforces the defensive reading. It can
be flipped to a strength with modest changes.

Current state:
- The caption ends "Two carry caveats, recorded honestly." The word "caveats"
  and the apologetic "recorded honestly" frame the table as confession.
- The column header is "Reduction status," and three of five cells contain
  qualifiers (per-coordinate-only, informative-regime-only, asymptotic,
  Gaussian-only).
- discussion.tex "Where the unification is seamed" opens "A synthesis is only
  as honest as its account of what does not fit," again framing seams as
  not-fitting.

Why this undersells: a Statistical Science referee reading "here are exactly the
four domains that reduce exactly, here is the one that needs a second regime,
here are the two precise conditions under which the other two are exact vs
asymptotic" should come away thinking the authors have COMPLETE control of the
boundary of their principle. That is a strength. The current framing instead
invites "so the unification only half-works."

Recommended reframing (HIGH value, low effort):
- Recast tab:reduction's purpose as a REACH MAP, not a failure ledger. Caption:
  "How far the single principle reaches. Four domains reduce exactly through the
  exponential-family regime; differential privacy is captured by the
  location-family regime; the precise conditions for exactness vs asymptotic
  recovery are stated for each." Drop "caveats" and "recorded honestly."
- Add a positive-framing sentence before the table: e.g., "Because the
  reduction is explicit, we can state exactly where the principle is exact,
  where it is asymptotic, and where a second regime is needed. That precision is
  the point: a unification whose boundary is known is more useful than one whose
  boundary is asserted."
- In discussion, change "what does not fit" to "the boundary of the principle"
  or "how far the reduction reaches." The content stays identical; the
  connotation flips from apology to mastery.
- Consider a third column or a check/qualifier glyph so the eye sees "4 exact,
  1 second-regime" at a glance rather than reading five prose qualifiers.

The honesty itself is a genuine strength and IS the right move for this venue;
the problem is purely connotative framing. Do not remove the seams; reframe
them as the demonstrated reach of the principle.

## 4. Minor prose items
- abstract: "two regular regimes" is slightly odd phrasing ("regimes" already
  implies regularity); consider "two regularity regimes" or just "two regimes."
- introduction "wears a different costume in each field" and discussion
  "wearing five costumes" reuse the costume metaphor; fine once, mild when
  doubled; keep one.
- consistency.tex closing moral paragraph and discussion.tex "shared diagnostic
  moral" state the marginal-fit-is-not-unbiasedness point twice in nearly
  identical words. One can reference the other rather than restate.

## Prose-auditor findings list
- MAJOR (framing, shared with novelty): reframe tab:reduction and the
  "seamed"/"what does not fit" language from a failure ledger to a reach map of
  the principle. Highest-value presentation fix. Content unchanged.
- MINOR: rebalance the abstract so the seam-free singleton/rank unification is
  not subordinated to the seamed consistency theorem.
- MINOR (notation): one stray c_i; clarify m(theta) vs mu(theta) coincidence in
  regime B; otherwise notation is consistently reconciled across domains.
- MINOR: de-duplicate the marginal-fit-not-unbiasedness moral (stated twice).

Confidence: HIGH (direct reading and grep-verified notation counts).
