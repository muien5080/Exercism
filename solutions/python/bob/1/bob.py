def response(hey_bob):
    # Remove leading/trailing whitespace
    hey_bob = hey_bob.strip()
    
    # Silence
    if hey_bob == "":
        return "Fine. Be that way!"
    
    # Question
    is_question = hey_bob.endswith("?")
    
    # Yelling (has letters and all letters are uppercase)
    has_letters = any(char.isalpha() for char in hey_bob)
    is_yelling = has_letters and hey_bob.isupper()
    
    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    else:
        return "Whatever."