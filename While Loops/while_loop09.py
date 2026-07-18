#Student Result Management
student_count = int(input("Enter total students: "))

counter = 1
passed_students = 0
failed_students = 0
total_marks = 0

while counter <= student_count:
    print("\nStudent", counter)

    name = input("Enter student name: ")
    marks = float(input("Enter marks out of 100: "))

    if marks < 0 or marks > 100:
        print("Invalid marks. Enter marks again.")
        continue

    total_marks += marks

    if marks >= 50:
        print(name, "has passed.")
        passed_students += 1
    else:
        print(name, "has failed.")
        failed_students += 1

    counter += 1

average = total_marks / student_count

print("\nResult Summary")
print("Passed Students:", passed_students)
print("Failed Students:", failed_students)
print("Class Average:", round(average, 2))