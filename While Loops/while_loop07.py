#Employee Salary Processing
employee_count = int(input("Enter number of employees: "))

counter = 1
total_payroll = 0

while counter <= employee_count:
    print("\nEmployee", counter)

    employee_name = input("Enter employee name: ")
    basic_salary = float(input("Enter basic salary: "))

    if basic_salary >= 100000:
        bonus_rate = 0.15
    elif basic_salary >= 50000:
        bonus_rate = 0.10
    else:
        bonus_rate = 0.05

    bonus = basic_salary * bonus_rate
    final_salary = basic_salary + bonus

    total_payroll += final_salary

    print("Employee:", employee_name)
    print("Bonus:", bonus)
    print("Final Salary:", final_salary)

    counter += 1

print("\nTotal company payroll:", total_payroll)