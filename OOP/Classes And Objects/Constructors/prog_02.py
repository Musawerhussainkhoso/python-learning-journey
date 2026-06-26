#Program 2 — Employee Management
class Employee:

    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary

    def display(self):
        print("Employee:", self.name)
        print("Designation:", self.designation)
        print("Salary:", self.salary)

emp = Employee("Ahmed", "Data Analyst", 120000)

emp.display()