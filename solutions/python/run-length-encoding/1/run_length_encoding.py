def encode(string):
    if not string:
        return ""
    
    result = []
    count = 1
    prev = string[0]
    
    for char in string[1:]:
        if char == prev:
            count += 1
        else:
            # Append count only if greater than 1
            result.append((str(count) if count > 1 else "") + prev)
            prev = char
            count = 1
    
    # Append the last run
    result.append((str(count) if count > 1 else "") + prev)
    
    return "".join(result)


def decode(string):
    result = []
    count = ""
    
    for char in string:
        if char.isdigit():
            count += char
        else:
            # If no count, default is 1
            repeat = int(count) if count else 1
            result.append(char * repeat)
            count = ""
    
    return "".join(result)