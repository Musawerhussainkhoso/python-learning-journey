#Employee Salary Management System
print("=" * 50)
print("EMPLOYEE SALARY MANAGEMENT SYSTEM")
print("=" * 50)

number_of_employees = int(input("Enter number of employees: "))

employee_counter = 1
total_salary = 0
highest_salary = 0
highest_paid_employee = ""

while employee_counter <= number_of_employees:
    print(f"\nEmployee {employee_counter}")

    employee_name = input("Enter employee name: ").strip()

    while employee_name == "":
        print("Employee name cannot be empty.")
        employee_name = input("Enter employee name again: ").strip()

    basic_salary = float(input("Enter basic salary: "))

    while basic_salary < 0:
        print("Salary cannot be negative.")
        basic_salary = float(input("Enter valid basic salary: "))

    bonus_percentage = float(input("Enter bonus percentage: "))

    while bonus_percentage < 0:
        print("Bonus percentage cannot be negative.")
        bonus_percentage = float(
            input("Enter valid bonus percentage: ")
        )

    bonus_amount = basic_salary * bonus_percentage / 100
    final_salary = basic_salary + bonus_amount

    total_salary += final_salary

    if final_salary > highest_salary:
        highest_salary = final_salary
        highest_paid_employee = employee_name

    print("\nSalary Details")
    print("-" * 30)
    print("Employee Name :", employee_name)
    print("Basic Salary  :", basic_salary)
    print("Bonus Amount  :", bonus_amount)
    print("Final Salary  :", final_salary)

    employee_counter += 1

average_salary = total_salary / number_of_employees

print("\n" + "=" * 50)
print("FINAL SALARY REPORT")
print("=" * 50)
print("Total Employees       :", number_of_employees)
print("Total Salary Expense  :", total_salary)
print("Average Salary        :", average_salary)
print("Highest Paid Employee :", highest_paid_employee)
print("Highest Salary        :", highest_salary)