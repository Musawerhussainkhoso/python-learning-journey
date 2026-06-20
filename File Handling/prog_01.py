#1. Student Record Manager
#Concepts: Create, Read, Update, Delete (CRUD)
def add_student():
    name = input("Enter student name: ")

    with open("students.txt", "a") as file:
        file.write(name + "\n")

    print("Student added successfully!")

add_student()