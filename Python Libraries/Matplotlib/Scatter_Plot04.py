#Product Price vs Customer Rating
import matplotlib.pyplot as plt

product_prices = [
    1500,
    2200,
    2800,
    3500,
    4200,
    5000,
    5800,
    6500,
    7200,
    8000
]

customer_ratings = [
    3.2,
    3.8,
    4.0,
    3.6,
    4.3,
    4.5,
    4.1,
    4.7,
    4.4,
    4.8
]

units_sold = [
    500,
    450,
    420,
    370,
    340,
    300,
    260,
    220,
    180,
    140
]

bubble_sizes = [units / 2 for units in units_sold]

plt.figure(figsize=(11, 7))

scatter = plt.scatter(
    product_prices,
    customer_ratings,
    s=bubble_sizes,
    c=units_sold,
    alpha=0.65,
    edgecolors="black"
)

plt.title("Product Price vs Customer Rating")
plt.xlabel("Product Price (PKR)")
plt.ylabel("Customer Rating")

plt.ylim(2.5, 5.0)

plt.colorbar(
    scatter,
    label="Units Sold"
)

plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()