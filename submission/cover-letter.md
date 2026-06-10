# Cover letter: Statistical Science

Dear Editors,

I am pleased to submit "One consistency theorem for coarsened-data maximum
likelihood: a cross-domain synthesis of the coarsening-at-random framework" for
consideration as a synthesis article in Statistical Science.

The paper makes a unifying observation. A single statistical structure, coarsening
at random (the C1, C2, C3 conditions of Heitjan and Rubin 1991 and Gill, van der
Laan and Robins 1997), recurs across seven application areas that are usually
studied with separate toolkits: reliability with masked failure causes,
single-cell and spatial genomics, differential privacy, programmatic weak
supervision, electronic-health-record phenotyping, and multiple instance learning.
In each, a latent quantity is observed only through a coarsening (a candidate set,
a dropout, a noised release, a vote, a diagnostic code, a bag label), and two
results have been derived independently, once per field. I state both once at the
right generality and recover each field's version as a special case:

1. An augmented-candidate-set rank condition for identifiability, with a singleton
   candidate set (a report that pins the latent quantity) restoring identifiability
   by restoring column rank. The singleton is one mechanism wearing a different
   costume in each field (spike-ins, single-cell-resolution probes, gold labels,
   non-private releases, chart review, singleton bags).
2. A consistency identity at the maximum-likelihood fit: under coarsening at random
   the face-value likelihood may be maximized without modeling the coarsening, and
   the fit reproduces the empirical mean of a coarsening-sufficient statistic. This
   identity has appeared under six names (cell-total, spot-level, release,
   agreement, code-frequency, and bag-prevalence consistency).

I believe the work fits Statistical Science specifically because its value is
unification and organization rather than new mathematics, the genre the journal
publishes. In that spirit the paper is deliberately honest about where the
reduction is clean and where it is seamed: the consistency identity is an exact
finite-sample equality in a regular exponential family but only a population
first-moment identity (exact for the Gaussian kernel) in a location family, and
two domains do not reduce cleanly (differential privacy enters through the
location-family branch, and weak supervision reduces exactly only under a
sufficiency-complete parametrization). I locate these boundaries precisely rather
than smoothing them over.

The empirical weight is carried by the sibling papers, which are cited rather than
re-derived; each is a publicly available preprint with a Zenodo concept DOI (listed
in the data-availability note). This manuscript is itself available as a preprint
(concept DOI 10.5281/zenodo.20533912, which resolves to the current version).

The manuscript is single-author work, is not under review elsewhere, and reports no
competing interests. It is prepared in the IMS imsart class with the Statistical
Science option; LaTeX source and class files accompany the submission.

Thank you for your consideration.

Sincerely,
Alexander Towell
Department of Computer Science, Southern Illinois University Edwardsville
lex@metafunctor.com, ORCID 0000-0001-6443-9897
