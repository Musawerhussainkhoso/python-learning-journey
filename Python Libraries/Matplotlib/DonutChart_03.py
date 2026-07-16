#E-commerce Revenue by Product Category
import matplotlib.pyplot as plt

product_categories = [
    "Electronics",
    "Clothing",
    "Home Appliances",
    "Beauty",
    "Sports"
]

revenue = [
    4_500_000,
    3_200_000,
    2_400_000,
    1_600_000,
    1_300_000
]

total_revenue = sum(revenue)

plt.figure(figsize=(10, 7))

plt.pie(
    revenue,
    labels=product_categories,
    autopct="%1.1f%%",
    startangle=90,
    pctdistance=0.80,
    wedgeprops={
        "width": 0.42,
        "edgecolor": "black"
    }
)

plt.text(
    0,
    0,
    f"Total Revenue\nPKR {total_revenue / 1_000_000:.1f}M",
    ha="center",
    va="center",
    fontsize=12
)

plt.title("Revenue Share by Product Category")
plt.tight_layout()
plt.show()