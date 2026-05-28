import numpy as np

# ── DERIVATIVES ──────────────────────────────
def f(x):
    return x ** 2 # f(x) = x²

def derivative_f(x):
    return 2 * x # f'(x) = 2x

# Verify your paper calculations
for x in [1, 3, 5, 0, -3]:
    print(f"x={x}: f(x)={f(x)}, slope={derivative_f(x)}")

# ── GRADIENT DESCENT SIMULATION ──────────────
print("\n--- Gradient Descent ---")
w = 4.0 # starting weight
lr = 0.1 # learning rate
steps = 20 # number of steps

for step in range(steps):
    loss = f(w)
    slope = derivative_f(w)
    w = w - lr * slope # gradient descent step
    print(f"Step {step+1:2d}: w={w:.4f} loss={loss:.4f}")

print(f"\nFinal w: {w:.6f} (should be close to 0)")
print(f"Final loss: {f(w):.6f} (should be close to 0)")