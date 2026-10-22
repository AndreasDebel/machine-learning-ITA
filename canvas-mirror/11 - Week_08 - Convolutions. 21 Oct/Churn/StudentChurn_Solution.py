# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:41:07 2021

@author: sila
"""

#import panda library and a few others we will need.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix

col_names = ["Id", "Churn", "Line", "Grade", "Age", "Distance", "StudyGroup"]

data = pd.read_csv('studentchurn.csv')

# show the data
print ( data .describe( include = 'all' ))
#the describe is a great way to get an overview of the data
print ( data .values)

print(data.columns)
print(data.shape)

data[['Id','Churn','Line','Grade','Age','Distance','StudyGroup']] = data['Id;Churn;Line;Grade;Age;Distance;StudyGroup'].str.split(';', expand=True)

x = data[ "Line" ]
y = data[ "Age" ]
plt.figure()
plt.scatter(x.values, y.values, color = 'black' , s = 20 )
plt.show()

# Replace unknown values. Unknown class set to 0
data["StudyGroup"].fillna(0, inplace = True)

# Remove empty rows
data.replace("", np.nan, inplace=True)
data.dropna(how='any', axis=0, inplace=True)

data['Churn'] = data['Churn'].replace(['Completed'],1.0 )
data['Churn'] = data['Churn'].replace(['Stopped'],0.0 )

data['Line'] = data['Line'].replace(['HF'],1.0 )
data['Line'] = data['Line'].replace(['HHX'],2.0 )
data['Line'] = data['Line'].replace(['STX'],3.0 )
data['Line'] = data['Line'].replace(['EUX'],4.0 )
data['Line'] = data['Line'].replace(['HTX'],5.0 )

yvalues = pd.DataFrame( dict ( Churn =[]), dtype = int )
yvalues[ "Churn" ] = data [ "Churn" ].copy()
#now the yvalues should contain just the churn column

# Now we can delete the churn column from the data (because
# We have copied that already into the yvalues).
data.drop('Id;Churn;Line;Grade;Age;Distance;StudyGroup', axis = 1 , inplace = True )
data.drop('Id' , axis = 1 , inplace = True )

data.drop( 'Churn' , axis = 1 , inplace = True )

print ( data .values)

print(data.columns)
print(data.shape)

print(yvalues)

xtrain = data.head( 838 )
xtest = data.tail( 238 )

ytrain = yvalues.head( 838 )
ytest = yvalues.tail( 238 )

print ( ytrain )

# Scale data set
scaler = StandardScaler()
scaler.fit(xtrain)
xtrain = scaler.transform(xtrain)
xtest= scaler.transform(xtest)

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier( hidden_layer_sizes =( 10 , 10 , 10), max_iter = 1000 , random_state = 42 )

mlp.fit(xtrain, ytrain.values.ravel())
#the reason for the values.ravel is that these data has not
#been scaled and they need to be converted to the correct
#input format for the mlp.fit. Data that is scaled already has
#this done to them.

#predictions
predictions = mlp.predict(xtest)

matrix = confusion_matrix(ytest,predictions)
print (matrix)
print (classification_report(ytest,predictions))



