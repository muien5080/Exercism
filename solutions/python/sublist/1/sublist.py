# Possible sublist categories.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(a, b):
    if a == b:
        return EQUAL

    # Helper function to check if small is a contiguous sublist of big
    def is_sublist(small, big):
        if not small:
            return True
        for i in range(len(big) - len(small) + 1):
            if big[i:i + len(small)] == small:
                return True
        return False

    if is_sublist(a, b):
        return SUBLIST

    if is_sublist(b, a):
        return SUPERLIST

    return UNEQUAL