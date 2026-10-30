# Titanic hand-in - decisions

Outcome of the grill-me session. The requirements themselves are in `expected-solution-findings.md`.

## Decided

| Area                | Decision                                                                                           |
|---------------------|----------------------------------------------------------------------------------------------------|
| Goal                | Get the assignment approved; nothing more                                                          |
| Exercise            | Titanic, because it is well-defined and safer; one sentence in the report                          |
| Data                | `titanic_800.csv` only; `titanic_alternative.csv` (887 rows) is skipped                            |
| Report              | Danish, 1 page, plus `.py` file(s), zipped to one file of 1-2 MB                                   |
| Way of working      | Claude writes the code a little at a time; the user follows along and asks questions               |
| Split               | 80:20 (640 train / 160 test), random, fixed `random_state`, stratified on `Survived`               |
| Split reason        | Enough rows to learn the pattern; enough test rows for a stable precision/recall score             |
| Features            | Keep `Sex`, `Pclass`, `Age`, `Fare`, `Embarked`; drop `SibSp`, `Parch`, `Ticket`, `Cabin`          |
| Missing `Age`       | Training-set median + `Age_missing` flag (missing-age passengers survived less)                    |
| Missing `Embarked`  | 1 row; `S` filled before the split (the mode in any split)                                         |
| `Embarked` encoding | One-hot: `Embarked_C`, `Embarked_Q`, `Embarked_S` (ports have no order)                            |
| Scaling             | `StandardScaler` on `Pclass`, `Age`, `Fare` only; fitted on training set (course week 6 precedent) |
| Model               | Decision tree (section C), for now; random forest planned for section E; see `final-report.md`     |

## Terms agreed on

- **Fixed seed** (`random_state`): makes the random split repeatable, so results match on every run.
- **Stratify**: keep the survived/died ratio equal in the train and test sets.
