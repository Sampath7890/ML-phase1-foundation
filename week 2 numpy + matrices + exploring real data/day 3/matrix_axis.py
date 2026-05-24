"""P4. Create this array manually:
marks = [[72, 85, 90],
         [60, 55, 70],
         [88, 92, 78],
         [45, 60, 55],
         [95, 88, 100]]
Compute each student's average. No loops. Print result with shape (5,)."""

import numpy as np 

marks = np.array([[72, 85, 90],
                  [60, 55, 70],
                  [88, 92, 78],
                  [45, 60, 55],
                  [95, 88, 100]])


average = np.average(marks , axis = 1)
print(average)
print(average.shape)