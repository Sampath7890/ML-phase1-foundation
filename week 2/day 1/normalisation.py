"""Normalisation
Normalisation = scale values to range 0 to 1.
Formula: (value - min) / (max - min)
Take marks = [45, 78, 92, 35, 88, 61]
Normalise the entire array in ONE line using NumPy.
All values should now be between 0 and 1.
This is exactly what ML preprocessing does to your data before training."""

import numpy as np 
marks = np.array([45, 78, 92, 35, 88, 61])
normalisation_marks = (marks - np.min(marks))  / (np.max(marks) - np.min(marks))

print(f"normalisation marks = {normalisation_marks}.2f")