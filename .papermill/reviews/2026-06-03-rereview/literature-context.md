# Literature Context Packet (merged scouts)

Date: 2026-06-03 (re-review)
Paper: One consistency theorem for coarsened-data maximum likelihood: a
cross-domain synthesis of the coarsening-at-random framework
Confidence: MEDIUM (model knowledge; no live web search available in this
environment). A live papermill:prior-art pass remains advisable before
submission, but the field position is stable and well understood.

## Field position

The paper sits squarely in the coarsening-at-random (CAR) and
missing-data-ignorability tradition. The canonical lineage is correctly
anchored: Heitjan and Rubin (1991, Ann. Stat.) introduced "coarse data"
and ignorability; Gill, van der Laan, and Robins (1997) gave the CAR
characterizations and counterexamples; Little and Rubin (2002) is the
standard ignorability reference; Tsiatis (2006) supplies the
semiparametric missing-data theory. van der Vaart (1998) covers the
exponential-family mean-value identity (regime A) and the M-estimation
asymptotics (regime B). This backbone is complete; no foundational CAR
reference is missing.

The genre is unification/synthesis. Statistical Science explicitly
publishes this genre (review and synthesis pieces, light on new theorems,
heavy on perspective and cross-domain connection). A simulation-free
theory-plus-worked-examples paper is squarely in scope, and the
cross-domain reach (reliability, genomics, privacy, ML weak supervision,
clinical informatics) suits the venue's broad readership. The main thing
Statistical Science referees expect from a synthesis is that the
organizing idea be genuinely load-bearing (not a superficial analogy) and
that the boundary of the unification be characterized honestly. The
revised paper now does both: the singleton/rank half is a literal shared
device, and the consistency half has its boundary located exactly (the
Gaussian-iff characterization).

## Competing and kindred unifications (subsumption verdicts)

1. Measurement-error / misclassification correction (Carroll, Ruppert,
   Stefanski, Crainiceanu; SIMEX; regression calibration). KINDRED, does
   not subsume. This umbrella unifies bias correction under known or
   estimated error structure, and Rogan-Gladen (1978) is one of its
   special cases. But it does not cast scRNA dropout, DP noise, weak-sup
   votes, and candidate-set masking as one CAR object, nor does it state
   the MLE-stationarity identity at this generality. Worth a one-sentence
   acknowledgment to place the synthesis among kindred umbrellas
   (suggestion, not required).

2. Latent-class / EM crowdsourcing unifications (Dawid-Skene 1979 and its
   modern descendants). KINDRED. Already cited as the ancestor of the
   weak-supervision label model. These unify observer-error estimation
   but not across the five non-crowdsourcing domains.

3. Semiparametric missing-data theory (Tsiatis 2006; Robins-Rotnitzky-Zhao
   influence-function program). KINDRED, more general in machinery but
   different in aim: it builds efficient estimators under MAR/CAR, it does
   not catalog the recurrence of one stationarity identity across these
   six applied fields. Cited.

4. Any single prior paper unifying two or more of these specific domains
   (scRNA dropout, spatial deconvolution, DP, weak supervision, EHR
   phenotyping) under CAR. NONE FOUND. This is the paper's novelty claim
   and it stands: the recurrence has not, to my knowledge, been named and
   organized before. The six sibling preprints are the author's own and
   are the source material, correctly framed as such.

VERDICT: no prior work subsumes the synthesis claim. The contribution as
organization is safe.

## Candidate missing citations (prioritized)

1. PRIMARY-SOURCE CITATION FOR THE GAUSS CHARACTERIZATION. The regime-(B)
   boundary result, "the location MLE equals the arithmetic sample mean
   for every sample if and only if the kernel is Gaussian," is classically
   Gauss's characterization of the normal law (Gauss 1809, Theoria Motus).
   Modern treatments: Teicher (1961, "Maximum likelihood characterization
   of distributions," Ann. Math. Statist. 32) and the characterization-
   theorems literature (Kagan, Linnik, Rao, Characterization Problems in
   Mathematical Statistics, 1973). The paper currently states this
   characterization and its Cauchy-functional-equation mechanism without a
   primary citation. For a Statistical Science audience this is a known
   classical fact and a single citation (Teicher 1961 or Kagan-Linnik-Rao)
   would properly attribute it. PRIORITY: MEDIUM-HIGH. This is the single
   clearest scholarly gap introduced by leaning on the characterization.

2. M-ESTIMATION / ROBUST-STATISTICS ANCHOR FOR THE psi-LOCATION LANGUAGE.
   Regime (B) uses psi = -p0'/p0 and the sample psi-location throughout.
   This is M-estimation of location (Huber 1964; Huber and Ronchetti,
   Robust Statistics). van der Vaart (1998) Ch. 5 is already cited and
   covers the asymptotics, which is adequate, but a dedicated Huber
   citation at the first use of psi would orient readers. PRIORITY: LOW
   (van der Vaart already carries the load).

3. MEASUREMENT-ERROR UMBRELLA (Carroll-Ruppert-Stefanski-Crainiceanu) as
   a one-line "kindred unification" acknowledgment. PRIORITY: LOW
   (optional placement, improves scholarly situating).

## Weak-supervision rate (targeted)

The settled rate now stated in the paper, Theta(r/gap^2) gold labels for
L2 / total model recovery with Theta(log r/gap^2) for the per-direction
loss, is consistent with the data-programming and crowdsourcing
sample-complexity literature (Ratner et al. 2016 and follow-ups). The
paper correctly attributes the rate to the weak-sup sibling
(towell2026weaksupcoarsening) and correctly frames the log-r rate as a
DIFFERENT-LOSS rate, not a weakness. No external collision.

## Rogan-Gladen attribution

Rogan and Gladen (1978) is correctly cited and correctly framed as the
chart-review-calibrated special case (prevalence correction with the two
error rates estimated rather than assumed). The two-code no-chart-review
corner is correctly identified as Hui-Walter (1980). Attribution is
adequate.

## Venue-fit summary

Statistical Science is the right primary venue and the revised framing
(reach map, not failure ledger) matches what its referees reward in a
synthesis. The generic article class is submittable as-is (IMS applies its
house style post-acceptance). The only scholarly addition the literature
suggests is the Gauss-characterization primary citation.
