#Advertising Spend vs Sales Revenue
import matplotlib.pyplot as plt

advertising_spend = [20, 25, 30, 35, 40, 45, 50, 55]
sales_revenue = [110, 125, 145, 160, 175, 190, 215, 230]

plt.figure(figsize=(10, 6))

plt.scatter(
    advertising_spend,
    sales_revenue,
    s=100,
    alpha=0.7,
    marker="o",
    edgecolors="black",
    label="Monthly performance"
)

plt.title("Advertising Spend vs Sales Revenue")
plt.xlabel("Advertising Spend (Thousand PKR)")
plt.ylabel("Sales Revenue (Thousand PKR)")

plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()#graph ke title, labels aur axes ke darmiyan spacing automatically adjust karta hai.
plt.show()