#Study Hours vs Exam Scores
import matplotlib.pyplot as plt

study_hours = [1, 2, 2.5, 3, 4, 5, 6, 7, 8]
exam_scores = [42, 48, 55, 57, 65, 72, 78, 86, 91]

plt.figure(figsize=(10, 6))

plt.scatter(
    study_hours,
    exam_scores,
    s=90,
    alpha=0.8,
    marker="^",
    edgecolors="black"
)

plt.title("Study Hours vs Examination Scores")
plt.xlabel("Study Hours per Day")
plt.ylabel("Exam Score (%)")

plt.xlim(0, 9)
plt.ylim(35, 100)

plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()