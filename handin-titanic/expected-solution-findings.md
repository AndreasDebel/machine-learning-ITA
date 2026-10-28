# Titanic assignment - what solution is expected?

Findings from comparing `canvas-mirror/INDEX.md` with the assignment text and the Week 6 material
(`Exercises_Week_06.md`, `Ex5 - Titanic/`). Week 7 slides were **not** checked yet.

## Verdict

A small, classic tabular classification pipeline built with scikit-learn and pandas. Not a research project.

## Evidence

- **Week 6 Ex. 5 is the template.** Same task (predict `Survived`), same steps: load the CSV with pandas, split
  `Survived` off as y, handle missing `Age`, scale with `StandardScaler`, split train/test, fit `MLPClassifier`, then
  `confusion_matrix` and `classification_report`.
- **Baseline to beat.** Ex. 5 used "always predict died" (about 64 %) as the bar. Compare your accuracy against it.
- **Evaluation.** Weeks 6-7 cover accuracy computed by hand from TP/TN/FP/FN, plus precision and recall.
  Assignment section D asks for exactly those.
- **Model.** Any course model is allowed (MLP, decision tree, random forest). MLP is the safest fit; justify the choice.
- **Scope.** A 1-page report plus `.py` file(s), zipped to 1-2 MB.

## What is new compared with Week 6

| Area             | Requirement                                                                              |
|------------------|------------------------------------------------------------------------------------------|
| Feature choice   | Drop likely irrelevant features (`name`, `passengerId`, probably `ticket`, `cabin`); back it with correlation or plots |
| Encoding         | Convert `sex` and `embarked` to numbers in both train and test set                       |
| Split            | Choose and justify the train/test split of the 800 samples                               |
| Experiments      | Vary parameters or compare a second model (section E); document the results             |

## Open points

- Check the Week 7 slides (`MachineLearning_Week_07.md`) for Titanic-specific hints.
- `titanic_alternative.csv` (887 rows) is skipped; see `decisions.md`.
