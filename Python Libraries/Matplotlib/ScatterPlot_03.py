#Employee Experience vs Monthly Salary
import matplotlib.pyplot as plt

experience_years = [1, 2, 3, 4, 5, 6, 8, 10, 12]
monthly_salary = [
    45000,
    52000,
    60000,
    68000,
    76000,
    85000,
    105000,
    130000,
    155000
]

employee_names = [
    "Ali",
    "Sara",
    "Hamza",
    "Ayesha",
    "Bilal",
    "Hina",
    "Usman",
    "Zara",
    "Ahmed"
]

plt.figure(figsize=(11, 7))

plt.scatter(
    experience_years,
    monthly_salary,
    s=120,
    marker="o",
    alpha=0.75,
    edgecolors="black",
    label="Employees"
)

for experience, salary, name in zip(
    experience_years,
    monthly_salary,
    employee_names
):
    plt.annotate(#plt.annotate() ka matlab hai graph ke kisi specific point ke paas text, label ya note likhna.
        name,
        (experience, salary),
        xytext=(5, 7),
        textcoords="offset points"
    )

plt.title("Employee Experience vs Monthly Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Monthly Salary (PKR)")

plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()