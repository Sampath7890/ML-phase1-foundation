"""Unit Vector + Similarity
Given two vectors, normalize both to unit vectors, then compute their dot product. A result close to 1 means they're similar."""

import numpy as np

a = np.array([3.0, 4.0, 0.0])
b = np.array([1.0, 2.0, 2.0])

norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)

unit_a = a/norm_a
unit_b = b/norm_b

similarity = np.dot(unit_a,unit_b)

print(f"similarity = {similarity:.4f}")
print("Perfectly similar = 1.0, No similarity = 0.0, Opposite = -1.0")
