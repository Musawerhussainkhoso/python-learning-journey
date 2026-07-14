#This program converts nested list data into a flat list while remembering the location of every value.
def flatten_with_paths(
    nested_data: list,
    current_path: list[int] | None = None
) -> list[dict]:

    if current_path is None:
        current_path = []

    flattened_records = []

    for index, item in enumerate(nested_data):
        item_path = current_path + [index]

        if isinstance(item, list):
            nested_result = flatten_with_paths(
                item,
                item_path
            )

            flattened_records.extend(nested_result)

        else:
            flattened_records.append({
                "path": item_path,
                "value": item
            })

    return flattened_records


company_structure = [
    "CEO",
    [
        "Engineering Manager",
        [
            "Backend Developer",
            "Frontend Developer"
        ]
    ],
    [
        "Finance Manager",
        [
            "Accountant",
            "Auditor"
        ]
    ]
]

flattened_data = flatten_with_paths(
    company_structure
)

print("FLATTENED ORGANIZATION DATA")
print("=" * 60)

for record in flattened_data:
    path_text = " → ".join(
        str(position)
        for position in record["path"]
    )

    print(
        f"Path: {path_text:<12} "
        f"Value: {record['value']}"
    )