#Search for a student name.
students = []

total = int(input("How many students? "))

for i in range(total):
    students.append(input("Enter student name: "))

search = input("Enter name to search: ")

if search in students:
    print("Student found")
else:
    print("Student not found")