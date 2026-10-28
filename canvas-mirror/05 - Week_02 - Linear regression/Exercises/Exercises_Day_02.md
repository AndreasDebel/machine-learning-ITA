# Machine Learning - Exercises Day 2

Source: `Exercises_Day_02.pdf`, 9 pages. Header: "Machine Learning, Feb 11th, 2026"; "Sila. Sept 2nd, 2026" [sic, as printed]. Faithful transcription; code reproduced as in the PDF (including its quirks).

## Exercise 1.1
Jupyter, up and running. See exercise in `JupyterUpAndRunnng.pdf` (Canvas).

## Exercise 1.2 - Getting started
Let's start by plotting some points:

```python
import matplotlib.pyplot as plt
import numpy as np

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

plt.plot(X,y, "b.")
plt.axis([0,2,0,15])
plt.plot()
plt.show()
```

See (check) that X and y are arrays as expected.

Notice:

```python
import numpy
a = [1, 1, 1 ,1, 1]
ar = numpy.array(a)
print ar + 2
```

gives `[3, 3, 3, 3, 3]` (Python 2 print syntax in the PDF).

Many resources exist on how numpy arrays work, e.g. https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf (also in `Python/Numpy_Python_Cheat_Sheet.pdf`).

## Exercise 1.3 - Intuition about the cost function
Find a hypothesis h_theta(x) = theta0 + theta1*x that minimizes the cost function. Given X and y as in 1.2, assume theta0 in range [1,10] and theta1 in range [0.5,5]. Calculate the cost function for these theta values. One numpy version:

```python
def cost(a,b,X,y):
    ### Evaluate half MSE (Mean square error)
    m = len(y)
    error = a + b*X - y
    J = np.sum(error ** 2)/(2*m)
    return J
```

Use this or your own implementation; verify that it works. Intervals to investigate:

```python
ainterval = np.arange(1,10, 0.05)
binterval = np.arange(0.5,5, 0.05)
```

Step through them:

```python
for atheta in ainterval:
    for btheta in binterval:
        print("xy: %f:%f:%f" % (atheta,btheta,cost(atheta,btheta, X, y)))
```

Questions: What do you find? What are the best values for theta? Experiment with the parameters, change the intervals and the step value from 0.05 to higher and smaller values.

## Exercise 1.4 - Plot the cost function
A plot of the cost function helps build intuition about where local minima are. Pick any tool you like; Python example below (library versions may behave differently). Make small alterations/improvements and figure out what it does; i.e. make a number of plots that allow you to "zoom" in on the solution.

*[Figure p.3: 3D surface plot of cost vs. Theta0 (-10..10) and Theta1, bowl-shaped, cost axis up to ~350.]*

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def cost(a,b):
    ### Evaluate half MSE (Mean square error)
    m = len(Ydots)
    error = a + b*Xdots - Ydots
    J = np.sum(error ** 2)/(2*m)
    return J

