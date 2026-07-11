from abc import ABC, abstractmethod
from datetime import datetime


# ============================================================
# ABSTRACT EMPLOYEE CLASS
# ============================================================

class Employee(ABC):

    company_name = "TechVision Software House"

    def __init__(
        self,
        employee_id: str,
        full_name: str,
        department: str,
        email: str
    ):
        # Encapsulation: private attributes
        self.__employee_id = employee_id
        self.__full_name = full_name
        self.__department = department
        self.__email = email
        self.__joining_date = datetime.now()
        self.__is_active = True
        self.__bonus = 0.0
        self.__deduction = 0.0

    # Getter methods
    def get_employee_id(self) -> str:
        return self.__employee_id

    def get_full_name(self) -> str:
        return self.__full_name

    def get_department(self) -> str:
        return self.__department

    def get_email(self) -> str:
        return self.__email

    def get_joining_date(self) -> datetime:
        return self.__joining_date

    def get_bonus(self) -> float:
        return self.__bonus

    def get_deduction(self) -> float:
        return self.__deduction

    def is_active(self) -> bool:
        return self.__is_active

    # Setter methods
    def set_full_name(self, full_name: str) -> None:
        if not full_name.strip():
            raise ValueError("Employee name cannot be empty.")

        self.__full_name = full_name

    def set_department(self, department: str) -> None:
        if not department.strip():
            raise ValueError("Department cannot be empty.")

        self.__department = department

    def set_email(self, email: str) -> None:
        if "@" not in email:
            raise ValueError("Invalid email address.")

        self.__email = email

    def add_bonus(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Bonus cannot be negative.")

        self.__bonus += amount

    def add_deduction(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Deduction cannot be negative.")

        self.__deduction += amount

    def deactivate_employee(self) -> None:
        self.__is_active = False

    def activate_employee(self) -> None:
        self.__is_active = True

    def calculate_net_salary(self) -> float:
        gross_salary = self.calculate_gross_salary()

        net_salary = (
            gross_salary
            + self.__bonus
            - self.__deduction
        )

        return net_salary

    def display_basic_information(self) -> None:
        status = "Active" if self.__is_active else "Inactive"

        print("\n" + "=" * 60)
        print("EMPLOYEE INFORMATION")
        print("=" * 60)
        print(f"Company        : {self.company_name}")
        print(f"Employee ID    : {self.__employee_id}")
        print(f"Name           : {self.__full_name}")
        print(f"Department     : {self.__department}")
        print(f"Email          : {self.__email}")
        print(f"Employee Type  : {self.get_employee_type()}")
        print(f"Status         : {status}")
        print(
            f"Joining Date   : "
            f"{self.__joining_date.strftime('%d-%m-%Y')}"
        )
        print("=" * 60)

    # Abstraction
    @abstractmethod
    def calculate_gross_salary(self) -> float:
        pass

    @abstractmethod
    def calculate_tax(self) -> float:
        pass

    @abstractmethod
    def get_employee_type(self) -> str:
        pass

    @abstractmethod
    def display_salary_details(self) -> None:
        pass


# ============================================================
# FULL-TIME EMPLOYEE
# ============================================================

class FullTimeEmployee(Employee):

    def __init__(
        self,
        employee_id: str,
        full_name: str,
        department: str,
        email: str,
        basic_salary: float,
        house_allowance: float,
        medical_allowance: float
    ):
        super().__init__(
            employee_id,
            full_name,
            department,
            email
        )

        self.__basic_salary = basic_salary
        self.__house_allowance = house_allowance
        self.__medical_allowance = medical_allowance

    def get_basic_salary(self) -> float:
        return self.__basic_salary

    def set_basic_salary(self, salary: float) -> None:
        if salary <= 0:
            raise ValueError("Basic salary must be greater than zero.")

        self.__basic_salary = salary

    def calculate_gross_salary(self) -> float:
        return (
            self.__basic_salary
            + self.__house_allowance
            + self.__medical_allowance
        )

    def calculate_tax(self) -> float:
        gross_salary = self.calculate_gross_salary()

        if gross_salary <= 50000:
            return gross_salary * 0.02

        elif gross_salary <= 100000:
            return gross_salary * 0.05

        return gross_salary * 0.10

    def calculate_net_salary(self) -> float:
        gross_salary = self.calculate_gross_salary()
        tax = self.calculate_tax()

        return (
            gross_salary
            + self.get_bonus()
            - self.get_deduction()
            - tax
        )

    def get_employee_type(self) -> str:
        return "Full-Time Employee"

    def display_salary_details(self) -> None:
        print("\n" + "-" * 60)
        print("FULL-TIME EMPLOYEE SALARY DETAILS")
        print("-" * 60)
        print(f"Basic Salary       : Rs. {self.__basic_salary:,.2f}")
        print(
            f"House Allowance    : "
            f"Rs. {self.__house_allowance:,.2f}"
        )
        print(
            f"Medical Allowance  : "
            f"Rs. {self.__medical_allowance:,.2f}"
        )
        print(
            f"Gross Salary       : "
            f"Rs. {self.calculate_gross_salary():,.2f}"
        )
        print(f"Bonus              : Rs. {self.get_bonus():,.2f}")
        print(
            f"Other Deduction    : "
            f"Rs. {self.get_deduction():,.2f}"
        )
        print(f"Tax                : Rs. {self.calculate_tax():,.2f}")
        print(
            f"Net Salary         : "
            f"Rs. {self.calculate_net_salary():,.2f}"
        )
        print("-" * 60)


# ============================================================
# PART-TIME EMPLOYEE
# ============================================================

class PartTimeEmployee(Employee):

    def __init__(
        self,
        employee_id: str,
        full_name: str,
        department: str,
        email: str,
        hourly_rate: float,
        hours_worked: float
    ):
        super().__init__(
            employee_id,
            full_name,
            department,
            email
        )

        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def add_working_hours(self, hours: float) -> None:
        if hours <= 0:
            raise ValueError("Working hours must be greater than zero.")

        self.__hours_worked += hours

    def calculate_gross_salary(self) -> float:
        regular_hours = min(self.__hours_worked, 160)
        overtime_hours = max(self.__hours_worked - 160, 0)

        regular_salary = regular_hours * self.__hourly_rate

        overtime_salary = (
            overtime_hours
            * self.__hourly_rate
            * 1.5
        )

        return regular_salary + overtime_salary

    def calculate_tax(self) -> float:
        gross_salary = self.calculate_gross_salary()

        if gross_salary <= 40000:
            return 0

        return gross_salary * 0.03

    def calculate_net_salary(self) -> float:
        return (
            self.calculate_gross_salary()
            + self.get_bonus()
            - self.get_deduction()
            - self.calculate_tax()
        )

    def get_employee_type(self) -> str:
        return "Part-Time Employee"

    def display_salary_details(self) -> None:
        regular_hours = min(self.__hours_worked, 160)
        overtime_hours = max(self.__hours_worked - 160, 0)

        print("\n" + "-" * 60)
        print("PART-TIME EMPLOYEE SALARY DETAILS")
        print("-" * 60)
        print(f"Hourly Rate        : Rs. {self.__hourly_rate:,.2f}")
        print(f"Total Hours        : {self.__hours_worked}")
        print(f"Regular Hours      : {regular_hours}")
        print(f"Overtime Hours     : {overtime_hours}")
        print(
            f"Gross Salary       : "
            f"Rs. {self.calculate_gross_salary():,.2f}"
        )
        print(f"Bonus              : Rs. {self.get_bonus():,.2f}")
        print(
            f"Deduction          : "
            f"Rs. {self.get_deduction():,.2f}"
        )
        print(f"Tax                : Rs. {self.calculate_tax():,.2f}")
        print(
            f"Net Salary         : "
            f"Rs. {self.calculate_net_salary():,.2f}"
        )
        print("-" * 60)


# ============================================================
# CONTRACT EMPLOYEE
# ============================================================

class ContractEmployee(Employee):

    def __init__(
        self,
        employee_id: str,
        full_name: str,
        department: str,
        email: str,
        contract_amount: float,
        completed_percentage: float
    ):
        super().__init__(
            employee_id,
            full_name,
            department,
            email
        )

        self.__contract_amount = contract_amount
        self.__completed_percentage = completed_percentage

    def update_completion_percentage(
        self,
        percentage: float
    ) -> None:
        if percentage < 0 or percentage > 100:
            raise ValueError(
                "Completion percentage must be between 0 and 100."
            )

        self.__completed_percentage = percentage

    def calculate_gross_salary(self) -> float:
        return (
            self.__contract_amount
            * self.__completed_percentage
            / 100
        )

    def calculate_tax(self) -> float:
        return self.calculate_gross_salary() * 0.08

    def calculate_net_salary(self) -> float:
        return (
            self.calculate_gross_salary()
            + self.get_bonus()
            - self.get_deduction()
            - self.calculate_tax()
        )

    def get_employee_type(self) -> str:
        return "Contract Employee"

    def display_salary_details(self) -> None:
        print("\n" + "-" * 60)
        print("CONTRACT EMPLOYEE PAYMENT DETAILS")
        print("-" * 60)
        print(
            f"Contract Amount    : "
            f"Rs. {self.__contract_amount:,.2f}"
        )
        print(
            f"Work Completed     : "
            f"{self.__completed_percentage}%"
        )
        print(
            f"Gross Payment      : "
            f"Rs. {self.calculate_gross_salary():,.2f}"
        )
        print(f"Bonus              : Rs. {self.get_bonus():,.2f}")
        print(
            f"Deduction          : "
            f"Rs. {self.get_deduction():,.2f}"
        )
        print(f"Tax                : Rs. {self.calculate_tax():,.2f}")
        print(
            f"Net Payment        : "
            f"Rs. {self.calculate_net_salary():,.2f}"
        )
        print("-" * 60)


# ============================================================
# PAYROLL MANAGEMENT CLASS
# ============================================================

class PayrollManagementSystem:

    def __init__(self):
        self.__employees = []

    def add_employee(self, employee: Employee) -> None:
        for existing_employee in self.__employees:
            if (
                existing_employee.get_employee_id()
                == employee.get_employee_id()
            ):
                raise ValueError(
                    "An employee with this ID already exists."
                )

        self.__employees.append(employee)

        print(
            f"{employee.get_full_name()} added successfully "
            "to the payroll system."
        )

    def remove_employee(self, employee_id: str) -> None:
        for employee in self.__employees:
            if employee.get_employee_id() == employee_id:
                self.__employees.remove(employee)

                print(
                    f"Employee {employee_id} removed successfully."
                )
                return

        print("Employee not found.")

    def search_employee(self, employee_id: str):
        for employee in self.__employees:
            if employee.get_employee_id() == employee_id:
                return employee

        return None

    def calculate_total_payroll(self) -> float:
        total_payroll = 0

        for employee in self.__employees:
            if employee.is_active():
                total_payroll += employee.calculate_net_salary()

        return total_payroll

    def display_all_employees(self) -> None:
        print("\n" + "=" * 75)
        print("COMPLETE EMPLOYEE PAYROLL REPORT")
        print("=" * 75)

        for employee in self.__employees:
            employee.display_basic_information()
            employee.display_salary_details()

        print(
            f"\nTotal Monthly Payroll: "
            f"Rs. {self.calculate_total_payroll():,.2f}"
        )


# ============================================================
# POLYMORPHIC FUNCTION
# ============================================================

def process_salary(employee: Employee) -> None:
    print("\nProcessing salary...")
    print(f"Employee Name : {employee.get_full_name()}")
    print(f"Employee Type : {employee.get_employee_type()}")
    print(
        f"Net Salary    : "
        f"Rs. {employee.calculate_net_salary():,.2f}"
    )


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    payroll_system = PayrollManagementSystem()

    full_time_employee = FullTimeEmployee(
        employee_id="EMP-101",
        full_name="Ahmed Raza",
        department="Software Development",
        email="ahmed@techvision.com",
        basic_salary=90000,
        house_allowance=20000,
        medical_allowance=10000
    )

    part_time_employee = PartTimeEmployee(
        employee_id="EMP-102",
        full_name="Sara Khan",
        department="Graphic Design",
        email="sara@techvision.com",
        hourly_rate=800,
        hours_worked=175
    )

    contract_employee = ContractEmployee(
        employee_id="EMP-103",
        full_name="Bilal Ahmed",
        department="Cyber Security",
        email="bilal@techvision.com",
        contract_amount=300000,
        completed_percentage=70
    )

    try:
        full_time_employee.add_bonus(10000)
        full_time_employee.add_deduction(2500)

        part_time_employee.add_bonus(5000)
        part_time_employee.add_deduction(1000)

        contract_employee.add_bonus(15000)
        contract_employee.add_deduction(3000)

        payroll_system.add_employee(full_time_employee)
        payroll_system.add_employee(part_time_employee)
        payroll_system.add_employee(contract_employee)

    except ValueError as error:
        print("Payroll Error:", error)

    # Polymorphism
    employees = [
        full_time_employee,
        part_time_employee,
        contract_employee
    ]

    for employee in employees:
        process_salary(employee)

    payroll_system.display_all_employees()


if __name__ == "__main__":
    main()