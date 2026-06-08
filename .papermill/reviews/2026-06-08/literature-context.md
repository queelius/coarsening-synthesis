# Literature Context Packet

**Paper**: One consistency theorem for coarsened-data maximum likelihood: a
cross-domain synthesis of the coarsening-at-random framework
**Date**: 2026-06-08

Note on method: the orchestrator's literature-scout subagents could not be
spawned in this environment (the Task tool is unavailable inside the agent
threads). The area chair assembled this packet directly from domain knowledge
and from the manuscript's own bibliography, and flagged each claim's confidence.
Treat author/year/venue strings below as orienting pointers a domain referee
should confirm, not as machine-verified records.

## 1. Coarsening-at-random (CAR) lineage and prior unifications

- **Heitjan & Rubin (1991), Ann. Statist. 19(4):2244-2253** ("Ignorability and
  Coarse Data"). The origin of "coarse data" and the ignorability conditions.
  Cited.
- **Gill, van der Laan & Robins (1997)**, First Seattle Symposium in
  Biostatistics, LNS 123:255-294. CAR characterizations and counterexamples.
  Cited.
- **Little & Rubin (2002)**, *Statistical Analysis with Missing Data*, 2nd ed.
  The ignorability tradition. Cited.
- **Tsiatis (2006)**, *Semiparametric Theory and Missing Data*. Cited.
- **Jacobsen & Keiding (1995)**, "Coarsening at random in general sample
  spaces..."; **Nielsen (2000)** on CAR with continuous data. NOT cited.
  Relevance: these extend CAR to general/continuous sample spaces, which is
  exactly the move the paper makes in carrying the candidate set to a
  "kernel-weighted continuum" for differential privacy. A continuous-CAR
  referee may want one of these acknowledged when the framework section claims
  the discrete and continuous candidate sets "are the same object at different
  cardinalities." Confidence: high that these works exist and are the standard
  continuous-CAR references; medium on exact framing.

Verdict on prior unification: There is no well-known prior paper that unifies
CAR/coarsening across this *particular* seven-domain span (reliability +
single-cell + spatial + DP + weak supervision + phenotyping + MIL). The
missing-data/ignorability literature unifies *missingness* mechanisms; this
paper's move (reading dropout, noised release, votes, codes, and bag labels as
one coarsening) is genuinely its own. The closest competing "unifier" genres
are (a) EM as the unifier of latent-variable estimation
(Dempster-Laird-Rubin 1977), and (b) semiparametric influence-function theory
(Bickel-Klaassen-Ritov-Wellner 1993; Tsiatis 2006; van der Vaart 1998).
Neither makes the specific "fitted marginal moment equals empirical moment at
the MLE, and this does not certify latent unbiasedness" point that is this
paper's diagnostic spine. The positioning against the CAR literature
(discussion section) is adequate; the one gap a careful referee may raise is
the continuous-CAR lineage above.

## 2. Moment-matching at the MLE in exponential families

The fact that at the MLE of a regular exponential family the fitted mean of the
natural sufficient statistic equals its empirical mean is textbook. The paper
cites van der Vaart (1998, Ch. 5), which is correct and sufficient. Canonical
alternatives a referee might expect named: **Brown (1986)**, *Fundamentals of
Statistical Exponential Families* (IMS Lecture Notes); **Barndorff-Nielsen
(1978)**, *Information and Exponential Families*; **Lehmann & Casella (1998)**,
*Theory of Point Estimation*. The paper is candid that regime (A) is the
textbook identity ("the textbook score equation"), so no citation gap is fatal,
but a single Brown (1986) or Barndorff-Nielsen (1978) cite would strengthen the
exponential-family-foundations footing for a Statistical Science audience.
Confidence: high.

## 3. The Gaussian/Teicher characterization (regime B)

