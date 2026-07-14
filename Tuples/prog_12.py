#7. Group Sales Records by Region
def analyse_regional_sales(
    sales_records: list[tuple[str, str, int, float]]
) -> tuple[
    list[tuple[str, float]],
    tuple[str, float] | None
]:
    """
    Calculate regional revenue from tuple records.
    """

    regional_revenue = {}

    for region, product, quantity, unit_price in sales_records:
        sale_amount = quantity * unit_price

        regional_revenue[region] = (
            regional_revenue.get(region, 0)
            + sale_amount
        )

    regional_summary = []

    for region, revenue in regional_revenue.items():
        regional_summary.append(
            (region, revenue)
        )

    regional_summary.sort(
        key=lambda record: record[1],
        reverse=True
    )

    best_region = (
        regional_summary[0]
        if regional_summary
        else None
    )

    return regional_summary, best_region


sales = [
    ("Karachi", "Laptop", 3, 150000),
    ("Lahore", "Monitor", 5, 45000),
    ("Karachi", "Keyboard", 10, 5000),
    ("Islamabad", "Laptop", 2, 150000),
    ("Lahore", "Mouse", 15, 3000),
    ("Karachi", "Monitor", 4, 45000)
]

regional_report, best_region = analyse_regional_sales(sales)

print("REGIONAL SALES REPORT")
print("=" * 55)

for region, revenue in regional_report:
    print(f"{region:<20} Rs. {revenue:>15,.2f}")

if best_region:
    region_name, revenue = best_region

    print("-" * 55)
    print(f"Best-performing region: {region_name}")
    print(f"Revenue: Rs. {revenue:,.2f}")