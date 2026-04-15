def recite(start, take=1):
    def number_to_word(n):
        words = {
            10: "Ten", 9: "Nine", 8: "Eight", 7: "Seven",
            6: "Six", 5: "Five", 4: "Four", 3: "Three",
            2: "Two", 1: "One", 0: "No"
        }
        return words[n]

    verses = []

    for i in range(start, start - take, -1):
        current = number_to_word(i)
        next_num = i - 1
        next_word = number_to_word(next_num)

        bottle = "bottle" if i == 1 else "bottles"
        next_bottle = "bottle" if next_num == 1 else "bottles"

        verse = [
            f"{current} green {bottle} hanging on the wall,",
            f"{current} green {bottle} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {next_word.lower()} green {next_bottle} hanging on the wall."
        ]

        verses.extend(verse)

        if i != start - take + 1:
            verses.append("")  # blank line between verses

    return verses
    