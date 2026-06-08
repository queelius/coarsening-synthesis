# Format Validator Report

Date: 2026-06-03
Checks run directly: full build, undefined-reference scan, label/cref
resolution, PDF unresolved-marker scan, abstract length, frontmatter, venue
formatting posture, convention compliance (no em-dash, no vanity counts).

## Verdict summary
- Build: PASS. make paper -> exit 0, 13 pages.
- Undefined references: 0.
- Label/cref resolution: all 28 labels defined; 0 broken crefs; 0 "??" in PDF.
- Bibtex: 0 warnings.
- Conventions (no U+2014 em-dash, no vanity counts): PASS.
- Venue formatting: currently generic article 11pt; acceptable for submission
  to Statistical Science (which uses its own production style post-acceptance).
  One posture note below.

## 1. Build (HIGH confidence, executed)

Command: make paper (pdflatex + bibtex + pdflatex + pdflatex).
- Exit status: 0.
- Output: main.pdf, 13 pages (pdfinfo confirms; matches state.md target-ish,
  state page_target was 18, actual 13 -- shorter than planned, see note 6).
- main.log: 0 undefined-reference warnings, 0 multiply-defined labels.
- main.blg: 0 warnings, 0 errors.
Reproducible from a clean tree as shipped.

## 2. Cross-reference integrity (HIGH confidence)

- Labels defined (28): cond:c1/c2/c3; cor:dp/phenotype/scrna/spatial/weaksup;
  prop:singleton; rem:loc-sketch; sec:* (7); tab:css/reduction/singletons;
  thm:general-consistency; thm:general-rank; eq:* (5).
- All \cref / \eqref targets resolve to a defined label (comm diff of
  referenced vs defined: empty -> no dangling references).
- PDF body: 0 occurrences of "??" (no unresolved refs rendered).
- cleveref + hyperref: configured correctly (\crefname/\Crefname for
  condition); links colored (linkcolor/citecolor/urlcolor blue). The 3-pass
  build resolves all cleveref forward references (the "rerun" notes in the log
  are the standard intermediate-pass messages, cleared by pass 3).

## 3. Document structure

- documentclass[11pt,letterpaper]{article}, geometry margin=1in. Clean.
- Packages: amsmath/amsthm/amssymb, mathtools, bm, booktabs, enumitem,
  microtype, hyperref, natbib, cleveref. Standard, no conflicts, no obsolete
  packages.
- Theorem environments: theorem/proposition/lemma/corollary (plain),
  definition/condition (definition), remark (remark). Counters as intended.
- Frontmatter: \title, \author (with ORCID hyperlink), \maketitle, \date{\today}
  all present. abstract present (281 words; within typical journal limits,
  though Statistical Science abstracts are often shorter -- consider trimming
  to ~200 if the venue specifies, MINOR).
- Three tables (tab:css, tab:reduction, tab:singletons) via booktabs, all with
  captions and labels, all referenced. Float placement [ht]. No figures (by
  design; synthesis paper).
- Bibliography: abbrvnat, footnotesize, tight bibsep. Fine.

## 4. Convention compliance (project hooks)

- Em-dash (U+2014): NONE in any source file (state.md em_dash_check PASS;
  re-confirmed by scan). All ranges use -- (en-dash) or commas/parens. PASS.
- Vanity counts: the enumerations ("five named theorems," "six fields," "six
  singleton devices") are descriptive structure, not achievement-scale
  framing. No "N references," "N pages," "N directions" filler. PASS. (Note:
  the 5-vs-6 slippage is a clarity item for prose/novelty, not a vanity-count
  violation.)

## 5. Venue formatting posture (Statistical Science)

Statistical Science accepts submissions in a generic format and applies its IMS
production style (imsart) after acceptance, so the current article-class
manuscript is submittable as-is. No action required pre-submission. IF the
author wants to pre-empt: IMS provides imsart-stat.cls; converting is a
post-acceptance nicety, not a submission requirement. Leave as generic for now.

One posture note: Statistical Science papers typically carry a discussion/
rejoinder format and run longer; a 13-page synthesis is on the short side for
the venue. This is a substance question (see methodology/novelty: the
rank/singleton proofs are sketches; expanding them and adding the
moment-matching-defense paragraph would naturally bring length toward the
venue's norm). Not a formatting defect.

## 6. Page count vs plan

state.md page_target: 18; actual: 13. The paper is 5 pages under its own
target. Combined with the specialists' recommendations to (a) add a
moment-matching-defense paragraph, (b) reframe the seam table with positive
framing, (c) split the T definition by regime, (d) optionally expand the
rank/singleton sketches, the paper will grow toward its target naturally. Not a
defect, but the shortfall is consistent with the "sketches, not full proofs"
status and supports the reviewers' view that there is room to strengthen
without bloating.

## Format-validator findings list
- NO build, reference, or convention failures. Clean throughout.
- MINOR: abstract 281 words; trim toward ~200 if the venue specifies a limit.
- MINOR (optional): unused dwork2006calibrating in bib (also flagged by
  citation-verifier) is the only bib hygiene item.
- POSTURE: 13 pp is short for Statistical Science; substance additions
  recommended by other specialists will close the gap. No formatting change
  needed pre-submission.

Confidence: HIGH (all checks executed against the live source and PDF).
