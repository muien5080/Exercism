import random
import string

class Cipher:
    def __init__(self, key=None):
        if key is None:
            # Generate random key of at least 100 lowercase letters
            self.key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
        else:
            if not key.islower() or not key.isalpha():
                raise ValueError("Key must be lowercase alphabetic characters only.")
            self.key = key

    def encode(self, text):
        return self._transform(text, mode="encode")

    def decode(self, text):
        return self._transform(text, mode="decode")

    def _transform(self, text, mode):
        result = []
        key_length = len(self.key)

        for i, char in enumerate(text):
            if not char.islower():
                raise ValueError("Text must be lowercase alphabetic characters only.")

            shift = ord(self.key[i % key_length]) - ord('a')

            if mode == "encode":
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:  # decode
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

            result.append(new_char)

        return ''.join(result)