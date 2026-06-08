# Citation Verifier Report

**Paper**: One consistency theorem for coarsened-data maximum likelihood
**Date**: 2026-06-08

## Summary

Bibliography integrity is clean. All 27 keys cited in the sources are defined in
refs.bib, and all 27 defined keys are cited (no orphans, no undefined). BibTeX
emitted zero warnings (main.blg). No undefined-citation or undefined-reference
messages in main.log. Classical references (Heitjan-Rubin, Gill-vdL-Robins,
Teicher, van der Vaart, Tsiatis, Meilijson, Rogan-Gladen, Hui-Walter,
Dawid-Skene, Ratner, Cable, Wasserman-Zhou, Dwork-Roth, Jiang) carry correct
years and venues as spot-checked. The substantive issues are two missing
domain-anchor citations and one deliberate-but-noted URL-only sibling.

## Verification method
- Extracted every \cite[tp] key from main.tex and sections/ (27 unique).
- Extracted every @entry key from refs.bib (27).
- Diffed: exact match, no orphans either direction.
- Read main.blg: "warning$ -- 0", no errors.
- Scanned main.log for undefined: none substantive (only harmless Font-shape
  lines).

## Findings

### [MAJOR] MUSK benchmark named but its foundational MIL paper is uncited
**Location**: applications.tex:108 ("a MUSK1/MUSK2 application"); cor:mil and the
MIL subsection cite only towell2026milcoarsening.
**Problem**: the MUSK1/MUSK2 datasets and the multiple-instance problem itself
originate with Dietterich, Lathrop & Lozano-Perez (1997), "Solving the multiple
instance problem with axis-parallel rectangles," Artificial Intelligence
89(1-2):31-71. Naming MUSK without citing its source is a citation gap a MIL
referee will catch immediately, and MIL is the one domain in the paper with no
external anchor citation at all (every other domain cites a classical source).
**Suggestion**: add Dietterich et al. (1997) to refs.bib and cite it where MUSK
is named (applications.tex) and ideally where the noisy-OR/MIL model is
introduced (cor:mil). Optionally add one noisy-OR-MIL reference (Viola, Platt &
Zhang 2005; or Zhang & Goldman 2001, EM-DD) so the model has a named ancestor.

### [MINOR] mil-coarsening sibling cited by GitHub URL, no DOI
**Location**: refs.bib:130-137 (towell2026milcoarsening, publisher = GitHub,
url = github.com/queelius/mil-coarsening, note "Zenodo concept DOI pending
deposit").
**Status**: this is DELIBERATE and disclosed (the brief and the bib comment both
say MIL has no Zenodo concept DOI yet; interim). Not an error. Flagged only so
the area chair tracks it: the other six siblings cite Zenodo concept DOIs, so
the MIL sibling is the lone URL-only reference and is also the deferral target
for the MIL exponential-family claim (see methodology-auditor). Before
submission, depositing it and swapping in the concept DOI would remove the one
non-archival citation. No action required for internal consistency now.

### [MINOR] Optional continuous-CAR lineage citation
**Location**: framework.tex:26-30 (the discrete-to-continuous "same object at
different cardinalities" move); discussion.tex:111-115 (relation to CAR).
**Problem**: the paper extends CAR from discrete candidate sets to a continuous
kernel-weighted continuum (for DP) but cites only the discrete-era CAR
foundations (Heitjan-Rubin, Gill-vdL-Robins, Little-Rubin). The continuous-CAR
references (Jacobsen & Keiding 1995; Nielsen 2000) are the natural anchors for
that extension.
**Suggestion**: optional. One cite to Jacobsen-Keiding or Nielsen where the
continuum candidate set is introduced would close a gap a CAR-foundations
referee might raise. Not required for acceptance.

### [SUGGESTION] Optional exponential-family-foundations cite
The regime-(A) machinery cites only van der Vaart (1998). A single Brown (1986,
IMS Lecture Notes, Fundamentals of Statistical Exponential Families) or
Barndorff-Nielsen (1978) cite would strengthen the exponential-family footing.
Optional.

## Bibliographic spot-checks (no errors found)
- teicher1961maximum: Ann. Math. Statist. 32(4):1214-1222, 1961, DOI
  10.1214/aoms/1177704861. Correct, and correctly used for the Gaussian-iff
  characterization.
- meilijson1981: J. Appl. Probab. 18(4):829-838, DOI 10.2307/3213058. Correct.
- tsiatis1975: PNAS 72(1):20-22. Correct, used for competing-risks
  nonidentifiability.
- ratner2016data: NeurIPS 29, 2016. Correct.
- cable2021robust: Nature Biotechnology 40(4):517-526. Correct (RCTD).
- All sibling Zenodo DOIs are formatted as concept DOIs per the family
  convention; not independently resolved here but internally consistent with the
  state file's sibling table.
