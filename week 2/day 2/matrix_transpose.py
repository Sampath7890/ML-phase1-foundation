"""Write a function show_transpose(M) that:
→ prints the original matrix and its shape
→ prints the transposed matrix and its shape
→ prints: "Rows became columns, columns became rows"

Test with a (3×4) matrix of your own numbers."""

import numpy as np

def show_transpose(M) :
    print("original matrix")
    print(M)
    print(f"shape = {M.shape}")

    print("transposed matrix")
    T =M.T
    print(T)
    print(f"shape = {T.shape}")
    print("Rows became columns, columns became rows")


M = np.array([
    [1,2,3],
    [2,3,4],
    [3,4,5],
    [5,6,7]
])

print(show_transpose(M))