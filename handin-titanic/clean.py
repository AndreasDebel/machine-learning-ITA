import pandas as pd

# Reads the raw data, applies the cleaning steps, writes the cleaned copy.
# The raw file is never changed; re-run this script after adding a step.
df = pd.read_csv("data/titanic_800.csv")

# --- Step 1: fix corrupted Fare values ---
# 98 fares lost their decimal point (7.925 -> 7925, 262.375 -> 262375). All of them
# originally had three decimals; the highest real fare is 512.33, so anything above
# 600 is corrupted and divided by 1000 to restore it.
bad_fare = df["Fare"] > 600
print(f"Corrupted fares fixed: {bad_fare.sum()}")
df["Fare"] = df["Fare"].where(~bad_fare, df["Fare"] / 1000)
print(f"Fare range after fix: {df['Fare'].min()} - {df['Fare'].max()}")

# --- Step 2: text to numbers ---
df["Sex"] = df["Sex"].replace(["female"], 1.0)
df["Sex"] = df["Sex"].replace(["male"], 0.0)
df["Sex"] = df["Sex"].astype(float)
print(df["Sex"].unique())
print("Sex column type after conversion:")
print(df["Sex"].dtype)

# --- Step 3: flag missing Age ---
# Passengers with no recorded age survived less often (30 % vs 41 %), so the fact
# that Age is missing carries information. The flag keeps it after Age is filled in.
# The fill itself (median) happens in titanic.py after the split, so the median is
# computed from the training set only.
df["Age_missing"] = df["Age"].isna().astype(int)
print(f"\nAge missing (flagged): {df['Age_missing'].sum()}")
rate = df.groupby("Age_missing")["Survived"].mean()
print(f"Survival rate - age known: {rate[0]:.1%}, age missing: {rate[1]:.1%}")

# --- Step 4: fill the one missing Embarked ---
# Only PassengerId 62 has no port. It is filled with the most common port, S, before
# the split. The mode is S in the full data and in any training set (577 of 800), so
# this leaks nothing from the test set.
df["Embarked"] = df["Embarked"].fillna("S")

# --- Step 5: one-hot encode Embarked ---
# The ports have no natural order, so S/C/Q -> 0/1/2 would invent one. Instead each
# port gets its own 0/1 column: Embarked_C, Embarked_Q, Embarked_S.
df = pd.get_dummies(df, columns=["Embarked"], dtype=int)

# --- Save (all columns) ---
# Keeps every column, including the ones dropped below, so correlation.ipynb can
# still show the evidence for dropping them.
df.to_csv("data/titanic_800_cleaned.csv", index=False)
print("\nSaved data/titanic_800_cleaned.csv")

# --- Step 6: drop features not used by the model ---
# Reasons are in final-report.md ("Valg af features"). PassengerId and Name are only
# identification.
df = df.drop(columns=["PassengerId", "Name", "SibSp", "Parch", "Ticket", "Cabin"])
print(f"\nModel columns: {list(df.columns)}")

# --- Save (model-ready) ---
df.to_csv("data/titanic_800_model.csv", index=False)
print("Saved data/titanic_800_model.csv")

# --- Step 7: split into training and test set ---
# 80/20 = 640 train / 160 test. Stratified so both sets keep the same survived/died
# ratio; fixed random_state so the split is the same on every run.
from sklearn.model_selection import train_test_split

train, test = train_test_split(df, test_size=0.2, stratify=df["Survived"], random_state=42)
print(f"\nTrain rows: {len(train)}, test rows: {len(test)}")

# --- Step 8: fill missing Age with the training median ---
# The median is computed on the training set only and used for both sets, so no
# information from the test set leaks into training. Age_missing (step 3)
# remembers which ages were filled in.
age_median = train["Age"].median()
train["Age"] = train["Age"].fillna(age_median)
test["Age"] = test["Age"].fillna(age_median)
print(f"Age filled with training median: {age_median}")

# --- Step 9: scale Pclass, Age and Fare ---
# StandardScaler (as in the course's week 6 Titanic solution): each column gets
# mean 0 and standard deviation 1. Fitted on the training set only, then applied to
# both. The 0/1 columns and the label Survived are left as they are.
from sklearn.preprocessing import StandardScaler

to_scale = ["Pclass", "Age", "Fare"]
scaler = StandardScaler()
scaler.fit(train[to_scale])
train[to_scale] = scaler.transform(train[to_scale])
test[to_scale] = scaler.transform(test[to_scale])
print(f"Scaled {to_scale} - training mean: {scaler.mean_.round(2)}, std: {scaler.scale_.round(2)}")

# --- Save (train / test) ---
train.to_csv("data/titanic_800_train.csv", index=False)
test.to_csv("data/titanic_800_test.csv", index=False)
print("Saved data/titanic_800_train.csv and data/titanic_800_test.csv")
