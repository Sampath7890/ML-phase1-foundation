"""Axis Prediction Challenge
Before running ANY code — write your prediction for each output. Then run and check. If you're wrong, explain why in a comment."""

import numpy as np

data = np.array([[10, 20, 30, 40],
                 [50, 60, 70, 80],
                 [90, 10, 20, 30]])

# Predict BEFORE running (write answers as comments):
# np.sum(data)              → ? all data should be added
# np.sum(data, axis=0)      → ?
# np.sum(data, axis=1)      → ?
# np.mean(data, axis=0)     → ?
# data.max()                → ?
# np.argmax(data, axis=1)   → ?   # what does argmax do?

print(np.sum(data))
print(np.sum(data, axis=0))
print(np.sum(data, axis=1))
print(np.mean(data, axis=0))
print(data.max())
print(np.argmax(data, axis=1))