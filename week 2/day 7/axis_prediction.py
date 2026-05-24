"""Axis Prediction Challenge
Before running ANY code — write your prediction for each output. Then run and check. If you're wrong, explain why in a comment."""

import numpy as np

data = np.array([[10, 20, 30, 40],
                 [50, 60, 70, 80],
                 [90, 10, 20, 30]])

# Predict BEFORE running (write answers as comments):
# np.sum(data)              → ? all data should be added
# np.sum(data, axis=0)      → ? addation each column  
# np.sum(data, axis=1)      → ? addation of each row
# np.mean(data, axis=0)     → ? mean of each column
# data.max()                → ? maximum number of the data (90)
# np.argmax(data, axis=1)   → ?   # what does argmax do?  position of the highest number in the data (index number of highest point in data)

print(np.sum(data))
print(np.sum(data, axis=0))
print(np.sum(data, axis=1))
print(np.mean(data, axis=0))
print(data.max())
print(np.argmax(data, axis=1))