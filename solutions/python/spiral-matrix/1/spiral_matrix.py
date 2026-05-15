def spiral_matrix(size):
    # Create an empty size x size matrix
    matrix = [[0] * size for _ in range(size)]

    num = 1
    left, right = 0, size - 1
    top, bottom = 0, size - 1

    while left <= right and top <= bottom:

        # Move left → right
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1

        # Move top ↓ bottom
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1

        # Move right → left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1

        # Move bottom ↑ top
        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1

    return matrix