#This program uses Kadane’s algorithm to find the continuous period with the highest total profit.
def find_best_profit_period(
    daily_profits: list[float]
) -> dict:

    if not daily_profits:
        raise ValueError(
            "Profit list cannot be empty."
        )

    current_profit = daily_profits[0]
    maximum_profit = daily_profits[0]

    current_start = 0
    best_start = 0
    best_end = 0

    for index in range(1, len(daily_profits)):
        profit = daily_profits[index]

        if profit > current_profit + profit:
            current_profit = profit
            current_start = index
        else:
            current_profit += profit

        if current_profit > maximum_profit:
            maximum_profit = current_profit
            best_start = current_start
            best_end = index

    return {
        "start_day": best_start + 1,
        "end_day": best_end + 1,
        "total_profit": maximum_profit,
        "period_values": daily_profits[
            best_start:best_end + 1
        ]
    }


profits = [
    -15000,
    22000,
    35000,
    -12000,
    18000,
    -5000,
    27000,
    -40000
]

best_period = find_best_profit_period(profits)

print("BEST BUSINESS PROFIT PERIOD")
print("=" * 60)
print(f"Starting day : {best_period['start_day']}")
print(f"Ending day   : {best_period['end_day']}")
print(f"Daily values : {best_period['period_values']}")
print(
    f"Total profit : "
    f"Rs. {best_period['total_profit']:,.2f}"
)