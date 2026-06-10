# Statistical Science submission metadata (coarsening-synthesis)

Form-ready values. The manuscript is in the IMS `imsart` class with the
Statistical Science option (`\documentclass[sts]{imsart}`); class files are
vendored in the source bundle.

## Manuscript

- **Type:** Article (synthesis / unifying review).
- **Title:** One consistency theorem for coarsened-data maximum likelihood: a cross-domain synthesis of the coarsening-at-random framework
- **Running head:** A consistency theorem for coarsened-data MLE
- **Pages:** 12
- **Preprint:** https://doi.org/10.5281/zenodo.20533912 (concept DOI; resolves to the current v0.2.0)

## Author

- Alexander Towell, Department of Computer Science, Southern Illinois University Edwardsville, Edwardsville, Illinois, USA
- lex@metafunctor.com, ORCID 0000-0001-6443-9897
- Single author. No competing interests. Not under review elsewhere.

## Abstract (plain text)

A recurring statistical structure appears, under different names, across reliability, single-cell and spatial genomics, differential privacy, programmatic weak supervision, electronic-health-record phenotyping, and multiple instance learning. In each, a latent quantity is observed only through a coarsening: a candidate set, a dropout, a noised release, a vote, a diagnostic code, a bag label. Two results recur. The first is seam-free across all seven domains: an augmented-candidate-set rank condition decides when the latent parameter is identifiable, and a singleton candidate set, a report that pins the latent quantity to a point, restores identifiability by restoring column rank. The singleton wears a different costume in each field (spike-ins, single-cell-resolution probes, gold labels, non-private releases, chart review, singleton bags) but is one mechanism, and we state it once. The second recurring result is a consistency identity at the maximum-likelihood fit. When the coarsening satisfies the coarsening-at-random conditions C1, C2, C3, the face-value likelihood can be maximized without modeling the coarsening, and the fit reproduces the empirical mean of a coarsening-sufficient statistic at the optimum. This identity has been stated six separate times, as cell-total consistency in single-cell data, its spot-level variant in spatial deconvolution, release consistency for differential privacy, agreement consistency for weak supervision, code-frequency consistency for phenotyping, and bag-prevalence consistency for multiple instance learning; we state it once and recover each named version as a special case. Its boundary is the more nuanced part of the synthesis, and we locate it exactly. In a regular exponential family the identity is an exact finite-sample equality; in a location family it is exact for a single report and a population first-moment identity otherwise, with the finite-sample sample-mean form holding only up to an order n^(-1/2) remainder and exactly only for the Gaussian kernel, which itself sits in the exponential-family regime. The weak-supervision case reduces exactly under a sufficiency-complete parametrization and asymptotically otherwise, and differential privacy is recovered through the location-family branch as a single-release identity. The empirical weight is carried by the sibling papers, which are cited rather than re-derived.

## Keywords

coarsening at random; masked-data inference; identifiability; maximum likelihood; consistency

## MSC 2020 subject classifications (proposed; author to confirm)

- Primary: 62F12 (asymptotic properties of parametric estimators), 62D10 (missing data)
- Secondary: 62B05 (sufficient statistics and fields), 62N05 (reliability and life testing), 62P10 (applications to biology and medical sciences)

Note: the published v0.2.0 PDF does not render MSC codes on the title page (the
manuscript's `keyword` block has subject keywords but no `MSC2020` block). Supplying
the codes in the submission form is standard at submission. If the editor wants them
in the manuscript, add an `\begin{keyword}[class=MSC2020] ... \end{keyword}` block to
the frontmatter and issue a v0.3.0 preprint to keep the Zenodo record in sync.

## Data and code availability

This is a synthesis paper with no new data or simulations; the empirical weight is
carried by the cited sibling papers, each a published preprint with a concept DOI:

- masked-causes-in-series-systems (reliability foundation): 10.5281/zenodo.18725577
- scrna-coarsening: 10.5281/zenodo.20414734
- spatial-coarsening: 10.5281/zenodo.20422883
- dp-coarsening: 10.5281/zenodo.20422885
- weaksup-coarsening: 10.5281/zenodo.20422888
- phenotype-coarsening: 10.5281/zenodo.20422890
- mil-coarsening: 10.5281/zenodo.20502964
- coarsening-sensitivity (C2-violation companion): 10.5281/zenodo.20604314
