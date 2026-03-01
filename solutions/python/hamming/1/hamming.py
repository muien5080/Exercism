def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    differences = 0
    
    for a, b in zip(strand_a, strand_b):
        if a != b:
            differences += 1
    
    return differences
    