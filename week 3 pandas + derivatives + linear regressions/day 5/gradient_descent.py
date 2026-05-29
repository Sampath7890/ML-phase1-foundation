"""Write gradient_descent(start, learning_rate, steps):
→ Loss function: L(w) = w²
→ Derivative: 2w
→ Update: w = w - learning_rate × derivative
→ Store w and loss at each step in two NumPy arrays
→ Return both arrays

Run with: start=10.0, lr=0.1, steps=50

Print a table:
Step | w value | loss
Show how both decrease toward 0."""

import numpy as np
def gradient_descent(start, learning_rate, steps):
    w = start
    w_values = []
    loss_values = []

    for step in range(steps) :
        loss = w ** 2
        derivative = 2*w

        w_values.append(w)
        loss_values.append(loss)

        w = w - learning_rate * derivative
    return np.array(w_values) , np.array(loss_values)


w_array, loss_array = gradient_descent(
    start=10.0,
    learning_rate=0.1,
    steps=50
)

print("Step | w value | loss")
print("-" *30)

for i in range (len(w_array)):
    print(f"{i:>4} | {w_array[i]:>7.4f} | {loss_array[i]:>10.6f}")



