#The shopping cart items are protected from direct external modification.
class ShoppingCart:
    def __init__(self, customer_name: str):
        self.__customer_name = customer_name
        self.__items = []

    @property
    def customer_name(self) -> str:
        return self.__customer_name

    @property
    def item_count(self) -> int:
        total_quantity = 0

        for item in self.__items:
            total_quantity += item["quantity"]

        return total_quantity

    def add_item(
        self,
        product_code: str,
        product_name: str,
        price: float,
        quantity: int = 1
    ) -> None:

        if price <= 0:
            raise ValueError(
                "Product price must be greater than zero."
            )

        if quantity <= 0:
            raise ValueError(
                "Quantity must be greater than zero."
            )

        for item in self.__items:
            if item["product_code"] == product_code:
                item["quantity"] += quantity
                return

        self.__items.append({
            "product_code": product_code,
            "product_name": product_name,
            "price": price,
            "quantity": quantity
        })

    def remove_item(self, product_code: str) -> None:
        for item in self.__items:
            if item["product_code"] == product_code:
                self.__items.remove(item)
                return

        raise KeyError("Product does not exist in the cart.")

    def update_quantity(
        self,
        product_code: str,
        quantity: int
    ) -> None:

        if quantity <= 0:
            raise ValueError(
                "Quantity must be greater than zero."
            )

        for item in self.__items:
            if item["product_code"] == product_code:
                item["quantity"] = quantity
                return

        raise KeyError("Product does not exist in the cart.")

    def calculate_subtotal(self) -> float:
        subtotal = 0.0

        for item in self.__items:
            subtotal += item["price"] * item["quantity"]

        return subtotal

    def calculate_final_amount(self) -> dict:
        subtotal = self.calculate_subtotal()

        if subtotal >= 200000:
            discount_rate = 0.15
        elif subtotal >= 100000:
            discount_rate = 0.10
        elif subtotal >= 50000:
            discount_rate = 0.05
        else:
            discount_rate = 0.0

        discount = subtotal * discount_rate
        discounted_total = subtotal - discount

        tax = discounted_total * 0.05
        final_amount = discounted_total + tax

        return {
            "subtotal": subtotal,
            "discount": discount,
            "tax": tax,
            "final_amount": final_amount
        }

    def display_invoice(self) -> None:
        totals = self.calculate_final_amount()

        print("\nSHOPPING CART INVOICE")
        print("=" * 75)
        print(f"Customer: {self.__customer_name}")
        print("-" * 75)

        for item in self.__items:
            item_total = item["price"] * item["quantity"]

            print(
                f"{item['product_name']:<25}"
                f"{item['quantity']:<8}"
                f"Rs. {item_total:>15,.2f}"
            )

        print("-" * 75)
        print(f"Total Items : {self.item_count}")
        print(f"Subtotal    : Rs. {totals['subtotal']:,.2f}")
        print(f"Discount    : Rs. {totals['discount']:,.2f}")
        print(f"Tax         : Rs. {totals['tax']:,.2f}")
        print(f"Final Total : Rs. {totals['final_amount']:,.2f}")


try:
    cart = ShoppingCart("Abdul Majid")

    cart.add_item(
        "P101",
        "Laptop",
        175000,
        1
    )

    cart.add_item(
        "P102",
        "Wireless Mouse",
        4500,
        2
    )

    cart.add_item(
        "P103",
        "External SSD",
        28000,
        1
    )

    cart.display_invoice()

except (ValueError, KeyError) as error:
    print(f"Shopping cart error: {error}")