#E-commerce Payment Methods
import matplotlib.pyplot as plt

payment_methods = [
    "Cash on Delivery",
    "Debit/Credit Card",
    "Bank Transfer",
    "Digital Wallet"
]

transactions = [450, 280, 120, 150]

plt.figure(figsize=(10, 7))

plt.pie(
    transactions,
    labels=payment_methods,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={"edgecolor": "black"}
)

plt.title("Customer Payment Method Distribution")

plt.tight_layout()
plt.show()