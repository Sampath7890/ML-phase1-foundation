"""CHALLENGE 2
Full Pipeline: Marks → Averages → Top Students
Build the complete analysis pipeline using ONLY NumPy. No loops. No Pandas."""

import numpy as np

np.random.seed(42)
marks = np.random.randint(50, 100, size=(8, 5))
subjects = ["Math", "Python", "ML", "Stats", "English"]

print("Marks:\n", marks)

# 1. Each student's average (1 line)
student_avg = np.mean(marks , axis=1)
print(f"student average = {student_avg}")

# 2. Each subject's class average (1 line)  
subject_avg = np.mean(marks , axis=0)
print(f"subject average = {subject_avg}")

# 3. Student with highest overall average
top_student_idx = np.argmax(student_avg)
print(f"Top student: #{top_student_idx}, avg: {student_avg[top_student_idx]:.1f}")

# 4. Boolean mask: students with avg > 75
above_75 = student_avg > 75
print(f"Students above 75 avg: {np.where(above_75)[0]}")

# 5. Subject where class average is lowest
hardest_subject = subjects[np.argmin(subject_avg)]
print(f"Hardest subject: {hardest_subject}")