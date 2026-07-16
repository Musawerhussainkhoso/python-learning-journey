#Employee Performance Comparison
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]

employee_a = [82, 85, 88, 91, 95]
employee_b = [78, 80, 83, 86, 90]
target = [80, 80, 85, 90, 90]

plt.figure(figsize=(10,6))

plt.plot(
    months,
    employee_a,
    color="blue",
    linestyle="-",
    marker="o",
    linewidth=2,
    label="Employee A"
)

plt.plot(
    months,
    employee_b,
    color="green",
    linestyle="--",
    marker="s",
    linewidth=2,
    label="Employee B"
)

plt.plot(
    months,
    target,
    color="red",
    linestyle=":",
    linewidth=3,
    label="Target"
)

plt.title("Employee Monthly Performance")
plt.xlabel("Months")
plt.ylabel("Performance Score")

plt.grid(True, linestyle=":")
plt.legend()

plt.tight_layout()
plt.show()