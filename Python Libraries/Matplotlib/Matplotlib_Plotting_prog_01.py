#Monthly Sales Performance
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120000, 145000, 138000, 170000, 195000, 210000]

plt.figure(figsize=(10, 6))#10 = width , 6 = height

plt.plot(
    months,
    sales,
    marker="o",
    linewidth=2,
    markersize=7
)

plt.title("Monthly Sales Performance", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales Amount", fontsize=12)

plt.grid(True, linestyle="--", alpha=0.6)

#True → grid lines on kar deta hai.
#linestyle="--" → grid lines dashed hongi.
#alpha=0.6 → grid lines thori transparent hongi.

plt.tight_layout()
plt.show()
