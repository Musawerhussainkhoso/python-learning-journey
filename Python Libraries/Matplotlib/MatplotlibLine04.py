#Website Visitors vs Registered Users
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

visitors = [1200, 1800, 2500, 3200, 4200, 5000]
registered = [200, 400, 700, 1000, 1500, 2200]

plt.figure(figsize=(10,6))

plt.plot(
    months,
    visitors,
    color="purple",
    linestyle="-",
    marker="o",
    linewidth=2,
    label="Visitors"
)

plt.plot(
    months,
    registered,
    color="brown",
    linestyle="-.",
    marker="^",
    linewidth=2,
    label="Registered Users"
)

plt.title("Website Growth Report")
plt.xlabel("Months")
plt.ylabel("Users")

plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()