"""Create a (5×3) matrix — 5 KMCE students, 3 subject marks.
Using NumPy only (no loops):
→ Average mark per student (axis=1)
→ Average mark per subject (axis=0)
→ Highest scoring student: np.argmax(row averages)
→ Lowest scoring subject: np.argmin(column averages)
Print all 4 results with proper labels."""

import numpy as np 

marks = np.array([
    [90,80,70], 
    [88,70,88],
    [80,75,60],
    [70,60,50],
    [80,40,60]

])

average_student = np.mean(marks , axis = 1)
average_subject = np.mean(marks , axis = 0)
highest_student = np.argmax(average_student)
lowest_subject = np.argmax(average_subject)
print(f"→ Average mark per student = {average_student}")
print(f"→ Average mark per subject = {average_subject}")
print(f"Highest scoring student : {highest_student}")
print(f"Lowest scoring subject : {lowest_subject}")
