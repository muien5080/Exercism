def largest_product(series, size):
    if size < 0:
        raise ValueError("span must not be negative")
    
    if size > len(series):
        raise ValueError("span must not exceed string length")
    
    if not series.isdigit() and series != "":
        raise ValueError("digits input must only contain digits")
    
    if size == 0:
        return 1

    max_product = 0

    for i in range(len(series) - size + 1):
        product = 1
        for j in range(size):
            product *= int(series[i + j])
        max_product = max(max_product, product)

    return max_product