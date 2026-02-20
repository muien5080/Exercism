def translate(text):
    vowels = ("a", "e", "i", "o", "u")
    
    def translate_word(word):
        # Rule 1
        if word.startswith(vowels) or word.startswith(("xr", "yt")):
            return word + "ay"
        
        index = 0
        
        while index < len(word):
            # Rule 3: "qu"
            if word[index:index+2] == "qu":
                index += 2
                break
            
            # vowel
            if word[index] in vowels:
                break
            
            # Rule 4: 'y' as vowel (not first letter)
            if word[index] == "y" and index != 0:
                break
            
            index += 1
        
        return word[index:] + word[:index] + "ay"
    
    return " ".join(translate_word(word) for word in text.split())