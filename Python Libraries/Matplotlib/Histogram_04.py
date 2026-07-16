#Customer Purchase Amounts
import matplotlib.pyplot as plt

purchase_amounts = [
    500, 750, 900, 1100, 1250, 1500, 1700,
    1800, 2100, 2300, 2500, 2800, 3100,
    3500, 3900, 4200, 4800, 5200, 6000
]

plt.figure(figsize=(10, 6))

plt.hist(
    purchase_amounts,
    bins=7,
    edgecolor="black"
)

plt.title("Customer Purchase Amount Distribution")
plt.xlabel("Purchase Amount (PKR)")
plt.ylabel("Number of Customers")

plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()