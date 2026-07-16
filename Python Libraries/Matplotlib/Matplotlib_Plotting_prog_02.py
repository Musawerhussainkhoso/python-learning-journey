#Employee Productivity Comparison
import matplotlib.pyplot as plt

employees = ["Ali", "Sara", "Hamza", "kainat", "Bilal"]
tasks_completed = [48, 62, 55, 70, 59]

plt.figure(figsize=(10, 6))

plt.bar(employees, tasks_completed)

plt.title("Employee Productivity Report", fontsize=16)
plt.xlabel("Employees", fontsize=12)
plt.ylabel("Tasks Completed", fontsize=12)

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()