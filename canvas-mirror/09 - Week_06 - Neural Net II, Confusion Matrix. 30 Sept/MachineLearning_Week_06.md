# Machine Learning - Week 6 slides (Neural Nets II, Confusion Matrix)

Source: `MachineLearning_Week_06.pdf` (51 slides, "Sila, Sept 30th 2026"). Condensed summary from extracted text; formula/diagram-only slides described from context.

## Program
Theory: general problems training NNs, activation functions and dying neurons. Hands-on: scikit-learn `MLPClassifier`, measuring prediction accuracy, Titanic mini dataset, exercises on real (limited) data, competition.

## Review of Week 5 exercises
Groups of 2 discuss Iris (Ex. 6) and Blobs (Ex. 7) classification with NNs. Moons dataset (labelled "Exercise 1, Week 7" [sic] on the slide; it is Exercise 1 of Week 6): minimum number of hidden layers / neurons per layer for `make_moons(n_samples=1000, noise=0.1)`; try other sample sizes, noise and test ratios (see `Exercises_Week_06.md`).

## General training problems
- **Vanishing gradients:** very small gradients -> weights barely change -> no convergence (saturation).
- **Exploding gradients:** gradients grow, huge weight updates -> divergence.
- **Saturation of sigmoid:** Glorot and Bengio (2010), "Understanding the Difficulty of Training Deep Feedforward Neural Networks". For very large/small inputs the sigmoid slope approaches 0, so back-prop updates vanish.
- **ReLU:** constant slope, no saturation for large values, but **dead neurons**: if the weighted input sum is < 0 the output is 0 almost always; can trickle through the network. A risk, not a certainty.
- **Alternatives:** ELU (Clevert et al., 2015) - better than ReLU but slower to compute.

## scikit-learn MLPClassifier workflow
1. Load data; 2. clean and scale; 3. define topology; 4. train; 5. evaluate on test data; 6. if happy predict on new data, else change parameters and retrain.

- **Load:** `pd.read_csv('titanic_train_500_age_passengerclass.csv', sep=',', header=0)`; `data.describe(include='all')`; `data.values`.
- **Clean:** `data.drop('PassengerId', axis=1, inplace=True)`; fill missing age with mean (`data['Age'].fillna(avg)`; "maybe not best with the average"); split `head(400)` / `tail(100)`.
- **Scale:** `StandardScaler` fit on train, transform train and test; y not scaled (already 0/1). Why scale: puts features on equal footing (grams vs kg example), gradient-descent NNs converge faster.
- **Topology:** `MLPClassifier(hidden_layer_sizes=(32), max_iter=1000, random_state=0)` (1 hidden layer, 32 neurons); `hidden_layer_sizes=(16,8)` = 2 layers. `max_iter` = max epochs.
- **Train:** `mlp.fit(xtrain, ytrain)` (supervised, needs labels).
- **Epoch and batch size:** one epoch = one forward + backward pass over all training samples; batch size = samples per pass (1000 samples, batch 100 -> 10 iterations per epoch). Small batch: less memory, faster convergence, but more fluctuation (outliers). sklearn: `batch_size=32, learning_rate_init=0.01` (default learning rate 0.001).
- **Evaluate:** `predictions = mlp.predict(xtest)`; `confusion_matrix(ytest, predictions)`; use test data, NOT train data.
- **Predict:** `model.predict(row)` returns an array (0/1 for Titanic).

## Measuring performance
- **Confusion matrix:** TN, FP, FN, TP.
  - Accuracy = (TP+TN)/total.
  - Precision = TP/(TP+FP): ratio of correct positive predictions to all predicted positives.
  - Recall (TPR) = TP/(TP+FN): ratio of correct positive predictions to all actual positives.
  - FPR = FP/(FP+TN).
  - F1 = harmonic mean of precision and recall; emphasizes the lowest value (precision 1 and recall 0 -> F1 = 0).
- **ROC curve** (receiver operating characteristic): plots TPR vs FPR at all classification thresholds. Lowering the threshold classifies more items as positive, raising both FP and TP. *[Slides: ROC plots; AUC.]*
- **Exercise 2** (50/10/5/100 matrix, accuracy, TPR, FPR), **Exercise 3** (TN=12, TP=23, FP=5, FN=10 -> accuracy), **Exercise 4** ("always predict 5" classifier: recall, precision). See `Exercises_Week_06.md`.
- Digit "5 or not 5" example: recall 0.60 (ratio of positives correctly predicted), precision 0.75 (accuracy of positives predicted); book p. 91 has the definitions. Always predicting 5 gives 100 % recall but very low precision. Perfect prediction: FN = FP = 0.
- **In Python:** matrix `[[61 3] [26 10]]` -> `tn, fp, fn, tp = matrix.ravel()` = (61, 3, 26, 10). `classification_report`:

| class     | precision | recall | f1-score | support |
|-----------|-----------|--------|----------|---------|
| 0         | 0.70      | 0.95   | 0.81     | 64      |
| 1         | 0.77      | 0.28   | 0.41     | 36      |
| avg/total | 0.73      | 0.71   | 0.66     | 100     |

