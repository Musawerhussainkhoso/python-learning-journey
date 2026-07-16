#Product Category Revenue
import matplotlib.pyplot as plt

categories = [
    "Electronics",
    "Clothing",
    "Home Appliances",
    "Beauty Products",
    "Sports"
]

revenue = [
    4_500_000,
    2_800_000,
    2_200_000,
    1_400_000,
    1_100_000
]

plt.figure(figsize=(10, 7))

plt.pie(
    revenue,
    labels=categories,
    autopct="%1.1f%%",
    startangle=90,
    pctdistance=0.78,
    wedgeprops={
        "edgecolor": "black",
        "width": 0.45
    }
)

plt.title("Revenue Share by Product Category")

plt.text(
    0,
    0,
    "Total\nRevenue",
    ha="center",
    va="center",
    fontsize=13
)

plt.tight_layout()
plt.show()