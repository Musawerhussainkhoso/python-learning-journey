#Employee Age Distribution
import matplotlib.pyplot as plt

ages = [
    22, 25, 27, 29, 31, 32, 34, 35, 36, 38,
    40, 42, 43, 45, 47, 49, 52, 54, 56, 60
]

plt.figure(figsize=(10, 6))

plt.hist(
    ages,
    bins=[20, 30, 40, 50, 60, 70],
    edgecolor="black"
)

plt.title("Employee Age Distribution")
plt.xlabel("Age Groups")
plt.ylabel("Number of Employees")

plt.grid(axis="y", linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()