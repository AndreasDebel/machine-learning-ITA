# Exercises Day 3 (Machine Learning, Week 3 - Logistic Regression)

Source: `Exercises/Exercises_Day_03.pdf`, 11 pages, "Machine Learning, Sept 9th, 2026", author Sila. Companion scripts in the same folder: `Exercise31.py`, `Exercise31_Extra.py`, `Exercise32.py`, `Exercise33.py`, `Exercise34.py`, `Exercise35.py`, `Exercise35b.py`, `forge_dataset.py`, `Exercise_Iris_Precision.py`. Figures in the PDF: a scatter plot with decision line (3.1), a decision-boundary sketch (3.2), mesh/contour plots (3.3, 3.4), iris plots (3.5).

Figures seen on page images:
- *[p.2 shaded box (3.1): "You want to plot theta^T X = 0, where X is the vector containing (1, x, y). That is, you want to plot the line defined by theta[0] + theta[1]*x + theta[2]*y = 0. Solve for y: y = -(theta[0] + theta[1]*x)/theta[2]".]*
- *[p.3 (3.2): scatter of red (pass) and blue (fail) points, axes about 30-100, with a black diagonal decision line sloping down from upper left to lower right.]*
- *[p.6 (3.4): forge dataset scatter, x about 8-12, y about -1 to 5.5; orange triangles (upper group) and blue circles (lower group).]*
- *[p.7-8 (3.5): photo of an iris flower, labelled flower-part diagrams (petal, sepal), and a 4x4 scatter-matrix with histograms on the diagonal for sepal-length, sepal-width, petal-length, petal-width.]*

## Exercise 3.1

A binary classifier separates two classes using a line, a plane or a hyper-plane. In a linear model the prediction is made according to

`y = w[0]*x[0] + w[1]*x[1] + ... + w[p]*x[p] + b > 0`

If the function is smaller than zero predict class -1 (Type 1); if larger than zero predict class +1 (Type 2). There are many ways to find the coefficients w and the intercept b. A decision boundary is found where y = 0.

