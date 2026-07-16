#jab numerical data ko ranges/groups mein divide karke 
# frequency dekhni ho, tab histogram use karte hain.
# 1 : Student Marks Distribution program
import matplotlib.pyplot as plt

marks = [
    45, 56, 67, 78, 89, 92, 34, 55, 61, 73,
    81, 88, 49, 58, 64, 76, 85, 90, 42, 69
]

plt.figure(figsize=(10, 6))

plt.hist(
    marks,
    bins=5,
    edgecolor="black"
)

plt.title("Student Marks Distribution")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")

plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
