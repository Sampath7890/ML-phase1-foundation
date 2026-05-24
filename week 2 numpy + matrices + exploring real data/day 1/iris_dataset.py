"""Iris dataset with NumPy
Load the Iris dataset. X = iris.data (already a NumPy array).
Using only NumPy operations (no loops):
Print shape, mean of each feature, max of each feature.
Find which flower (row) has the largest sepal length: np.argmax(X[:,0])
Print that flower's full feature vector."""

from sklearn.datasets import load_iris
import numpy as np
iris = load_iris()

x = iris.data

print(f"shape of the iris = {x.shape}")

print(f"mean of each feature = {np.mean(x , axis = 0)}")
print(f"max of each feature = {np.max(x , axis = 0)}")
largest_index = np.argmax(x[:,0])
print(f"which flower (row) has the largest sepal length = {largest_index}")

print(f"flower's full feature vector = {x[largest_index]}")
