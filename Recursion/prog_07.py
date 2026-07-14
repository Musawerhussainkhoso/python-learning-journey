def recursive_binary_search(
    numbers: list[int],
    target: int,
    left: int,
    right: int
) -> int:
    """
    Search for a target value in a sorted list.

    Returns:
        Index of the target if found.
        -1 if the target does not exist.
    """

    # Base case: search area is finished
    if left > right:
        return -1

    middle = (left + right) // 2

    # Target found
    if numbers[middle] == target:
        return middle

    # Search in the left side
    if target < numbers[middle]:
        return recursive_binary_search(
            numbers,
            target,
            left,
            middle - 1
        )

    # Search in the right side
    return recursive_binary_search(
        numbers,
        target,
        middle + 1,
        right
    )


numbers = [10, 20, 30, 40, 50, 60, 70]

try:
    target = int(input("Enter the number you want to search: "))

    result = recursive_binary_search(
        numbers,
        target,
        0,
        len(numbers) - 1
    )

    if result == -1:
        print(f"{target} was not found.")
    else:
        print(f"{target} was found at index {result}.")

except ValueError:
    print("Please enter a valid whole number.")