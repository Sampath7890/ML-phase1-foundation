import numpy as np
import pandas as pd
import matplotlib.pylab as plt
mean = 72
std = 10
x = np.linspace(mean - 4*std, mean + 4*std, 300)
y = ((1/(std*np.sqrt(2*np.pi))) *
     np.exp(-0.5*((x-mean)/std)**2))

plt.figure(figsize=(9, 5))
plt.plot(x, y, "steelblue", linewidth=2)
plt.axvline(mean, color="red", linestyle="--", label=f"Mean={mean}")
plt.axvline(mean+std, color="green", linestyle=":", label=f"+1σ={mean+std}")
plt.axvline(mean-std, color="green", linestyle=":", label=f"-1σ={mean-std}")
plt.axvline(mean+2*std, color="orange", linestyle=":", label=f"+2σ={mean+2*std}")
plt.axvline(mean-2*std, color="orange", linestyle=":", label=f"-2σ={mean-2*std}")
plt.fill_between(x, y,
                 where=(x>=mean-std) & (x<=mean+std),
                 alpha=0.2, color="green", label="68% of students")
plt.xlabel("Exam Score")
plt.ylabel("Probability Density")
plt.title("KMCE Exam Score Distribution (Normal)")
plt.legend(fontsize=9)
plt.savefig("normal_distribution.png")
plt.show()