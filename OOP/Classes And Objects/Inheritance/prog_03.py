#university management
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):

    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display(self):
        print("----- Student -----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)


class Teacher(Person):

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        print("----- Teacher -----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Subject:", self.subject)


student = Student("Ahmed", 20, "DS-101")
teacher = Teacher("Bilal", 35, "Machine Learning")

student.display()
print()
teacher.display()