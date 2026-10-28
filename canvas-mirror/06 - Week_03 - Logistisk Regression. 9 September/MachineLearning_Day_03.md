# Machine Learning - Day 3 (slides)

Source: `MachineLearning_Day_03.pdf`, 37 slides, "Sila, Sept 9th 2026", Erhvervsakademi Aarhus template. Condensed per-section summary.

## Agenda (slide 2)
Comments about last week's exercises; Chicago Crimes, real-life data; introduction to Logistic Regression; starting out with Logistic Regression; comment about SVMs; exercises.

## Recap: What can ML do? (slides 3-5)
- Detect anomalies (security, fraud) *[fish-school image with one red fish]*.
- Healthcare second opinion: historical datasets of patient characteristics; data and algorithm combined into a predictive model; models assign probabilities; patient outcome is predicted.
- Customer segmentation for targeted marketing.

## ML - How (slide 6)
A project may not be linear but has known steps: 1. Define problem. 2. Prepare data. 3. Evaluate algorithms. 4. Improve results. 5. Present results.

## Misc. techniques / last week: linear regression (slides 7-9)
- Linear regression, logistic regression, neural nets and more *[three small figures: regression line, classification regions, neural net]*.
- Linear regression scatter plot with fitted line; gradient descent minimizing the cost function; repeat until convergence: theta0 := theta0 - alpha (1/m) sum (h(x_i) - y_i); theta1 := theta1 - alpha (1/m) sum (h(x_i) - y_i) x_i.
- Slide 10: "Comments to last weeks exercises?" Slide 11: "Getting to know the data - Chicago Crime" (see the exercise "Chicago crimes" on Canvas).

## Logistic regression (slides 12-26)
- Definition: logistic regression models the probability of a certain class or event existing, such as pass/fail, win/lose, alive/dead, healthy/sick *[diagram: inputs X1..X3 with weights theta -> happy/sad penguin]*.
- Figures: sigmoid fit over a scatter of 0/1 points; 2D classification regions (blue/red) with linear boundary; 3D data separated by a plane; regression line vs. classification.
- One-vs-all (one-vs-rest) for 3 classes: train one classifier h(i)(x) per class.
- Estimating probabilities (Geron p.143-144): p_hat = h_theta(x) = sigma(theta^T x); sigma(t) = 1/(1+exp(-t)) is S-shaped, outputs between 0 and 1. Prediction: y_hat = 0 if p_hat < 0.5, 1 if p_hat >= 0.5.
- Cost for a single instance (Eq. 4-16): c(theta) = -log(p_hat) if y = 1; -log(1 - p_hat) if y = 0.
- Andrew Ng: predict y=1 if h_theta(x) >= 0.5, i.e. theta^T x >= 0; y=0 if theta^T x < 0. Decision boundary example: theta = [-3, 1, 1], predict y=1 if -3 + x1 + x2 >= 0.
- Slide "A little help from chatGPT": exercise Logistic Regression and ChatGPT (see `Exercises/Exercise_LogReg_ChatGPT.md`).
- Log-loss cost (Eq. 4-17): J(theta) = -(1/m) sum [y log p_hat + (1-y) log(1-p_hat)]; no closed form, but convex, so gradient descent finds the global minimum; partial derivatives dJ/dtheta_j = (1/m) sum (sigma(theta^T x_i) - y_i) x_ij (Geron p.145). Andrew Ng: Cost(h,y) = -log h if y=1, -log(1-h) if y=0; gradient descent repeat theta_j := theta_j - alpha dJ/dtheta_j, updating all theta_j simultaneously.
- "But don't worry :) We will just use SciKit-Learn's built-in functions!"
- Exercises 3.1 & 3.2.

## Iris dataset (slides 27-29)
Quotes and bullets as in Exercise 3.5 (best known pattern-recognition database; 4 attributes, 150 rows; same units/scale); figures of an iris flower and petal/sepal diagram; link https://archive.ics.uci.edu/ml/datasets/Iris.

## Support Vector Machines (slides 30-34)
- SVM classifier = fitting the widest possible street between the classes: "large margin classification" (Geron p.156, Fig 5-1; Iris-Versicolor vs Iris-Setosa on petal length/width).
- Andrew Ng: use SVM packages (liblinear, libsvm) to solve for theta; must choose parameter C and kernel. Linear kernel ("no kernel"): predict 1 if theta^T x >= 0. Gaussian kernel: f_i = exp(-||x - l(i)||^2 / (2 sigma^2)), need to choose sigma^2 (large sigma^2: higher bias, lower variance; small: the opposite).
- Many datasets are not linearly separable; SVMs can handle some cases by adding "kernels" (Geron p.154); example in exercise 2.6, no math.
- Slide 35: "Remaining Exercises...".

## Homework (slides 36-37)
Do the week's exercises. Read Geron p.164-170 (142-147 v2) Logistic Regression, p.175-185 (153-161 v2) SVMs; Brink et al. "Real-World Machine Learning" Chapter 3, p.52-63 and p.69-76 (repeat from week 2).
