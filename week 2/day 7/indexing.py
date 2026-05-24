"""CHALLENGE 2
2D Indexing Master
Given a 4×5 marks matrix, extract specific elements and slices using 2D indexing."""

import numpy as np

# 4 students, 5 subjects
marks = np.array([[72, 85, 60, 91, 78],
                  [90, 88, 95, 82, 70],
                  [55, 60, 58, 67, 72],
                  [80, 75, 82, 88, 65]])


# 1. Print row 2 (student 3's all marks)
# YOUR CODE
print(marks[2])
# 2. Print column 0 (all students' first subject)
# YOUR CODE
print(marks[: , 0])
# 3. Print top-right 2×2 corner (rows 0-1, cols 3-4)
# YOUR CODE
print(marks[0:2 , 3:5])
print(marks[2:4 , 0:2])
# 4. Print the shape, ndim, and size
# YOUR CODE
print("shape :",marks.shape)
print("dimensions :",marks.ndim)