def encode(message, rails):
    if rails == 1 or rails >= len(message):
        return message

    fence = ['' for _ in range(rails)]
    rail = 0
    direction = 1  # 1 = down, -1 = up

    for char in message:
        fence[rail] += char
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    return ''.join(fence)


def decode(encoded_message, rails):
    if rails == 1 or rails >= len(encoded_message):
        return encoded_message

    # Step 1: Create zig-zag pattern with placeholders
    pattern = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for _ in encoded_message:
        pattern[rail].append(None)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    # Step 2: Fill the pattern row by row with encoded message
    index = 0
    for r in range(rails):
        for c in range(len(pattern[r])):
            pattern[r][c] = encoded_message[index]
            index += 1

    # Step 3: Read in zig-zag order to reconstruct message
    result = []
    rail = 0
    direction = 1
    positions = [0] * rails

    for _ in encoded_message:
        result.append(pattern[rail][positions[rail]])
        positions[rail] += 1

        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    return ''.join(result)