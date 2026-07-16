#Company Expenses by Department
import matplotlib.pyplot as plt

departments = [
    "Information Technology",
    "Human Resources",
    "Marketing",
    "Operations",
    "Customer Support",
    "Finance"
]

expenses = [
    850000,
    320000,
    620000,
    950000,
    410000,
    500000
]

plt.figure(figsize=(11, 7))

bars = plt.barh(
    departments,
    expenses,
    height=0.6,
    edgecolor="black"
)

plt.title("Department-wise Company Expenses")
plt.xlabel("Expenses (PKR)")
plt.ylabel("Departments")

plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.5
)

for bar in bars:
    width = bar.get_width()

    plt.text(
        width + 15000,
        bar.get_y() + bar.get_height() / 2,
        f"PKR {width:,.0f}",
        va="center"
    )

plt.tight_layout()
plt.show()