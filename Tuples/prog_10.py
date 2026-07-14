#5. Transpose a Matrix Stored as Tuples
def transpose_matrix(
    matrix: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, ...], ...]:
    """
    Transpose a matrix stored as a tuple of tuples.
    """

    if not matrix:
        return tuple()

    column_count = len(matrix[0])

    for row in matrix:
        if len(row) != column_count:
            raise ValueError(
                "All matrix rows must have equal length."
            )

    transposed_rows = []

    for column_index in range(column_count):
        new_row = []

        for row_index in range(len(matrix)):
            new_row.append(
                matrix[row_index][column_index]
            )

        transposed_rows.append(tuple(new_row))

    return tuple(transposed_rows)


def display_matrix(
    matrix: tuple[tuple[int, ...], ...]
) -> None:

    for row in matrix:
        for value in row:
            print(f"{value:>5}", end="")

        print()


original_matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (10, 11, 12)
)
transposed_matrix = transpose_matrix(original_matrix)
print("ORIGINAL MATRIX")
display_matrix(original_matrix)
print("\nTRANSPOSED MATRIX")
display_matrix(transposed_matrix)