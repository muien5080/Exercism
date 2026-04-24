def transpose(text):
    lines = text.split("\n")
    max_len = max(len(line) for line in lines)

    # Pad all lines to same length
    padded = [line.ljust(max_len) for line in lines]

    # Transpose using zip
    transposed = [''.join(row) for row in zip(*padded)]

    # Remove trailing spaces ONLY if they are from bottom padding
    result = []
    for i, row in enumerate(transposed):
        # Look at column i downward in original
        # Find last line that has a real character in this column
        last_real = -1
        for j in range(len(lines)):
            if i < len(lines[j]):
                last_real = j

        # Keep only up to that point
        result.append(row[:last_real + 1])

    return "\n".join(result)