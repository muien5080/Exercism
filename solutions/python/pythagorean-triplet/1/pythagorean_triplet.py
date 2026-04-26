def triplets_with_sum(number):
    triplets = set()
    
    for m in range(2, int((number // 2) ** 0.5) + 1):
        for n in range(1, m):
            denom = 2 * m * (m + n)
            
            if denom > number:
                break
            
            if number % denom == 0:
                k = number // denom
                
                a = k * (m * m - n * n)
                b = k * (2 * m * n)
                c = k * (m * m + n * n)
                
                triplet = tuple(sorted([a, b, c]))
                triplets.add(triplet)
    
    return [list(t) for t in triplets]