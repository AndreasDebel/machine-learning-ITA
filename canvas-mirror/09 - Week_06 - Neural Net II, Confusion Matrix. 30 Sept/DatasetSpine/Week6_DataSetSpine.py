# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 11:02:21 2021

@author: sila
"""

#This is a short example of using a MLpClassifier to predict data.
# Here using a Neural Net to predict datapoints from the Spine dataset.

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import matplotlib.pyplot as plt
import seaborn as sns

# Lower Back Pain Symptoms Dataset
# Collection of physical spine data

# Col1 - pelvic_incidence
# Col1 - pelvic tilt
# Col1 - lumbar_lordosis_angle
# Col1 - sacral_slope
# etc.
df = pd.read_csv('Dataset_spine.csv')

df = df.drop(['Unnamed: 13'], axis=1)

print(df.head())

print("Great we got some rows from the dataset...")

print(df.describe())

print("Take a moment to look at the results from the describe function ...")

df = df.drop(['Col7','Col8','Col9','Col10','Col11','Col12'], axis=1)

print(df.head())

print("Removing some rows from the dataset... Irrelevant rows...")

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

df=df.replace(to_replace="Abnormal",value="1")
df=df.replace(to_replace="Normal",value="0")

y = df['Class_att']
x = df.drop(['Class_att'], axis=1)

print("y - begin")
print(y)
print("y - end")



print("Creating the dataset we can train on...")

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.25, random_state=27)

''' clf = MLPClassifier(hidden_layer_sizes=(5,5), max_iter=500, alpha=0.0001,
                     solver='sgd', verbose=10,  random_state=21,tol=0.000000001) '''

clf = MLPClassifier(hidden_layer_sizes=(3,3))

print("Begin training")
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
print("End of training")

print(accuracy_score(y_test, y_pred))

con_mat = confusion_matrix(y_test, y_pred)

print(con_mat)

sns.heatmap(con_mat, center=True)
plt.show()

