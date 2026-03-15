def prime(n):
    if n < 1:
        raise ValueError("there is no zeroth prime")

    count = 0
    num = 1

    while count < n:
        num += 1
        if is_prime(num):
            count += 1

    return num


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True