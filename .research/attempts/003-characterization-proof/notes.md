# Attempt 003: characterization proof (Gaussian iff) + asymptotic constant

## Tried
- functional_eq.py: reduce "identity for all samples" to functional equation (FE) on
  the sum-zero hyperplane; show n=3 case is Cauchy's equation; sympy test that odd
  cubic correction is killed; numeric FE check for linear/sign/tanh/cubic at n=3,4,5.
- rigor_boundary_cases.py: (I) Laplace via objective not score (kink-robust); (II)
  student-t nu=2 bimodal likelihood, mean is a valley (need log-concavity); (III)
  Gaussian unique max at xbar.
- asymptotic_constant.py: derive V = Var(psi(Z)/J - Z), J=E[psi'(Z)], for laplace
  (closed form V=1) and logistic (numeric); Monte-Carlo confirm at n=20000.

## Happened
- (FE) <=> Cauchy psi(r1)+psi(r2)=psi(r1+r2) <=> psi linear (continuous/monotone)
  <=> p0 Gaussian. Odd cubic killed (3 a3 = 0). FE numerically holds only for linear.
- (II) student-t nu=2 data (-4,4): two global maxima at +-3.74, mean (0) is a local
  MIN. Unimodality insufficient; log-concavity needed for unique MLE.
- (III) Gaussian: gap 0 over 20000 random samples.
- Asymptotic constant: Laplace sqrt(V)=1.000 (MC 1.004); logistic sqrt(V)=0.538
  (MC 0.530). Matches the sweep's rms*sqrt(n).

## Interpretation
Complete proof of the exact characterization (Gaussian iff), the right regularity
(log-concave for a unique MLE), and the explicit asymptotic gap law.
