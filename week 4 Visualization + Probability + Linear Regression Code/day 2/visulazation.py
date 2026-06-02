#Chart 1 — Line plot
import matplotlib.pyplot as plt
import numpy as np

# Line plot — gradient descent loss curve
epochs = list(range(1, 21))
loss = [100 * (0.85**i) for i in epochs]

plt.figure(figsize=(8, 5))
plt.plot(epochs, loss, color="blue", linewidth=2, marker="o")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss Over Epochs")
plt.grid(True, alpha=0.3)
plt.savefig("loss_curve.png")
plt.show()