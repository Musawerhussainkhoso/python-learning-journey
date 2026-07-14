'''
This program calculates basic salary, overtime payment, tax, and final salary.
'''
def calculate_payroll(employees: list[dict]) -> None:
    company_salary_expense = 0.0

    print("\nEMPLOYEE PAYROLL REPORT")
    print("=" * 75)

    for employee in employees:
        basic_salary = employee["basic_salary"]
        overtime_hours = employee["overtime_hours"]
        overtime_rate = employee["overtime_rate"]

        overtime_payment = overtime_hours * overtime_rate
        gross_salary = basic_salary + overtime_payment

        if gross_salary >= 150000:
            tax_rate = 0.15
        elif gross_salary >= 100000:
            tax_rate = 0.10
        elif gross_salary >= 50000:
            tax_rate = 0.05
        else:
            tax_rate = 0.0

        tax_amount = gross_salary * tax_rate
        net_salary = gross_salary - tax_amount

        company_salary_expense += net_salary

        print(f"Employee ID      : {employee['employee_id']}")
        print(f"Employee Name    : {employee['name']}")
        print(f"Basic Salary     : Rs. {basic_salary:,.2f}")
        print(f"Overtime Payment : Rs. {overtime_payment:,.2f}")
        print(f"Gross Salary     : Rs. {gross_salary:,.2f}")
        print(f"Tax Deduction    : Rs. {tax_amount:,.2f}")
        print(f"Net Salary       : Rs. {net_salary:,.2f}")
        print("-" * 75)

    print(
        f"Total company payroll expense: "
        f"Rs. {company_salary_expense:,.2f}"
    )


employees = [
    {
        "employee_id": "EMP-101",
        "name": "Ali Khan",
        "basic_salary": 85000,
        "overtime_hours": 12,
        "overtime_rate": 1000
    },
    {
        "employee_id": "EMP-102",
        "name": "Sara Ahmed",
        "basic_salary": 135000,
        "overtime_hours": 8,
        "overtime_rate": 1500
    },
    {
        "employee_id": "EMP-103",
        "name": "Hamza Tariq",
        "basic_salary": 45000,
        "overtime_hours": 15,
        "overtime_rate": 700
    }
]
calculate_payroll(employees)
