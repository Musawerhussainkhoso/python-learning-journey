#This program protects salary information and validates salary updates.
class Employee:
    def __init__(
        self,
        employee_id: str,
        name: str,
        department: str,
        basic_salary: float
    ):
        self.__employee_id = employee_id
        self.__name = name
        self.__department = department
        self.basic_salary = basic_salary

    @property
    def employee_id(self) -> str:
        return self.__employee_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        new_name = new_name.strip()

        if len(new_name) < 3:
            raise ValueError(
                "Employee name must contain at least 3 characters."
            )

        self.__name = new_name.title()

    @property
    def department(self) -> str:
        return self.__department

    @department.setter
    def department(self, new_department: str) -> None:
        if not new_department.strip():
            raise ValueError("Department cannot be empty.")

        self.__department = new_department.strip().title()

    @property
    def basic_salary(self) -> float:
        return self.__basic_salary

    @basic_salary.setter
    def basic_salary(self, salary: float) -> None:
        if salary < 25000:
            raise ValueError(
                "Basic salary cannot be less than Rs. 25,000."
            )

        self.__basic_salary = salary

    def calculate_net_salary(
        self,
        overtime_hours: float,
        overtime_rate: float
    ) -> dict:

        if overtime_hours < 0 or overtime_rate < 0:
            raise ValueError(
                "Overtime values cannot be negative."
            )

        overtime_payment = overtime_hours * overtime_rate
        gross_salary = self.__basic_salary + overtime_payment

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

        return {
            "basic_salary": self.__basic_salary,
            "overtime_payment": overtime_payment,
            "gross_salary": gross_salary,
            "tax_amount": tax_amount,
            "net_salary": net_salary
        }


try:
    employee = Employee(
        "EMP-101",
        "Ali Khan",
        "Software Development",
        120000
    )

    payroll = employee.calculate_net_salary(
        overtime_hours=10,
        overtime_rate=1500
    )

    print("\nEMPLOYEE PAYROLL")
    print("=" * 55)
    print(f"Employee ID      : {employee.employee_id}")
    print(f"Name             : {employee.name}")
    print(f"Department       : {employee.department}")
    print(f"Basic Salary     : Rs. {payroll['basic_salary']:,.2f}")
    print(f"Overtime Payment : Rs. {payroll['overtime_payment']:,.2f}")
    print(f"Gross Salary     : Rs. {payroll['gross_salary']:,.2f}")
    print(f"Tax              : Rs. {payroll['tax_amount']:,.2f}")
    print(f"Net Salary       : Rs. {payroll['net_salary']:,.2f}")

except ValueError as error:
    print(f"Payroll error: {error}")