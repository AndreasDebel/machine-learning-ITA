# Extra Note: Gradient of the Logistic Regression Cost Function

Source: `Gradient (Optional)/ExtraNote_GradientLogReg.pdf`, 2 pages, "Feb 2025. ChatGPT explains..." (screenshots of formulas).

Derivation of dJ/d(theta_j) for the logistic regression cost:

- J(theta) = (1/m) * sum_i [ -y_i log h(x_i) - (1 - y_i) log(1 - h(x_i)) ].
- Step 1: differentiate the cost with the chain rule (terms -y/h * dh/dtheta_j and (1-y)/(1-h) * d(1-h)/dtheta_j).
- Step 2: h(x) = 1/(1 + e^(-theta^T x)) (sigmoid); dh/dtheta_j = h(x)(1 - h(x)) x_j.
- Step 3: substitute back and simplify: **dJ/dtheta_j = (1/m) * sum_i x_j^(i) (h(x^(i)) - y^(i))**.
- Gradient descent update: theta_j := theta_j - alpha * (1/m) * sum_i (h(x^(i)) - y^(i)) x_j^(i), where alpha is the learning rate and (h - y) is the prediction error.
