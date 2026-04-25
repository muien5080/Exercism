def sum_of_multiples(limit, multiples):
    result = set()
    
    for m in multiples:
        if m == 0:
            continue  # avoid infinite multiples of 0
        
        for i in range(m, limit, m):
            result.add(i)
    
    return sum(result)
    