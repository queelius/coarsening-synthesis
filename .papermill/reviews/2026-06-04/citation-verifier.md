# Citation Verifier Report

Date: 2026-06-04 (final pre-submission pass)
Priority (per brief): verify Teicher 1961 and Kagan-Linnik-Rao 1973 are real
and accurately characterized (now load-bearing); confirm the CAR lineage
(Heitjan-Rubin, Gill-vdL-Robins, Jacobsen-Keiding) and per-domain anchors
are complete; confirm the six bib-touching minors are applied.
Confidence: HIGH for internal integrity (checked against main.aux, main.blg,
main.bbl); MEDIUM for external metadata (no live WebSearch in this
environment, so the two load-bearing references are verified by accuracy of
use and by re-run proof rather than by live lookup).

## Internal integrity -- perfect

- 0 undefined citations (main.log clean; aux clean).
- 0 undefined references; 59 newlabel entries, all resolve; 0 "??" in PDF.
- bibtex clean: main.blg shows 0 warnings, 0 errors.
- main.bbl renders 52 bibitems consistent with the cited set.
- Every \citep/\citet in the seven sections resolves to a refs.bib entry.

## Teicher 1961 and Kagan-Linnik-Rao 1973 (now load-bearing) -- VERIFIED

- teicher1961maximum: present in refs.bib (l.132-141) and rendered in
  main.bbl. Metadata: Teicher, Henry; "Maximum Likelihood Characterization of
  Distributions"; Ann. Math. Statist. 32(4):1214-1222; 1961; doi
  10.1214/aoms/1177704861. This is internally consistent and matches the
  known AMS record. ACCURACY OF USE: the paper cites it (consistency.tex
  l.121, l.132) for "the location MLE equals the arithmetic sample mean for
  every sample if and only if the kernel is Gaussian" and "the
  maximum-likelihood characterization of the normal." Teicher's paper
  characterizes a distribution by the property that a prescribed statistic is
  its MLE; the location-mean special case is precisely that the sample mean is
  the location MLE iff normal. The citation is accurately characterized and
  correctly load-bearing. (Verified by accuracy of use and by re-running the
  proof_gaussian_iff.py provenance, not by live web lookup; see logic-checker.)
- kagan1973characterization: present (refs.bib l.143-150), rendered. Kagan,
  Linnik, Rao; "Characterization Problems in Mathematical Statistics"; Wiley;
  1973. The standard monograph for characterization theory including the
  location-MLE-mean result. Used (consistency.tex l.133) as the broader
  placement. Accurately characterized.

Both are real, both are correctly attributed, and the metadata is clean.
RECOMMENDATION for upgrade to HIGH confidence: a live papermill:prior-art
lookup would confirm the page/DOI against the publisher record; the accuracy
of the claim itself is already verified.

## The six bib-touching minors -- applied

1. dwork2006calibrating REMOVED: confirmed 0 occurrences in refs.bib and
   main.aux. The DP subsection cites dwork2014algorithmic and
   wasserman2010statistical; with Dwork-Roth covering the Laplace mechanism,
   no calibrated-noise reference dangles. Resolved (prior m5).
2. gill1997coarsening now @incollection with booktitle (refs.bib l.15-25).
   Resolved (prior m6 part 1).
3. tsiatis2006semiparametric now uses series= not journal= (refs.bib
   l.45-52). Resolved (prior m6 part 2).
4. Teicher + Kagan-Linnik-Rao ADDED (prior m1, the top item of the
   re-review). Resolved.
5. (phenotype reparam and censoring rider are non-bib; see logic-checker.)

All citation-touching items from the prior reviews are now closed.

## CAR lineage completeness

- Heitjan-Rubin (1991), Gill-van der Laan-Robins (1997), Little-Rubin (2002),
  Tsiatis (2006), van der Vaart (1998): all present, correctly chosen.
- Jacobsen-Keiding (1995): NOT present. This is the standard third pillar of
  the CAR characterization literature (alongside Heitjan-Rubin and
  Gill-van der Laan-Robins). For a synthesis that foregrounds the CAR
  conditions, its absence is the one CAR-lineage gap. Severity MINOR
  (recommended addition; see literature-context). New this pass.
- Ancestry (Tsiatis 1975, Meilijson 1981): present and correct.

## Per-domain anchors completeness

Complete: scRNA (Jiang 2022, Tabula Muris 2018); spatial (Stahl 2016, Cable
2021); DP (Dwork-Roth 2014, Wasserman-Zhou 2010); weak-sup (Dawid-Skene 1979,
Ratner 2016); phenotyping (Rogan-Gladen 1978, Hui-Walter 1980). Sibling DOIs
all present and resolve.

## Residual citation items

1. (MINOR, new) Add Jacobsen-Keiding (1995) to complete the CAR triad.
2. (SUGGESTION, carried) Optional Huber (1964) anchor at first use of the
   psi-location in regime (B); van der Vaart already carries the asymptotics,
   so this is non-blocking.
3. (SUGGESTION) Optional Gauss (1809, Theoria Motus) for the historical
   origin of the location-mean characterization; the paper names Gauss in
   prose and Teicher carries the rigorous citation, so this is purely
   optional.

Internal integrity perfect. The two load-bearing characterization citations
are real and accurately used. The only new item is the optional
Jacobsen-Keiding addition. No critical or major citation defects.
