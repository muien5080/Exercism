def annotate(board):
    if not board:
        return []

    row_len = len(board[0])

    for row in board:
        if len(row) != row_len:
            raise ValueError("The board is invalid with current input.")
        for ch in row:
            if ch not in (" ", "*"):
                raise ValueError("The board is invalid with current input.")

    rows = len(board)
    cols = row_len
    result = []

    for r in range(rows):
        new_row = ""
        for c in range(cols):

            if board[r][c] == "*":
                new_row += "*"
                continue

            count = 0

            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue

                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] == "*":
                            count += 1

            new_row += " " if count == 0 else str(count)

        result.append(new_row)

    return result