#4. To-Do List Manager
task = input("Enter task: ")

with open("tasks.txt", "a") as file:
    file.write(task + "\n")

print("Task Added!")