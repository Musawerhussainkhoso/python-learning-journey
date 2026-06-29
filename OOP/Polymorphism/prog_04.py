class Order:

    def bill(self, amount):
        print("Total Bill:", amount)


class FoodPanda(Order):

    def bill(self, amount):
        total = amount + 50
        print("FoodPanda Total Bill: Rs.", total)


class Careem(Order):

    def bill(self, amount):
        total = amount + 100
        print("Careem Total Bill: Rs.", total)


class InDrive(Order):

    def bill(self, amount):
        total = amount + 75
        print("InDrive Total Bill: Rs.", total)


amount = 1000

foodpanda = FoodPanda()
careem = Careem()
indrive = InDrive()

foodpanda.bill(amount)
careem.bill(amount)
indrive.bill(amount)