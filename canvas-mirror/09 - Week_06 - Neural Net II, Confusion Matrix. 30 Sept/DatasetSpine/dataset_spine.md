# dataset_spine.csv (schema summary)

Source: `dataset_spine.csv` (UTF-8, comma separated, header row). Lower back pain / spine dataset (see `Exercise_DataSetSpine.md`).

- **Rows:** 310 data rows. **Columns:** 13 real columns plus a trailing unnamed 14th column.
- **Target:** `Class_att` (binary: `Abnormal` 210, `Normal` 100).
- **Missing values:** none in Col1-Col12 or Class_att.
- The unnamed 14th column is empty except in ~14 rows, where it holds free-text notes (leftover documentation): "Prediction is done by using binary classification."; attribute names (below); and the class attribute definition ("Attribute class {Abnormal, Normal}"). Drop this column before training.

| Column     | Attribute (from notes)    | dtype   | Example (row 1) | Min     | Max      | Mean  |
|------------|---------------------------|---------|-----------------|---------|----------|-------|
| Col1       | pelvic_incidence          | float   | 63.0278175      | 26.15   | 129.83   | 60.50 |
| Col2       | pelvic_tilt               | float   | 22.55258597     | -6.55   | 49.43    | 17.54 |
| Col3       | lumbar_lordosis_angle     | float   | 39.60911701     | 14.00   | 125.74   | 51.93 |
| Col4       | sacral_slope              | float   | 40.47523153     | 13.37   | 121.43   | 42.95 |
| Col5       | pelvic_radius             | float   | 98.67291675     | 70.08   | 163.07   | 117.92|
| Col6       | degree_spondylolisthesis  | float   | -0.254399986    | -11.06  | 418.54   | 26.30 |
| Col7       | pelvic_slope              | float   | 0.744503464     | 0.003   | 0.999    | 0.47  |
| Col8       | Direct_tilt               | float   | 12.5661         | 7.03    | 36.74    | 21.32 |
| Col9       | thoracic_slope            | float   | 14.5386         | 7.04    | 19.32    | 13.06 |
| Col10      | cervical_tilt             | float   | 15.30468        | 7.03    | 16.82    | 11.93 |
| Col11      | sacrum_angle              | float   | -28.658501      | -35.29  | 6.97     | -14.05|
| Col12      | scoliosis_slope           | float   | 43.5123         | 7.01    | 44.34    | 25.65 |
| Class_att  | class label               | string  | Abnormal        | -       | -        | -     |