## Titanic mini dataset
500 rows, 400 train / 100 test. **Lazy unoptimized benchmark:** NN predicts 71 % correct (61 + 10 = 71 out of 100). "Surely you can do better!" Finish exercises 1-4 first, then Exercise 5.

## Homework (Week 6)
Hands-On ML chapter 3 p. 108-128 (confusion matrix, ROC) and chapter 11 p. 357-366; exercises for week 6.

## Figure notes (from page images)
- *[Slide 26: cartoon of Type I error (false positive: doctor tells a male patient "You're pregnant") and Type II error (false negative: "You're not pregnant" to a visibly pregnant woman).]*
- *[Slide 29: annotated confusion matrix, rows Actual Positive/Negative, columns Predicted Positive/Negative. Margins: Sensitivity = TP/(TP+FN), Specificity = TN/(TN+FP), Precision = TP/(TP+FP), Negative Predictive Value = TN/(TN+FN), Accuracy = (TP+TN)/(TP+TN+FP+FN). FN = Type II error, FP = Type I error.]*
- *[Slide 32: Recall = TP/(TP+FN) = TP/Total Actual Positive, with the Actual Positive row of the matrix highlighted in red.]*
- *[Slide 37: TPR (recall) = TP/(TP+FN); FPR = FP/(FP+TN).]*
- *[Slide 39: ROC plot, TPR vs FPR; curves blue (best, hugging top-left, "Perfect classifier" point at (0,1)), green, orange, red dashed diagonal = random classifier; arrow "Better" toward top-left, "Worse" toward the diagonal.]*

## Additional figure notes (all 51 slides viewed)
- *[Slide 4: Moons code and a-c questions (identical to Exercise 1).]*
- *[Slide 11-12: sigmoid saturation plot beside text; ReLU plot R(z) = max(0,z) on [-10,10].]*
- *[Slide 13: ELU equation: ELU_alpha(z) = alpha(exp(z) - 1) if z < 0, z if z >= 0; plot (alpha=1) with a smooth negative saturation at -1.]*
- *[Slide 21: scaling motivation: table Orange (weight 15, price 1), Apple (18, 3), Banana (12, 2), Grape (10, 5); two contour plots of J(w) - without scaling (x1 >> x2) the contours are a narrow ellipse and gradient descent zigzags; after scaling (0<=x<=1) the contours are circular and descent goes straight. Slide 22: density plots of five distributions before and after StandardScaler (centred around 0, similar spread).]*
- *[Slide 25: spam-filter confusion matrix: TP 320, FN 43, FP 20, TN 538; Recall = 320/(320+43) = 0.882; Precision = 320/(320+20) = 0.941. Spam = positive.]*
- *[Slides 27-28: large formulas P = TP/(TP+FP) (precision; "terrorists correctly identified" example text) and R = TP/(TP+FN) (recall).]*
- *[Slide 30: recall/precision definitions: Precision = TP/(TP+FP) = TP/Total Predicted Positive; Recall = TP/(TP+FN) = TP/Total Actual Positive; Predicted-Positive column or Actual-Positive row highlighted in red (slides 31-32).]*
- *[Slide 33: Accuracy = number of correct predictions / total = (TP+TN)/(TP+TN+FP+FN).]*
- *[Slide 35-36: tables of logistic-regression output (0.05 ... 0.95) with actual class (0/1) and predicted class at a threshold line (red = 0, green = 1); the second table has the threshold moved lower, so more items are predicted positive.]*
- *[Slide 38: sketch ROC curve: TP rate vs FP rate (0-1), dashed curve with two points "TP vs FP rate at one decision threshold" and "at another decision threshold".]*
- *[Slide 40: left: diagnosis grid (True/False positive/negative, Sensitivity = true positive / has disease, Specificity = true negative / healthy) and AUC plot of sensitivity vs 1-specificity for three biomarkers; right: the annotated confusion matrix again.]*
- *[Slide 42: F1 score: F1 = 2 x (precision x recall)/(precision + recall); text: F1 combines precision and recall; perfect when 1, a total failure when 0; with precision = 1 and recall = 0, F1 = 0; emphasizes the lowest value.]*
- *[Slide 44 (Ex. 4 cont.): grid of handwritten digits split into TN/FP/FN/TP regions: Predicted Negative column holds non-5 digits (8 3 9 7 2) = TN, and a 5 = FN; Predicted Positive column holds a 6 = FP and three 5s = TP. Recall (e.g. 3 out of 5) and Precision (e.g. 3 out of 4) marked with arrows.]*
- *[Slide 49: Titanic CSV opened in a spreadsheet (columns PassengerId, Survived, Pclass, Age; rows 1-10, some Age cells empty). Slide 50: lazy benchmark table (100 in test set): actual dead / predicted dead TN 61; actual dead / predicted survived FP 3; actual survived / predicted dead FN 26 (marked "Bad!"); TP 10.]*
