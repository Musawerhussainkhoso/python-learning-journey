#Temperature Distribution
import matplotlib.pyplot as plt

temperatures = [
    21, 22, 23, 24, 25, 26, 27,
    28, 29, 30, 31, 32, 33, 34,
    35, 36, 37, 38, 39, 40
]

plt.figure(figsize=(10, 6))

plt.hist(
    temperatures,
    bins=5,
    edgecolor="black"
)

plt.title("Daily Temperature Distribution")
plt.xlabel("Temperature (°C)")
plt.ylabel("Number of Days")

plt.grid(axis="y", linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()