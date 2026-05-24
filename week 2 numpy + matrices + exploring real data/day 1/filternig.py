"""Filtering
Create array: [78, 35, 92, 28, 65, 88, 15, 72, 45, 60]
Using NumPy boolean indexing (no loops, no if/else):
Print all marks above 60.
Print all failing marks (below 40).
Count how many passed: len(marks[marks >= 40])"""

import numpy as np 

marks = np.array([78, 35, 92, 28, 65, 88, 15, 72, 45, 60])

print(f"all marks above 60 = {marks[marks >= 60]}")
print(f"all failing marks (below 40) = {marks[marks <= 40]}")
print(f"how many passed = {len(marks[marks >= 40])}")
