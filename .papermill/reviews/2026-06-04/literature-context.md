# Literature Context Packet (merged scouts)

Date: 2026-06-04
Confidence: MEDIUM. This orchestration environment cannot spawn the two
literature-scout subagents and has no live WebSearch (documented constraint:
see memory papermill-reviewer-no-recursive-subagents, and both prior review
sessions on 2026-06-03). The field position below rests on model knowledge,
the on-disk research provenance in `.research/`, and the two prior reviews'
literature passes, which agreed. The brief's request for a live WebSearch
verification of Teicher 1961 and Kagan-Linnik-Rao 1973 could not be
satisfied with a live query; instead those two load-bearing references are
verified for accuracy of characterization against the manuscript's own use
and against the independently re-run proof scripts (see logic-checker). A
live `papermill:prior-art` pass in the main loop remains the one residual
literature action and is the same standing recommendation both prior reviews
left open.

## Field position of the paper

The paper is a cross-domain synthesis, not a new-theory contribution. It
unifies, under the coarsening-at-random (CAR) umbrella, five named
"consistency" results and one rank/singleton identifiability apparatus that
recur across reliability, single-cell and spatial genomics, differential
privacy, programmatic weak supervision, and EHR phenotyping. Its closest
neighbors are the foundational CAR/ignorability literature and the author's
own six sibling preprints, which carry the empirical weight.

## CAR / missing-data lineage (the backbone) -- COMPLETE

- Heitjan and Rubin (1991), Ignorability and Coarse Data, Ann. Statist.
  19(4):2244-2253. The origin of the coarse-data ignorability conditions.
  Correctly cited as the CAR source.
- Gill, van der Laan, and Robins (1997), Coarsening at random:
  characterizations, conjectures, counter-examples, Proc. First Seattle
  Symposium in Biostatistics, LNS 123:255-294. The CAR characterization
  reference. Now correctly typed as @incollection (minor fix applied).
- Little and Rubin (2002), Statistical Analysis with Missing Data, 2nd ed.
  The ignorability textbook anchor.
- Tsiatis (2006), Semiparametric Theory and Missing Data. Semiparametric
  missing-data anchor. Now correctly uses series= not journal= (minor fix).
- Jacobsen and Keiding: the brief asks whether the CAR lineage including
  Jacobsen-Keiding is complete. Jacobsen and Keiding (1995, "Coarsening at
  random in general sample spaces and random censoring," Ann. Statist.) is a
  standard third pillar of the CAR characterization literature alongside
  Heitjan-Rubin and Gill-van der Laan-Robins. It is NOT currently cited. For
  a Statistical Science synthesis that foregrounds the CAR conditions, adding
  Jacobsen-Keiding (1995) would complete the canonical CAR triad and is the
  single clearest scholarly addition the literature suggests. Severity:
  MINOR (optional but recommended for a CAR-centered synthesis at this
  venue). This is the one genuinely new literature item this pass surfaces
  beyond what the prior reviews settled.

## Characterization theory (now load-bearing) -- VERIFIED ACCURATE

- Teicher (1961), Maximum Likelihood Characterization of Distributions,
  Ann. Math. Statist. 32(4):1214-1222, doi 10.1214/aoms/1177704861. This is
  the citation the regime-(B) Gauss-iff boundary now leans on. Teicher's
  paper characterizes distributions by the property that a given statistic is
  the MLE; the relevant special case is that the arithmetic sample mean is
  the maximum-likelihood estimator of a location parameter if and only if the
  underlying density is normal (Gaussian). This is EXACTLY the property the
  manuscript invokes in rem:loc-sketch ("the location MLE equals the
  arithmetic sample mean for every sample if and only if the kernel is
  Gaussian"). The characterization is correctly attributed. The bibliographic
  metadata (volume, number, pages, year, DOI) is internally consistent and
  matches the known Annals of Mathematical Statistics record.
- Kagan, Linnik, and Rao (1973), Characterization Problems in Mathematical
  Statistics, Wiley. The standard monograph placing the Gauss/Teicher
  location-MLE characterization in the broader characterization-theory
  context. Correctly cited as the secondary placement. Metadata consistent.

The mathematics these two references support was independently re-verified
this pass by re-running `.research/findings/proof_gaussian_iff.py` (the
Cauchy-functional-equation reduction at n=3 forcing linear psi, hence
Gaussian) and `.research/findings/counterexample_laplace_n3.py` (the
Laplace median-vs-mean exact gap on data (0,1,5)). Both confirm the claim
the citation backs. See logic-checker for the run output.

## Per-domain anchors -- COMPLETE

- scRNA-seq: Jiang et al. (2022) zero-inflation controversy; Tabula Muris
  (2018). Correct anchors.
- Spatial: Stahl et al. (2016) spatial transcriptomics; Cable et al. (2021)
  RCTD. Correct anchors.
- Differential privacy: Dwork-Roth (2014) foundations; Wasserman-Zhou (2010)
  statistical DP. Correct anchors. (The previously unused dwork2006calibrating
  has been removed; the DP subsection no longer leaves a calibrated-noise
  reference dangling, which is acceptable since Dwork-Roth covers the Laplace
  mechanism.)
- Weak supervision: Ratner et al. (2016) data programming; Dawid-Skene
  (1979) error-rate model. Correct anchors.
- Phenotyping: Rogan-Gladen (1978) prevalence correction; Hui-Walter (1980)
  latent-class. Correct anchors.

## Ancestry

- Tsiatis (1975) competing-risks nonidentifiability; Meilijson (1981)
  autopsy-model estimation. Both correctly used as the finite-case ancestry
  of the rank/identifiability result.

## Kindred unifications (does anything subsume the claim?)

No prior work unifies these specific six domains under CAR. The kindred
umbrellas (measurement-error / misclassification correction, of which
Rogan-Gladen is a special case; latent-class crowdsourcing a la Dawid-Skene;
semiparametric missing-data theory a la Tsiatis) each touch one or two of the
domains but none spans the set or frames the recurrence as a single
consistency identity plus a single rank/singleton device. The
novelty-as-organization claim therefore stands. Optional: a one-sentence
acknowledgment situating the synthesis against the broader measurement-error
correction umbrella would pre-empt a referee's "isn't this subsumed by
misclassification correction" reflex (carried suggestion from prior reviews).

## Net literature actions

1. (MINOR, recommended) Add Jacobsen-Keiding (1995) to complete the CAR
   characterization triad. New this pass.
2. (SUGGESTION) Optional measurement-error-umbrella sentence.
3. (SUGGESTION) Optional Huber (1964) anchor at first use of the psi-location
   in regime (B); van der Vaart already carries the asymptotics.
4. (STANDING) Run a live `papermill:prior-art` pass from the main loop for
   web-grounded confirmation before final submission. The two now-load-bearing
   characterization citations are verified accurate by use and by re-run
   proof, but a live lookup would upgrade MEDIUM to HIGH.
