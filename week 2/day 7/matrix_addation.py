"""Matrix Addition by Hand → Verify
Add these matrices by hand. Then verify with NumPy. Both must match."""

import numpy as np 

A = np.array([[1, 4, 7],
              [2, 5, 8],
              [3, 6, 9]])

B = np.array([[9, 6, 3],
              [8, 5, 2],
              [7, 4, 1]])
size = np.size(A)
print("size :",size)

dimensions = np.ndim(B)
print("dimensions : ",dimensions)

addation = A +  B

print(f"addation of {A} and {B} = {addation}")

transpose_a = A.T
transpose_b = B.T
print("transpose of A =",transpose_a)
print("transpose of B = ",transpose_b)


