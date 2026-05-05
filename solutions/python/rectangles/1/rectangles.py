def rectangles(strings):
    if not strings:
        return 0

    rows = len(strings)
    cols = len(strings[0])
    count = 0

    def is_horizontal_edge(row, c1, c2):
        return all(strings[row][c] in '-+' for c in range(c1 + 1, c2))

    def is_vertical_edge(col, r1, r2):
        return all(strings[r][col] in '|+' for r in range(r1 + 1, r2))

    for top in range(rows):
        for bottom in range(top + 1, rows):
            for left in range(cols):
                for right in range(left + 1, cols):
                    # Check corners
                    if (strings[top][left] == '+' and
                        strings[top][right] == '+' and
                        strings[bottom][left] == '+' and
                        strings[bottom][right] == '+'):

                        # Check edges
                        if (is_horizontal_edge(top, left, right) and
                            is_horizontal_edge(bottom, left, right) and
                            is_vertical_edge(left, top, bottom) and
                            is_vertical_edge(right, top, bottom)):
                            
                            count += 1

    return count