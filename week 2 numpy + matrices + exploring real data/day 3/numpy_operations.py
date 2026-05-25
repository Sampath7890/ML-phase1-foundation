#P2. Create a 3×5 matrix of all zeros. Replace the entire second row with the value 9 — without a loop.

import numpy as np 

A = np.zeros((3,5))
print(A)

A[1] =9
print(f"\n {A}")