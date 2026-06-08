# Citation Verifier Report

Date: 2026-06-03
Note: No live web search available in this context; bibliographic-accuracy
checks below are against the manuscript bib and model knowledge (MEDIUM
confidence on external metadata, HIGH on internal key resolution). Recommend a
live papermill:prior-art pass to confirm volume/page metadata before camera-
ready.

## Verdict summary
- Internal citation integrity: PERFECT. Every used key is defined; 0 undefined.
- Unused entries: exactly one (dwork2006calibrating). Decide to cite or drop.
- CAR-lineage citations: complete and correct (Heitjan-Rubin, Gill et al.,
  Little-Rubin, Tsiatis).
- Per-domain anchors: complete.
- Recommended additions: 2 (M-estimation/robust-stats anchor for regime B;
  optionally a broader measurement-error-correction umbrella reference).
- Metadata nits: a few entries have minor field issues (below).

## 1. Internal integrity (HIGH confidence)

Cross-checked all \cite keys used in sections/*.tex against entries defined in
refs.bib:
- 24 distinct keys used; 25 defined. All 24 used keys are defined -> 0
  undefined citations (confirms state.md and the clean bibtex run).
- DEFINED-but-UNUSED: dwork2006calibrating (Dwork-McSherry-Nissim-Smith 2006,
  "Calibrating Noise to Sensitivity"). This is the foundational DP mechanism
  paper. It is odd to ship it in the bib unused given the DP subsection cites
  dwork2014algorithmic and wasserman2010statistical. RECOMMEND: cite it in the
  DP applications subsection (it is the natural reference for "calibrated noise"
  / the Laplace mechanism) OR remove it. Currently dead weight. (MINOR)
- bibtex run: 0 warnings (main.blg clean), abbrvnat style, footnotesize bib.

## 2. CAR / foundational lineage (the citations a referee will police)

- heitjan1991ignorability: Heitjan and Rubin, Ann. Statist. 19(4):2244-2253,
  1991. Correct anchor for coarse data / CAR origin. Metadata plausible.
- gill1997coarsening: Gill, van der Laan, Robins, First Seattle Symposium in
  Biostatistics, 1997, pp. 255-294. Correct canonical CAR-characterization
  reference. (This is a proceedings/book chapter; the entry uses journal field
  for the proceedings name, acceptable under abbrvnat but @incollection with
  booktitle would be cleaner. MINOR metadata.)
- little2002statistical: Little and Rubin, 2nd ed., Wiley, 2002. Correct;
  cited as Ch. 6 for ignorability. Good.
- tsiatis2006semiparametric: Tsiatis, Springer Series in Statistics, 2006. The
  entry has BOTH a journal field ("Springer Series in Statistics") AND
  publisher=Springer on a @book; the journal field is wrong for a book (should
  be series=). MINOR metadata fix.

Assessment: the CAR backbone is complete and correctly chosen. A Statistical
Science referee will look for exactly Heitjan-Rubin and Gill-van der
Laan-Robins and will find both. No missing foundational CAR citation.

## 3. Engine and ancestry citations

- vandervaart1998asymptotic: cited (Ch. 5) for the log-partition gradient.
  Correct and standard.
- tsiatis1975: competing-risks nonidentifiability. Correct ancestry anchor.
- meilijson1981: autopsy-statistics lifetime estimation. Correct finite-case
  ancestry. doi present.

## 4. Per-domain anchors (all appropriate)

scRNA: tabula2018single, jiang2022zero -- correct.
Spatial: stahl2016visualization, cable2021robust (RCTD) -- correct.
DP: dwork2014algorithmic, wasserman2010statistical -- correct; dwork2006
unused (see above).
Weak sup: ratner2016data (data programming), dawid1979maximum (Dawid-Skene) --
correct.
Phenotype: rogan1978estimating (Rogan-Gladen), hui1980estimating (Hui-Walter)
-- correct.

## 5. Recommended ADDITIONS (MEDIUM confidence; verify against venue norms)

1. Regime B currently uses the M-estimation language "psi-location,"
   "psi = -p_0'/p_0 odd and monotone," with NO citation for the general
   theory. This is classical robust-statistics / M-estimation material. Add a
   Huber (Robust Statistics) or van der Vaart M-estimation pointer so the
   psi-function machinery is anchored rather than appearing ad hoc. (MINOR,
   strengthens regime B's standing.)

2. Optional: a one-line acknowledgement of the broader measurement-error /
   misclassification-correction umbrella (Rogan-Gladen is itself a special
   case) would help a referee place the synthesis among other unifications.
   Not required. (SUGGESTION.)

## 6. Sibling preprint citations

The six sibling @misc Zenodo entries (towell2026{masked,mdrelax,scrna,spatial,
dp,weaksup,phenotype}) all have DOIs and URLs. Appropriate for preprints. Two
considerations for camera-ready (MINOR): (i) if any sibling is published by
submission time, upgrade @misc -> the published venue; (ii) self-citation
density is high (7 of 25 entries) but unavoidable and legitimate for a
synthesis of one's own family. A Statistical Science referee will not object
given the genre, but ensure the siblings are publicly resolvable at the DOIs
(they are Zenodo, so yes).

## Citation-verifier findings list
- MINOR: dwork2006calibrating defined but unused -> cite in DP subsection or
  remove.
- MINOR (metadata): tsiatis2006semiparametric has a journal field on a @book
  (use series=); gill1997coarsening better as @incollection with booktitle.
- MINOR (addition): add an M-estimation/robust-stats anchor for the regime-B
  psi-location language.
- SUGGESTION: optional measurement-error-correction umbrella reference.
- NO undefined citations; NO missing foundational CAR reference.

Confidence: HIGH on internal resolution and on which anchors are present/absent;
MEDIUM on external metadata correctness (no live lookup).