Try it with logistic regression. First plot some points:

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# Array of points with a classification
X = np.array(np.matrix('6,350; 2.5, 400;4.5,500; 3.5,350;
2,300;4,600;7,300;5,500;5,400;6,400;3,400;4,500;1,200;3,400;7,700;3,550;2.5,650'))
y = np.array(np.matrix('0;0;1;0;0;1;1;1;0;1;0;0;0;0;1;1;0'))[:,0]

pos=np.where(y==1)
neg=np.where(y==0)

plt.plot(X[pos[0],0], X[pos[0],1], 'ro')
plt.plot(X[neg[0],0], X[neg[0],1], 'bo')
plt.xlim([min(X[:,0]),max(X[:,0])])
plt.ylim([min(X[:,1]),max(X[:,1])])
plt.plot
plt.show()
```

Then use sklearn to find the weights:

```python
logreg = linear_model.LogisticRegression(C=1000)
model = logreg.fit(X, y)
# model.coef_[0,0]*x + model.coef_[0,1]*y + model.intercept_[0] = 0
# y = - ( model.coef_[0,0]*x + model.intercept_[0]) / model.coef_[0,1]
xx = np.linspace(1, 7)
yy = - (model.coef_[0,0] / model.coef_[0,1]) * xx - ( model.intercept_[0] / model.coef_[0,1])
plt.plot(xx, yy, 'k-')
```

Afterwards try a slightly different set of points:

```python
X = np.array(np.matrix('4,450;5,600;6,700;4.5,550;4.9,500;5,650;5.5,500; 5.25,525; 4.25,625; 4.75,575'))
y = np.array(np.matrix('0;1;1;0;0;1;0;1;1;1'))[:,0]
```

The trade-off parameter that determines regularization strength is C; higher C = less regularization (the regularization function can be specified). C is the inverse of regularization strength (lambda). Higher C values risk overfitting. **Task: try adjusting C.**

## Exercise 3.2

Techniques above work on more realistic data: the "exam dataset" - scores for students on two exams (0..100 points each) plus whether they passed the course. Beginning of the dataset (exam1, exam2, passed):

```
34.62365962451697,78.0246928153624,0
30.28671076822607,43.89499752400101,0
35.84740876993872,72.90219802708364,0
60.18259938620976,86.30855209546826,1
79.0327360507101,75.3443764369103,1
45.08327747668339,56.3163717815305,0
61.10666453684766,96.51142588489624,1
75.02474556738889,46.55401354116538,1
76.09878670226257,87.42056971926803,1
84.43281996120035,43.53339331072109,1
95.86155507093572,38.22527805795094,0
75.01365838958247,30.60326323428011,0
82.30705337399482,76.48196330235604,1
69.36458875970939,97.71869196188608,1
39.53833914367223,76.03681085115882,0
53.9710521485623,89.20735013750205,1
69.07014406283025,52.74046973016765,1
67.94685547711617,46.67857410673128,0
70.66150955499435,92.92713789364831,1
76.97878372747498,47.57596364975532,1
67.37202754570876,42.83843832029179,0
89.67677575072079,65.79936592745237,1
50.534788289883,48.85581152764205,0
34.21206097786789,44.20952859866288,0
77.9240914545704,68.9723599933059,1
62.27101367004632,69.95445795447587,1
80.1901807509566,44.82162893218353,1
93.114388797442,38.80067033713209,0
61.83020602312595,50.25610789244621,0
38.78580379679423,64.99568095539578,0
61.379289447425,72.80788731317097,1
85.40451939411645,57.05198397627122,1
52.10797973193984,63.12762376881715,0
52.04540476831827,69.43286012045222,1
40.23689373545111,71.16774802184875,0
54.63510555424817,52.21388588061123,0
33.91550010906887,98.86943574220611,0
64.17698887494485,80.90806058670817,1
74.78925295941542,41.57341522824434,0
```

Transform (some of) the data to the right format (first 21 rows are used in the PDF):

```python
X = np.array(np.matrix('34.62365962451697,78.0246928153624;30.28671076822607,43.89499752400101;
35.84740876993872,72.90219802708364;60.18259938620976,86.30855209546826;79.0327360507101,75.3443764369103;45.08327747668339,56.3163717815305;
61.10666453684766,96.51142588489624; 75.02474556738889,46.55401354116538; 76.09878670226257,87.42056971926803;84.43281996120035,43.53339331072109;
95.86155507093572,38.22527805795094; 75.01365838958247,30.60326323428011; 82.30705337399482,76.48196330235604; 69.36458875970939,97.71869196188608;
39.53833914367223,76.03681085115882; 53.9710521485623,89.20735013750205; 69.07014406283025,52.74046973016765; 67.94685547711617,46.67857410673128;
70.66150955499435,92.92713789364831; 76.97878372747498,47.57596364975532;67.37202754570876,42.83843832029179'))
y = np.array(np.matrix('0;0;0;1;1;0;1;1;1;1;0;0;1;1;0;1;1;0;1;1;0'))[:,0]
```

**Tasks:** Plot the data. Make small adjustments to the program from 3.1 so it yields a decision boundary via logistic regression (figure in PDF shows a roughly diagonal line separating pass/fail). Experiment with the C value. Which value is best?

## Exercise 3.3

In sklearn's logistic regression one can set C, the regularization parameter, C = 1/lambda (the parameter is the inverse of lambda as used in other linear models; the higher C, the less regularized). Lambda controls the trade-off between letting the model increase complexity freely and keeping it simple: if lambda is very low or 0 the model can overfit by assigning big weights; if lambda is increased the model tends to underfit (too simple).

High C: the algorithm tries to fit the training data as well as possible, each data point must be classified correctly. Low C: the algorithm adjusts to the "majority" of data points with a simple model, perhaps too simple (underfitting).

Points:

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

X = np.array(np.matrix('2,300;4,600;7,300;5,500;5,400;6,400;3,400;4,500;1,200;3,400;7,700;3,550;2.5,650'))
y = np.array(np.matrix('0;1;1;1;0;1;0;0;0;0;1;1;0'))[:,0]

pos=np.where(y==1)
neg=np.where(y==0)

plt.plot(X[pos[0],0], X[pos[0],1], 'ro')
plt.plot(X[neg[0],0], X[neg[0],1], 'bo')
plt.xlim([min(X[:,0]),max(X[:,0])])
plt.ylim([min(X[:,1]),max(X[:,1])])

plt.show()
```

Insert, just before `plt.show()`, classifier code:

```python
logreg = linear_model.LogisticRegression(C=10000)

h = .02 # step size in the mesh

# we fit the data.
logreg.fit(X, y)

score= logreg.score(X, y)

# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, x_max]x[y_min, y_max].
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Ravel() return a contiguous flattened array.
# Predict the color for each x,y point
Z = logreg.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot. Reshape point to xx format
Z = Z.reshape(xx.shape)

# figure(Num = our figure number, figsize=(1,1)) creates an inch-by-inch image
plt.figure(1, figsize=(4, 3))
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)
```

**Tasks:** Understand the code. Investigate the `score` value - what is it? Print it. Change/tune C; try at least 5-10 C values to see what happens. Are the statements in the introduction to this exercise correct?

## Exercise 3.4

Small synthetic datasets are useful for highlighting aspects of ML algorithms. Andreas Mueller (author of "Introduction to ML with Python") made the "forge dataset" available at https://github.com/amueller/introduction_to_ml_with_python/tree/master/mglearn . A version of the script (`forge_dataset`) is on Canvas. Run it with different values in the `make_forge` method.

Code to classify the data (make it work, understand the idea in broad strokes, think about adapting it to similar problems):

```python
# Use logistic regression for classification
model = LogisticRegression().fit(X, y)

x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

# evenly spaced numbers over a specified interval
xx = np.linspace(x_min, x_max, 1000)
yy = np.linspace(y_min, y_max, 1000)

#coordinate matrices from coordinate vectors
X1, X2 = np.meshgrid(xx, yy)
#contiguous flattened array
X_grid = np.c_[X1.ravel(), X2.ravel()]
#Predict confidence scores for samples.
#A plane of equal probability, where the model has determined
#both target classes are equally likely.
decision_values = model.decision_function(X_grid)

#A contour plot displays line with equal likelyhood, draw decision boundary
axes.contour(X1, X2, decision_values.reshape(X1.shape), levels=[0],
          colors="black", alpha=1, linewidths=None,
          linestyles="solid", zorder=5)
```

**Tasks:** Try non-default C values (re-introduce a C setting), 3-4 different values. Redo with different forge sets, i.e. different `random_state` and `n_samples` in `make_forge`.

## Exercise 3.5

(Preferably) discuss code and results in groups of 2-3; add extra print statements to clarify the code.

Iris Data Set (https://archive.ics.uci.edu/ml/datasets/Iris): "This is perhaps the best known database to be found in the pattern recognition literature"; "A good project because it is so well understood". Bullets: a classification problem, an easier type of supervised learning; only 4 attributes and 150 rows (fits in memory, on a screen or A4 page); all numeric attributes in the same units and scale, so no scaling or transforms needed.

Load:

```python
import pandas
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)
```

If that causes problems, download `iris.data` locally and point the url there, or use `from sklearn.datasets import load_iris; iris = load_iris()`.

Inspect: `print(dataset.shape)`, `print(dataset.head(20))`, `print(dataset.describe())`; histograms `dataset.hist(); plt.show()`; scatter matrix `scatter_matrix(dataset); plt.show()`.

Classify using only petal-width:

```python
array = dataset.values
X = array[:,3] # petal width
Y = array[:,4] # classification

# Make y into numbers
a_enc = pandas.factorize(Y)
yvalues = a_enc[0]

y = []
for i in yvalues:
 if i == 2:
    y = np.append(y,[1])
 else:
    y = np.append(y,[0])

# l2 is default,
# Intuitively, the model will be adjusted to minimize single outlier case,
# at the expense of many other common examples
log_reg = LogisticRegression(penalty="l2")
log_reg.fit(X.reshape(-1, 1),y)

plt.plot(X,y,"b.")

X_new = np.linspace(0,3,1000).reshape(-1,1)
y_proba = log_reg.predict_proba(X_new)

plt.plot(X_new,y_proba[:,1],"g-",label="Iris-Virginica")
plt.plot(X_new,y_proba[:,0],"b--",label="Not Iris-Virginca")   # [sic]
plt.xlabel("Petal width", fontsize=14)
plt.ylabel("Probability", fontsize=14)
plt.legend(loc="upper left", fontsize=14)
plt.show()
```

**Tasks:** test/verify the code; try a few examples by hand from the dataset and check results; print the whole dataset instead of 20 rows; change default `l2` to `l1` regularization and see if the graph is better (no precise math needed).

Then plot both petal-width and petal-length:

```python
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

iris = datasets.load_iris()

X = iris["data"][:,(2,3)] # petal length, petal width
yy = iris["target"]

y = []
for i in yy:
 if i == 2:
    y = np.append(y,[1])
 else:
    y = np.append(y,[0])

#model = LogisticRegression(multi_class="multinomial", solver="lbfgs", C=5)
model = LogisticRegression(C=1000)
model.fit(X,y)

plt.plot(X[:, 0][y==1], X[:, 1][y==1], "y.", label="Virginica")
plt.plot(X[:, 0][y==0], X[:, 1][y==0], "b.", label="Setosa or versicolor")

plt.legend(loc="upper left", fontsize=14)
plt.xlabel("Petal length", fontsize=14)
plt.ylabel("Petal width", fontsize=14)

xx = np.linspace(1, 6)
yy = - (model.coef_[0,0] / model.coef_[0,1]) * xx - ( model.intercept_[0] / model.coef_[0,1])

plt.plot(xx, yy, 'k-')
plt.show()
```

**Tasks:** Verify the plot supports the findings from the previous plot. Change the program to solidify understanding. Try other LogisticRegression parameters (C etc.). "Write down you findings" [sic]. Reference: http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html
