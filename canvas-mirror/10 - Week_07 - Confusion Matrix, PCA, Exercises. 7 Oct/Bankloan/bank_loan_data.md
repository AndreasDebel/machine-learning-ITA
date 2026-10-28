# bank_loan_data.csv - schema

Source: bank_loan_data.csv (comma separated), 614 rows, 13 columns. Target: `Loan_Status` (Y 422, N 192). Used by the Bank Loan exercise.

| Column            | Type  | Missing | Values / examples                        |
|-------------------|-------|---------|------------------------------------------|
| Loan_ID           | str   | 0       | unique, e.g. LP001002                    |
| Gender            | cat   | 13      | Male 489, Female 112                     |
| Married           | cat   | 3       | Yes 398, No 213                          |
| Dependents        | cat   | 15      | 0 (345), 1 (102), 2 (101), 3+ (51)       |
| Education         | cat   | 0       | Graduate 480, Not Graduate 134           |
| Self_Employed     | cat   | 32      | No 500, Yes 82                           |
| ApplicantIncome   | int   | 0       | 150 - 81000, e.g. 5849, 4583             |
| CoapplicantIncome | float | 0       | 0 - 41667                                |
| LoanAmount        | float | 22      | 9 - 700, e.g. 128, 66                    |
| Loan_Amount_Term  | float | 14      | 12 - 480, 10 distinct, mostly 360        |
| Credit_History    | float | 50      | 1 (475), 0 (89)                          |
| Property_Area     | cat   | 0       | Semiurban 233, Urban 202, Rural 179      |
| Loan_Status       | cat   | 0       | Y 422, N 192 (target)                    |
