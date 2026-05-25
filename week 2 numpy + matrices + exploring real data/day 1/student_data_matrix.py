"""Create a 5×3 matrix representing 5 KMCE students and 3 subject marks.
Print: shape, first row, third column, average mark per student (axis=1), average per subject (axis=0).
Which student has the highest average? Which subject has the lowest average?"""

import numpy as np 
 

marks = np.array([
    [60,70,80],
    [80,60,80],
    [60,80,50],
    [40,90,80],
    [80,50,60]
])

print(f"shape = {marks.shape}")

print(f"first row = {marks[0]}")
print(f"third row = {marks[:, 2]}")

averge_student = np.mean(marks , axis=1)
average_subject = np.mean(marks , axis =0)

print(f"average mark per student = {averge_student}")
print(f"average per subject = {average_subject}")

print(f"student with highest average = {np.argmax(averge_student)}")
print(f"student with lowest average = {np.argmin(averge_student)}")
