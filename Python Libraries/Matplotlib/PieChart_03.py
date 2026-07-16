#Employee Work Mode Distribution
import matplotlib.pyplot as plt

work_modes = [
    "On-site",
    "Remote",
    "Hybrid"
]

employees = [120, 60, 90]

plt.figure(figsize=(9, 7))

plt.pie(
    employees,
    labels=work_modes,
    autopct="%1.0f%%",
    startangle=90,
    counterclock=False,
    wedgeprops={
        "edgecolor": "black",
        "linewidth": 1
    }
)

plt.title("Employee Work Mode Distribution")

plt.tight_layout()
plt.show()