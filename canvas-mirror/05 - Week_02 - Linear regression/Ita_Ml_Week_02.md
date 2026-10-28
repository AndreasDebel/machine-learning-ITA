# Machine Learning - Week 2 (lecture slides)

Source: `Ita_Ml_Week_02.pdf`, 32 slides, EAAA template, mixed Danish/English. No author/date visible. Condensed per-slide summary.

## Slides 1-4: Program and warm-up
- Today's program: Python exercises; up and running with Jupyter notebooks; linear regression.
- Python exercises: talk in groups of 2. How did the exercises go? What do you think of Python as a language so far?
- Jupyter - Up and Running: see `JupyterUpAndRunnng.pdf`. Get a Jupyter notebook running; follow `RunningJupyter_QuickGuide.pdf`, work in groups of 2 (help on the projector afterwards).

## Slides 5-11: What can Machine Learning do?
*[Figures: slide 5 school of blue fish with one red fish (anomaly); slide 8 flowchart of the traditional approach: Study the problem -> Write rules -> Evaluate -> (ok) Launch / (not ok) Analyze errors -> back to Study the problem.]*
- Detect anomalies (security, fraud).
- Healthcare second opinion: historical datasets of patient characteristics; data + algorithm create a predictive model; model assigns probabilities; patient outcome is predicted.
- Customer segmentation for targeted marketing.
- Traditional approach vs. ML approach (figures from Geron, Hands-On ML p. 5 v2).
- Use ML when (Geron p. 7 v2): problems where existing solutions need lots of hand tuning or long rule lists; complex problems with no good traditional solution; fluctuating environments (system adapts to new data); getting insights about complex problems and large data.
- How (Geron p. 22 v2): you studied the data, selected a model, trained on training data, applied the model to make predictions on new cases.
- A ML project is not necessarily linear but has known steps: 1. Define Problem, 2. Prepare Data, 3. Evaluate Algorithms, 4. Improve Results, 5. Present Results.
- Misc. techniques: linear regression, logistic regression, neural nets and more.

## Slide 12: Big picture - discussion task
In groups of 2: How would you define Machine Learning? Can you name problems where it shines, and explain why?

## Slides 13-16: Misc. techniques, big picture, LR plot
- Slide 13 (Misc. Techniques): *[Figures: scatter with fitted line (regression); two-class scatter with a linear decision boundary (logistic regression); small neural-net diagram with input layer x1..x3, +1 bias, hidden layer, output h(x).]*
- Slide 15 (Using LR): *[Figure: dense scatter of blue points with a black regression line.]*
- Slide 16: "A plot using chatGPT" - ask ChatGPT for Python code that creates a line through points where linear regression is possible. See exercise `LinearRegressionWithChatGPT`.
- *[Figure: dense scatter of blue points (x up to 1.5e7, y up to ~15000) with a black regression line through them.]*

## Slide 17: Linear regression model
- Hypothesis: h_theta(x) = theta0 + theta1 * x
- Parameters: theta0, theta1
- Cost function: J(theta0, theta1) = 1/(2m) * sum_{i=1..m} (h_theta(x^(i)) - y^(i))^2
- Goal: minimize J(theta0, theta1) over theta0, theta1.

## Slides 18-21: Exact equations
- Closed-form simple regression: a = [(sum y)(sum x^2) - (sum x)(sum xy)] / [n sum x^2 - (sum x)^2]; b = [n sum xy - (sum x)(sum y)] / [n sum x^2 - (sum x)^2]. (a here is the intercept, b the slope.)
- Normal Equation (Geron Eq. 4.4, p. 116 v2): theta-hat = (X^T X)^(-1) X^T y. More on p. 108 v2.
- Slides 19-21: "Udledning af formel" (derivation of the formula) - NOT part of the curriculum ("Ikke en del af pensum"). *[Slide 21 completes the derivation: L = (Y-Xw)^T(Y-Xw) = Y^T Y - Y^T X w - w^T X^T Y + w^T X^T X w; gradient wrt w set to 0: -2 X^T Y + 2 X^T X w = 0, so X^T X w = X^T Y and w = (X^T X)^(-1) X^T Y; uses (A+B)^T = A^T+B^T and (AB)^T = B^T A^T.]*
*[Figures: blackboard derivation with y vector, X matrix (m examples), weight vector w, error vector y_i minus (x_i1 w1 + ... + x_iN wN).]*

## Slides 22-27: Cost minimisation and gradient descent
- Slide 22: *[Figure: 3D bowl-shaped surface J(theta0,theta1) over theta0 and theta1, with cost function and goal formulas.]*
- Gradient descent algorithm: repeat until convergence { theta_j := theta_j - alpha * d/d theta_j J(theta0, theta1) for j = 0 and 1 }. alpha = learning rate.
- *[Figure: 3D surface with several hills/valleys and red step paths showing descent from different starting points toward minima.]*
- Slides 25-26 "The Gradient": the gradient at each point points in the direction of steepest ascent. Since we minimise the loss, we move in the opposite direction (steepest descent). *[Figures: paraboloid bowl with gradient arrow.]*
- Slide 27: explicit update rules: repeat until convergence { theta0 := theta0 - alpha*(1/m)*sum_i (h(x^(i)) - y^(i)); theta1 := theta1 - alpha*(1/m)*sum_i (h(x^(i)) - y^(i))*x^(i) }.

## Slide 28: The right model
Underfitting vs. overfitting. *[Figures: Price vs Size with 3 fits: straight line theta0+theta1 x (underfit), quadratic theta0+theta1 x+theta2 x^2 (good), 4th-degree polynomial wiggling through points (overfit); below, three small plots labelled Underfitting, Balanced, Overfitting.]*

## Slide 29: Regularization
Constraining a model to make it simpler and reduce the risk of overfitting is called regularization (Geron p. 29 v2).

## Slide 30: Feature scaling
ML does not perform well when inputs have very different scales. E.g. Min-Max scaling (often called normalization): values shifted and rescaled to range 0 to 1 (subtract min, divide by max - min). Geron p. 72 v2.

## Slide 31: Exercises
Today is all about linear regression. Exercises 1.2 - 1.7 (see `Exercises/Exercises_Day_02`).

## Slide 32: Homework
Do the exercises for this week. Read Geron "Hands-On Machine Learning": Chapter 1 The Machine Learning Landscape p. 3-37 (p. 3-33 v2); Chapter 4 Training models p. 131-151 (p. 113-132 v2; p. 105-126 1st ed.). Alternative: Brink et al. "Real-World Machine Learning" Ch. 1 and 2, plus p. 69-73 Linear Regression and p. 78-84 Overfitting, underfitting, cross validation.
