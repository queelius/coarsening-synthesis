# Format Validator Report (re-review)

Date: 2026-06-03
Confidence: HIGH (build executed directly).

## Build

- Command: make paper (pdflatex + bibtex + pdflatex + pdflatex).
- Exit code: 0.
- Output: main.pdf, 15 pages (was 13 at the prior review; the
  +2 pages are the intro rebuttal paragraph, the corrected/expanded
  regime-(B) theorem and remark, and the reach-map legend, all substantive
  additions).
- 0 undefined references (main.log).
- 0 undefined citations (main.log).
- bibtex: 0 warnings, 0 errors (main.blg).
- 28 labels, all resolve; 0 "??" in the PDF.
- No "Label(s) may have changed" rerun warning in the final pass.

## Did the revision break the build?

No. The restructure (abstract reorder, new intro paragraph, expanded
theorem/remark, glyph table column) builds clean with no new warnings. The
glyph column in tab:reduction uses \bullet, \circ, \triangleright (math-
mode amssymb glyphs already loaded); renders correctly.

## Conventions

- Em-dash (U+2014): PASS. grep -P "\x{2014}" over all source files finds
  nothing.
- Vanity counts: PASS. Enumerations are of corollaries and contributions
  (structural), not achievement-scale framing.

## Venue formatting

- Document class: generic article, 11pt, letterpaper, 1in margins.
  Submittable to Statistical Science as-is; IMS applies its house style
  (imsart) post-acceptance, so the generic class is not a blocker.
- Abstract length: 322 words. Statistical Science does not publish a hard
  abstract word limit, so this is acceptable, though on the long side; see
  prose-auditor for an optional trim. Not a formatting defect.
- Bibliography style: abbrvnat (natbib). Fine for submission.
- Page count: 15 pages. Comfortable for a Statistical Science synthesis
  (the venue runs longer review/synthesis pieces); the prior review's
  "13 pp is short" note is now moot.

## Residual formatting items

1. MINOR (carried, cosmetic): two bib-metadata malformations
   (tsiatis2006semiparametric journal-on-@book; gill1997coarsening
   article-vs-incollection). These do not break the build and render
   acceptably under abbrvnat; see citation-verifier. No "??" or undefined
   output results from them.
2. MINOR (carried): one unused bib entry (dwork2006calibrating); harmless
   to the build (bibtex only emits used entries), flagged for the author
   to cite or remove. See citation-verifier.

No critical, major, or build-blocking formatting issues. The revision is
production-clean.
