#bar plot use when different categories ki values compare karni hon.
#Department-wise Employees
import matplotlib.pyplot as plt

departments = ["IT", "HR", "Finance", "Marketing", "Operations"]
employees = [45, 20, 30, 35, 50]

plt.figure(figsize=(10, 6))

plt.bar(
    departments,
    employees,
    width=0.6,
    edgecolor="black"
)

plt.title("Number of Employees by Department")
plt.xlabel("Departments")
plt.ylabel("Number of Employees")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()
plt.show()