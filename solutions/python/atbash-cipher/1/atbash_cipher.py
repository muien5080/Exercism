import string

# Create Atbash mapping
alphabet = string.ascii_lowercase
reversed_alphabet = alphabet[::-1]
atbash_map = {a: b for a, b in zip(alphabet, reversed_alphabet)}

def encode(text):
    result = []
    
    for char in text.lower():
        if char.isalpha():
            result.append(atbash_map[char])
        elif char.isdigit():
            result.append(char)
        # ignore punctuation
    
    # group into chunks of 5
    grouped = []
    for i in range(0, len(result), 5):
        grouped.append("".join(result[i:i+5]))
    
    return " ".join(grouped)


def decode(text):
    result = []
    
    for char in text.lower():
        if char.isalpha():
            result.append(atbash_map[char])
        elif char.isdigit():
            result.append(char)
        # ignore spaces and punctuation
    
    return "".join(result)


# Examples
print(encode("test"))  
# gvhg

print(encode("x123 yes"))  
# c123b vh

print(decode("gvhg"))  
# test

print(decode("gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"))  
# thequickbrownfoxjumpsoverthelazydog