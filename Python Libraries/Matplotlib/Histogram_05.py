#Website Session Duration
import matplotlib.pyplot as plt

session_minutes = [
    2, 3, 4, 5, 5, 6, 7, 8, 8, 9,
    10, 11, 12, 13, 15, 17, 18, 20, 22, 25
]

plt.figure(figsize=(10, 6))

plt.hist(
    session_minutes,
    bins=6,
    edgecolor="black"
)

plt.title("Website Session Duration")
plt.xlabel("Session Duration (Minutes)")
plt.ylabel("Number of Users")

plt.grid(axis="y", linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()