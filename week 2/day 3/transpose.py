"""P8. Stack these two arrays vertically, then horizontally:
pythona = np.ones((2, 3))
b = np.zeros((2, 3))
Print shape of each result. What changed?"""

import numpy as np

a = np.ones((2, 3))
b = np.zeros((2, 3))
vertical_stack = np.vstack((a,b))
horizontal_stack = np.hstack((a,b))

print(f"a  matrix = {a}")
print("\nArray b:\n", b)

print("\nVertical Stack:\n", vertical_stack)
print("Shape of vertical stack =", vertical_stack.shape)

print("\nHorizontal Stack:\n", horizontal_stack)
print("Shape of horizontal stack =", horizontal_stack.shape)

