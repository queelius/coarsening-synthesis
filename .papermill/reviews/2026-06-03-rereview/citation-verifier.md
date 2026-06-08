# Citation Verifier Report (re-review)

Date: 2026-06-03
Confidence: HIGH for internal integrity (checked against main.aux and
main.blg); MEDIUM for external metadata (no live lookup).

## Internal integrity

- 0 undefined citations (main.log: 0 "undefined citation"; aux: 0
  undefined).
- 0 undefined references; 28 labels, all resolve.
- bibtex clean: main.blg shows 0 warnings, 0 errors.
- Every \citep / \citet in the seven sections resolves to an entry in
  refs.bib. Spot-checked the regime-(B) and weak-sup additions: the new
  text cites towell2026dpcoarsening (DP first-moment identity, n=1 form)
  and towell2026weaksupcoarsening (Theta(r/gap^2) rate) and
  vandervaart1998asymptotic (M-estimator asymptotics for the n^{-1/2}
  statement). All present.

## Did the revision break or orphan any citation?

No. The restructure did not orphan a previously used reference, and the
corrected regime-(B) prose reuses references already in the bibliography
(van der Vaart for the M-estimator asymptotics, the DP sibling for the
first-moment identity). No dangling \cite introduced.

## Unused entry (carried from prior review, NOT yet fixed)

- dwork2006calibrating is defined in refs.bib but cited 0 times
  (confirmed: 0 occurrences in main.aux). The DP applications subsection
  cites dwork2014algorithmic and wasserman2010statistical but not the
  calibrating-noise paper, which is the natural reference for the Laplace
  mechanism / calibrated noise that regime (B) is about. RECOMMEND: cite
  it in the DP subsection (applications.tex l.49-63, at "calibrated noise"
  in the introduction l.8-9, or at the kernel-scale singleton in
  tab:singletons) OR remove it. Severity MINOR.

## Missing canonical citation introduced by the revision (NEW, the most
## important citation item this pass)

The corrected regime (B) now leans explicitly on the Gauss
characterization: "the location MLE equals the arithmetic sample mean for
every sample if and only if the kernel is Gaussian" (consistency.tex
l.119-129, discussion.tex l.47-50, conclusion.tex l.31-33), with the
Cauchy-functional-equation mechanism and an explicit invocation of
"Gauss's characterization of the normal law as the unique location family
whose most probable value is the arithmetic mean." This classical result
is stated WITHOUT a primary citation. For a Statistical Science audience
this is a known fact, but it should be attributed. Candidates: Gauss
(1809, Theoria Motus) for the original; Teicher (1961, "Maximum likelihood
characterization of distributions," Ann. Math. Statist. 32, 1214-1222) or
Kagan, Linnik, and Rao (1973, Characterization Problems in Mathematical
Statistics) for a citable modern treatment. RECOMMEND adding one. Severity
MINOR (escalating toward MAJOR for a proofs-bearing venue such as JASA T&M
or Biometrika, where an uncited classical characterization invites a
referee note). This is the single clearest citation gap the revision
created by promoting the characterization from an open step to a stated
result.

## M-estimation anchor (carried from prior review)

Regime (B)'s psi-location language (psi = -p0'/p0, sample psi-location,
M-estimator variance V) currently relies on vandervaart1998asymptotic
Ch. 5, which is adequate for the asymptotics. A dedicated Huber (1964,
"Robust estimation of a location parameter," Ann. Math. Statist.) citation
at first use of psi would orient readers but is not required. Severity
SUGGESTION.

## Bib metadata fixes (carried from prior review, NOT yet fixed)

- tsiatis2006semiparametric is a @book but carries a journal field
  (refs.bib l.41-47: journal = {Springer Series in Statistics}). Use
  series = instead of journal = on a @book. Severity MINOR (cosmetic in
  abbrvnat output, but technically malformed).
- gill1997coarsening is a @article with journal = {Proceedings of the
  First Seattle Symposium in Biostatistics}, which is a proceedings volume;
  @incollection with booktitle = would be more correct. Severity MINOR.

## CAR / domain-anchor completeness

The CAR backbone (Heitjan-Rubin 1991, Gill-van der Laan-Robins 1997,
Little-Rubin 2002, Tsiatis 2006, van der Vaart 1998) and the ancestry
(Tsiatis 1975, Meilijson 1981) are complete and correctly chosen. Per-
domain anchors are complete (scRNA: Jiang 2022, Tabula Muris 2018;
spatial: Stahl 2016, Cable 2021; DP: Dwork-Roth 2014, Wasserman-Zhou 2010,
and dwork2006 if cited; weak-sup: Dawid-Skene 1979, Ratner 2016;
phenotyping: Rogan-Gladen 1978, Hui-Walter 1980). Sibling DOIs all present.
No missing foundational reference.

## Summary

Internal integrity perfect. One NEW citation gap from the revision (the
Gauss-characterization primary source, the top item), plus carried items
(unused dwork2006, two bib-metadata fixes, optional M-estimation anchor).
All MINOR for Statistical Science.
