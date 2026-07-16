#Student Attendance Analysis
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

present = [45, 47, 46, 48, 49]
absent = [5, 3, 4, 2, 1]

plt.figure(figsize=(10,6))

plt.plot(
    days,
    present,
    color="blue",
    linestyle="-",
    marker="o",
    linewidth=2,
    label="Present"
)

plt.plot(
    days,
    absent,
    color="orange",
    linestyle=":",
    marker="D",
    linewidth=2,
    label="Absent"
)

plt.title("Weekly Student Attendance")
plt.xlabel("Days")
plt.ylabel("Number of Students")

plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

plt.show()