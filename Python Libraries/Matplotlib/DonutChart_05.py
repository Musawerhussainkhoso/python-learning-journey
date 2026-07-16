#Software Project Status Dashboard
import matplotlib.pyplot as plt

project_status = [
    "Completed",
    "In Progress",
    "Under Review",
    "Not Started"
]

projects = [18, 10, 6, 4]

total_projects = sum(projects)
completed_projects = projects[0]

completion_rate = (
    completed_projects / total_projects
) * 100

plt.figure(figsize=(10, 7))

plt.pie(
    projects,
    labels=project_status,
    autopct="%1.1f%%",
    startangle=90,
    counterclock=False,
    pctdistance=0.79,
    wedgeprops={
        "width": 0.43,
        "edgecolor": "black"
    }
)

plt.text(
    0,
    0,
    f"{completion_rate:.1f}%\nCompleted",
    ha="center",
    va="center",
    fontsize=14,
    fontweight="bold"
)

plt.title("Software Project Status Overview")
plt.tight_layout()
plt.show()