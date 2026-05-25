"""Create and explore
Create a NumPy array of your KMCE marks in 5 subjects.
Print: sum, mean, max, min, std, sorted version.
All in one line each — no loops."""


import numpy as np 

marks = np.array([40,50,60,80,80])

print(f"sum = {np.sum(marks)}")
print(f"mean = {np.mean(marks)}")
print(f"max = {np.max(marks)}")
print(f"min = {np.min(marks)}")
print(f"sorted = {np.sort(marks)}")
print(f"std = {np.std(marks)}")

