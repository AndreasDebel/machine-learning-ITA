import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# Second point set from the exercise
X = np.array(np.matrix('4,450;5,600;6,700;4.5,550;4.9,500;5,650;5.5,500;5.25,525;4.25,625;4.75,575'))
y = np.array(np.matrix('0;1;1;0;0;1;0;1;1;1'))[:, 0]

C = 100  # try 0.01, 1, 1000

pos = np.where(y == 1)
neg = np.where(y == 0)

plt.plot(X[pos[0], 0], X[pos[0], 1], 'ro')
plt.plot(X[neg[0], 0], X[neg[0], 1], 'bo')
plt.xlim([min(X[:, 0]), max(X[:, 0])])
plt.ylim([min(X[:, 1]), max(X[:, 1])])

logreg = linear_model.LogisticRegression(C=C)
model = logreg.fit(X, y)
print("C =", C, "score =", model.score(X, y))

xx = np.linspace(min(X[:, 0]), max(X[:, 0]))
yy = -(model.coef_[0, 0] / model.coef_[0, 1]) * xx - (model.intercept_[0] / model.coef_[0, 1])
plt.plot(xx, yy, 'k-')

plt.show()
