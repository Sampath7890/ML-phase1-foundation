"""Write a function matrix_add(A, B) that:
→ checks if shapes are equal using .shape
→ if shapes match → return A + B
→ if shapes don't match → return "Error: shapes don't match"

Test with:
- two (2×2) matrices → should add
- a (2×3) and (3×2) → should give error"""
import numpy as np 

def matrix_add(A, B) :
    if A.shape == B.shape :
        return A+B
    else :
        return "error : shape does't exist"
    
A = np.array(
    [[1,2],
     [2,3]]
)

B = np.array(
    [[2,3],
     [1,2]]
)

print("addition of 2 matrix A and B :")
print(matrix_add(A,B))

C = np.array(
    [[1,2],
     [2,3],
     [1,2]]
)

D = np.array(
    [[1,2,2],
     [2,3,5]]
)

print("addition of matrix C and D :")
print(matrix_add(C,D))