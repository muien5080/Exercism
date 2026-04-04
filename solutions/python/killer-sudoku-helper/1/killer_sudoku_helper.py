def combinations(target, size, exclude):
    result = []
    
    digits = [d for d in range(1, 10) if d not in exclude]
    
    def backtrack(start, path, remaining):
        if len(path) == size:
            if remaining == 0:
                result.append(path)
            return
        
        for i in range(start, len(digits)):
            num = digits[i]
            
            if num > remaining:
                break
            
            backtrack(i + 1, path + [num], remaining - num)
    
    backtrack(0, [], target)
    
    return result