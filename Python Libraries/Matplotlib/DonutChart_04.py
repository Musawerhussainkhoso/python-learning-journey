#Employee Work Mode Distribution
import matplotlib.pyplot as plt

work_modes = [
    "On-site",
    "Remote",
    "Hybrid"
]

employees = [140, 70, 90]

total_employees = sum(employees)

explode_values = [0.04, 0, 0]

plt.figure(figsize=(9, 7))

plt.pie(
    employees,
    labels=work_modes,
    autopct="%1.0f%%",
    startangle=90,
    explode=explode_values,
    pctdistance=0.78,
    wedgeprops={
        "width": 0.45,
        "edgecolor": "black"
    }
)

plt.text(
    0,
    0,
    f"Total\n{total_employees} Employees",
    ha="center",
    va="center",
    fontsize=13
)

plt.title("Employee Work Mode Distribution")
plt.tight_layout()
plt.show()