# titanic_train_500_age_passengerclass.csv (schema summary)

Source: `titanic_train_500_age_passengerclass.csv`. Limited Titanic dataset for Week 6 Exercise 5.

- **Rows:** 500 (header + 500 data rows). Intended split: first 400 train, last 100 test.
- **Target:** `Survived` (0 = died, 1 = survived).

| Column      | dtype | Example | Notes                                               | Missing |
|-------------|-------|---------|-----------------------------------------------------|---------|
| PassengerId | int   | 1       | 1-500, unique; likely not a useful feature          | 0       |
| Survived    | int   | 0       | 0: 307, 1: 193 (whole file: 61.4 % died)            | 0       |
| Pclass      | int   | 3       | 1: 116, 2: 105, 3: 279                              | 0       |
| Age         | float | 22      | range 0.75-71, mean 29.28 (non-missing)             | 103     |

First rows: (1,0,3,22), (2,1,1,38). The exercise text says 64 % of the last 100 rows (test set) died, so an "always died" predictor scores 64 %.