- **Teicher (1961), Ann. Math. Statist. 32(4):1214-1222** ("Maximum Likelihood
  Characterization of Distributions"). This is the correct primary reference for
  "the location MLE equals the arithmetic sample mean for every sample iff the
  kernel is Gaussian." Cited and correctly attributed.
- **Kagan, Linnik & Rao (1973)**, *Characterization Problems in Mathematical
  Statistics*. The broad characterization-theory home; cited.
- Historical: **Gauss (1809)** characterization (arithmetic mean as most
  probable value) is invoked in prose, correctly framed as the classical face.
- The Cauchy-functional-equation route at n=3 (psi additive forces psi linear)
  is the standard short proof and is correctly sketched. Confidence: high that
  Teicher is the right cite and the attribution is accurate.

## 4. Per-domain anchors (gaps a domain expert would notice)

- **scRNA-seq**: Jiang et al. (2022), Genome Biology, zero-inflation
  controversy. Cited. A referee may also expect **Svensson (2020)** (droplet
  scRNA-seq is not zero-inflated) or **Kim et al. / Sarkar & Stephens (2021)**
  on the statistics of expression variation; not fatal. Confidence: high.
- **Spatial deconvolution**: RCTD / Cable et al. (2021) cited. Competing
  deconvolution methods a spatial referee will expect at least name-checked:
  **CARD (Ma & Zhou 2022)**, **cell2location (Kleshchevnikov et al. 2022)**,
  **SPOTlight (Elosua-Bayes et al. 2021)**, **Stereoscope (Andersson et al.
  2020)**. The paper cites only RCTD. For Statistical Science this is
  acceptable (it is not a methods-comparison paper), but a one-clause "and
  related deconvolution methods" would inoculate against the gap. Confidence:
  high.
- **Differential privacy**: Wasserman & Zhou (2010), Dwork & Roth (2014)
  cited. The statistical-DP / minimax literature (**Duchi, Jordan & Wainwright
  2018**, local DP minimax) is the natural further anchor but not required.
  Confidence: high.
- **Weak supervision**: Ratner et al. (2016) data programming, Dawid & Skene
  (1979) cited. The triplet/MeTaL line (**Ratner et al. 2019**, "Training
  complex models with multi-task weak supervision"; **Fu et al. 2020**, Flying
  Squid) is the modern label-model-identifiability work and is the single most
  likely "missing reference" a weak-supervision referee will name, because the
  paper's rank-deficit-under-LF-dependence claim is exactly that line's
  territory. Recommend the sibling, not necessarily this synthesis, carry it;
  but one cite here is cheap insurance. Confidence: high.
- **EHR phenotyping**: Rogan & Gladen (1978), Hui & Walter (1980) cited; both
  are the correct classical anchors. The modern phenotyping-with-anchors line
  (**Halpern et al. 2016**; **Agarwal et al. 2016 PheNorm**) is optional.
  Confidence: high.
- **Multiple instance learning** (the newly folded-in domain): the paper cites
  only the sibling (towell2026milcoarsening). The MIL field's foundational
  reference is **Dietterich, Lathrop & Lozano-Perez (1997), Artificial
  Intelligence 89(1-2):31-71** ("Solving the multiple instance problem with
  axis-parallel rectangles"), which also introduced the MUSK1/MUSK2 benchmark
  the corollary's prose alludes to ("a MUSK1/MUSK2 application"). The noisy-OR
  probabilistic-MIL line includes **Maron & Lozano-Perez (1998)** (Diverse
  Density), **Zhang & Goldman (2001)** (EM-DD), **Viola, Platt & Zhang (2005)**
  (multiple-instance boosting). **GAP/SIGNIFICANT for the synthesis**: the MIL
  corollary and the applications subsection both name the MUSK benchmark but
  cite no MIL primary source other than the author's own sibling. Because MIL
  is the one domain folded in most recently, and the sibling itself is the one
  reference cited only by GitHub URL (no Zenodo DOI), the MIL domain is the
  thinnest-anchored in the bibliography. At minimum Dietterich et al. (1997)
  should be cited where MUSK is named. Confidence: high.

## 5. The "marginal fit is not evidence of unbiasedness" diagnostic

This is the paper's recurring moral. It is closely related to, but distinct
from, several known ideas the paper could position against: identifiability of
finite mixtures (**Teicher 1963**), label shift / prior-probability shift
(**Saerens, Latinne & Decaestecker 2002**; **Lipton, Wang & Smola 2018**), and
the general point that goodness-of-fit on observables does not identify latent
structure (the competing-risks nonidentifiability of **Tsiatis 1975**, which
the paper *does* cite for identifiability). The diagnostic as stated ("a fitted
model reproducing the observed marginal is structurally uninformative about the
latent parameter") is not, to my knowledge, packaged under a single canonical
name in the literature, which supports the paper's claim that stating it once
across domains is a genuine organizing contribution. No direct-prior-art threat
to this framing was found. Confidence: medium-high.

## Overall positioning verdict

No direct prior-art threat to the central unification claim was found: nobody
has published this seven-domain CAR synthesis. The contribution is correctly
self-described as organization rather than new mathematics. The two citation
soft-spots a domain referee is most likely to name are (1) the MIL domain
(no Dietterich et al. 1997 despite naming MUSK; sibling cited only by URL) and
(2) the continuous-CAR lineage (Jacobsen-Keiding / Nielsen) given the paper's
discrete-to-continuous candidate-set move. Both are cheap to fix and neither
undermines the thesis.
