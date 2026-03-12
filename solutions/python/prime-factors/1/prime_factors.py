def factors(value):
    result = []

    # handle factor 2
    while value % 2 == 0:
        result.append(2)
        value //= 2

    # check odd factors
    i = 3
    while i * i <= value:
        while value % i == 0:
            result.append(i)
            value //= i
        i += 2

    # if remaining value is prime
    if value > 1:
        result.append(value)

    return result