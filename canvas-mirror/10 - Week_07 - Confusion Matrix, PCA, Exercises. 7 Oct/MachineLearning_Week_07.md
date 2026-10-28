# Machine Learning Week 7 - lecture slides

Source: MachineLearning_Week_07.pdf, 61 slides, Sila, Oct 7th 2026. Condensed from extracted text plus viewed page images (key figures described in italics).

## Program
Titanic competition; model optimization (evaluation, spotting anomalies, underfit/overfit, confusion matrix revisited, feature engineering revisited, data compression with PCA); ML pipeline putting it all together.

## Handins (reminders)
Do the work; individual reports; plan ahead. Hand in a zip with pdf report and .py files (typically 1-10 MB, not hundreds of MB). Hand in individual code and reflections.

*[Slide 9: photo of the Titanic liner with a tug alongside.]*

## Recap (groups of 2-3)
What is accuracy, precision, recall? Discuss: which algorithm is best?

## Titanic competition (groups of 2)
How and what did you do? Show solutions, discuss what you did and would have liked to do; what was the result? Then class discussion.

## Model evaluation, cross validation
Use part of the training data to evaluate how good the model will be on new data (Real World ML, Brink et al., p. 83; Titanic cross-validation example p. 87).
*[Slide 14: scanned book figure: full Titanic table split into a training set (used only for building the model) and a testing set (used only for evaluating the model).]*

## Anomaly detection / cleaning data
- Exercise 1: in groups of two, how can you spot anomalies in a dataset? What can/should you do?
- Normally distributed data (three sigma rule): roughly 1 in 22 observations differ by 2 std or more from the mean, 1 in 370 by 3 std. (Andrew Ng, Coursera.)

## Finding the right model: underfit and overfit
- Three fits to a "corn-production" training set (Real World ML p. 80).
- Exercise 2 (groups of 2-3): if the model under- or overfits, what might make it better, what could you try?
- Bias/variance (Andrew Ng): variance is sensitivity of the learning algorithm to specifics (noise) of the training data. Left region with high training and validation error = high bias; right region with low training but high validation error = high variance; aim for the sweet spot in the middle.
*[Slides 20-25: Andrew Ng Coursera figures: small vs large neural network (small: fewer parameters, prone to underfitting, cheaper; large: more parameters, prone to overfitting, more expensive, use regularization lambda); fits of a model; training vs validation error curves.]* High variance means small training changes cause large result changes and the model fits noise (overfitting).

## Selecting a good model: confusion matrix and ROC curves
Several slides (Real World ML p. 90-91): confusion matrix, ROC (receiver operating characteristics) curves, effect of the decision threshold on the Titanic dataset.
*[Slide 26: 2x2 confusion matrix with prediction outcome (p, n) vs actual value (p', n'): True Positive, False Negative, False Positive, True Negative, with marginal totals. Slide 30: ROC space plot (x = FPR or 1-specificity, y = TPR or sensitivity, dashed diagonal = random guess, top-left = perfect classification, above diagonal = better, below = worse) with points A, B, C, C' and their four confusion matrices (counts out of 100 positives/100 negatives).]*

## Feature engineering
Feature evaluation/engineering and model evaluation (Real World ML p. 112).

## Data compression: PCA
- Unsupervised transformation: a high-dimensional representation is transformed to a new representation with fewer features summarizing the essential characteristics; commonly reduction to 2 dimensions for visualization.
*[Slide 39: scatter of two temperature anomalies with the principal component axes drawn as rotated coordinate system; Andrew Ng figure reducing 2D data (x1 cm, x2 inches) to 1D z1 by projecting points onto a line.]*
- PCA "rotates the coordinate system"; finds directions of maximum variance and projects onto a subspace of equal or fewer dimensions; sorts components by explained variance.
- Exercise 3: why is data compression useful in ML?
- Uses: reduce memory/disk, speed up learning, visualization (k = 2 or 3).
- Not a good way to avoid overfitting: PCA is unsupervised, unaware of labels, discards information without knowing what is useful for classification. (Sometimes it helps by removing highly correlated features.) Only discard components that are not valuable (example: spectroscopy data where the effect of interest was in PCs 4 and 5, while PC1 was background light).
- For picture classification, 100-200 components may be too few.
- Other techniques: manifold learning (unroll a "roll" to a 2D dataset).

## ML pipeline: putting it all together
- Exercise 4 (see Canvas; groups of 2-3): what steps would a pipeline need to get a car to stay on the road (markings), read road signs, spot people? *[Slide 50: screenshot of a car-driving neural net; road image with human vs neural-net steering outputs.]* Slides show End to End Learning for Self-Driving Cars (Nvidia), finding people in an image, reading characters in an image (Andrew Ng).
- Use lots of compute: data parallelism runs the same model over different data streams and synchronizes weights (model parallelism: different layers on different GPUs). See Horovod: https://github.com/horovod/horovod
- Recipe: start with a simple algorithm implemented quickly and test on cross-validation data; plot learning curves to decide if more data/features help; error analysis (manually examine errors in the cross-validation set for systematic patterns).

## Remaining exercises
Exercises 5, 6, 7: slides only show titles; see the exercise PDFs (Bankloan, Student Absence, Student Grade).

## Homework
Do the exercises. Read Geron "Hands-On Machine Learning" and Brink et al. "Real-World Machine Learning" Ch. 4 (model evaluation and optimization) and Ch. 5 (basic feature engineering, p. 106-126).
