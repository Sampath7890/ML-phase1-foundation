"""Scatter with color-coded categories
Create synthetic data for 3 flower types (30 points each):
Type A: x≈2, y≈3. Type B: x≈5, y≈6. Type C: x≈8, y≈2.
Add random noise to both x and y.
Plot scatter with different colors per type. Add legend.
This is exactly what you'll see when visualizing the Iris dataset."""

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

# Type A around (2,3)
x1 = np.random.normal(2, 0.5, 30)
y1 = np.random.normal(3, 0.5, 30)

# Type B around (5,6)
x2 = np.random.normal(5, 0.5, 30)
y2 = np.random.normal(6, 0.5, 30)

# Type C around (8,2)
x3 = np.random.normal(8, 0.5, 30)
y3 = np.random.normal(2, 0.5, 30)

plt.figure(figsize=(7,5))

plt.scatter(x1, y1, color="red", label="Type A")
plt.scatter(x2, y2, color="blue", label="Type B")
plt.scatter(x3, y3, color="green", label="Type C")

plt.xlabel("Feature X")
plt.ylabel("Feature Y")
plt.title("Flower Type Scatter Plot")
plt.legend()

plt.show()