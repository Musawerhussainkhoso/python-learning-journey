#3. Sort Employees by Salary and Experience
employees = [
    {"name": "Ali", "salary": 50000, "experience": 2},
    {"name": "Sara", "salary": 80000, "experience": 5},
    {"name": "Ahmed", "salary": 65000, "experience": 3}
]

employees.sort(
    key=lambda emp: (emp["salary"], emp["experience"]),
    reverse=True
)

for emp in employees:
    print(emp)