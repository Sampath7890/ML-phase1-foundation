#P7. Create two 3×3 arrays — A filled with 2s, B as the identity matrix. Compute A @ B. Explain the result in a comment inside your notebook.

import numpy as np 
A = np.full((3,3),2)

B = np.eye(3)


result = A @ B

print("A =\n", A)
print("\nB =\n", B)
print("\nA @ B =\n", result)
