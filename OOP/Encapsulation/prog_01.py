#Student Details
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks     # Private Attribute

    def show_marks(self):
        print("Marks:", self.__marks)


student = Student("Ahmed", 90)

print("Name:", student.name)
student.show_marks()