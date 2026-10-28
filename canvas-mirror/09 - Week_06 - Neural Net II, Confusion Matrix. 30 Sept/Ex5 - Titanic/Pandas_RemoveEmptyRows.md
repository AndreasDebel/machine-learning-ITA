# Pandas_RemoveEmptyRows

Source: `Pandas_RemoveEmptyRows.txt` (6 lines, all commented out).

Hint snippet: "Something like this" - drop rows with missing values from a DataFrame `data`:

```python
import numpy as np
print(data.shape)
data.replace("", np.nan, inplace=True)
data.dropna(how='any', axis=0, inplace=True)
print(data.shape)
```

(Lines carry a leading `#` in the original.) Relevant for the missing `Age` values in `titanic_train_500_age_passengerclass.csv`.
