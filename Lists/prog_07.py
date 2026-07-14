'''
This program combines overlapping appointment or meeting times.
'''
def merge_time_slots(
    time_slots: list[tuple[int, int]]
) -> list[tuple[int, int]]:

    if not time_slots:
        return []

    for start, end in time_slots:
        if start >= end:
            raise ValueError(
                f"Invalid time slot: ({start}, {end})"
            )

    sorted_slots = sorted(time_slots)

    merged_slots = [sorted_slots[0]]

    for current_start, current_end in sorted_slots[1:]:
        previous_start, previous_end = merged_slots[-1]

        if current_start <= previous_end:
            merged_slots[-1] = (
                previous_start,
                max(previous_end, current_end)
            )
        else:
            merged_slots.append(
                (current_start, current_end)
            )

    return merged_slots
appointments = [
    (9, 11),
    (10, 12),
    (14, 16),
    (15, 18),
    (19, 20)
]
result = merge_time_slots(appointments)
print("Original slots:", appointments)
print("Merged slots  :", result)
