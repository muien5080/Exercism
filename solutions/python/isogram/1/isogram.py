def is_isogram(string):
    cleaned = string.lower()
    seen = set()
    
    for char in cleaned:
        if char.isalpha():  # Ignore spaces and hyphens (and any non-letter)
            if char in seen:
                return False
            seen.add(char)
    
    return True