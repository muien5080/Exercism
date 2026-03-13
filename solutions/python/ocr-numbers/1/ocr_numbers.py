DIGITS = {
    (" _ ",
     "| |",
     "|_|",
     "   "): "0",

    ("   ",
     "  |",
     "  |",
     "   "): "1",

    (" _ ",
     " _|",
     "|_ ",
     "   "): "2",

    (" _ ",
     " _|",
     " _|",
     "   "): "3",

    ("   ",
     "|_|",
     "  |",
     "   "): "4",

    (" _ ",
     "|_ ",
     " _|",
     "   "): "5",

    (" _ ",
     "|_ ",
     "|_|",
     "   "): "6",

    (" _ ",
     "  |",
     "  |",
     "   "): "7",

    (" _ ",
     "|_|",
     "|_|",
     "   "): "8",

    (" _ ",
     "|_|",
     " _|",
     "   "): "9",
}


def convert(input_grid):

    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    result = []

    for r in range(0, len(input_grid), 4):
        block = input_grid[r:r+4]
        digits = []

        for c in range(0, len(block[0]), 3):
            pattern = tuple(row[c:c+3] for row in block)
            digits.append(DIGITS.get(pattern, "?"))

        result.append("".join(digits))

    return ",".join(result)