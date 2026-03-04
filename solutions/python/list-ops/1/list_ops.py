def append(list1, list2):
    result = []
    for item in list1:
        result += [item]
    for item in list2:
        result += [item]
    return result


def concat(lists):
    result = []
    for lst in lists:
        for item in lst:
            result += [item]
    return result


def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result += [item]
    return result


def length(list):
    count = 0
    for _ in list:
        count += 1
    return count


def map(function, list):
    result = []
    for item in list:
        result += [function(item)]
    return result


def foldl(function, list, initial):
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, list, initial):
    accumulator = initial

    size = 0
    for _ in list:
        size += 1

    while size > 0:
        size -= 1
        accumulator = function(accumulator, list[size])

    return accumulator

    while size > 0:
        size -= 1
        accumulator = function(list[size], accumulator)
    return accumulator


def reverse(list):
    result = []
    size = 0
    for _ in list:
        size += 1

    while size > 0:
        size -= 1
        result += [list[size]]
    return result