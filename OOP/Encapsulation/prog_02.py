#ATM Machine
class ATM:

    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def withdraw(self, entered_pin, amount):

        if entered_pin == self.__pin:

            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal Successful")
                print("Remaining Balance:", self.__balance)

            else:
                print("Insufficient Balance")

        else:
            print("Incorrect PIN")


atm = ATM(1234, 10000)

atm.withdraw(1234, 2500)