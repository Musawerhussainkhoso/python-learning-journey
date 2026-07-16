#Actual Sales vs Target Sales
import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May"]

actual_sales = [120, 150, 135, 180, 210]
target_sales = [130, 145, 160, 175, 200]

positions = np.arange(len(months))
bar_width = 0.35

plt.figure(figsize=(11, 6))

plt.bar(
    positions - bar_width / 2,
    actual_sales,
    width=bar_width,
    label="Actual Sales",
    edgecolor="black"
)

plt.bar(
    positions + bar_width / 2,
    target_sales,
    width=bar_width,
    label="Target Sales",
    edgecolor="black"
)

plt.title("Actual Sales vs Target Sales")
plt.xlabel("Months")
plt.ylabel("Sales Units")

plt.xticks(positions, months)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.legend()
plt.tight_layout()
plt.show()