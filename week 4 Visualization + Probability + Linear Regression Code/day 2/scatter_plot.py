import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
study_hours = np.random.uniform(1, 8, 20)
exam_scores = 8 * study_hours + np.random.normal(30, 8, 20)

# Trend line using polyfit
m, b = np.polyfit(study_hours, exam_scores, 1)
trend = m * study_hours + b

plt.figure(figsize=(8, 5))
plt.scatter(study_hours, exam_scores,
           color="steelblue", s=80, alpha=0.7, label="Students")
plt.plot(sorted(study_hours),
        [m*x+b for x in sorted(study_hours)],
        color="red", linewidth=2, label=f"Trend: y={m:.1f}x+{b:.1f}")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Score — KMCE Students")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("scatter_study.png")
plt.show()
print(f"Slope: {m:.2f} — each extra hour adds {m:.1f} marks")