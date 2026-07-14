#1. Sort Employee Records Using Multiple Conditions
def sort_employees(
    employees: list[tuple[int, str, str, float, int]]
) -> list[tuple[int, str, str, float, int]]:
    """
    Sort employees by department, salary, and experience.
    """

    return sorted(
        employees,
        key=lambda employee: (
            employee[2],
            -employee[3],
            -employee[4]
        )
    )


employees = [
    (101, "Ali Khan", "Development", 120000, 4),
    (102, "Sara Ahmed", "Data Analytics", 145000, 5),
    (103, "Hamza Ali", "Development", 135000, 3),
    (104, "Ayesha Noor", "Data Analytics", 145000, 6),
    (105, "Usman Tariq", "Development", 120000, 7)
]

sorted_employees = sort_employees(employees)

print("SORTED EMPLOYEE REPORT")
print("=" * 75)

for employee in sorted_employees:
    employee_id, name, department, salary, experience = employee

    print(f"Employee ID : {employee_id}")
    print(f"Name        : {name}")
    print(f"Department  : {department}")
    print(f"Salary      : Rs. {salary:,.2f}")
    print(f"Experience  : {experience} years")
    print("-" * 75)