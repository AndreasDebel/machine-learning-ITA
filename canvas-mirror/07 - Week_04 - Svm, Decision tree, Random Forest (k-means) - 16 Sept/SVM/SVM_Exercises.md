# SVM exercises

Source: `SVM_Exercises.pdf` (4 pages). "Machine Learning, March 10th, 2023. Sila, March 2023." In groups of 2-3.

## Exercise 1
What is the intuition behind an SVM? Run `SVM_1.py` to get an intuition: a dataset where linear classification is impossible; a function "lifts" some data to higher dimensions, which may change this.

## Exercise 2
Sometimes linear classification is impossible; an SVM (with a kernel) can help, but it also works for linear separation. Use Iris with the first two features: sepal length and sepal width. A kernel is a function given to the ML algorithm (not limited to SVMs).

Code (`SVM_2.py` on Canvas), summarized: load iris, `X = iris.data[:, :2]`; make a binary target (class 2 -> 1, else 0); mesh step `h = .02`; `C = 1.0`; `svc = svm.SVC(kernel='linear', C=C).fit(X, y)`; commented alternatives: `SVC(kernel='rbf', gamma=0.7, C=C)`, `SVC(kernel='poly', degree=5, C=C)`, `LinearSVC(C=C)`; build meshgrid, predict on grid, `plt.contourf` (coolwarm), scatter training points, axis labels "Sepal length"/"Sepal width", title "SVC with linear kernel".

Tasks:
- First try the linear kernel.
- Try polynomial kernels: degrees at least 1, 3, 5 and 7, and for each degree at least a small C, C=1, and a big C. What works best?
- Try an RBF kernel with different gamma values, from 0.1 to about 100. Higher gamma = more exact fit to the training set, risk of overfitting.

## Exercise 3
Breast cancer dataset (`SVM_gamma.py`, Canvas): plots for different gamma values (SVM with rbf kernel). Note the effects on the test set (marked with x). Try different values of C and gamma.
