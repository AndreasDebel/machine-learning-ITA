import pandas as pd

# --- B) Prepared data ---
# All cleaning, the split, the Age fill and scaling happen in clean.py, which writes
# the training and test sets. Run clean.py first.
train = pd.read_csv("data/titanic_800_train.csv")
test = pd.read_csv("data/titanic_800_test.csv")

xtrain = train.drop(columns=["Survived"])
ytrain = train["Survived"]
xtest = test.drop(columns=["Survived"])
ytest = test["Survived"]
print(f"\nTraining set: {xtrain.shape}, test set: {xtest.shape}")

# --- C) Model ---
# The tree's depth is chosen with 5-fold cross-validation on the training set only:
# 640 rows are split into 5 parts, and each part takes a turn as validation data
# while the tree trains on the other 4. The test set stays unseen until section D.
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier, export_text

folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

print("\nDepth | train accuracy | cross-validation accuracy (mean +/- std)")
for depth in [1, 2, 3, 4, 5, 6, 8, 10, None]:
    tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
    scores = cross_val_score(tree, xtrain, ytrain, cv=folds)
    train_score = tree.fit(xtrain, ytrain).score(xtrain, ytrain)
    print(f"{str(depth):>5} | {train_score:.3f} | {scores.mean():.3f} +/- {scores.std():.3f}")

# The simplest depth scoring at least the best mean minus the best depth's std. Deeper
# trees score higher on the training data, but not reliably on data they have not seen.
best_depth = 5

model = DecisionTreeClassifier(max_depth=best_depth, random_state=42)
model.fit(xtrain, ytrain)

print(f"\nFinal tree (max_depth={best_depth}):")
print(export_text(model, feature_names=list(xtrain.columns)))

# --- D) Evaluation on the test set ---
# The tree sees only the features of the 160 test passengers and guesses 0 or 1 for each.
ypred = model.predict(xtest)
print(f"\nPredictions: {len(ypred)}, survived: {(ypred == 1).sum()}, died: {(ypred == 0).sum()}")
print(f"First 10 predictions: {ypred[:10]}")

# Confusion matrix: rows are the true answers, columns the tree's guesses.
from sklearn.metrics import confusion_matrix

tn, fp, fn, tp = confusion_matrix(ytest, ypred).ravel()
print("\nConfusion matrix (test set):")
print("             | predicted died | predicted survived")
print(f"true died    | {tn:>14} | {fp:>18}")
print(f"true survived| {fn:>14} | {tp:>18}")

# All three scores come straight from the matrix; survived (1) is the positive class.
accuracy = (tn + tp) / (tn + fp + fn + tp)
precision = tp / (tp + fp)
recall = tp / (tp + fn)
print(f"\nCorrectly classified: {tn + tp} of {len(ytest)} = {accuracy:.1%}")
print(f"Precision: {tp} of {tp + fp} = {precision:.1%}")
print(f"Recall: {tp} of {tp + fn} = {recall:.1%}")

# Best and worst: how much of each true group the tree got right (the matrix's rows).
print(f"\nTrue died, predicted right: {tn} of {tn + fp} = {tn / (tn + fp):.1%}")
print(f"True survived, predicted right: {tp} of {tp + fn} = {tp / (tp + fn):.1%}")
