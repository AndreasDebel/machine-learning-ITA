# Machine Learning E2026 - Mandatory Assignment, Autumn 2026

Source: `Ita_ML_SupplyChain_Titanic.pdf` (4 pages, A4, Word -> PDF, dated October 5th, 2026, author "Sila").
The only image in the PDF is the Erhvervsakademi Aarhus logo (page 1, decorative). Quotes keep the original wording
(including typos) where it matters; typos are marked `[sic]`.

## Hand-in rules

- **Individual** reports only; group hand-ins are not allowed.
- Language: Danish or English.
- Deliverable: your **Python code** plus a **small document, 1 page**, that tells what you have done.
- **Deadline: Monday 2 November 2026, 20:00** on Canvas (PDF says "Novemberl" [sic]).
- Multiple files (report, scripts) must be **zipped into one file**. Make the zip correctly ("Ask chatGPT if in doubt").
- Expected size of the complete zip: **1-2 MB** - verify before hand-in.
- No individual feedback; the assignment is discussed in class next time.
- Choose **either** the Titanic exercise **or** the Supply Chain exercise, and **explain your choice** in the hand-in.
- Note from the teacher: Titanic is a relatively well-known, well-defined teaching exercise; Supply Chain is more like a
  real-world scenario with a (little bit) more messy dataset.

## Local files for this assignment

```
Supply Chain Management/
    DataCoSupplyChainDataset.csv
    SupplyChain.py
Titanic/
    titanic_800.csv
    titanic_alternative.csv
    Titanic_alternative_Columns.txt
```

---

## Option 1: Titanic

### Background

- In class you worked with a limited version of real Titanic data (survived/died plus other data). Goal: **predict who
  survives and who dies** based on other passenger data.
- This exercise uses a larger dataset. Download as `.csv` from Canvas: header + **800 passenger records**.
- An alternative version with **887 records**, `Titanic_alternative.csv`, is also on Canvas. **Do not use it until the
  entire exercise is completed with the 800-passenger file.** It is only for those who want to dig deeper after
  answering all questions, or who run into problems with the 800-passenger file.
- The csv can be opened in a text program or csv reader (teacher recommends OpenOffice).
- `name` and `passengerId` are self-explanatory.

### Data dictionary

| Variable in data | Definition                                  | Key                                              |
|------------------|---------------------------------------------|--------------------------------------------------|
| Survival         | Survived or not                             | 1 = survived, 0 = died                           |
| pclass           | Passenger class                             | 1 = 1st class, 2 = 2nd class, 3 = 3rd class      |
| Sex              | Sex                                         | Male or female                                   |
| age              | Age in years                                |                                                  |
| sibsp            | # of siblings / spouses aboard the Titanic  |                                                  |
| parch            | # of parents / children aboard the Titanic  |                                                  |
| Ticket           | A ticket number                             |                                                  |
| fare             | The price paid for the ticket               |                                                  |
| cabin            | The cabin number [sic: "numer"]             |                                                  |
| embarked         | Port city where the passenger embarked      | C = Cherbourg, Q = Queenstown, S = Southampton   |

Instructions: several sections below are marked with capital letters, each with several questions. Answer as many
questions correctly as you can. Also hand in the `.py` file(s) in the zip.

### A) Getting to know the data and the problem

1. What kind of machine learning problem are we talking about? Be as precise as possible.
2. How many different features (not counting labels / y-values) are there in this dataset?
3. How many of these features would the Y-data (the labels) consist of?

### B) Cleaning the data

- Decide which features to use for the X training dataset, then what to do with missing data for the features you keep.
- Think about which features will most likely have **no impact on survival** and discuss why. Removing features can be
  "dangerous" (they may have limited value), but this dataset has features that can be safely removed.
- Back up claims by checking for a relationship between feature and survival rate: **correlation** or a graph such as a
  **scatterplot** (part of a previous class exercise). No correlation is not an absolute guarantee a feature can be
  removed - there could be multi-dimensional relationships between 3-4 features you cannot see.
- Removed features are not used in training **and not in the test set**.
- Some features have missing data (e.g. `age`). Discuss **how you will handle missing data** (think back to earlier class
  discussions about similar problems).
- Non-numerical data must be converted to numbers in **both training and test set**. Pandas example from the PDF:

  ```python
  xtrain['Sex'] = xtrain['Sex'].replace(['female'], 1.0)
  ```

  This changes all `'female'` labels into `1.0` (`male` also needs a value).
- After cleaning (and **scaling** - see slides/previous exercise), split into a training set and an evaluation (test) set.
  There are 800 samples. **How many in training, how many in test? Give reasons.**

### C) Choosing a model and doing training

- Models worked with in the course: random forests, decision trees, neural networks, etc.
- Choose **at least 1 model**, **explain the reason** for the choice, and train it on the training data.

### D) Evaluating performance on the test set

(Evaluation was covered in earlier exercises, slides and the book.)

- Give the **precision** and **recall** for your model.
- Give the **confusion matrix** and use its values to calculate the **percentage of samples classified correctly**.
- Looking at the confusion matrix: what is the model **best at** and what is it **worst at**?

### E) Experiments

- Do a few experiments: vary the **parameters** of your chosen model, **or** choose another model and compare
  prediction performance with the old one.
- **Document your experiments and results.**

---

## Option 2: Supply Chain

### Background

- Dataset: **DataCo Smart Supply Chain** (on Kaggle, where code examples can also be found).
- Task: make a Python program that **predicts late delivery risk** (target: `Late_delivery_risk`).
- As in Titanic, explain what you have done for:

| Step             | Requirement                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------|
| Cleaning         | Remove unnecessary columns, handle NaN values (missing data), convert text categories into numerical values.         |
| Visualization    | Show the balance of the target (`Late_delivery_risk`) and a correlation matrix to identify interconnected variables. **Not mandatory**, but may help understanding. |
| Modeling         | Choose **at least 1 model**, explain the reason for the choice, train it on the training data.                        |
| Confusion Matrix | Provide a **visual overview** of how many times the model predicted correctly vs. incorrectly regarding late deliveries. |

### Recall question

> In a supply chain, it is often more important to catch all potential delays (high recall) than to be right every time
> you make a prediction. What does your solution give concerning this?

---

## Checklist (derived, not in the PDF)

- [ ] Pick Titanic or Supply Chain and justify the choice in the 1-page document.
- [ ] 1-page report + `.py` file(s), zipped into one file of 1-2 MB.
- [ ] Upload to Canvas by Mon 2 Nov 2026, 20:00.
- [ ] Titanic: answer A-E; keep the 887-record file for after finishing with the 800-record file.
- [ ] Supply Chain: cleaning, (optional) target balance + correlation matrix, model, visual confusion matrix, recall discussion.
