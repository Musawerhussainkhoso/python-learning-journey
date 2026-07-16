#Product Sales Comparison
import matplotlib.pyplot as plt

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Headphones",
    "Smartwatch"
]

units_sold = [120, 210, 95, 180, 140]

plt.figure(figsize=(10, 6))

bars = plt.bar(
    products,
    units_sold,
    width=0.6,
    edgecolor="black"
)

plt.title("Product Sales Performance")
plt.xlabel("Products")
plt.ylabel("Units Sold")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5#alpha transparency set karta hai.
)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 3,
        str(height),
        ha="center" #text should be in center 
    )

plt.tight_layout()
plt.show()