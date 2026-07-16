#Company Expense Distribution
import matplotlib.pyplot as plt

categories = [
    "Salaries",
    "Marketing",
    "Operations",
    "Technology",
    "Training"
]

expenses = [45, 18, 20, 12, 5]

plt.figure(figsize=(9, 7))

plt.pie(
    expenses,
    labels=categories,
    autopct="%1.1f%%",
    startangle=90,
    pctdistance=0.78,
    wedgeprops={
        "width": 0.45,
        "edgecolor": "black"
    }
)

plt.text(
    0,
    0,
    "Company\nExpenses",
    ha="center",
    va="center",
    fontsize=13
)

plt.title("Company Expense Distribution")
plt.tight_layout()
plt.show()