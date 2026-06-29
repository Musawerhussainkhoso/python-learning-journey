#Online Shopping Cart
class ShoppingCart:

    def __init__(self):
        self.__items = []

    def add_item(self, item, price, quantity):
        self.__items.append({"item": item, "price": price, "quantity": quantity})

    def remove_item(self, item):
        for i in self.__items:
            if i["item"] == item:
                self.__items.remove(i)
                break

    def total_price(self):
        total = 0
        for i in self.__items:
            total += i["price"] * i["quantity"]
        return total

    def show_cart(self):
        print("Items in Cart:")
        for i in self.__items:
            print(f"- {i['item']}: Rs. {i['price']} x {i['quantity']}")

cart = ShoppingCart()
cart.add_item("Laptop", 50000, 1)
cart.add_item("Mouse", 500, 2)
cart.show_cart()
print("Total Price:", cart.total_price())