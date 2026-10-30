# Hand-in: Titanic (individual) - due Mon 2 Nov 2026, 20:00

This folder holds everything for the hand-in. To submit: zip the folder contents into **one** file (1-2 MB), upload
to Canvas.

## References

| File                                                                                                                                                                                       | Purpose                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| [Assignment text](../canvas-mirror/03%20-%20Obligatorisk%20Opgave%20-%20Supply%20Chain,%20Titanic%20opg.%20(Individuel%20opgave)%20-%20Aflevering%202%20Nov/Ita_ML_SupplyChain_Titanic.md) | The assignment (rules, sections A-E) |

## Files

Run from inside this folder: `clean.py` first (writes everything in `data/`), then `titanic.py`.

| File                                                           | Purpose                                                                                        |
|----------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [clean.py](clean.py)                                           | All data prep: fix `Fare`, encode, flag missing `Age`, drop features, split, fill `Age`, scale |
| [titanic.py](titanic.py)                                       | Section A exploration; loads the train/test CSVs; the model (sections C-E, to do)              |
| [correlation.ipynb](correlation.ipynb)                         | Evidence for the feature choice (correlation chart, age plot)                                  |
| [data/](data/INDEX.md)                                         | All CSV files, raw to train/test; `data/INDEX.md` says what each one is                        |
| [final-report.md](final-report.md)                             | Draft answers in Danish, section by section; the source for the 1-page report                  |
| [decisions.md](decisions.md)                                   | Decisions made so far and what is still open                                                   |
| [expected-solution-findings.md](expected-solution-findings.md) | What kind of solution is expected, from the Canvas files                                       |
| [visuals/](visuals/)                                           | Learning aids, not handed in: model plots and comparison; run the notebooks from that folder  |

## Hand-in contents (to be added)

- [ ] `clean.py` and `titanic.py` - the Python code
- [ ] `report` - 1-page document (Danish or English), includes why Titanic was chosen over Supply Chain
- [ ] Data file(s) only if needed and the zip stays under 2 MB (`data/` is about 0.2 MB)

Working notes, leave out of the zip: `INDEX.md`, `data/INDEX.md`, `expected-solution-findings.md`, `decisions.md`,
`final-report.md`, `visuals/`.
