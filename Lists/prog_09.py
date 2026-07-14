#This program checks whether current sales are unusually high or low compared with previous days.
def detect_sales_anomalies(
    daily_sales: list[float],
    window_size: int = 3,
    threshold: float = 0.30
) -> list[dict]:

    if window_size <= 0:
        raise ValueError(
            "Window size must be greater than zero."
        )

    if len(daily_sales) <= window_size:
        return []

    anomalies = []

    for index in range(window_size, len(daily_sales)):
        previous_sales = daily_sales[
            index - window_size:index
        ]

        average_sales = (
            sum(previous_sales) / window_size
        )

        current_sale = daily_sales[index]

        percentage_change = (
            current_sale - average_sales
        ) / average_sales

        if abs(percentage_change) >= threshold:
            if percentage_change > 0:
                anomaly_type = "Unusually high"
            else:
                anomaly_type = "Unusually low"

            anomalies.append({
                "day": index + 1,
                "sale": current_sale,
                "previous_average": average_sales,
                "change_percentage": percentage_change * 100,
                "type": anomaly_type
            })

    return anomalies


sales = [
    100000,
    105000,
    98000,
    102000,
    175000,
    110000,
    45000,
    108000
]

sales_anomalies = detect_sales_anomalies(
    sales,
    window_size=3,
    threshold=0.30
)

print("SALES ANOMALY REPORT")
print("=" * 65)

for anomaly in sales_anomalies:
    print(f"Day              : {anomaly['day']}")
    print(f"Current sale     : Rs. {anomaly['sale']:,.2f}")
    print(
        f"Previous average : "
        f"Rs. {anomaly['previous_average']:,.2f}"
    )
    print(
        f"Change           : "
        f"{anomaly['change_percentage']:.2f}%"
    )
    print(f"Status           : {anomaly['type']}")
    print("-" * 65)
