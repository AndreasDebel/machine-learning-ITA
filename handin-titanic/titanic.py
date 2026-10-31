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