Xdots = 2 * np.random.rand(100, 1)
Ydots = -5 + 7 * Xdots + np.random.randn(100, 1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ainterval = np.arange(-10,10, 0.05)
binterval = np.arange(-10,10, 0.05)
X, Y = np.meshgrid(ainterval, binterval)
zs = np.array([cost(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)
ax.set_xlabel('Thete0')   # [sic]
ax.set_ylabel('Theta1')
ax.set_zlabel('Cost')
plt.show()
```

## Exercise 1.5 - Gradient descent
We would like a method to find theta0 and theta1 precisely: gradient descent. Math is given, not derived: apply partial derivatives of the cost function with respect to theta0 and theta1 to point to the lowest point. A derivative of zero means a local minimum or maximum; the closer to zero, the better. Looking at the plot from 1.4, there appear to be no other local minima (not proven).

*[Figure p.5: 1D bowl J(w) with initial weight on the slope, gradient tangent line, and "Global cost minimum Jmin(w)" at the bottom.]*

Update function (alpha = learning rate):

    theta_j := theta_j - alpha * d/d theta_j J(theta0, theta1)    (for j = 0 and 1)

Derivatives (handwritten in the PDF):

    j=0:  d/d theta0 J(theta0,theta1) = 1/m * sum_{i=1..m} (h_theta(x^(i)) - y^(i))
    j=1:  d/d theta1 J(theta0,theta1) = 1/m * sum_{i=1..m} (h_theta(x^(i)) - y^(i)) * x^(i)

In Python:

```python
theta0_gradient = (2/N) * sum(y_hypothesis - y)
theta1_gradient = (2/N) * sum(X * (y_hypothesis - y))
```

Update:

```python
theta0_current = theta0_current - (learning_rate * theta0_gradient)
theta1_current = theta1_current - (learning_rate * theta1_gradient)
```

Question: Why is there a minus sign here? What happens if you switch the sign in front of the learning rate?

Program:

```python
import matplotlib.pyplot as plt
import numpy as np

def linear_regression(X, y, theta0=0, theta1=0, epochs=10000, learning_rate=0.0001):
    N = float(len(y))
    for i in range(epochs):
        y_hypothesis = (theta1 * X) + theta0
        cost = sum([data**2 for data in (y-y_hypothesis)]) / N
        theta1_gradient = -(2/N) * sum(X * (y - y_hypothesis))
        theta0_gradient = -(2/N) * sum(y - y_hypothesis)
        theta0 = theta0 - (learning_rate * theta0_gradient)
        theta1 = theta1 - (learning_rate * theta1_gradient)
    return theta0, theta1, cost

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

theta0, theta1, cost = linear_regression(X, y, 0, 0, 1000, 0.01)

plt.plot(X,y, "b.")
plt.axis([0,2,0,15])
# lets plot that line:
#X_new = np.array([[0],[2]])
#X_new_b = np.c_[np.ones((2,1)), X_new]
#y_predict = X_new_b.dot([theta0, theta1])
#plt.plot(X_new, y_predict, "g-")
```

*[Figure p.6: scatter of blue points with a green fitted line rising from ~4 at x=0 to ~10 at x=2.]*

Tasks: Understand what the program does, run it, check you get the expected values. Experiment with data size and learning rates; does it work as expected?

## Exercise 1.6 - Normal equation and scikit-learn
A mathematical equation gives the result directly. See p. 116 (v2) in Hands-On ML: Equation 4-4, Normal Equation: theta-hat = (X^T . X)^(-1) . X^T . y. Take it as given; the book shows the Python version:

```python
import matplotlib.pyplot as plt
import numpy as np

X = 2 * np.random.rand(50, 1)
y = 4 + 3 * X + np.random.randn(50, 1)

X_b = np.c_[np.ones((50, 1)), X]
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

X_new = np.array([[0],[2]])
X_new_b = np.c_[np.ones((2,1)), X_new]
y_predict = X_new_b.dot(theta_best)

plt.plot(X,y, "g.")
plt.axis([0,2,0,15])
plt.plot(X_new, y_predict, "r-")

plt.plot()
plt.show()
```

Go through the steps and check the result looks right; a small gist of the math is fine.

Scikit-learn makes it easier:

```python
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

X = 2 * np.random.rand(500, 1)
y = 4 + 3 * X + np.random.randn(500, 1)

lm = linear_model.LinearRegression()
model = lm.fit(X,y)

plt.plot(X,y, "g.")
plt.axis([0,2,0,15])

#fit function
f = lambda x: lm.coef_*x + lm.intercept_
plt.plot(X,f(X), c="red")
plt.plot()
plt.show()
```

Go through the steps and verify it works as expected.

## Exercise 1.7 - Polynomial regression
Work through the polynomial regression example on p. 130 (v2) in Hands-On ML to see that models can fit more complex data than a straight line. Something along these lines:

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X = 6 * np.random.rand(100, 1) - 3
y = 0.5 * X * X + X + 2 + np.random.randn(100, 1)

plt.plot(X,y, "g.")
plt.axis([-3,3,0,10])

poly_features = PolynomialFeatures(2, include_bias=False)
X_poly = poly_features.fit_transform(X)

lm = LinearRegression()
lm.fit(X_poly, y)

#fit function
f = lambda x: lm.coef_[0][1]*x*x + lm.coef_[0][0]*x + lm.intercept_
plt.plot(X,f(X), "b.")
plt.show()
```

Extra task: try a 3rd-degree polynomial: redo the exercise with points where a 3rd-degree polynomial gives the best fit, Y = a * x^3 + b * x^2 + c*x + d.
