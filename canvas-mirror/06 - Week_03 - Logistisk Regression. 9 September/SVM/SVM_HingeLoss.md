# Extra Note on the "Hinge Loss" function

Source: `SVM/SVM_HingeLoss.pdf`, 3 pages, "ML, Nov. 8th 2019. Sila." Math symbols were partly lost in text extraction; reconstructed below.

- Hinge loss is a loss function for training classifiers, used for "maximum-margin" classification, most notably SVMs. c = loss function, x = sample, y = true label, f(x) = predicted label.
- Idea: maximize the distance between positive and negative points (say the distance from the optimal hyperplane to each class is 1), i.e. maximize 2/||w||, equivalently minimize ||w||/2, subject to y_i(w^T x_i + b) >= 1 - e_i, where e_i are errors (distance from the correct hyperplane in the wrong direction), so e_i >= 0.
- Optimization: minimize ||w||/2 + C * (1/n) * sum(e_i)^2.
- Hinge loss: max(1 - z_i, 0) with z_i = y_i f(x_i) = y_i (w^T x_i + b). From the constraint, e_i >= 1 - z_i and e_i >= 0, so e_i = max(1 - z_i, 0): zero when correctly classified (with margin), 1 - z_i otherwise. So the two formulations are the same: min(||w||/2 + C (1/n) sum e_i^2) and min(max(1 - z_i, 0) + ||w||), with C ~ 1/lambda. "Thus SVMs try to minimise hinge loss."
- Hinge loss penalizes wrong predictions heavily, correct-but-unconfident predictions a little, and confident correct predictions not at all. Binary form: sum_i max(0, 1 - y_i h(x_i)); labels y_i are -1 or +1, so loss is zero only when signs match and |h(x_i)| >= 1. Example: score 0.2 with label -1 gives penalty 1.2; score -0.7 (predicted -1) still gives 0.3; predicting -1.1 gives no penalty.
- Verified formulas (page images): c(x, y, f(x)) = (1 - y*f(x))_+, i.e. 0 if y*f(x) >= 1, else 1 - y*f(x). The final forms are min(||w||/2 + C (1/n) sum(e_i)^2) and min(max(1 - Z_i, 0) + lambda ||w||), with C = 1/lambda.
- *[Figure p.1: left, scatter of red circles and green plusses with a dashed line, captioned "Which hyperplane?"; right, "SVM: Maximize the margin" showing x1/x2 axes, decision boundary w^T x = 0, "negative" hyperplane w^T x = -1, "positive" hyperplane w^T x = 1, margin and support vectors circled.]*
- *[Figure p.3: red squares and blue circles in x1-x2 with an "Optimal hyperplane" line, dashed margin lines and "Maximum margin" arrow.]*
- Closing line: "What makes Support Vector Machines tick..."
