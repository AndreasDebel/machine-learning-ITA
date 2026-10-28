# Exercises - Week 6

Source: `Exercises_Week_06.pdf` (7 pages, Erhvervsakademi Aarhus). Transcribed from text plus page images; code condensed.

## Exercise 1 - Moons dataset
Continues last week's Exercise 6 (MLP on Iris): the technique applies to other datasets. Starting from the Moons dataset:

```python
X, y = make_moons(n_samples=1000, noise=0.1)
# DataFrame(x, y, label), scatter plot grouped by label: 0 red, 1 blue
```

Construct a neural net (like last week) and train it so it predicts data points of the Moons dataset.
- a) What is the minimum number of hidden layers needed?
- b) What is the minimum number of neurons per layer needed?
- c) Try other values for the `make_moons` sample size and noise, and other test-size ratios. Then redo a) and b).

## Exercise 2 - Confusion matrix
A confusion matrix describes the performance of a classifier on test data with known true values.

*[Figure p.2: confusion matrix, n=165]*

|                | Predicted: NO | Predicted: YES |
|----------------|---------------|----------------|
| Actual: NO     | 50            | 10             |
| Actual: YES    | 5             | 100            |

- How often (in percent) is this model correct?
- True Positive Rate: when it is actually yes, how often does it predict yes?
- False Positive Rate: when it is actually no, how often does it predict yes?

## Exercise 3 - prediction accuracy
A binary predictor has TN = 12, TP = 23, FP = 5, FN = 10. What percentage of all predictions did it classify correctly? Needed to calculate accuracy for the mini-titanic exercise. Take your time. HINT: the percentage should be a nice round number.

## Exercise 4 - Recall and confusion matrix, continued
A zip code reader should identify a number as either a 5 or not a 5. A very simple algorithm *always predicts 5*, whatever the digit (0-9). Be very careful when inserting numbers in the confusion matrix.
- What is recall - is that a good value?
- What is precision - is that a good value?

## Exercise 5 - train on new data: limited Titanic dataset (real data)
Groups of 2-3. Small **competition** (against yourself and other groups): get the highest prediction accuracy (calculated as in exercises 2-3). Be systematic and keep track of the hyperparameters giving the best result.

**Data** (`Ex5 - Titanic/titanic_train_500_age_passengerclass.csv`, see its .md): 500 rows; PassengerId; Survived (0 died, 1 survived); Pclass (1/2/3); Age (some missing). Roughly 67 % of Titanic passengers died; in this test set (last 100 rows) 64 % died, so "always died" gives 64 %. Aim for more than 64 %.

**Split:** 80:20; first 400 rows train, last 100 test (`data.head(400)`, `data.tail(100)`). Only Pclass and Age may be used as features on the test set.

**Pandas help:** https://www.youtube.com/watch?v=XDAnFZqJDvI ; https://www.learnpython.org/en/Pandas_Basics

**Starter code (condensed):**
1. Imports: pandas, matplotlib, `StandardScaler`, `MLPClassifier`, `classification_report`, `confusion_matrix`.
2. `data = pd.read_csv('titanic_train_500_age_passengerclass.csv', sep=',', header=0)`; `print(data.describe(include='all'))`; `print(data.values)`.
3. `yvalues = pd.DataFrame(dict(Survived=[]), dtype=int)`; `yvalues["Survived"] = data["Survived"].copy()`.
4. Plot Age vs Pclass scatter (`plt.show()` blocks; best placed at the end). Also plot Age vs Survived and Pclass vs Survived: 3 plots in total.
5. `data.drop('Survived', axis=1, inplace=True)`. Question: keep or delete `PassengerId` (does it affect survival)? Mean age is 29.
6. Split into xtrain/xtest (head 400 / tail 100) and the same for ytrain/ytest (single column; 400 and 100 entries).
7. **Missing ages:** options - `fillna(0.0)`, fill with the mean age, or delete the rows (fewer training samples). Pick one, change later and compare.
8. **Scale:** `scaler = StandardScaler(); scaler.fit(xtrain); xtrain = scaler.transform(xtrain); xtest = scaler.transform(xtest)`. Scale only x, NOT y. (Text says "scale into [0;1]", but StandardScaler standardizes to mean 0 / unit variance.)
9. **Network:** think about hidden layers/neurons, batch size, epochs; check MLPClassifier defaults; set `random_state` (e.g. 0) for determinism. Example: `MLPClassifier(hidden_layer_sizes=(8, 8), max_iter=1000, random_state=0)`. sklearn adds input/output neurons automatically.
10. `mlp.fit(xtrain, ytrain.values.ravel())` (ravel needed because y is an unscaled DataFrame column); `predictions = mlp.predict(xtest)`.
11. Evaluate: `matrix = confusion_matrix(ytest, predictions)`; `print(classification_report(ytest, predictions))`; `tn, fp, fn, tp = matrix.ravel()`. Compute accuracy from TP/TN/FP/FN in Python (general formula from Ex. 2-3).

**Experiments (be systematic, record parameters + accuracy each time):**
- a) Network topology (nodes and layers) - higher accuracy?
- b) Handling of missing age data - effect on accuracy?
- c) Can we do without the scaler?
- d) Batch size - effect?
- e) Number of epochs - effect?
- f) Activation function (see sklearn MLP docs: http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html)

**First attempt (hints; "Can you reproduce, or do better?"):** use `StandardScaler`; `MLPClassifier(hidden_layer_sizes=(2, 2), max_iter=1000, random_state=1)`; `mlp.fit(xtrain, ytrain.values.ravel())`; predict; confusion matrix and classification report as above.

## Exercise 6 (a)
See `DatasetSpine/Exercise_DataSetSpine.md`. Improve the MLPClassifier to get better accuracy. Groups of 2-3.

## Further exercise
See the Canvas exercise "Create your own dataset" (`Exercises/Exercise_CreateOwnDataSet_ChatGPT.md`).

*[Page images viewed: p.1 header with Erhvervsakademi Aarhus logo; p.2 contains the confusion matrix table reproduced above.]*
