#Change nahi ho sakti (immutable)
#1: Store Student Names in a Tuple
students = []

total = int(input("How many students? "))

for i in range(total):
    name = input(f"Enter student {i+1} name: ")
    students.append(name)

students_tuple = tuple(students)

print("Students:", students_tuple)