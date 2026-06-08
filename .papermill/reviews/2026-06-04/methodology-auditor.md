# Methodology Auditor Report

Date: 2026-06-04 (final pre-submission pass)
Priority (per brief): reproduce the reasoning of the general consistency
theorem in both regimes; confirm the corrected regime-(B) statement is
sound; confirm the boundary characterization is a rigorous result rather
than an asserted one. Confidence: HIGH (build reproduced, proof scripts
re-run, formulas spot-checked).

## Synthesis method and empirical delegation

The method is "state the recurring result once at the right generality,
recover each named instance as a corollary, and delegate the empirical
weight to the six sibling preprints." For a Statistical Science synthesis
this is a legitimate and appropriate method: the venue's mandate is unity of
the field at moderate technical level, and the empirical validation of each
named identity demonstrably lives in the corresponding sibling (state.md
siblings block, DOIs present in refs.bib). No new simulation is expected or
required of a synthesis paper. The delegation is honest and traceable: every
named identity points to a sibling DOI.

## Reproducing the regime-(A) reasoning

Reproduced. The exponential-family mean-value identity nabla A(eta)=E_eta[T]
gives score n(Tbar-E_eta[T]) in the natural parameter; full-column-rank
partial-eta/partial-theta is exactly the ingredient that carries the
interior stationarity partial_theta ell=0 to partial_eta ell=0, hence
E_hat[T]=Tbar. This is the standard log-partition gradient (van der Vaart
Ch.5, correctly cited). The methodology is sound and the rank hypothesis is
the right and only nontrivial ingredient.

## Reproducing the regime-(B) reasoning and the boundary

Reproduced and the boundary is a rigorous characterized result, not an
assertion. I re-ran the on-disk provenance:

- proof_gaussian_iff.py (re-run, exit 0): the "arithmetic mean is the MLE
  for every sample" condition reduces at n=3 to Cauchy's functional equation
  for psi, whose continuous/monotone solutions are linear, forcing p_0
  Gaussian. The numerical cross-check shows the functional-equation defect is
  ~1e-15 for the linear (Gaussian) score and O(1) for Laplace/logistic/cubic
  at n=3,4,5. This certifies the Gauss-iff boundary.
- counterexample_laplace_n3.py (re-run, exit 0): data (0,1,5), Laplace MLE =
  median = 1 vs mean = 2, exact gap -1, ell(median)-ell(mean)=1/b>0. Matches
  rem:loc-sketch verbatim.
- The synthesis.md provenance additionally documents the logistic MLE
  (1.5752...), the kernel battery, the O_p(n^{-1/2}) constant V=Var(psi(Z)/J
  - Z) with V=1 for Laplace and 0.290 for logistic (Monte-Carlo confirmed at
  n=20000), and the Student-t_2 bimodality justifying log-concavity. The
  methodology behind the boundary is complete and independently checkable.

The corrected regime-(B) statement (exact at n=1, population first-moment for
any n, n^{-1/2} for n>1, exact-iff-Gaussian) is the methodologically correct
reading of this provenance. The prior review's sec:css over-claim (that the
likelihood depends on the data only through Tbar in regime B) is fixed:
framework.tex sec:css (l.97-108) now splits by regime and states the
psi-location dependence correctly.

## The two-regime partition

The partition is correctly argued as non-nested (rem:loc-sketch l.147-149):
(A) is a curved constraint on a discrete/count report; (B) is a location
shift of a continuous report; DP is recovered only from (B). This is a
methodological strength, not a defect, and the reach-map table presents it as
controlled scope rather than apology.

## The six minors, methodological soundness

- Teicher/Kagan-Linnik-Rao citations: these attach a rigorous classical
  characterization to the boundary; methodologically this upgrades the
  boundary from "we proved it" to "this is the known characterization,"
  which is the correct scholarly framing for a synthesis venue.
- phenotype 3-to-1 reparam: methodologically this correctly links the scalar
  consistency identity (pins q) to the identifiability deficit (cannot split
  the triple), motivating the singleton. Sound.
- censoring rider moved to remark: methodologically correct; the general
  sufficiency hypothesis is the column-rank condition alone, and the
  domain-specific support condition belongs in instantiation. The general
  statement is not weakened (the rank condition is unchanged); the rider was
  never a hypothesis of the general theorem, only of its reliability instance.
- 5-vs-6 count, bib removal, bib metadata: no methodological content; clean.

## Build reproducibility

`make clean && make paper` exits 0; 11 pages; 0 undefined references; no
rerun-needed warning; bibtex blg shows 0 warnings, 0 errors; 0 "??" in the
PDF text; 59 newlabel entries resolve. The build is fully reproducible from
the bundled imsart class files. The reformat is format-only: the abstract
block is byte-identical to the article-class backup, and the section inputs
are unchanged.

## Residual methodology items

SUGGESTION (carried): one global sentence making the delegated empirical base
visible at a glance (each named identity confirmed in its sibling: three
exactly, weak-sup at the predicted n^{-1/2} rate, DP for the single release /
Gaussian kernel). Optional for the venue.

No critical or major methodology defects. The corrected regime-(B) statement
is methodologically sound and its boundary is a rigorous result.
