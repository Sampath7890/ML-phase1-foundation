# Create a 2×6 array with values 10–21. Reshape it to 3×4, then to 6×2. Compute the column means at each shape. Do the means change?

import numpy as np

A = np.array([
    [10 ,11,12,13,14,15],
    [16,17,18,19,20,21]
])

print(A.shape)
mean_2x6 = np.mean(A, axis=0)
print(f"mean(2*6) = {mean_2x6}")

B = A.reshape(3, 4)

print("\nReshaped to 3x4:\n", B)

# Column means of 3x4
mean_3x4 = np.mean(B, axis=0)
print("\nColumn means (3x4):", mean_3x4)

# Reshape to 6x2
C = A.reshape(6, 2)

print("\nReshaped to 6x2:\n", C)

# Column means of 6x2
mean_6x2 = np.mean(C, axis=0)
print("\nColumn means (6x2):", mean_6x2)