#1. Sort Students by Marks (Dictionary + Lambda)
students = {
    "Ali": 85,
    "Ahmed": 92,
    "Sara": 78,
    "Fatima": 95
}

sorted_students = sorted(
    students.items(),
    key=lambda x: x[1],
    reverse=True
)

for name, marks in sorted_students:
    print(name, ":", marks)