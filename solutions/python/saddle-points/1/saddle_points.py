def saddle_points(matrix):
    if not matrix:
        return []

    # Check for irregular matrix
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise ValueError("irregular matrix")

    result = []

    for i, row in enumerate(matrix):
        row_max = max(row)
        for j, value in enumerate(row):
            if value == row_max:
                column_values = [matrix[k][j] for k in range(len(matrix))]
                if value == min(column_values):
                    result.append({"row": i + 1, "column": j + 1})

    return result