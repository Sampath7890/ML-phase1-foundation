import numpy as np
import matplotlib.pyplot as plt

classes = np.array(["Class 1", "Class 2", "Class 3"])
survival_rates = np.array([0.63, 0.47, 0.24])
colors = np.array(["#4ACD8A", "#4A90E2", "#F472B6"])

plt.figure(figsize=(7, 5))
bars = plt.bar(classes, survival_rates, color=colors, width=0.5)
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.title("Titanic Survival Rate by Class")
plt.ylim(0, 1)
# Add value labels on top of bars
for bar, rate in zip(bars, survival_rates):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 0.02,
             f"{rate:.0%}", ha="center", fontsize=11)
plt.savefig("survival_bar.png")
plt.show()