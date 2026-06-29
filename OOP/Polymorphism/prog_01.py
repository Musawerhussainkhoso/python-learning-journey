#Different Employees Calculate Bonus
class Employee:

    def bonus(self):
        print("No bonus")


class Manager(Employee):

    def bonus(self):
        print("Bonus: 50000")


class Developer(Employee):

    def bonus(self):
        print("Bonus: 30000")


manager = Manager()
developer = Developer()

manager.bonus()
developer.bonus()