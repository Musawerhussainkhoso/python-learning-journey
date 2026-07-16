import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
actual_sales = [100, 140, 130, 180]
target_sales = [120, 120, 150, 170]
forecast_sales = [110, 150, 160, 200]

plt.plot(
    months,
    actual_sales,
    linestyle="-",
    marker="o",
    label="Actual Sales"
)

plt.plot(
    months,
    target_sales,
    linestyle=":",
    label="Target"
)

plt.plot(
    months,
    forecast_sales,
    linestyle="--",
    marker="s",
    label="Forecast"
)

plt.legend()
plt.grid(True)
plt.show()