# Format Validator Report

**Paper**: One consistency theorem for coarsened-data maximum likelihood
**Date**: 2026-06-08
**Venue target**: Statistical Science (IMS imsart class, sts option)

## Summary

Build is clean and venue-appropriate. `make paper` exits 0; main.pdf is 12
pages; zero substantive undefined references; zero undefined citations; no
multiply-defined labels; all six corollary labels and all cross-references
resolve. The IMS imsart frontmatter is complete (title, runtitle, author with
ORCID, runauthor, address, abstract, five keywords). The only items are cosmetic
box warnings and one stale page count in the state file.

## Build verification
- Command: `make paper` (runs pdflatex; bibtex; pdflatex; pdflatex). Exit 0.
- Undefined check: `LC_ALL=C grep -ai undefined main.log | wc -l` = 3, all three
  are harmless "Font shape ... undefined" lines (treated as harmless per the
  brief). Substantive undefined count after excluding Font-shape: 0.
- `LC_ALL=C grep -ai "multiply.defined\|undefined references\|undefined
  citations\|LaTeX Warning: Reference"`: none.
- Output: "Output written on main.pdf (12 pages, 309473 bytes)."
- BibTeX (main.blg): zero warnings, 27 entries used.

## Label / cross-reference resolution
- Six corollary labels defined (cor:scrna, cor:spatial, cor:phenotype, cor:mil,
  cor:weaksup, cor:dp) and all referenced; the intro \cref list
  (introduction.tex:98) names all six including cor:mil. Resolves.
- thm:general-consistency, thm:general-rank, prop:singleton, rem:loc-sketch,
  cond:c1/c2/c3, tab:css/tab:reduction/tab:singletons, eq:* all resolve.

## Findings

### [MINOR] Cosmetic overfull hboxes, one in tab:reduction
**Location**: main.log overfull list. Magnitudes: 3.84pt, 7.24pt, 13.92pt,
8.48pt, 3.84pt. The two largest (13.92pt and 8.48pt) are both "in paragraph at
lines 295--295," i.e., the tab:reduction table (consistency.tex:295, the
\textbf header row / wide cells).
**Problem**: 13.9pt is below the ~20pt threshold where text visibly protrudes
into the margin, so this is cosmetic, but the tab:reduction column widths
(p{0.20} p{0.07} p{0.07} p{0.50}) are tight and the long "How far the principle
reaches" cells push slightly. The MIL row added a long cell, which likely
nudged these.
**Suggestion**: widen the last column slightly (e.g., p{0.48}->p{0.50} is
already large; instead trim the MIL and spatial cell wording, or reduce the
header to fit). Cosmetic; not blocking.

### [MINOR] State file page count is stale (says 13, build is 12)
**Location**: .papermill/state.md build_status.main_pdf "13 pages, clean build"
and Dashboard "13 pages"; CLAUDE.md also says "13 pages." Current build: 12
pages.
**Problem**: documentation drift, not a manuscript defect. The brief confirms 12
pages is current ("builds clean at 12 pages").
**Suggestion**: update the state file's page count to 12 when next editing it
(the review-history update for 2026-06-08 is the natural moment).

### [SUGGESTION] 55 underfull boxes
**Location**: main.log. These are spacing-only underfull \hbox/\vbox warnings,
typical of justified text with p{} table columns and the imsart class. Harmless.
No action.

## Venue-format notes (informational, not defects)
- The class is correctly imsart with the `sts` option, matching the Statistical
  Science requirement identified in the state file's venue analysis. Class files
  are vendored in the repo root, so the build is self-contained.
- imsart-nameyear.bst is selected with authoryear natbib; bibliography renders.
- No hard page cap applies to a regular STS article (per the state file's venue
  research), so 12 pages is fine.
- Frontmatter \orcid, \ead, \address all present and correctly formatted for
  imsart.
