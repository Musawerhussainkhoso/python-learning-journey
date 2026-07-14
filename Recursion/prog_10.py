def find_maximum(numbers: list[int], index: int = 0) -> int:
    """
    Find the maximum value in a non-empty list
    using recursion.
    """

    # Base case: last element
    if index == len(numbers) - 1:
        return numbers[index]

    # Find maximum from the remaining list
    remaining_maximum = find_maximum(numbers, index + 1)

    # Compare current value with remaining maximum
    if numbers[index] > remaining_maximum:
        return numbers[index]

    return remaining_maximum


numbers = [45, 12, 89, 34, 67, 102, 56]

if not numbers:
    print("The list is empty.")
else:
    result = find_maximum(numbers)

    print(f"Numbers: {numbers}")
    print(f"Maximum value: {result}")