'''
Real APIs often allow only a limited number of records per request.
This program divides a large list into smaller batches.
'''
def create_batches(
    records: list[dict],
    batch_size: int
) -> list[list[dict]]:

    if batch_size <= 0:
        raise ValueError(
            "Batch size must be greater than zero."
        )

    batches = []

    for start_index in range(
        0,
        len(records),
        batch_size
    ):
        end_index = start_index + batch_size

        batch = records[start_index:end_index]

        batches.append(batch)

    return batches


def process_batches(
    batches: list[list[dict]]
) -> None:

    for batch_number, batch in enumerate(
        batches,
        start=1
    ):
        print(f"\nProcessing batch {batch_number}")
        print("-" * 50)

        for record in batch:
            print(
                f"Sending customer "
                f"{record['customer_id']}: "
                f"{record['name']}"
            )


customer_records = [
    {"customer_id": 101, "name": "Ali"},
    {"customer_id": 102, "name": "Sara"},
    {"customer_id": 103, "name": "Ahmed"},
    {"customer_id": 104, "name": "Hina"},
    {"customer_id": 105, "name": "Usman"},
    {"customer_id": 106, "name": "Ayesha"},
    {"customer_id": 107, "name": "Hamza"}
]

customer_batches = create_batches(
    customer_records,
    batch_size=3
)
process_batches(customer_batches)
