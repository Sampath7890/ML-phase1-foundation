"""Vector operations in one line
Create v1 = [1,2,3,4] and v2 = [5,6,7,8] as NumPy arrays.
Print: v1+v2, v1*v2, v1*3, np.dot(v1,v2)
Verify dot product matches your hand calculation from Week 1.
"""

import numpy as np
v1 = np.array([1,2,3,4]) 
v2 = np.array([5,6,7,8])

print(f"addition of two vectors = {v1 + v2}")
print(f"multiplication of two vectors = {v1 * v2}")
print(f"multiplication with a scalar v1 = {v1 * 3 }")
print(f"multiplication with a scalar v2 = {v2 * 3 }")
print(f"dot product of v1 and v2 = {np.dot(v1,v2) }")





