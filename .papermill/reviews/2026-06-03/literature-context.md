# Literature Context Packet (merged scouts)

Date: 2026-06-03
Paper: One consistency theorem for coarsened-data maximum likelihood (coarsening-synthesis)

ENVIRONMENT NOTE: Live web search was unavailable in this review context (see
memory: papermill-reviewer-no-recursive-subagents). The literature assessment
below rests on model knowledge plus direct inspection of the manuscript bib
(refs.bib) and the seven sibling repositories. Treat "closest prior art" and
"missing citation" claims as MEDIUM confidence; the author should run
papermill:prior-art for a live-grounded pass before submission. Build checks,
formula re-derivations, and sibling cross-references are HIGH confidence.

## Field map: where this paper sits

The paper is a cross-domain SYNTHESIS in the coarsening-at-random (CAR) /
missing-data-ignorability tradition. Its move is not a new theorem but the
recognition that one MLE-stationarity identity and one rank/singleton
identifiability apparatus recur across six applied literatures that do not cite
each other.

### Foundational CAR / ignorability lineage (cited, correct anchors)
- Heitjan and Rubin (1991), Ignorability and Coarse Data, Ann. Statist. The
  origin of the "coarse data" formalism and the CAR concept. CITED.
- Gill, van der Laan, Robins (1997), Coarsening at random: characterizations,
  conjectures, counter-examples. The canonical CAR characterization reference,
  including the everywhere-CAR vs CAR subtlety. CITED.
- Little and Rubin (2002), Statistical Analysis with Missing Data. Standard
  ignorability text. CITED (Ch. 6).
- Tsiatis (2006), Semiparametric Theory and Missing Data. CITED.

These four are the right and sufficient backbone for the CAR positioning. A
Statistical Science referee will expect exactly these and will find them.

### The mean-value / exponential-family engine (regime A)
- van der Vaart (1998), Asymptotic Statistics. CITED for the log-partition
  gradient identity nabla A(eta) = E_eta[T]. Correct and standard.

### Competing-risks / masked-cause ancestry (the finite case)
- Tsiatis (1975), nonidentifiability of competing risks without independence.
  CITED. Correct anchor for the necessity direction of the rank theorem.
- Meilijson (1981), autopsy statistics / lifetime estimation. CITED. Correct
  historical anchor for the finite incidence-matrix identifiability argument.

### Per-domain anchors (all present and appropriate)
- scRNA: Tabula Muris (2018), Jiang et al. (2022) zero-inflation controversy.
- Spatial: Stahl et al. (2016) ST, Cable et al. (2021) RCTD.
- DP: Dwork et al. (2006) calibrating noise, Dwork-Roth (2014), Wasserman-Zhou
  (2010) statistical DP. The Wasserman-Zhou anchor is the right "statistics
  meets DP" citation.
- Weak sup: Ratner et al. (2016) data programming, Dawid-Skene (1979).
- Phenotyping: Rogan-Gladen (1978) prevalence correction, Hui-Walter (1980)
  latent-class error rates.

## Differentiation from the sibling papers

The seven siblings (towell2026masked, mdrelax, scrna/spatial/dp/weaksup/
phenotype-coarsening) are the source material, all cited with Zenodo DOIs. The
synthesis's contribution is delineated as "the organization, not the math":
it states C1/C2/C3 once, the consistency identity once (two regimes), the rank
condition once, the singleton device once, and recovers each sibling's named
theorem as a corollary. This is a legitimate and recognizable Statistical
Science genre (cf. the journal's unifying/review pieces).

## Candidate prior art a referee may raise (MEDIUM confidence, verify live)

1. Self-consistency / mean-matching at the MLE is a general property of
   exponential-family score equations; a referee may ask whether the "one
   consistency theorem" is more than the textbook moment-matching identity
   (sum T(R_i) = n E_eta[T] at the MLE). The paper's honest answer is YES it
   is that identity, and the contribution is recognizing five named theorems
   are it. The paper should preempt the "this is just exp-family
   moment-matching" reaction more directly (see novelty-assessor).

2. The CAR-for-coarse-data + ignorable-likelihood result is classical
   (Heitjan-Rubin, Gill et al.). The paper is clear it is specializing, not
   re-proving, CAR. Good.

3. Generic "unification of latent-variable / measurement-error models" work
   (e.g., the EM / latent-class umbrella, Rogan-Gladen as a special case of
   misclassification correction) could be cited as kindred unifications. Not
   strictly required, but a sentence acknowledging the broader
   measurement-error-correction umbrella would strengthen positioning.

4. The location-family score / M-estimation framing of regime B is classical
   robust-statistics material (Huber psi-functions). The paper uses psi =
   -p_0'/p_0 correctly; a Huber/M-estimation citation in regime B would help a
   referee place the "psi-location" language (currently uncited as general
   theory).

## Takeaways for the review
- CAR positioning is complete and correctly anchored.
- Per-domain anchors are complete.
- Two gaps worth closing for a top venue: (i) an M-estimation/robust-stats
  citation for the regime-B psi-location language; (ii) an explicit sentence
  distinguishing the synthesis from "textbook exponential-family
  moment-matching" so the novelty is not mistaken for triviality.
