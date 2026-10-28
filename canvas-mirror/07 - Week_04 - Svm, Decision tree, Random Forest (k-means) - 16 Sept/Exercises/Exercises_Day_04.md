# ML Exercises, week 4

Source: `Exercises_Day_04.pdf` (2 pages).

## Exercise 1 - generating test sets
Read about toy datasets easily available in Python with scikit-learn:
- https://scikit-learn.org/stable/datasets/toy_dataset.html
- https://python-course.eu/machine-learning/available-data-sets-in-sklearn.php
- (wayback) https://machinelearningmastery.com/a-guide-to-getting-datasets-for-machine-learning-in-python/
- (wayback) https://machinelearningmastery.com/generate-test-datasets-python-scikit-learn/

## Exercise 2 - clustering
"Moons Classification Problem": 2D dataset labelled into two classes (binary). Here only the 2D data matters, not the labels.
- Visualize the data (use code from the page). Use 1000 samples instead of 100. Docs: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html
- Run K-means with K=2; visualize the two clusters in colors.
- How does the clustering compare to the real categories? (Probably quite different shapes - shows limitations of standard clustering.)

## Exercise 3 - classification using a Decision Tree
- 3.1 Split moons 80/20 into train and test (how to do it in Python is part of the exercise): first 800 samples + labels for training, last 200 for testing.
- 3.2 Train a Decision Tree on the first 800.
- 3.3 Test on the last 200 and compute percent correct. A random classifier gets ~50%.
- 3.4 Visualize the resulting tree.
- 3.5 Find examples classified correctly and incorrectly.

## Exercise 4 - classification using a Random Forest
Do the same as exercise 3 (questions 1, 2 and 3) with a Random Forest instead of one tree. Experiment with the number of trees. Finally visualize how more trees improve the result (see the RandomForest tutorial python file on Canvas).

## Exercise 5 - classification on other data
Do exercise 3 on the Circles dataset (labelled) from the article in exercise 1.

## Exercise 6 - hard and soft voting
What is the difference between hard and soft voting classifiers? Write it in your own words.
