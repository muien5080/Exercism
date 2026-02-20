"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix."""
    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string
    with the prefix followed by the words with prefix prepended.
    """
    prefix = vocab_words[0]
    # Apply prefix to each word after the first element
    prefixed_words = [prefix + word for word in vocab_words[1:]]
    
    # Combine prefix and new words
    return " :: ".join([prefix] + prefixed_words)


def remove_suffix_ness(word):
    """Remove the suffix 'ness' while keeping spelling in mind."""
    root = word[:-4]  # Remove 'ness'
    
    # If word ended with consonant + 'y' originally,
    # it became 'i' before adding 'ness'
    if root.endswith("i"):
        return root[:-1] + "y"
    
    return root


def adjective_to_verb(sentence, index):
    """Extract adjective from sentence and add 'en' suffix."""
    words = sentence.split()
    
    # Remove trailing punctuation like '.' or '!'
    word = words[index].rstrip(".,!?")
    
    return word + "en"