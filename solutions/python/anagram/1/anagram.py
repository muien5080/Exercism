def find_anagrams(word, candidates):
    target_lower = word.lower()
    target_sorted = sorted(target_lower)
    
    result = []
    for candidate in candidates:
        # Skip if the candidate is the same as the target (case-insensitive)
        if candidate.lower() == target_lower:
            continue
        # Check if letters match after sorting
        if sorted(candidate.lower()) == target_sorted:
            result.append(candidate)
    
    return result
