def tick(matrix):
    if not matrix or not matrix[0]:
        return matrix

    rows = len(matrix)
    cols = len(matrix[0])

    def count_neighbors(r, c):
        count = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    count += matrix[nr][nc]
        return count

    new_matrix = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            neighbors = count_neighbors(r, c)

            if matrix[r][c] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_matrix[r][c] = 1
            else:
                if neighbors == 3:
                    new_matrix[r][c] = 1

    return new_matrix