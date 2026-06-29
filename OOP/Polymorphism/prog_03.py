#University Portal
class User:

    def dashboard(self):
        print("User Dashboard")


class Student(User):

    def dashboard(self):
        print("Student Dashboard")
        print("View Courses")
        print("Check Attendance")


class Teacher(User):

    def dashboard(self):
        print("Teacher Dashboard")
        print("Upload Marks")
        print("Take Attendance")


class Admin(User):

    def dashboard(self):
        print("Admin Dashboard")
        print("Manage Users")
        print("Generate Reports")


users = [
    Student(),
    Teacher(),
    Admin()
]

for user in users:
    user.dashboard()
    print("----------------")