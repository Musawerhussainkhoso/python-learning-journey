#Username Checker
while True:

    username = input("Enter username (type exit to stop): ")

    # break
    if username == "exit":
        print("Program closed")
        break

    # continue
    if username == "":
        print("Empty username skipped")
        continue

    # pass
    if username == "admin":
        pass

    print("Username accepted:", username)