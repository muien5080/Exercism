import re
from collections import Counter

def count_words(sentence):
    # Match words with optional internal apostrophes (for contractions)
    words = re.findall(r"[a-zA-Z0-9]+(?:'[a-zA-Z0-9]+)*", sentence.lower())
    return dict(Counter(words))