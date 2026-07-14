#This program uses a nested list to calculate branch totals, monthly totals, and the best-performing branch.
def analyze_branch_sales(
    branch_names: list[str],
    monthly_sales: list[list[float]],
    month_names: list[str]
) -> None:

    if len(branch_names) != len(monthly_sales):
        raise ValueError(
            "Every branch must have one sales row."
        )

    branch_totals = []

    for branch_sales in monthly_sales:
        branch_total = 0

        for sale in branch_sales:
            branch_total += sale

        branch_totals.append(branch_total)

    monthly_totals = []

    for month_index in range(len(month_names)):
        month_total = 0

        for branch_sales in monthly_sales:
            month_total += branch_sales[month_index]

        monthly_totals.append(month_total)

    best_branch_index = 0

    for index in range(1, len(branch_totals)):
        if branch_totals[index] > branch_totals[
            best_branch_index
        ]:
            best_branch_index = index

    print("BRANCH SALES REPORT")
    print("=" * 65)

    for index in range(len(branch_names)):
        print(
            f"{branch_names[index]:<15} "
            f"Rs. {branch_totals[index]:>15,.2f}"
        )

    print("\nMONTHLY COMPANY SALES")
    print("-" * 65)

    for index in range(len(month_names)):
        print(
            f"{month_names[index]:<15} "
            f"Rs. {monthly_totals[index]:>15,.2f}"
        )

    print("-" * 65)
    print(
        f"Best branch: "
        f"{branch_names[best_branch_index]}"
    )
    print(
        f"Total sales: "
        f"Rs. {branch_totals[best_branch_index]:,.2f}"
    )


branches = [
    "Karachi",
    "Lahore",
    "Islamabad"
]

months = [
    "January",
    "February",
    "March",
    "April"
]

sales_matrix = [
    [450000, 520000, 490000, 610000],
    [420000, 480000, 530000, 550000],
    [390000, 450000, 470000, 500000]
]

analyze_branch_sales(
    branches,
    sales_matrix,
    months
)