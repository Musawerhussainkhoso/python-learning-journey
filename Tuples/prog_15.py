#10. Calculate Portfolio Performance
def calculate_portfolio_performance(
    investments: list[tuple[str, int, float, float]]
) -> tuple[
    float,
    float,
    float,
    list[tuple[str, float, float]]
]:
    """
    Calculate portfolio cost, value, and profit or loss.
    """

    total_investment_cost = 0.0
    total_current_value = 0.0
    performance_records = []

    for investment in investments:
        symbol, quantity, purchase_price, current_price = investment

        investment_cost = quantity * purchase_price
        current_value = quantity * current_price

        profit_or_loss = current_value - investment_cost

        if investment_cost == 0:
            percentage_return = 0.0
        else:
            percentage_return = (
                profit_or_loss / investment_cost
            ) * 100

        total_investment_cost += investment_cost
        total_current_value += current_value

        performance_records.append(
            (
                symbol,
                profit_or_loss,
                percentage_return
            )
        )

    total_profit_or_loss = (
        total_current_value - total_investment_cost
    )

    performance_records.sort(
        key=lambda record: record[2],
        reverse=True
    )

    return (
        total_investment_cost,
        total_current_value,
        total_profit_or_loss,
        performance_records
    )


portfolio = [
    ("TECH-A", 100, 250.00, 310.00),
    ("BANK-B", 200, 175.00, 160.00),
    ("ENERGY-C", 150, 120.00, 145.00),
    ("HEALTH-D", 80, 300.00, 295.00)
]

cost, current_value, profit_loss, performance = (
    calculate_portfolio_performance(portfolio)
)

print("INVESTMENT PORTFOLIO REPORT")
print("=" * 70)

for symbol, return_amount, return_percentage in performance:
    if return_amount >= 0:
        status = "Profit"
    else:
        status = "Loss"

    print(f"Symbol       : {symbol}")
    print(f"Status       : {status}")
    print(f"Return       : Rs. {return_amount:,.2f}")
    print(f"Return rate  : {return_percentage:.2f}%")
    print("-" * 70)

print(f"Total investment : Rs. {cost:,.2f}")
print(f"Current value    : Rs. {current_value:,.2f}")
print(f"Net profit/loss  : Rs. {profit_loss:,.2f}")