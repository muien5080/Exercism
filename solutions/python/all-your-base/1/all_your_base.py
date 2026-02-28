def rebase(input_base, digits, output_base):
    # Validate bases
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    # Validate digits
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    # Convert input digits to base 10
    value = 0
    for d in digits:
        value = value * input_base + d

    # Special case: zero
    if value == 0:
        return [0]

    # Convert base 10 value to output base
    result = []
    while value > 0:
        result.append(value % output_base)
        value //= output_base

    return result[::-1]