"""Linear regression visualization
Use your study_hours and exam_scores data from Session 2.
Train your manual linear regression (from Week 4) for 500 epochs.
Create a 1×2 figure:
Left: scatter plot with the fitted regression line
Right: loss curve showing how MSE decreased over 500 epochs
Title each plot. Label axes. Save as regression_analysis.png"""


import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Create data
# -----------------------------
np.random.seed(42)

study_hours = np.random.uniform(1, 8, 20)
exam_scores = 8 * study_hours + np.random.normal(30, 8, 20)

# -----------------------------
# Step 2: Manual Linear Regression
# y = mx + b
# -----------------------------
m = 0
b = 0
learning_rate = 0.01
epochs = 500
n = len(study_hours)

losses = []

# Training loop
for epoch in range(epochs):

    # Predictions
    y_pred = m * study_hours + b

    # Mean Squared Error
    loss = np.mean((exam_scores - y_pred) ** 2)
    losses.append(loss)

    # Gradients
    dm = (-2/n) * np.sum(study_hours * (exam_scores - y_pred))
    db = (-2/n) * np.sum(exam_scores - y_pred)

    # Update parameters
    m = m - learning_rate * dm
    b = b - learning_rate * db

# Final predictions
final_line = m * study_hours + b

# -----------------------------
# Step 3: Create 1x2 Figure
# -----------------------------
plt.figure(figsize=(12, 5))

# LEFT: Scatter + Regression line
plt.subplot(1, 2, 1)
plt.scatter(study_hours, exam_scores,
            color="blue", label="Data Points")

plt.plot(study_hours, final_line,
         color="red", linewidth=2,
         label="Regression Line")

plt.title("Linear Regression Fit")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.legend()

# RIGHT: Loss curve
plt.subplot(1, 2, 2)
plt.plot(losses, color="green", linewidth=2)

plt.title("Loss Curve (MSE over 500 Epochs)")
plt.xlabel("Epoch")
plt.ylabel("Mean Squared Error")

plt.tight_layout()

# Save figure
plt.savefig("regression_analysis.png", dpi=300)

plt.show()