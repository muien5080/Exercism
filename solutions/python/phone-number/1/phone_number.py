import re

class PhoneNumber:
    def __init__(self, number):
        # 1. Check for letters
        if any(c.isalpha() for c in number):
            raise ValueError("letters not permitted")
        
        # 2. Check for unauthorized punctuation (anything not a digit, space, dot, dash, plus, or parens)
        # We allow specific symbols for now just to strip them, but others are "punctuation"
        if re.search(r"[^\d\s\.\-\+\(\)]", number):
            raise ValueError("punctuations not permitted")

        # 3. Strip all non-digit characters
        digits = "".join(filter(str.isdigit, number))

        # 4. Handle length and Country Code
        if len(digits) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits) > 11:
            raise ValueError("must not be greater than 11 digits")
        
        if len(digits) == 11:
            if not digits.startswith("1"):
                raise ValueError("11 digits must start with 1")
            # If valid country code, strip it to get the 10-digit number
            digits = digits[1:]

        # 5. Validate Area Code (First digit of the 10-digit number)
        if digits[0] == "0":
            raise ValueError("area code cannot start with zero")
        if digits[0] == "1":
            raise ValueError("area code cannot start with one")

        # 6. Validate Exchange Code (Fourth digit of the 10-digit number)
        if digits[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if digits[3] == "1":
            raise ValueError("exchange code cannot start with one")

        # Set the cleaned number as the number attribute
        self.number = digits

    @property
    def area_code(self):
        return self.number[:3]

    def pretty(self):
        """Formats the number as (NXX)-NXX-XXXX"""
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"