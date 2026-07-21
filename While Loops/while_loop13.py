#Student Result Processing System
print("=" * 50)
print("STUDENT RESULT PROCESSING SYSTEM")
print("=" * 50)

number_of_students = int(input("Enter number of students: "))

while number_of_students <= 0:
    print("Number of students must be greater than zero.")
    number_of_students = int(
        input("Enter valid number of students: ")
    )

student_counter = 1
passed_students = 0
failed_students = 0
class_total_marks = 0

highest_percentage = 0
top_student = ""

while student_counter <= number_of_students:
    print(f"\nStudent {student_counter}")
    print("-" * 30)

    student_name = input("Enter student name: ").strip()

    while student_name == "":
        print("Student name cannot be empty.")
        student_name = input("Enter student name again: ").strip()

    subject_counter = 1
    total_marks = 0
    failed_subjects = 0

    while subject_counter <= 5:
        marks = float(
            input(f"Enter marks for subject {subject_counter}: ")
        )

        while marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            marks = float(
                input(
                    f"Enter valid marks for subject "
                    f"{subject_counter}: "
                )
            )

        total_marks += marks

        if marks < 40:
            failed_subjects += 1

        subject_counter += 1

    percentage = total_marks / 5
    class_total_marks += total_marks

    if failed_subjects == 0:
        result = "Pass"
        passed_students += 1

        if percentage >= 80:
            grade = "A+"
        elif percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "D"

    else:
        result = "Fail"
        grade = "F"
        failed_students += 1

    if percentage > highest_percentage:
        highest_percentage = percentage
        top_student = student_name

    print("\nRESULT CARD")
    print("-" * 30)
    print("Student Name    :", student_name)
    print("Total Marks     :", total_marks, "/ 500")
    print("Percentage      :", percentage, "%")
    print("Failed Subjects :", failed_subjects)
    print("Grade           :", grade)
    print("Result          :", result)

    student_counter += 1

class_average = class_total_marks / (number_of_students * 5)

print("\n" + "=" * 50)
print("CLASS PERFORMANCE REPORT")
print("=" * 50)
print("Total Students     :", number_of_students)
print("Passed Students    :", passed_students)
print("Failed Students    :", failed_students)
print("Class Average      :", class_average, "%")
print("Top Student        :", top_student)
print("Highest Percentage :", highest_percentage, "%")