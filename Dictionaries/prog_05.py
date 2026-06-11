#Store a username and password in a dictionary and check user login.
users = {
    "admin": "1234",
    "hussain": "python"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login Successful!")
else:
    print("Invalid Username or Password!")