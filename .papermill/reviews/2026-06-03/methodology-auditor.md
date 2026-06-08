# Methodology Auditor Report

Date: 2026-06-03
Note: This is a synthesis paper with no new simulations or data by design;
empirical weight is delegated to the six siblings. "Methodology" here means
the soundness of the synthesis METHOD: are the regimes well-posed, are the
reductions logically complete as a method of unification, is the delegation of
empirical validation legitimate, and is the reproduction (build) sound.

## Verdict summary
- Synthesis method (state-once-recover-as-corollary): SOUND and well-executed.
- Two-regime partition: methodologically justified; the non-nestedness is
  argued correctly (rem:loc-sketch).
- Delegation of empirical validation to siblings: LEGITIMATE for the venue, but
  the paper should state once that each named identity was empirically
  confirmed in its sibling (it does so per-domain; a one-line global statement
  would help).
- Build reproducibility: VERIFIED. make paper -> exit 0, 13 pp, 0 undefined
  refs, 0 bibtex warnings.
- One methodological soft spot: the "coarsening-sufficient statistic" is
  DEFINED somewhat circularly; tightening would strengthen the method.

## 1. Is the two-regime structure a methodological defect?

A skeptic could read "the general theorem needs two non-nested regimes" as an
admission that there is no single theorem. The paper preempts this in
rem:loc-sketch: regime (A) is a curved constraint on a discrete/count report;
regime (B) is a location shift of a continuous report; they are genuinely
different score geometries. This is methodologically honest and, I judge,
correct: the unifying object is not a single regularity hypothesis but the
single CONCLUSION (fitted mean of T = empirical mean of T as an
MLE-stationarity consequence), reached through whichever score identity the
report law supplies. The synthesis claim is "one principle (stationarity forces
mean-matching), realized through two standard score identities," which is
defensible. See novelty-assessor for whether the FRAMING sells this; as
methodology it is sound.

## 2. The coarsening-sufficient statistic definition (soft spot)

framework.tex sec:css defines T as "a statistic of the observed report whose
expectation under the fitted model is a smooth function of theta ... and which
the face-value likelihood treats as its data summary," and "such that the
face-value log-likelihood depends on the data only through Tbar."

This is partly circular: in regime (A), T is just the exponential family's
natural sufficient statistic (clean, non-circular); in regime (B), T(R) = R is
asserted, but the "depends on data only through Tbar" clause does NOT hold for
a general location family at finite n (the likelihood depends on the full
sample through the psi-location, not through Rbar). So the DEFINITION of T as
"the thing the likelihood summarizes via its mean" is exact in regime (A) and
aspirational in regime (B). This is the same seam as the open regime-B step,
surfacing at the level of the definition.

Recommendation (MINOR-to-MAJOR depending on venue): define T cleanly via the
exponential-family sufficient statistic in regime (A), and in regime (B) define
it as the report with the explicit caveat that "summarized through its mean" is
the population/Gaussian statement. As written, a careful referee will notice
the definition over-promises for regime (B) and may read it as papering over
the open step at the definitional level rather than the theorem level. The fix
is presentational, not mathematical.

## 3. Legitimacy of delegating empirical validation

The paper makes no new empirical claim and cites each sibling for validation
(applications.tex: Tabula Muris for scRNA, ST data + RCTD for spatial,
simulation for DP, simulation for weak sup, validation for phenotype). For
Statistical Science (a synthesis venue) this is appropriate; the journal does
not require fresh experiments for a unifying piece. The siblings do contain the
empirical confirmations (verified: scrna conclusion "confirmed cell-total
consistency exactly"; phenotype validation "reproduces the observed code
frequency exactly"; weaksup validation tracks n^{-1/2}).

Recommendation (MINOR): add one sentence in sec:applications or discussion
stating globally that every named identity has been empirically confirmed in
its sibling (three exactly, weak-sup at the predicted n^{-1/2} rate, DP for the
Gaussian kernel). Right now the evidence is scattered per-subsection and the
reader cannot see at a glance that the synthesis rests on validated parts.

## 4. Statistical rigor of the claims that ARE made

- The mean-value identity (regime A) is exact, standard, correctly cited
  (van der Vaart Ch. 5). No rigor gap.
- The "marginal-fit is not unbiasedness" moral is a correct and important
  methodological diagnostic, stated once and correctly generalized. This is
  arguably the paper's most valuable methodological export.
- The singleton/rank apparatus is exact finite-dimensional linear algebra in
  the discrete case and a correctly-flagged operator analogue in the
  continuous cases.

## 5. Reproducibility / build

make paper: pdflatex + bibtex + pdflatex + pdflatex, exit 0.
- 13 pages (matches state file claim).
- 0 undefined references (grep of main.log: none).
- 0 bibtex warnings (main.blg clean).
- All \cref targets resolve (no "??" in PDF; no undefined-reference warnings).
Reproducible from source as shipped. No figures to regenerate (none used).

## Methodology-auditor findings list
- MINOR/MAJOR (presentational): the coarsening-sufficient-statistic definition
  over-promises in regime (B) ("likelihood depends on data only through Tbar"
  is false for general location families at finite n). Split the definition by
  regime. Severity depends on venue strictness; for Statistical Science MINOR,
  for JASA T&M closer to MAJOR.
- MINOR: add a single global sentence that each named identity is empirically
  validated in its sibling, so the delegated empirical base is visible at a
  glance.
- NO defect in the two-regime structure as METHODOLOGY; it is honestly argued.
- Build fully reproducible.

Confidence: HIGH on build and on the rigor of stated identities; MEDIUM on the
venue-appropriateness judgment of the delegation (depends on the specific
referee).
