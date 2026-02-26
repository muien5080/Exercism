def rotate(text, key):
    key = key % 26  # Normalize key to range 0–25
    result = []

    for char in text:
        if char.isalpha():
            # Determine base ASCII code depending on case
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap using modulo 26
            shifted = (ord(char) - base + key) % 26 + base
            result.append(chr(shifted))
        else:
            # Keep spaces and punctuation unchanged
            result.append(char)

    return ''.join(result)