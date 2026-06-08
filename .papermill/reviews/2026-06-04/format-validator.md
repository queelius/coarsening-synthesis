# Format Validator Report

Date: 2026-06-04 (final pre-submission pass)
Priority (per brief): verify the imsart reformat builds clean and is
submission-grade for Statistical Science; confirm conventions (no em-dash, no
vanity counts). Confidence: HIGH (build executed clean from scratch).

## Build

`make clean && make paper` (pdflatex; bibtex; pdflatex x2): EXIT 0.

- 11 pages (imsart sts, single-column, dense; the prior article-class build
  was 13-15 pp, so the imsart class runs denser as expected; no hard page cap
  applies to a regular STS article, and 11 dense imsart pages is comfortable
  for the venue).
- 0 undefined citations (main.log).
- 0 undefined references; 59 newlabel entries resolve.
- No "rerun needed" warning (labels stable).
- bibtex: main.blg shows 0 warnings, 0 errors.
- 0 "??" in the rendered PDF text.
- All result environments render with correct numbering (verified from aux):
  Theorem 1 (general-consistency), Theorem 2 (general-rank), Corollaries 1-5
  (scrna, spatial, phenotype, weaksup, dp), Proposition 1 (singleton),
  Remarks 1-2 (loc-sketch, rank-instantiation), Conditions 1-3, Definition.
- Tables (tab:css, tab:reduction, tab:singletons) render; the reach-map glyph
  column (bullet/circle/triangle) renders with no warnings.

## imsart conformance

- Document class: `\documentclass[sts]{imsart}` (the Statistical Science /
  Statistics Surveys option), with the bundled official IMS support files
  (imsart.cls, imsart.sty, imsart-nameyear.bst) in the repo root, so the
  build is self-contained. Confirmed these are the vtex-soft/texsupport.ims-sts
  package per the main.tex header.
- Frontmatter uses the imsart idioms correctly: `\begin{frontmatter}`,
  `\title`, `\runtitle`, `\begin{aug}` with `\author[A]{\fnms...\snm...}`,
  `\ead`, `\orcid`, `\address[A]`, `\runauthor`, `\begin{abstract}`,
  `\begin{keyword}\kwd{...}`. All present and well formed.
- Bibliography: `\bibliographystyle{imsart-nameyear}` with author-year
  natbib, the official STS author-year style. Renders correctly (52 bibitems
  with imsart's \bauthor/\bsnm markup).
- Theorem environments are declared inside `\startlocaldefs...\endlocaldefs`
  as imsart requires, and remarks use the definition style (imsart forbids
  \theoremstyle{remark}); the main.tex comment documents this correctly.

The reformat is faithful: the abstract is byte-identical to the article-class
backup and the section inputs are unchanged, so the conversion changed only
the class and frontmatter markup. This is a clean class migration, exactly
what STS/Statistics Surveys require, done before submission.

## Conventions

- Em-dash (U+2014): PASS. 0 occurrences across main.tex and all seven
  section files (and refs.bib). Verified by grep for the literal character.
- Vanity counts: PASS. The numbering present is structural (five corollaries,
  six domains, three conditions), not achievement-scale framing. No
  page/reference/direction counts used as filler.

## Submission-grade verdict for Statistical Science

YES. The build is production-clean on the venue's own required class, all
references and labels resolve, all results render with correct numbering, the
glyph table renders, and conventions pass. There is no build-blocker and no
formatting gap. The format gap noted in the venue analysis (article -> imsart
class swap) is now closed: the paper is on the imsart sts class. The same
file serves the Statistics Surveys backup (same template).

## Residual format items

None at any severity. The non-bib content suggestions live in the other
specialist reports; from a pure build/format standpoint the manuscript is
ready to submit.
