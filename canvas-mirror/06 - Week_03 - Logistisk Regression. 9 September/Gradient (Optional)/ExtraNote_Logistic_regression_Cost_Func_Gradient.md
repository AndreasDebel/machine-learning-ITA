# Regression with Numerical Optimization. Logistic regression

Source: `Gradient (Optional)/ExtraNote_Logistic_regression_Cost_Func_Gradient.pdf`, 8 pages. Header "CSG220 Machine Learning Fall 2008", "based on a document by Andrew Ng, October 3, 2014". Condensed summary (math symbols reconstructed from garbled extraction).

Notation check (page images): the note writes weights as w^d (superscript), data as x_t^d, and uses **lambda** (not alpha) for the learning rate: w^j := w^j - lambda dJ/dw^j; single point w^j := w^j - lambda (h_w(x) - y) x^j; logistic gradient ascent w^j := w^j + lambda (y_i - h_w(x_i)) x_i^j. In the sections below read "alpha" as that lambda. Figure 6.18 (p.3): four parabola plots - eta < eta_opt (slow convergence), eta = eta_opt (one step), eta_opt < eta < 2 eta_opt (oscillates but converges), eta > 2 eta_opt (diverges). Figure 1 (p.2): parabola with dotted steps x0=3, x1, x2, x3 toward the minimum at 2. Figure 3 (p.6): S-shaped sigmoid. Probabilistic section: errors eps_t = h(x_t) - y_t ~ N(0, sigma^2); l(w) = m log(1/(sqrt(2 pi) sigma)) - (1/(2 sigma^2)) sum (h_w(x_t) - y_t)^2. Hessian entries sum_t x_t^i x_t^j.

## 1 Linear regression
- Example: houses with features x1 = living area (ft2), x2 = #bedrooms; label = price (1000$s): (2104, 3 -> 400), (1600, 3 -> 330), (2400, 3 -> 369), (1416, 2 -> 232), (3000, 4 -> 540).
- Hypothesis h_w(x) = w0 + w1 x1 + w2 x2 = sum_d w_d x_d with dummy x0 = 1. Cost: squared error J(w) = sum_t (h_w(x_t) - y_t)^2 (least squares).

## 2 Least mean squares via gradient descent
- Update w_j := w_j - alpha dJ/dw_j; alpha = learning rate. Toy example J(x) = (x-2)^2 + 1, x0 = 3, alpha = 0.25: x1 = 2.5, x2 = 2.25, x3 = 2.125. *[Figures p.2: gradient-descent iterations; effect of different learning rates.]*
- With J = 1/2 sum (h - y)^2: single-point rule w_j := w_j - alpha (h_w(x) - y) x_j.
- Batch gradient descent: sum over all points per update. Stochastic (online) gradient descent: update per data point; often faster in practice; may "dance" around the optimum without converging (unlikely).
- J is convex (Hessian = X^T X is positive semi-definite), so a local minimum is the global minimum.

## 3 Probabilistic interpretation
- Assuming errors IID N(0, sigma^2), maximizing the log-likelihood is equivalent to minimizing mean squared error.

## 4 Classification and logistic regression
- Binary labels y in {0,1}. Plain linear regression is a poor fit (non-linear, outputs outside [0,1]).
- 4.1 Logistic (sigmoid) function g(z) = 1/(1+e^-z); derivative g'(z) = g(z)(1 - g(z)). *[Figure 3: S-curve from 0 to 1 over z in -6..6.]*
- 4.2 Hypothesis h_w(x) = g(w^T x). P(y=1|x;w) = h, P(y=0|x;w) = 1-h; combined P(y|x;w) = h^y (1-h)^(1-y). Likelihood L(w) = prod_i h(x_i)^y_i (1-h(x_i))^(1-y_i); log-likelihood l(w) = sum_i y_i log h(x_i) + (1-y_i) log(1 - h(x_i)). Maximize by gradient ascent.
- Gradient for one point: dl/dw_j = (y - h_w(x)) x_j. Stochastic gradient ascent: w_j := w_j + alpha (y_i - h_w(x_i)) x_ij; batch: sum over i.

## 4.3 Newton's method
- Uses first and second derivative (second-order Taylor expansion): w := w - f'(w)/f''(w); multi-dimensional w := w - H^-1 grad f(w), H = Hessian (H_ij = d2f/dw_i dw_j). Needs fewer iterations than batch gradient descent, but inverting the Hessian is costly for large d; quasi-Newton methods such as BFGS approximate it.
