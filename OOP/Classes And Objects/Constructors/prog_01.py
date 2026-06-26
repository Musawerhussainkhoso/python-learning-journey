#Program 1 — Student Information
class Student:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)

student = Student("Musawer", 21, "Software Engineering")

student.display()