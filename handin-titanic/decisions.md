# Titanic hand-in - decisions

Outcome of the grill-me session. The requirements themselves are in `expected-solution-findings.md`.

## Decided

| Area           | Decision                                                                                          |
|----------------|---------------------------------------------------------------------------------------------------|
| Goal           | Get the assignment approved; nothing more                                                         |
| Exercise       | Titanic, because it is well-defined and safer; one sentence in the report                         |
| Data           | `titanic_800.csv` only; `titanic_alternative.csv` (887 rows) is skipped                           |
| Report         | Danish, 1 page, plus `.py` file(s), zipped to one file of 1-2 MB                                  |
| Way of working | Claude writes the code a little at a time; the user follows along and asks questions              |
| Split          | 80:20 (640 train / 160 test), random, fixed `random_state`, stratified on `Survived`              |
| Split reason   | Enough rows to learn the pattern; enough test rows for a stable precision/recall score            |

## Postponed (not decided)

- **Model** - to be discussed at length; it is part of the assignment (section C).
- **Feature removal** and the evidence for it (correlation or plots) - section B.
- **Missing `Age`** - mean, 0, or drop rows - section B.

## Terms agreed on

- **Fixed seed** (`random_state`): makes the random split repeatable, so results match on every run.
- **Stratify**: keep the survived/died ratio equal in the train and test sets.
