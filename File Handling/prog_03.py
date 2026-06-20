#3. Personal Diary App
#Concepts: Append mode
entry = input("Write your diary entry: ")

with open("diary.txt", "a") as file:
    file.write(entry + "\n")

print("Diary saved!")