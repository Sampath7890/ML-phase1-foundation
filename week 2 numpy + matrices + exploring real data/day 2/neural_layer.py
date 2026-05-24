"""Simulate a 2-layer neural network using matrix multiplication:

Layer 1:
input = [[1, 2, 3]]        # shape (1×3)
W1 = your own (3×4) matrix # 3 inputs → 4 neurons

Layer 2:
W2 = your own (4×2) matrix # 4 neurons → 2 outputs

Compute:
layer1_output = input @ W1   # shape?
final_output  = layer1_output @ W2  # shape?

Print both outputs and their shapes.
Write a comment explaining what just happened."""


import numpy as np

input_data = np.array([[1,2,3]])

w1 = np.array(
    [
        [1,0,2,1],
        [1,0,5,1],
        [0,1,2,0]
    ]
)

w2 = np.array(
    [
        [1,0],
        [1,0],
        [0,1],
        [2,0]
    ]
)

layer1_output = input_data @ w1
final_output = layer1_output

print("layer 1 output:")
print(layer1_output)
print(f"out shape = {layer1_output.shape}")


print("final output:")
print(final_output)
print(f"output shape = {final_output.shape}")


