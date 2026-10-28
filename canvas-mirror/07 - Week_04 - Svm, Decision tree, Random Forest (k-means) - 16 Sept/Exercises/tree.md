# tree.png

Source: `tree.png` (image).

*[Figure: graphviz export of a depth-2 scikit-learn decision tree on the Iris dataset.]*

- Root: `petal width (cm) <= 0.8`, gini = 0.667, samples = 150, value = [50, 50, 50], class = setosa.
  - True -> leaf (orange): gini = 0.0, samples = 50, value = [50, 0, 0], class = setosa.
  - False -> node `petal width (cm) <= 1.75`, gini = 0.5, samples = 100, value = [0, 50, 50], class = versicolor.
    - True -> leaf (green): gini = 0.168, samples = 54, value = [0, 49, 5], class = versicolor.
    - False -> leaf (purple): gini = 0.043, samples = 46, value = [0, 1, 45], class = virginica.

Illustrates gini impurity, samples/value per node and class colouring.
