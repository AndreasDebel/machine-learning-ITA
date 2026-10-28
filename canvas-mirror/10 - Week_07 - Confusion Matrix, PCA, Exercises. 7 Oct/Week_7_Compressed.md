# Week_7_Compressed.zip - contents

Source: Week_7_Compressed.zip (extracted to scratchpad and inspected, nothing run). 14 files under `Week_7/`, about 3.9 MB. Bundles the week 7 material; most items duplicate files already in the week folder.

```
Week_7/
  bank_loan_data.csv              (614 rows; see Bankloan/bank_loan_data.md)
  Exercises_BankLoan.pdf
  Exercise_StudentAbsenceGrade.pdf
  Exercise_StudentGradePredictor.pdf
  MachineLearning_Week_07.pdf     (lecture slides)
  Loan Approval Prediction.ipynb
  Student Grades Predictor.ipynb
  StudentAbsenceGrade.csv / .ipynb
  StudentGrades.csv
  titanic_800.csv
  Week8_iris_kmeans.py
  Week8_iris_kmeans_pca.py
  Week8_Mnist.py
```

Non-code data not duplicated elsewhere:
- `titanic_800.csv`: 800 rows, comma separated, quoted. Columns: PassengerId, Survived (target), Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked (standard Titanic columns).

Code files (one line each):
- `Week8_iris_kmeans.py`: K-means clustering on the iris dataset with a matplotlib plot (2019).
- `Week8_iris_kmeans_pca.py`: K-means on iris plus PCA for dimensionality reduction/plotting (2019).
- `Week8_Mnist.py`: loads the sklearn digits dataset and trains a RandomForestClassifier with train/test split (2021).
- Notebooks (Loan Approval Prediction, Student Grades Predictor, StudentAbsenceGrade): the notebooks referenced by the exercises above.
