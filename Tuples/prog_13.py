#8. Find Duplicate Coordinate Pairs
def find_duplicate_coordinates(
    coordinates: list[tuple[float, float]]
) -> list[tuple[tuple[float, float], int]]:
    """
    Find coordinate tuples appearing more than once.
    """

    coordinate_counts = {}

    for coordinate in coordinates:
        coordinate_counts[coordinate] = (
            coordinate_counts.get(coordinate, 0) + 1
        )

    duplicate_coordinates = []

    for coordinate, count in coordinate_counts.items():
        if count > 1:
            duplicate_coordinates.append(
                (coordinate, count)
            )

    duplicate_coordinates.sort(
        key=lambda item: item[1],
        reverse=True
    )

    return duplicate_coordinates


gps_coordinates = [
    (24.8607, 67.0011),
    (31.5204, 74.3587),
    (24.8607, 67.0011),
    (25.3960, 68.3578),
    (24.8607, 67.0011),
    (31.5204, 74.3587),
    (33.6844, 73.0479)
]

duplicates = find_duplicate_coordinates(
    gps_coordinates
)

print("DUPLICATE GPS COORDINATES")
print("=" * 60)

for coordinate, count in duplicates:
    latitude, longitude = coordinate

    print(f"Latitude  : {latitude}")
    print(f"Longitude : {longitude}")
    print(f"Occurrences: {count}")
    print("-" * 60)