class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        # Remove spaces
        num = self.card_num.replace(" ", "")
        
        # Must be more than 1 digit and contain only digits
        if len(num) <= 1 or not num.isdigit():
            return False
        
        total = 0
        reverse_digits = num[::-1]
        
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            
            # Double every second digit (1-based index from right → i % 2 == 1)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            
            total += n
        
        return total % 10 == 0