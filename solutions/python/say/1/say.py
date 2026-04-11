def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    ones = [
        "", "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine"
    ]
    teens = [
        "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    tens = [
        "", "", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"
    ]

    def words_under_1000(n):
        result = []

        if n >= 100:
            result.append(ones[n // 100] + " hundred")
            n %= 100

        if n >= 20:
            result.append(tens[n // 10] + ("-" + ones[n % 10] if n % 10 else ""))
        elif n >= 10:
            result.append(teens[n - 10])
        elif n > 0:
            result.append(ones[n])

        return " ".join(result)

    parts = []
    billions = number // 1_000_000_000
    millions = (number // 1_000_000) % 1000
    thousands = (number // 1_000) % 1000
    remainder = number % 1000

    if billions:
        parts.append(words_under_1000(billions) + " billion")
    if millions:
        parts.append(words_under_1000(millions) + " million")
    if thousands:
        parts.append(words_under_1000(thousands) + " thousand")
    if remainder:
        parts.append(words_under_1000(remainder))

    return " ".join(parts)