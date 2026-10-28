# Machine Learning Day 04 (slides)

Source: `MachineLearning_Day_04.pdf` (51 slides), Sila, Sept 16th 2026. Condensed summary from the text layer (diagrams not viewed).

## Program
Comments on last week's exercises; Support Vector Machines; Clustering, Decision Trees, Random Forest, Ensemble methods; exercises.

## Last week recap
Iris dataset (UCI). In groups of 2-3 go through last week's exercise 3.5 plus "exercise iris precision" (logistic regression): how did you solve it, problems, comments. Explain `Exercise_Iris_Precision.py` to each other.

## SVM
- An SVM fits the widest possible "street" between classes: large margin classification (Geron p. 154). Slides credit Andrew Ng (Coursera).
- Many datasets are not linearly separable; SVMs handle some via kernels (no maths today).
- Exercises: code Svm1, Svm2, Svm_gamma (see `SVM/SVM_Exercises.md`).

## Recap: what can ML do
Anomaly detection (security, fraud); predictive models assign probabilities (e.g. patient outcome); customer segmentation for targeted marketing. Two general problems: (1) labelled data -> assign a category to new data = supervised learning; (2) unlabelled data -> divide into groups = clustering (unsupervised).

## Clustering / k-means
- Problem: group unlabelled multidimensional data (e.g. webshop customers: age, zipcode, monthly spend, country, gender) so distance inside groups is small and between groups big. How many groups?
- k-means: input data and k. Each point is closer to its own cluster centre than to others (multi-dimensional Pythagoras); centre = mean of the cluster's points. Optimal clustering is NP-hard, so no guarantee of the optimum.
- scikit-learn uses Lloyd's algorithm: start with k random centres, alternate (1) assign each point to the closest centre, (2) recompute centres as means; converges, but may land in a suboptimal solution.
- Tasks: look at `tutorial1kmeans.py` (are predicted classes as expected? try points); `kmeans.py` and `moons_dataset_kmeans.py`, exercises 1-2.

## Decision trees
- For classification and regression on multidimensional labelled data; the output is easy to understand and visualize (unlike black boxes).
- Training: scikit-learn uses CART, always binary trees (ID3 and others allow n-ary); goal is to minimize gini impurity at nodes.
- Strengths/weaknesses: no assumptions on data; works on any multidimensional data; can overfit; sensitive to small changes in training data.
- Task: run `tutorial2decisiontree.py`, increase max depth, verify probability scores for points (2,1), (4,1) and (5,2).
- Exercise 3 (moons, `moons_dataset_decisiontree.py`).

## Ensemble methods / Random Forest
- "Wisdom of the crowds": train a group of predictors and combine. Hard voting = majority vote; soft voting = average predicted probabilities, pick the highest. Analogy: US winner-take-all states vs proportional seats in Denmark.
- Netflix Prize 2009 ($1,000,000), 100M ratings; winner used 24 predictors with ensemble learning (gradient boosted decision trees).
- Why it works: usually combine already-good classifiers; Jeopardy "ask the audience" analogy. Book argument: 1000 predictors each 51% right -> majority vote ~75% right (law of large numbers; binomial calculator).
- Diversity: (1) different algorithms on the same data; (2) same algorithm on different subsets: pasting (without replacement) or bagging (with replacement).
- Random Forest: very popular; `n_estimators` = number of trees; trees trained on bagged subsets; scikit-learn predicts by soft voting; accuracy improves with more trees up to a point; defaults are usually good.
- Tasks: run `tutorial3randomforest.py`; Exercise 4; then exercises 5-6 (see `Exercises/Exercises_Day_04.md`).

## Figures and formulas from the slide images (viewed)
- *[Slides 7-10, SVM: 2D scatter of two classes with the maximum-margin hyperplane (w.x - b = 0), margin lines (w.x - b = +1 / -1) and the support vectors on the margin; "optimal hyperplane", "maximum margin" labels.]*
- *[Slide 11, Andrew Ng/Coursera handwritten slide: use liblinear/libsvm to solve for theta; must choose parameter C and kernel. "No kernel" (linear kernel): predict y=1 if theta^T x >= 0 (good when n large, m small). Gaussian kernel: f_i = exp(-||x - l(i)||^2 / (2 sigma^2)), l(i) = x(i); must choose sigma^2.]*
- *[Slide 14: shoal of blue fish with one red fish = anomaly detection. Slide 16: arrows splitting a crowd into red/orange/green groups = customer segmentation.]*
- *[Slide 20: bar chart "Popular machine learning methods - Kaggle Survey": Logistic Regression 63.5%, Decision Trees 49.9%, Random Forests 46.3%, Neural Networks 37.6%, Bayesian Techniques 30.6%, Ensemble Methods 38.5% [sic order], SVMs 26.7%, Gradient Boosted Machines 23.9%, CNNs 18.9%, RNNs 12.3%, others lower.]*
- *[Slide 22: Iris scatter (sepal length vs width, about 150 points, one colour) "Clustering - an example - 1 cluster"; asks "How many dimensions does this data have?"]*
- *[Slide 23: k-means on the same data, k=2 vs k=4, with coloured clusters and marked cluster centres.]*
- *[Slide 26 (K-means is linear - fails on non-linear data): "true cluster" vs "predicted using k-means" on the two-moons dataset - k-means cuts the moons with a straight boundary. Note: scikit-learn has non-linear clustering, called spectral clustering.]*
- *[Slide 31: photos of Iris setosa, versicolor, virginica (the data for the tree example).]*
- *[Slide 33, Decision Tree depth 2: tree root `petal length (cm) <= 2.45` (gini 0.6667, samples 150, value [50,50,50]); left leaf setosa [50,0,0]; right node `petal width <= 1.75` (gini 0.5, 100 samples) with leaves versicolor (gini 0.168, [0,49,5]) and virginica (gini 0.0425, [0,1,45]). Right: petal length/width scatter with the vertical split at 2.45 and horizontal at 1.75. Note: in total 6 points fall in the wrong group (5 + 1 in the lowest two boxes).]*
- *[Slide 34, Decision Tree depth 3: adds splits `petal length <= 4.95` and `<= 4.85` giving leaves [0,47,1], [0,2,4], [0,1,2], [0,0,43]. Note: 4 points (0+1+2+1+0) in the wrong category: better classification rate but slower classification.]*
- Slide 35 (training algorithm) formula: Gini impurity = 1 - sum_{i=1..J} p_i^2 (J = number of classes, p_i = fraction of items labelled class i; low gini good, high bad; gini 0 = pure node). Worked example for the versicolor leaf: 1 - (0^2 + (49/54)^2 + (5/54)^2) = 0.168.
- *[Slide 41, ensemble overview: three databases of training data each feed Model 1/2/3 -> Output 1/2/3 -> "final output" determined by voting (soft or hard).]*
- *[Slide 42, ensemble training example: one dataset feeds diverse predictors (Logistic Regression, SVM Classifier, Random Forest Classifier, Other...).]*
- *[Slide 43, ensemble prediction example: new instance -> four diverse predictors predicting 1, 1, 2, 1 -> ensemble prediction (majority vote) = 1.]*

## Homework
Week 4 topics as in `ML_Syllabus_Day_04.md`: Hands-On ML chapters 6 and 7, the video, do all exercises.
