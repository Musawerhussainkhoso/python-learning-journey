#User Login with Limited Attempts
correct_username = "admin"
correct_password = "python123"

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful.")
        break

    attempts -= 1
    print("Invalid credentials.")
    print("Remaining attempts:", attempts)

if attempts == 0:
    print("Account temporarily locked.")