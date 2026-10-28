# Machine Learning - Week 5: Exercises (Ita, ML)

Source: `Exercises_Week_05.pdf` (3 pages, Erhvervsakademi Aarhus). Code listing in Ex. 6 given in condensed form.

## Exercise 1
See Playground TensorFlow exercises (`PlaygroundTensorFlowExercises.md`).

## Exercise 2 - output layer
- A neural network classifying email spam: how many neurons in the output layer?
- A network classifying written digits 0-9 (MNIST): how many output neurons? And what is it reasonable to expect the output values actually represent?

## Exercise 3 - activation functions
Look in chapter 10 of the book. Find all the different activation functions used and draw a graph of each to get a feel for them. Think about disadvantages that could be an issue.

## Exercise 4 - weights and neural networks
Weights on connections are usually initialized to (small) random numbers before training. Why?

## Exercise 5 - more hidden layers
It may seem counterintuitive that training a network with 2 hidden layers can in some cases be faster than with 1 hidden layer (the number of neurons per layer is not the same). How can this be? If you do not know, (re)read p. 349-50 (323-24 in v2, 270-71 in v1) of chapter 10. "It is crucial you get this understanding."

## Exercise 6 - MLP on Iris
Use a multilayer perceptron to classify petal length and width for the Iris data set. Go through the supplied code step by step, adjust values to understand it. Try the code without feature scaling.

Code outline (given in the PDF):
1. `load_iris()`; `X = iris.data[:, (2,3)]` (petal length, width), `y = iris.target`; print number of samples.
2. Scatter plot of the data with colormap red/green/blue (`ListedColormap`), axis labels from `iris.feature_names`.
3. `train_test_split(X, y, test_size=0.20)`.
4. `StandardScaler` fit on train, transform train and test.
5. `MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)`, `fit`, `predict` on test.
6. Decision-region plot: meshgrid with step `h=.02`, `mlp.predict` on the grid, `contourf` (coolwarm, alpha 0.8) plus test points; labels 'Petal length' / 'Petal width', title "MLP".
(The PDF also imports `RandomForestClassifier`, unused.)

Questions:
- A) What happens if you change the test size? Make it smaller and larger: 5 %, 90 %.
- B) Remove the scaler (StandardScaler). Can the classifier work without it?
- C) Change the number of iterations (epochs, `max_iter`) to 100. Was that a good idea?
- D) Reset `max_iter` to 1000. Experiment with the number of hidden layers, starting with 1. How many hidden layers with how many nodes gives the best results? Will `MLPClassifier(hidden_layer_sizes=(2), max_iter=1000)` work? Why not?

## Exercise 7 - blobs dataset
Use a multilayer perceptron to classify the "blobs-dataset". See file `Week6_Exercise7.py` [sic - file name says Week6 although it is Week 5 material].
- A) Adjust the number of hidden layers and iterations to get a proper classification.
- B) Again, try without the scaler (?).
- C) Experiment with the settings for blob centers and number of samples.
