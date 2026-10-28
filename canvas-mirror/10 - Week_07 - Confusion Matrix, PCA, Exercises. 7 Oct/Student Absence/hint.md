# hint (Student Absence)

Source: hint.txt (one line)

Pandas snippet for exercise a) (replace grade values):

```
df.loc[df['grade']=='0', 'grade'] = '2'
```

*Note: compares against the string '0', i.e. assumes the grade column was read as strings.*
