# titanic_800.csv - schema note

Source: `Titanic/titanic_800.csv`. **800 rows x 12 columns** (standard Kaggle Titanic column set, first 800 passengers). Target: `Survived` (0/1).

| Column      | Type | Missing | Unique | Examples                                              |
|-------------|------|---------|--------|-------------------------------------------------------|
| PassengerId | num  | 0       | 800    | 1, 2, 3                                               |
| Survived    | num  | 0       | 2      | 0, 1 (target)                                         |
| Pclass      | num  | 0       | 3      | 3, 1, 2                                               |
| Name        | str  | 0       | 800    | "Braund, Mr. Owen Harris" (Surname, Title. First)     |
| Sex         | str  | 0       | 2      | male, female                                          |
| Age         | num  | 163     | 85     | 22, 38, 26                                            |
| SibSp       | num  | 0       | 7      | 1, 0, 3                                               |
| Parch       | num  | 0       | 7      | 0, 1, 2                                               |
| Ticket      | str  | 0       | 625    | A/5 21171, PC 17599                                   |
| Fare        | num  | 0       | 234    | 7.25, 71.2833; row 3 reads "7925" (7.925, decimal point lost) |
| Cabin       | str  | 615     | 136    | C85, C123, E46 (77% missing)                          |
| Embarked    | str  | 1       | 3      | S, C, Q                                               |

Notes: Age needs imputation (20% missing); Cabin mostly missing; check Fare for decimal-point errors.
