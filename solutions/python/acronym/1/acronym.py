import re

def abbreviate(words):
    # Replace hyphens with spaces
    words = words.replace('-', ' ')
    
    # Remove all non-letter characters except spaces
    words = re.sub(r'[^A-Za-z\s]', '', words)
    
    # Split into words and take first letters
    acronym = ''.join(word[0].upper() for word in words.split())
    
    return acronym