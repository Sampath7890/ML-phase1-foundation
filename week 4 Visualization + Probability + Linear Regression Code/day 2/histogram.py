import numpy as np
import matplotlib.pyplot as plt

scores = np.random.normal(70 , 12 , 200)
scores = np.clip(scores , 0 , 100)


plt.figure(figsize=(8, 5))
plt.hist(scores, bins=20, color="steelblue", edgecolor="white")
plt.axvline(np.mean(scores), color="red",
            linestyle="--", label=f"Mean: {np.mean(scores):.1f}")
plt.xlabel("Exam Score")
plt.ylabel("Number of Students")
plt.title("Distribution of KMCE Exam Scores")
plt.legend()
plt.savefig("score_histogram.png")
plt.show()