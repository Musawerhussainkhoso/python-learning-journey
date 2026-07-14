#Matrix multiplication is an important example of professional nested-loop logic.
def multiply_matrices(
    first_matrix: list[list[int]],
    second_matrix: list[list[int]]
) -> list[list[int]]:

    first_rows = len(first_matrix)
    first_columns = len(first_matrix[0])

    second_rows = len(second_matrix)
    second_columns = len(second_matrix[0])

    if first_columns != second_rows:
        raise ValueError(
            "Matrix multiplication is not possible. "
            "Columns of the first matrix must equal "
            "rows of the second matrix."
        )

    result = []

    for row in range(first_rows):
        result_row = []

        for column in range(second_columns):
            total = 0

            for index in range(first_columns):
                total += (
                    first_matrix[row][index]
                    * second_matrix[index][column]
                )

            result_row.append(total)

        result.append(result_row)

    return result


def display_matrix(matrix: list[list[int]]) -> None:
    for row in matrix:
        for value in row:
            print(f"{value:>6}", end="")

        print()


matrix_a = [
    [2, 4, 1],
    [3, 5, 2]
]

matrix_b = [
    [1, 2],
    [3, 4],
    [5, 6]
]

try:
    result_matrix = multiply_matrices(matrix_a, matrix_b)

    print("First Matrix:")
    display_matrix(matrix_a)

    print("\nSecond Matrix:")
    display_matrix(matrix_b)

    print("\nResult Matrix:")
    display_matrix(result_matrix)

except ValueError as error:
    print(error)