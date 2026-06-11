#Take a student's name, age, and city as input and store them in a dictionary.
student = {}

student["name"] = input("Enter student name: ")
student["age"] = int(input("Enter age: "))
student["city"] = input("Enter city: ")

print("\nStudent Information:")
print(student)