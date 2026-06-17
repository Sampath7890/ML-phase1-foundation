import numpy as np
import matplotlib.pyplot as plt


print("--- Basic Probability ---")
p_rain = 0.4
p_umbrella = 0.3
print(f"P(rain AND umbrella): {p_rain * p_umbrella:.2f}")
print(f"P(rain OR umbrella): {p_rain + p_umbrella - p_rain*p_umbrella:.2f}")