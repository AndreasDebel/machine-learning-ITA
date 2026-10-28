# StudentChurn.csv - schema

Source: StudentChurn.csv (named _csv.md because StudentChurn.md is the PDF), semicolon separated, 1086 rows, 7 columns. Target: `Churn` (Completed 768, Stopped 318). Fictive data. Id has 1085 unique values for 1086 rows (one duplicate id).

| Column     | Type  | Missing | Values / examples                          |
|------------|-------|---------|--------------------------------------------|
| Id         | int   | 0       | 15395 - 16494                              |
| Churn      | cat   | 0       | Completed 768, Stopped 318 (target)        |
| Line       | cat   | 0       | HF 427, STX 301, HTX 157, HHX 150, EUX 51  |
| Grade      | float | 0       | 2.0 - 12.0, e.g. 6.7, 8.8                  |
| Age        | int   | 0       | 18 - 44                                    |
| Distance   | float | 0       | 1 - 100, e.g. 6.0, 2.0                     |
| StudyGroup | float | 10      | 1 (617), 0 (459)                           |
