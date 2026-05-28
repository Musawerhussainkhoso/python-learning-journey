#User enters multiple student names and they are stored in a list.
students = []

total_students = int(input("How many students? "))

for i in range(total_students):
    name = input(f"Enter student {i+1} name: ")
    students.append(name)

print("\nStudent List:")

for student in students:
    print(student)