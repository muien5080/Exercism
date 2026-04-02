def encode(numbers):
    result = []

    for number in numbers:
        if number == 0:
            result.append(0)
            continue

        chunks = []
        while number > 0:
            chunks.append(number & 0x7F)
            number >>= 7

        # Reverse to get most significant first
        chunks.reverse()

        # Set continuation bit (MSB) on all but last
        for i in range(len(chunks) - 1):
            result.append(chunks[i] | 0x80)
        result.append(chunks[-1])

    return result


def decode(bytes_):
    result = []
    current = 0
    has_data = False

    for byte in bytes_:
        has_data = True
        current = (current << 7) | (byte & 0x7F)

        # If MSB is not set → end of this number
        if (byte & 0x80) == 0:
            result.append(current)
            current = 0
            has_data = False

    # If we ended but still expecting continuation
    if has_data:
        raise ValueError("incomplete sequence")

    return result