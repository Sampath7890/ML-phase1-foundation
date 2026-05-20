#P5. Using the same marks array — find the average score per subject (3 values). Which subject has the highest class average?

import numpy as np 

marks = np.array([[72, 85, 90],
                  [60, 55, 70],
                  [88, 92, 78],
                  [45, 60, 55],
                  [95, 88, 100]])

averae_sub = np.average(marks , axis = 0)
print(averae_sub)
highest_average = np.argmax(averae_sub)
print(highest_average)