#Number Processing System
while True:

    number = int(input("Enter number (0 to exit): "))

    # break
    if number == 0:
        print("Program stopped")
        break

    # continue
    if number < 0:
        print("Negative number skipped")
        continue

    # pass
    if number == 10:
        pass

    print("Number accepted:", number)