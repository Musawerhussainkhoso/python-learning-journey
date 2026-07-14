def find_gcd(first_number: int, second_number: int) -> int:
    """
    Calculate the greatest common divisor using
    Euclid's recursive algorithm.
    """

    first_number = abs(first_number)
    second_number = abs(second_number)

    # Base case
    if second_number == 0:
        return first_number

    # Recursive case
    return find_gcd(
        second_number,
        first_number % second_number
    )


try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    if first_number == 0 and second_number == 0:
        print("GCD is not defined when both numbers are zero.")
    else:
        result = find_gcd(first_number, second_number)

        print(
            f"The GCD of {first_number} and "
            f"{second_number} is {result}."
        )

except ValueError:
    print("Please enter valid whole numbers.")