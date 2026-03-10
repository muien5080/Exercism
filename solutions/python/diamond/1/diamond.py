import string

def rows(letter):
    letters = string.ascii_uppercase
    n = letters.index(letter)
    size = 2 * n + 1
    result = []

    for i in range(size):
        idx = i if i <= n else size - i - 1
        char = letters[idx]

        outer = n - idx
        if idx == 0:
            row = " " * outer + char + " " * outer
        else:
            inner = 2 * idx - 1
            row = " " * outer + char + " " * inner + char + " " * outer

        result.append(row)

    return result