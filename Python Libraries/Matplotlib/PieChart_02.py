#Website Traffic Sources
import matplotlib.pyplot as plt

traffic_sources = [
    "Google Search",
    "Social Media",
    "Direct Traffic",
    "Referral",
    "Email Marketing"
]

visitors = [4200, 2600, 1800, 900, 500]

explode_values = [0.08, 0, 0, 0, 0]

plt.figure(figsize=(10, 7))

plt.pie(
    visitors,
    labels=traffic_sources,
    autopct="%1.1f%%",#autopct pie chart ke har slice par percentage automatically show karta hai.
    startangle=90,
    explode=explode_values,
    shadow=True,
    wedgeprops={"edgecolor": "black"}
)

plt.title("Website Traffic Source Distribution")

plt.tight_layout()
plt.show()