#P6. Find the highest mark scored by any student in the entire array. Then find which student scored the overall highest total.


import numpy as np 

marks = np.array([[72, 85, 90],
                  [60, 55, 70],
                  [88, 92, 78],
                  [45, 60, 55],
                  [95, 88, 100]])

highest_marks = np.max(marks)
student_total = np.sum(marks  , axis = 1)
top_student = np.argmax(student_total)

print("Highest mark in the class =", highest_marks)
print("Student totals =", student_total)
print("Student with highest total =", top_student)


