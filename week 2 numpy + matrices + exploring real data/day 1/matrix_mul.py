"""P5 Medium
Matrix multiplication
Create A = [[1,2],[3,4]] and B = [[5,6],[7,8]]
Compute A @ B manually on paper first.
Then verify with NumPy.
They must match."""

import numpy as np 
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print(f"multiplication of matrix A and matrix B = {A @ B}")