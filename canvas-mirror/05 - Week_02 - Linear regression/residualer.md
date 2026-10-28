# Residualer (Residuals) - ML ITA, Dag 2

Source: `residualer.pdf`, 2 pages, in Danish. No author/date visible.

## Page 1
*[Figure p.1: ASCII sketch of y-axis/x-axis with points (Punkt 2, Punkt 3) and a line; vertical segments from points to the line are labelled "Residual (fejl)" and "Residual (negativ fejl)".]*

Text: These are the distances where we want to place our line such that these "residuals" are as small as possible.

*[Figure p.1: Khan Academy video screenshot: points (1,1), (2,2), (2,3), (3,6) with fitted line y-hat = 2.50x - 2, residual marked in red (+0.5 at x=1); stats x-bar = 2, s_x = 0.816, y-bar = 3, s_y = 2.160.]*

See the Khan Academy video (residual plots): https://da.khanacademy.org/math/statistics-and-probability-gammel/xe94a549e556e23cf:describing-relationships-quantitative-data/xe94a549e556e23cf:regression-library/v/residual-plots

## Page 2
The point is that we want to compute a and b in the line equation y = ax + b so that the residuals taken together become as small as possible.

Ways to do it:
- Make random guesses for a and b, see what total residual that gives, repeat 5,000 times, and take the best a and b as the answer.
- Or take the best values so far and take small steps from them, i.e. change a and b a little and see if it gets better.

"There are many possibilities..."
