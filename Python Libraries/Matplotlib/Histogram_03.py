#Monthly Salary Distribution
import matplotlib.pyplot as plt

salaries = [
    35000, 42000, 48000, 51000, 55000,
    60000, 62000, 67000, 70000, 75000,
    80000, 85000, 90000, 95000, 105000,
    115000, 125000, 140000, 150000, 180000
]

plt.figure(figsize=(11, 6))

plt.hist(
    salaries,
    bins=6,
    edgecolor="black"
)

plt.title("Employee Salary Distribution")
plt.xlabel("Monthly Salary (PKR)")
plt.ylabel("Number of Employees")

plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()