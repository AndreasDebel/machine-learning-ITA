# shows.csv - schema summary

Path: `Comedians/shows.csv`. Rows: 13 (plus header). Delimiter `,`. Missing values: none.

| Column      | Dtype  | Example values       |
|-------------|--------|----------------------|
| Age         | int    | 36, 42, 23, 52, 66   |
| Experience  | int    | 10, 12, 4, 21, 3     |
| Rank        | int    | 9, 4, 6, 8, 5, 7     |
| Nationality | string | UK, USA, N           |
| Go          | string | NO, YES (target)     |

Target: `Go` (did the person go to the show): 7 YES, 6 NO. Nationality is categorical and must be encoded (UK/USA/N -> numbers) before fitting a tree. Used by `Comedians.py` (see `ComediansDecisionTree.md`).
