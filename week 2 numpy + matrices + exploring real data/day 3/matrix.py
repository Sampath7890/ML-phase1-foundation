# Create a 4×4 identity matrix. Then multiply it by 7. What do you notice about the result?


import numpy as np 

A = np.eye(4,4)
print("before multiplication")
print(A)

print("\nafter multiplication")
print(A*7)

