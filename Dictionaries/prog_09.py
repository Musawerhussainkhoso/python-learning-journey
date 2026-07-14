'''
This program stores students, subjects, and marks.
It generates grades and finds the highest-performing student.
'''
from typing import Dict
StudentRecord = Dict[str, object]
def calculate_grade(average: float) -> str:
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"

    return "F"


def generate_student_results(
    students: Dict[str, StudentRecord]
) -> None:

    top_student = ""
    highest_average = -1.0

    print("\nSTUDENT RESULT REPORT")
    print("=" * 65)

    for roll_number, student in students.items():
        subjects = student["subjects"]

        if not isinstance(subjects, dict) or not subjects:
            print(f"No subjects found for {student['name']}.")
            continue

        total_marks = sum(subjects.values())
        average = total_marks / len(subjects)
        grade = calculate_grade(average)

        print(f"Roll Number : {roll_number}")
        print(f"Student     : {student['name']}")
        print(f"Department  : {student['department']}")

        print("Subject Marks:")

        for subject, marks in subjects.items():
            print(f"  {subject:<20}: {marks}")

        print(f"Total       : {total_marks}")
        print(f"Average     : {average:.2f}")
        print(f"Grade       : {grade}")
        print("-" * 65)

        if average > highest_average:
            highest_average = average
            top_student = str(student["name"])

    print(
        f"\nHighest-performing student: {top_student} "
        f"with {highest_average:.2f}% average."
    )


students = {
    "23SW001": {
        "name": "Abdul Majid",
        "department": "Software Engineering",
        "subjects": {
            "Python Programming": 89,
            "Database Systems": 92,
            "Software Design": 86,
            "Data Structures": 90
        }
    },
    "23SW002": {
        "name": "Ahmed Ali",
        "department": "Software Engineering",
        "subjects": {
            "Python Programming": 75,
            "Database Systems": 81,
            "Software Design": 78,
            "Data Structures": 73
        }
    },
    "23SW003": {
        "name": "Sara Khan",
        "department": "Software Engineering",
        "subjects": {
            "Python Programming": 94,
            "Database Systems": 96,
            "Software Design": 91,
            "Data Structures": 95
        }
    }
}
generate_student_results(students)
