"""Create a NumPy array of x values: np.linspace(-5, 5, 100)
Compute f(x) = x² for all x values in one line.
Compute the derivative 2x for all x values in one line.

Find using NumPy:
→ x value where slope is closest to 0 (bottom of curve)
→ x value where slope is steepest (largest absolute value)
→ All x values where slope is positive
→ All x values where slope is negative

Print each result clearly."""

import numpy as np
x = np.linspace(-5, 5, 100)

y = x ** 2
dy =  2 * x

bottom_x = x[np.argmin(np.abs(x))]
steepest_x = x[np.argmax(np.abs(dy))]

positive_slope = x[dy > 0]
negative_slope = x[dy<0]

print("x where slope is clsoed to 0 : ",bottom_x)
print("x where slope is steepest ",steepest_x)
print("x vales where slope is positive\n")
print(positive_slope)
print("x values where slope is negative\n")
print(negative_slope)