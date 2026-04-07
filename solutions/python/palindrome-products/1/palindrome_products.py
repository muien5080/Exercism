def is_palindrome(n):
    return str(n) == str(n)[::-1]


def largest(min_factor=0, max_factor=None):
    if max_factor is None or min_factor > max_factor:
        raise ValueError("min must be <= max")

    max_pal = None
    factors = []

    for i in range(max_factor, min_factor - 1, -1):
        for j in range(i, min_factor - 1, -1):
            product = i * j

            # Early break (critical optimization)
            if max_pal is not None and product < max_pal:
                break

            if is_palindrome(product):
                if max_pal is None or product > max_pal:
                    max_pal = product
                    factors = [(j, i)]
                elif product == max_pal:
                    factors.append((j, i))

    return (max_pal, factors)


def smallest(min_factor=0, max_factor=None):
    if max_factor is None or min_factor > max_factor:
        raise ValueError("min must be <= max")

    min_pal = None
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j

            # Early break (important optimization)
            if min_pal is not None and product > min_pal:
                break

            if is_palindrome(product):
                if min_pal is None or product < min_pal:
                    min_pal = product
                    factors = [(i, j)]
                elif product == min_pal:
                    factors.append((i, j))

    return (min_pal, factors)