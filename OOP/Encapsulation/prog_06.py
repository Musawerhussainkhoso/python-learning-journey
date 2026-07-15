#This program protects product price and stock quantity.
class Product:
    def __init__(
        self,
        product_code: str,
        name: str,
        price: float,
        stock: int,
        reorder_level: int = 5
    ):
        self.__product_code = product_code
        self.__name = name
        self.price = price
        self.stock = stock
        self.reorder_level = reorder_level

    @property
    def product_code(self) -> str:
        return self.__product_code

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            raise ValueError(
                "Product price must be greater than zero."
            )

        self.__price = new_price

    @property
    def stock(self) -> int:
        return self.__stock

    @stock.setter
    def stock(self, quantity: int) -> None:
        if quantity < 0:
            raise ValueError(
                "Stock quantity cannot be negative."
            )

        self.__stock = quantity

    @property
    def reorder_level(self) -> int:
        return self.__reorder_level

    @reorder_level.setter
    def reorder_level(self, level: int) -> None:
        if level < 0:
            raise ValueError(
                "Reorder level cannot be negative."
            )

        self.__reorder_level = level

    def add_stock(self, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError(
                "Added stock must be greater than zero."
            )

        self.__stock += quantity

    def sell(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError(
                "Sale quantity must be greater than zero."
            )

        if quantity > self.__stock:
            raise ValueError("Insufficient stock available.")

        self.__stock -= quantity

        return quantity * self.__price

    def requires_reorder(self) -> bool:
        return self.__stock <= self.__reorder_level

    def get_stock_value(self) -> float:
        return self.__stock * self.__price


try:
    product = Product(
        "P-1001",
        "Wireless Keyboard",
        8500,
        12,
        5
    )

    sale_amount = product.sell(8)

    print("\nPRODUCT INVENTORY REPORT")
    print("=" * 55)
    print(f"Product Code    : {product.product_code}")
    print(f"Product Name    : {product.name}")
    print(f"Sale Amount     : Rs. {sale_amount:,.2f}")
    print(f"Remaining Stock : {product.stock}")
    print(f"Stock Value     : Rs. {product.get_stock_value():,.2f}")
    print(f"Reorder Needed  : {product.requires_reorder()}")

except ValueError as error:
    print(f"Inventory error: {error}")