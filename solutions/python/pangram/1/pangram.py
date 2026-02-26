import string

def is_pangram(sentence):
    sentence = sentence.lower()
    letters = set(sentence)
    return all(char in letters for char in string.ascii_lowercase)