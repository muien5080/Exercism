def square_root(number):
    left = 1
    right = number

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == number:
            return mid
        elif square < number:
            left = mid + 1
        else:
            right = mid - 1