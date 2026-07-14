def count_nested_elements(data: list) -> int:
    """
    Count all non-list elements inside a nested list
    using recursion.
    """

    total = 0

    for item in data:

        # If the item is another list,
        # recursively count its elements
        if isinstance(item, list):
            total += count_nested_elements(item)

        # Otherwise count the normal element
        else:
            total += 1

    return total


company_data = [
    "Manager",
    ["Developer 1", "Developer 2"],
    [
        "Team Lead",
        ["Intern 1", "Intern 2", "Intern 3"]
    ]
]

result = count_nested_elements(company_data)

print("Company data:", company_data)
print("Total individual records:", result)