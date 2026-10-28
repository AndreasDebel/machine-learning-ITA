# titanic_alternative.csv - schema note

Source: `Titanic/titanic_alternative.csv`. **887 rows x 8 columns**, no missing values. Target: `Survived` (0/1). Column meanings: see `Titanic_alternative_Columns.md`.

| Column                  | Type | Missing | Unique | Examples                                               |
|-------------------------|------|---------|--------|--------------------------------------------------------|
| Survived                | num  | 0       | 2      | 0, 1 (target)                                          |
| Pclass                  | num  | 0       | 3      | 3, 1, 2                                                |
| Name                    | str  | 0       | 887    | "Mr. Owen Harris Braund" (title, first, surname order) |
| Sex                     | str  | 0       | 2      | male, female                                           |
| Age                     | num  | 0       | 89     | 22, 38, 26                                             |
| Siblings/Spouses Aboard | num  | 0       | 7      | 1, 0, 3                                                |
| Parents/Children Aboard | num  | 0       | 7      | 0, 1, 2                                                |
| Fare                    | num  | 0       | 248    | 7.25, 71.2833, 7.925                                   |

Notes: cleaned variant of the Kaggle data (no PassengerId/Ticket/Cabin/Embarked; Age complete; Fare decimals intact).
