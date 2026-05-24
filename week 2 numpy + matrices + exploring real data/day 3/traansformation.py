#P3. Create a 1D array of 12 elements (values 1–12). Reshape it into 3 different valid 2D shapes. Print all three.

import numpy as np

A = np.arange(1,13)
print(A)

B =A.reshape(3,4)
print("\n3 * 4 matrix  :")
print(f"\n {B}")

C = A.reshape(4,3)
print("\n4 * 3 matrix  :")
print(f"\n {C}")

D = A.reshape(2,6)
print("\n2 * 6 matrix  :")
print(f"\n {D}")