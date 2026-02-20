def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    # 1 is always deficient
    if number == 1:
        return "deficient"
    
    aliquot_sum = 1  # 1 is always a divisor (except for 1 itself)
    
    # Only iterate up to sqrt(number) for efficiency
    i = 2
    while i * i <= number:
        if number % i == 0:
            aliquot_sum += i
            if i != number // i:
                aliquot_sum += number // i
        i += 1
    
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"