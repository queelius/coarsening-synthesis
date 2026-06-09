# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Project Overview

Academic paper repository: **One consistency theorem for coarsened-data
maximum likelihood: a cross-domain synthesis of the coarsening-at-random
framework.**

This is the **flagship/synthesis** paper of the masked-data /
coarsening-at-random (CAR) paper family. The six siblings each port one
statistical idea (masked-data identifiability under C1/C2/C3) into one
domain. This paper does the inverse move: it states the shared results
once, at the right generality, and recovers each domain's named result
as a corollary. It is a methods/synthesis paper, not a new-application
paper, and it contains no new simulations (the siblings carry the
empirical weight).

## Build Commands

```bash
make paper      # builds main.pdf
make clean      # removes artifacts
```

No `make sim` / `make figures`: this is a synthesis paper with no
simulation. LaTeX with `natbib` and `cleveref` only.

## Architecture

- `main.tex`: pure-LaTeX top-level, preamble + `\input{sections/...}`.
  Preamble (documentclass, packages, theorem environments, macros) is
  copied from `papers/dp-coarsening/main.tex` so the family shares one
  LaTeX setup.
- `sections/`: 7 section files (no `\end{document}` in section files):
  `introduction`, `framework`, `consistency`, `identifiability`,
  `applications`, `discussion`, `conclusion`.
- `refs.bib`: BibTeX. Six sibling Zenodo concept DOIs (copied exactly
  from the siblings' bibs; do NOT invent DOIs), CAR lineage
  (Heitjan-Rubin 1991, Gill-van der Laan-Robins 1997, Little-Rubin
  2002), van der Vaart 1998, competing-risks ancestry (Tsiatis 1975,
  Meilijson 1981), and the domain anchors (Jiang 2022, Rogan-Gladen
  1978, Dawid-Skene 1979, Hui-Walter 1980, Ratner 2016, Cable 2021,
  Stahl 2016, Wasserman-Zhou 2010, Dwork-Roth 2014).

## The results (where they live)

- **General consistency theorem** (`thm:general-consistency`,
  `consistency.tex`): at an interior MLE the fitted mean of the
  coarsening-sufficient statistic equals its empirical mean. Two
  regimes: (A) regular exponential family (complete proof via
  log-partition gradient), (B) location family (settled: sample-mean
  identity exact iff Gaussian; otherwise the psi-location is the exact
  finite-sample identity and the sample-mean form is asymptotic, V tabulated).
- **Five named corollaries** (`cor:scrna`, `cor:spatial`,
  `cor:phenotype`, `cor:weaksup`, `cor:dp`, `consistency.tex`).
- **General rank condition** (`thm:general-rank`, `identifiability.tex`):
  the augmented-candidate-set rank condition, ported from
  `towell2026masked`.
- **Singleton restoration** (`prop:singleton`, `identifiability.tex`):
  singletons restore identifiability; per-domain devices in
  `tab:singletons`.

## CRITICAL: the two seams (do not paper over)

The synthesis is honest about where it does not reduce cleanly. Keep
this honesty in any revision:

1. **Differential privacy is regime (B), not (A).** Its release
   consistency is a continuous-convolution first-moment identity proved
   through the location-family score, NOT the exponential-family
   mean-value identity that serves the other four. It is exact only for
   the Gaussian kernel; the sample-mean form holds if and only if the
   kernel is Gaussian (SETTLED: stationarity at the mean for all samples is
   Cauchy's equation, forcing a Gaussian kernel). For a general symmetric
   log-concave kernel the exact finite-sample identity is the sample
   psi-location, and the sample-mean form is the n=1 / population /
   asymptotic (O_p(n^{-1/2}), constant V tabulated in rem:loc-sketch)
   statement. Do not claim a general-n sample-mean identity for non-Gaussian
   kernels (it is false). (The dp paper itself replaced an
   incorrect "regular-exponential-family" route with the location-family
   route during its own review; this is why dp does not sit in regime A.)
2. **Weak supervision reduces exactly only under a sufficiency-complete
   parametrization.** The naive-Bayes label model that data programming
   uses does NOT make pairwise agreement indicators sufficient
   statistics; for it the identity is only asymptotic (`n^{-1/2}`).

A milder seam: spatial's spot-level identity is exact per coordinate but
its vector form needs the joint rank condition.

## Conventions (Alex's preferences)

- **No em-dashes** (soul plugin hook enforces; U+2014 blocks any file
  write). Use commas, colons, periods, parentheses.
- **No vanity counts** as achievement filler. Normal enumeration of
  corollaries/contributions is fine; do NOT write framings like
  "N-paper family unified in this M-page work."
- LaTeX, not Quarto/RMarkdown.
- Synthesis register: state results once, cite siblings for
  domain-specific development and validation rather than re-deriving.
- Author: Alexander Towell, lex@metafunctor.com, SIUE Department of
  Computer Science, ORCID 0000-0001-6443-9897.

## Prior-art honesty (important)

The CAR conditions are classical (Heitjan-Rubin, Gill-van der
Laan-Robins, Little-Rubin). The exponential-family mean-value identity
that powers regime (A) is textbook (van der Vaart). The contribution is
NOT new mathematics: it is the recognition that one consistency identity
and one rank condition recur across six fields as instances of CAR, plus
the explicit reduction with a clean account of the two regimes and two
seams. Keep that framing; do not overclaim novelty.

## Venue

Primary target: **Statistical Science** (publishes unifying/review
pieces; best fit for a synthesis). Shortlist in `.papermill/state.md`:
Statistical Science, then JASA Theory & Methods, JRSS-B, Biometrika,
JMLR, with Annals of Statistics aspirational. A simulation-free
theory-plus-worked-examples paper is acceptable at a methods/synthesis
venue.

## Status

Scaffold v0.1 (June 2026). All seven sections substantive. Regime (A)
proof complete; regime (B) settled (Gaussian-iff sample-mean identity;
psi-location exact; V tabulated); rank and
singleton results are sketches citing `towell2026masked`. Build verified
clean (13 pages, 0 undefined).
