#4. Find the Nearest Delivery Location
from math import sqrt
def calculate_distance(
    first_point: tuple[float, float],
    second_point: tuple[float, float]
) -> float:
    """
    Calculate Euclidean distance between two points.
    """

    x_difference = second_point[0] - first_point[0]
    y_difference = second_point[1] - first_point[1]

    return sqrt(
        x_difference ** 2
        + y_difference ** 2
    )


def find_nearest_location(
    warehouse: tuple[float, float],
    locations: list[tuple[str, float, float]]
) -> tuple[str, float]:
    """
    Find the nearest delivery location.
    """

    if not locations:
        raise ValueError("Location list cannot be empty.")

    nearest_location = ""
    shortest_distance = float("inf")

    for location_name, x_coordinate, y_coordinate in locations:
        location_point = (x_coordinate, y_coordinate)

        distance = calculate_distance(
            warehouse,
            location_point
        )

        if distance < shortest_distance:
            shortest_distance = distance
            nearest_location = location_name

    return nearest_location, shortest_distance


warehouse_location = (2.0, 3.0)

delivery_locations = [
    ("Customer A", 5.0, 7.0),
    ("Customer B", 3.0, 4.0),
    ("Customer C", 10.0, 12.0),
    ("Customer D", 1.0, 8.0)
]

location, distance = find_nearest_location(
    warehouse_location,
    delivery_locations
)
print(f"Nearest location : {location}")
print(f"Distance         : {distance:.2f} units")