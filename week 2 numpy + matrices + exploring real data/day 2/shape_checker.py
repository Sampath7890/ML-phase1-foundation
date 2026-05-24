"""Write a function can_multiply(A, B) that:
→ returns True if A @ B is valid
→ returns False if not
→ if True — also prints the output shape

Test with all 4 cases from Problem 7 in today's plan."""
import numpy as np
def can_multiply(A, B) :
    if A.shape[1] == B.shape[0] :
        out_shape = (A.shape[0] , B.shape[1])
        print("multiplication possible")
        print(f"out shape = {out_shape}")
        return True
    
    else :
        print("matrix multiplication is not possible")
        return False
    

# Case 1: (2×3) @ (3×2) → Valid
A1 = np.array([[1, 2, 3],
               [4, 5, 6]])

B1 = np.array([[1, 2],
               [3, 4],
               [5, 6]])

print("Case 1:")
print(can_multiply(A1, B1))
print()


# Case 2: (3×2) @ (2×4) → Valid
A2 = np.array([[1, 2],
               [3, 4],
               [5, 6]])

B2 = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8]])

print("Case 2:")
print(can_multiply(A2, B2))
print()


# Case 3: (2×2) @ (3×2) → Invalid
A3 = np.array([[1, 2],
               [3, 4]])

B3 = np.array([[1, 2],
               [3, 4],
               [5, 6]])

print("Case 3:")
print(can_multiply(A3, B3))
print()


# Case 4: (4×1) @ (1×5) → Valid
A4 = np.array([[1],
               [2],
               [3],
               [4]])

B4 = np.array([[1, 2, 3, 4, 5]])

print("Case 4:")
print(can_multiply(A4, B4))