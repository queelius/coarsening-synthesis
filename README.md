# coarsening-synthesis

Paper: **One consistency theorem for coarsened-data maximum likelihood:
a cross-domain synthesis of the coarsening-at-random framework.**

Methods/synthesis-format draft. This is the flagship of the masked-data
/ coarsening-at-random (CAR) paper family. The siblings each port the
same statistical idea into one domain; this paper states the shared
results once, at the generality that explains the recurrence, and
recovers each domain's named result as a special case.

## Overview

A latent quantity observed only through a coarsening (a candidate set, a
dropout, a noised release, a vote, a diagnostic code) is the common
object across six fields. Under the coarsening-at-random conditions C1,
C2, C3 the face-value likelihood can be maximized without modeling the
coarsening, and one structural identity holds at the optimum. That
identity has been stated five times under five names:

- **cell-total consistency** (scRNA-seq),
- **spot-level / cell-total consistency** (spatial transcriptomics),
- **release consistency** (differential privacy),
- **agreement consistency** (weak supervision),
- **code-frequency consistency** (EHR phenotyping).

This paper proves it once (`thm:general-consistency`) and recovers each
named version as a corollary. Two companion structural results recur the
same way and are stated once: an augmented-candidate-set rank condition
for identifiability (`thm:general-rank`), and a singleton candidate set
that restores identifiability (`prop:singleton`). The per-domain
singletons (spike-ins, single-cell probes, gold labels, non-private
releases, chart review) are tabulated as one device.

## The central result, and its two regimes

The general consistency theorem says: at an interior MLE of the
face-value likelihood, the fitted mean of the coarsening-sufficient
statistic equals its empirical mean, `m(theta_hat) = T_bar`. It holds in
two regular regimes:

- **(A) regular exponential family**: the exact mean-value identity
  (log-partition gradient). Recovers scRNA, spatial, phenotype exactly,
  and weak supervision exactly under a sufficiency-complete
  parametrization.
- **(B) location family**: a first-moment identity proved through the
  location-family score. Recovers differential privacy. Exact for the
  Gaussian kernel.

The two seams (recorded honestly in the paper):

- Differential privacy lives in regime (B), not (A). Its
  kernel-general, finite-sample identity is the one genuinely open step.
- Weak supervision reduces exactly only under a parametrization
  practitioners do not use; for the naive-Bayes label model it is
  asymptotic.

## Build

```bash
make paper      # produces main.pdf
make clean
```

Requires LaTeX with `natbib` and `cleveref`. No simulation: this is a
synthesis paper; the empirical weight is carried by the sibling papers,
which are cited.

## Structure

- `main.tex`: top-level with preamble + section includes
- `sections/`:
  - `introduction.tex` (the family, the recurring pattern, the
    contribution: unification)
  - `framework.tex` (C1/C2/C3 stated once, abstract DGP, the
    coarsening-sufficient-statistic setup)
  - `consistency.tex` (the general consistency theorem + proof, then the
    five named corollaries)
  - `identifiability.tex` (general rank condition + singleton
    restoration, per-domain singleton devices tabulated)
  - `applications.tex` (compact tour: one subsection per domain as an
    instance, citing the sibling)
  - `discussion.tex` (what the unification buys, the two seams, open
    per-domain problems)
  - `conclusion.tex`
- `refs.bib`: bibliography (six sibling Zenodo concept DOIs, CAR
  lineage, domain anchors)

## Sibling papers

| Sibling | Domain | Named consistency theorem | Cite key |
|---|---|---|---|
| `masked-causes-in-series-systems/` | reliability (foundational) | (rank condition + likelihood) | `towell2026masked` |
| `mdrelax/` | C2-violation sensitivity | robustness bands | `towell2026mdrelax` |
| `scrna-coarsening/` | scRNA-seq dropout | cell-total consistency | `towell2026scrnacoarsening` |
| `spatial-coarsening/` | spatial deconvolution | spot-level consistency | `towell2026spatialcoarsening` |
| `dp-coarsening/` | differential privacy | release consistency | `towell2026dpcoarsening` |
| `weaksup-coarsening/` | weak supervision | agreement consistency | `towell2026weaksupcoarsening` |
| `phenotype-coarsening/` | EHR phenotyping | code-frequency consistency | `towell2026phenotypecoarsening` |

## Target venue

Primary: **Statistical Science** (the natural home for a unifying /
review piece). Shortlist and rationale in `.papermill/state.md`.

## Status

**Reviewed 2026-06-08 (papermill multi-agent): minor-revision.** No critical issues; the math was independently re-derived and the multiple-instance-learning fold-in (cor:mil) verified sound. The review's main items were addressed the same day: cor:mil restated as a true regime-(A) score corollary (carrying the noisy-OR link weight), the cor:dp corollary count corrected, and the Dietterich (1997) MUSK anchor added.

**Scaffold v0.1 (June 2026).** All seven sections have substantive
content. The general consistency theorem has a complete proof for regime
(A) and a proof-with-one-open-step for regime (B); the rank and
singleton results are proof sketches that cite the foundational paper
for shared apparatus. Build verified: `make paper` compiles to 13 pages
with zero undefined references.

## Conventions

- **No em-dash characters** (U+2014); soul plugin hook enforces this.
- **No vanity counts** as achievement filler; describe the work.
- LaTeX, not Quarto/RMarkdown.
- Author: Alexander Towell, lex@metafunctor.com, SIUE Department of
  Computer Science, ORCID 0000-0001-6443-9897.
- Cite siblings by their Zenodo concept DOIs; do not re-derive their
  domain-specific results.
