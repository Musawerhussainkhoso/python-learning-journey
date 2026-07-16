#Quarterly Revenue and Expenses
import matplotlib.pyplot as plt
import numpy as np

quarters = ["Q1", "Q2", "Q3", "Q4"]

revenue = [2_500_000, 3_100_000, 3_600_000, 4_200_000]
expenses = [1_800_000, 2_000_000, 2_300_000, 2_700_000]

positions = np.arange(len(quarters))
bar_width = 0.35

plt.figure(figsize=(11, 6))

revenue_bars = plt.bar(
    positions - bar_width / 2,
    revenue,
    width=bar_width,
    label="Revenue",
    edgecolor="black"
)

expense_bars = plt.bar(
    positions + bar_width / 2,
    expenses,
    width=bar_width,
    label="Expenses",
    edgecolor="black"
)

plt.title("Quarterly Financial Performance")
plt.xlabel("Quarter")
plt.ylabel("Amount (PKR)")

plt.xticks(positions, quarters)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.legend()

for bars in [revenue_bars, expense_bars]:
    for bar in bars:
        value = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            value + 50000,
            f"{value / 1_000_000:.1f}M",
            ha="center"
        )

plt.tight_layout()
plt.show()