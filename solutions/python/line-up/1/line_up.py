def line_up(name, number):
    # Determine ordinal suffix
    if 10 <= number % 100 <= 13:
        suffix = "th"
    else:
        last_digit = number % 10
        if last_digit == 1:
            suffix = "st"
        elif last_digit == 2:
            suffix = "nd"
        elif last_digit == 3:
            suffix = "rd"
        else:
            suffix = "th"

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"