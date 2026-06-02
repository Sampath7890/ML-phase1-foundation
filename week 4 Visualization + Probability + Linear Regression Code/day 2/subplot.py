import matplotlib.pyplot as plt
import numpy as np

# Data for plot 1 (Loss curve)
epochs = np.arange(1, 11)
loss = [1.2, 1.0, 0.85, 0.72, 0.60, 0.50, 0.42, 0.35, 0.30, 0.25]

# Data for plot 2 (Scatter)
study_hours = np.random.uniform(1, 8, 20)
exam_scores = 8 * study_hours + np.random.normal(30, 8, 20)

# Data for plot 3 (Bar chart)
classes = ["Class 1", "Class 2", "Class 3"]
survival_rates = [0.63, 0.47, 0.24]
colors = ["green", "blue", "pink"]

# Data for plot 4 (Histogram)
scores = np.random.normal(70, 12, 200)

# Create dashboard
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(epochs, loss, color="blue")
plt.title("Loss Curve")
plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.subplot(2, 2, 2)
plt.scatter(study_hours, exam_scores, color="steelblue")
plt.title("Study vs Score")

plt.subplot(2, 2, 3)
plt.bar(classes, survival_rates, color=colors)
plt.title("Titanic Survival by Class")

plt.subplot(2, 2, 4)
plt.hist(scores, bins=15, color="coral")
plt.title("Score Distribution")

plt.tight_layout()
plt.savefig("dashboard.png")
plt.show()