def _is_valid_triangle(sides):
    if len(sides) != 3:
        return False

    a, b, c = sides

    # All sides must be greater than 0
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Triangle inequality
    return (
        a + b >= c and
        b + c >= a and
        a + c >= b
    )


def equilateral(sides):
    if not _is_valid_triangle(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if not _is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a == b or b == c or a == c


def scalene(sides):
    if not _is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a != b and b != c and a != c