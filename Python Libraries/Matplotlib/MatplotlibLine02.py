#Monthly Revenue vs Expenses
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

revenue = [50000, 62000, 70000, 68000, 75000, 82000]
expenses = [35000, 40000, 42000, 45000, 47000, 50000]

plt.figure(figsize=(10, 6))

plt.plot(
    months,
    revenue,
    color="green",
    linestyle="-",
    linewidth=2,
    marker="o",
    markersize=7,
    label="Revenue"
)

plt.plot(
    months,
    expenses,
    color="red",
    linestyle="--",
    linewidth=2,
    marker="s",
    markersize=7,
    label="Expenses"
)

plt.title("Company Revenue vs Expenses")
plt.xlabel("Months")
plt.ylabel("Amount (PKR)")
plt.grid(True, linestyle=":")
plt.legend()

plt.tight_layout()
plt.show()