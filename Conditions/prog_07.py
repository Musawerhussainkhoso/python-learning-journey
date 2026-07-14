#This program updates stock after sales and identifies products that need restocking.
def calculate_grade(average: float) -> str:
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def generate_result_report(students: dict[str, dict]) -> None:
    top_student = ""
    highest_average = -1.0

    print("\nSTUDENT RESULT REPORT")
    print("=" * 70)

    for roll_number, student in students.items():
        total_marks = 0
        failed_subjects = []

        for subject, marks in student["subjects"].items():
            total_marks += marks

            if marks < 50:
                failed_subjects.append(subject)

        number_of_subjects = len(student["subjects"])
        average = total_marks / number_of_subjects
        grade = calculate_grade(average)

        print(f"Roll Number : {roll_number}")
        print(f"Name        : {student['name']}")

        for subject, marks in student["subjects"].items():
            print(f"  {subject:<22}: {marks}")

        print(f"Total       : {total_marks}")
        print(f"Average     : {average:.2f}")
        print(f"Grade       : {grade}")

        if failed_subjects:
            print(f"Failed in   : {', '.join(failed_subjects)}")
        else:
            print("Status      : Passed all subjects")

        print("-" * 70)

        if average > highest_average:
            highest_average = average
            top_student = student["name"]

    print(
        f"Top-performing student: {top_student} "
        f"with {highest_average:.2f}%"
    )


students = {
    "23SW001": {
        "name": "Ali Khan",
        "subjects": {
            "Python": 88,
            "Database": 91,
            "Data Structures": 84,
            "Software Engineering": 87
        }
    },
    "23SW002": {
        "name": "Sara Ahmed",
        "subjects": {
            "Python": 95,
            "Database": 92,
            "Data Structures": 96,
            "Software Engineering": 93
        }
    },
    "23SW003": {
        "name": "Usman Ali",
        "subjects": {
            "Python": 65,
            "Database": 45,
            "Data Structures": 58,
            "Software Engineering": 62
        }
    }
}
generate_result_report(students)