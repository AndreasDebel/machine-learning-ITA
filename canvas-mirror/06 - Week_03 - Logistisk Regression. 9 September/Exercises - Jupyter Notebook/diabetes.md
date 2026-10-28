# diabetes.csv (schema summary)

Source: `Exercises - Jupyter Notebook/diabetes.csv` (used by `diabetes.ipynb` in the same folder). Looks like the Pima Indians Diabetes dataset.

- Rows: 768 (plus header). Columns: 9. No empty cells (no NaN).
- Target: `Outcome` (0 = 500 rows, 1 = 268 rows).

| Column                   | Dtype | Example      | Zero values (likely missing) |
|--------------------------|-------|--------------|------------------------------|
| Pregnancies              | int   | 6, 1         | n/a                          |
| Glucose                  | int   | 148, 85      | 5                            |
| BloodPressure            | int   | 72, 66       | 35                           |
| SkinThickness            | int   | 35, 29       | 227                          |
| Insulin                  | int   | 0, 0         | 374                          |
| BMI                      | float | 33.6, 26.6   | 11                           |
| DiabetesPedigreeFunction | float | 0.627, 0.351 | n/a                          |
| Age                      | int   | 50, 31       | n/a                          |
| Outcome                  | int   | 1, 0         | target                       |

Note: zeros in Glucose, BloodPressure, SkinThickness, Insulin and BMI are physiologically impossible and act as hidden missing values.
