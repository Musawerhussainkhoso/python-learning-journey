#Pie chart kyun use karte hain?

#Pie chart tab use hota hai jab humein ek total ke different parts ya percentages show karne hon.

#Example:

#Company ka total budget 100% hai:

#Salaries = 40%
#Marketing = 20%
#Operations = 25%
#Technology = 15%

#Pie chart batata hai ke total mein har category ka kitna share hai.

#Q COMPANY BUDGET DISTRIBUTION
import matplotlib.pyplot as plt

departments = [
    "Salaries",
    "Marketing",
    "Operations",
    "Technology",
    "Training"
]

budget = [40, 20, 25, 10, 5]

plt.figure(figsize=(9, 7))

plt.pie(
    budget,
    labels=departments,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={"edgecolor": "black"}
)

plt.title("Company Annual Budget Distribution")

plt.tight_layout()
plt.show()