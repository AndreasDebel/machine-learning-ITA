import pandas as pd

# --- A) Getting to know the data ---
df = pd.read_csv("data/titanic_800.csv")

print("Shape (rows, columns):")
print(df.shape)

print("\nFirst 5 passengers:")
print(df.head())

print("\nMissing values per column:")
print(df.isna().sum())

print("\nSurvived (0 = died, 1 = survived) counts:")
print(df["Survived"].value_counts())

# --- B) Cleaning the data ---
print("\nAverage Pclass for those who died (0) vs survived (1):")
means = df.groupby("Survived")["Pclass"].mean()
print(means)

diff = abs(means[0] - means[1])
print("\nAbsolute difference between the two means:")
print(diff)

print("\nDifference as % of the died-group mean (survived vs died):")
print(f"{diff / means[0] * 100:.1f}%")

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
# To do.
