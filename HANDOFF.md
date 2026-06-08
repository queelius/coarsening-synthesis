# HANDOFF: coarsening-synthesis

State of the flagship synthesis paper at the end of the scaffold-v0.1
session. Read this plus `CLAUDE.md` before continuing.

## What this paper is

The flagship of the masked-data / coarsening-at-random (CAR) paper
family. The six siblings port the same idea into six domains. This paper
states the shared results once and recovers each domain's named result
as a corollary. Methods/synthesis paper; no new simulations.

## What was done this session

1. Read the foundational paper (`towell2026masked`) and the
   translation/identifiability sections of all six siblings to extract
   the exact form of each named consistency theorem, each domain's
   singleton device, and each domain's rank condition.
2. Mirrored the LaTeX setup of `papers/dp-coarsening/` (documentclass,
   preamble, theorem environments, Makefile) with a new
   title/abstract/author.
3. Wrote seven sections, `refs.bib` (six sibling Zenodo DOIs copied
   exactly + CAR lineage + domain anchors), README, CLAUDE.md, this
   HANDOFF, and `.papermill/state.md`.
4. Verified the build: `make paper` compiles to 13 pages with 0
   undefined references and no label-changed warning after settling.

## The central result, as settled

`thm:general-consistency` (in `consistency.tex`):

> At an interior maximum of the face-value likelihood, the fitted mean
> of the coarsening-sufficient statistic equals its empirical mean,
> `m(theta_hat) = T_bar`.

Two regular regimes:
- **(A) regular exponential family**: complete proof. The
  log-partition gradient gives `E_theta[T] = T_bar` at the MLE when the
  natural-parameter Jacobian has full column rank.
- **(B) location family**: proof with ONE open step. Uses the
  location-family score identity `d/dmu log p = -d/dr log p`. Exact for
  the Gaussian kernel (sample mean); for a general symmetric unimodal
  kernel it is a population first-moment identity
  (`E[M] = m_obs`), the form the dp sibling proves. The
  finite-sample, arbitrary-kernel statement is the open step
  (`rem:loc-sketch`).

## How cleanly each named theorem reduces (the honest audit)

See `tab:reduction` in `consistency.tex`.

| Named theorem | Regime | Reduces? |
|---|---|---|
| Cell-total (scRNA) | A | Exact. ZINB mean-parameterized score. |
| Spot-level (spatial) | A | Exact per coordinate; vector form needs joint rank. |
| Code-frequency (phenotype) | A | Exact in informative regime sens+spec > 1. |
| Agreement (weak sup.) | A | Exact only under sufficiency-complete parametrization; ASYMPTOTIC for naive-Bayes. |
| Release (DP) | B | NOT regime A. Location-family first-moment; exact for Gaussian kernel. |

Three clean (scRNA, spatial, phenotype). Two seamed (weak sup
asymptotic-for-the-used-parametrization, DP in a different regime).

## Does the synthesis hold together?

Yes, at the level of "MLE stationarity forces the fitted mean of the
coarsening-sufficient statistic to match its empirical mean." Four of
five domains are the same exponential-family identity; DP is the
location-family analogue of the same stationarity principle. The
singleton-restoration result and the rank condition unify with no seams:
all six singleton devices are literally `|c(r)| = 1` reports, and all six
rank conditions are full column rank of the (augmented) coarsening
operator. The consistency theorem is where the seams are, and they are
named, not hidden.

## What to do next (priority order)

1. **Close or formally bound the regime-(B) open step.** Either restrict
   the general statement to the Gaussian kernel, or replace `T_bar` with
   the kernel's psi-location for the finite-sample arbitrary-kernel case.
   This is the only mathematically open item.
2. **Decide the weak-supervision presentation.** Currently stated as
   exact-under-sufficiency + asymptotic-for-naive-Bayes. Consider
   whether to lead with the extended (sufficiency-complete)
   parametrization or the practitioner one.
3. **Expand the rank/singleton sketches to full proofs** if targeting
   Statistical Science / JASA T&M (they can absorb a proofs appendix).
   The foundational paper has the full proof to port
   (`paper-full-proofs.tex` in `masked-causes-in-series-systems/`).
4. **Run `papermill:prior-art`** to position against the broader
   CAR/ignorability and unification literature beyond the siblings.
5. **Consider a Statistical Science framing pass**: that venue rewards a
   strong opening narrative and a clear "what is new is the
   organization, not the math" statement; the introduction already
   gestures at this but could be sharpened for that audience.

## Build status

- `make paper`: clean, 13 pages, `grep -ci undefined main.log` = 0.
- No em-dashes (U+2014) in any source file (verified).
- No vanity-count framings (verified; "five named theorems" is content,
  not achievement filler).

## Risks / things a reviewer will probe

- A Statistical Science reviewer may ask whether regimes (A) and (B) can
  be unified into one statement rather than two branches. The honest
  answer (in `rem:loc-sketch` and discussion) is that they are not
  nested and DP genuinely sits in (B); do not pretend otherwise.
- The weak-supervision asymptotic caveat will draw scrutiny; keep
  `cor:weaksup` precise.
- The paper claims no new mathematics. Make sure the framing stays
  "unification/organization" so it is not judged as a thin theory paper.
