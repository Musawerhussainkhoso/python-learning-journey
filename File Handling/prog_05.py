#5. High Score Game System
score = int(input("Enter score: "))

with open("highscore.txt", "r") as file:
    highscore = int(file.read())

if score > highscore:
    with open("highscore.txt", "w") as file:
        file.write(str(score))

    print("New High Score!")
else:
    print("Try Again")