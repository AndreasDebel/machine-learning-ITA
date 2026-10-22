# -*- coding: utf-8 -*-
"""
Created on Mon February 19 18:11:34 2024

@author: sila
"""
from sklearn.tree import DecisionTreeClassifier, export_graphviz

from sklearn.datasets import make_circles;
import matplotlib.pyplot as plt

from pandas import DataFrame
# generate 2d classification dataset

X, y = make_circles(n_samples=1000, noise=0.05)
# scatter plot, dots colored by class value
df = DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
colors = {0:'red', 1:'blue'}
fig, ax = plt.subplots()
grouped = df.groupby('label')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='x', y='y', label=key, color=colors[key])
plt.show()


from timeit import default_timer as timer
start = timer()
#time the execution time for this tree.

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.20)

tree_clf = DecisionTreeClassifier(max_depth=8) ## indicate we do not want the tree to be deeper than 2 levels
tree_clf.fit(xtrain,ytrain) # training the classifier

accuracy = []
error = []

acc= tree_clf.score( xtest, ytest)
accuracy.append(acc)
print(accuracy)

#prediction
#print("probability of point = (2,1) = "+str(tree_clf.predict_proba([[2,1]])))
#print("probability of point = (4,1) = "+str(tree_clf.predict_proba([[4,1]])))
#print("probability of point = (5,2) =  "+str(tree_clf.predict_proba([[5,2]])))

end = timer()
print(end - start)

import pydotplus
from six import StringIO
import matplotlib.image as mpimg
import io

dot_data = io.StringIO()

export_graphviz(tree_clf,
                out_file=dot_data, # or put a filename here filename like "graph.dot", you then need to convert it into pgn
                feature_names=None,
                class_names=None,
                rounded=True,
                filled=True)

filename = "tree.png"
pydotplus.graph_from_dot_data(dot_data.getvalue()).write_png(filename) # write the dot data to a pgn file
img=mpimg.imread(filename) # read this pgn file

plt.figure(figsize=(8,8)) # setting the size to 10 x 10 inches of the figure.
imgplot = plt.imshow(img) # plot the image.
plt.show()