#Student Marks System
while True:

    marks = int(input("Enter marks (-1 to exit): "))

    # break
    if marks == -1:
        print("Program ended")
        break

    # continue
    if marks < 0:
        print("Negative marks skipped")
        continue

    # pass
    if marks == 100:
        pass

    print("Marks recorded:", marks)