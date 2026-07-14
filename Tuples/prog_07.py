#2. Merge Overlapping Time Intervals
def merge_intervals(
    intervals: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    """
    Merge overlapping time intervals.
    """

    if not intervals:
        return []

    for start_time, end_time in intervals:
        if start_time >= end_time:
            raise ValueError(
                f"Invalid interval: ({start_time}, {end_time})"
            )

    sorted_intervals = sorted(intervals)

    merged_intervals = [sorted_intervals[0]]

    for current_start, current_end in sorted_intervals[1:]:
        previous_start, previous_end = merged_intervals[-1]

        if current_start <= previous_end:
            merged_intervals[-1] = (
                previous_start,
                max(previous_end, current_end)
            )
        else:
            merged_intervals.append(
                (current_start, current_end)
            )

    return merged_intervals


meeting_slots = [
    (9, 11),
    (10, 12),
    (13, 15),
    (14, 17),
    (18, 20)
]
result = merge_intervals(meeting_slots)
print("Original intervals:", meeting_slots)
print("Merged intervals  :", result)