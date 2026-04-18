def recite(start_verse, end_verse):
    animals = [
        "fly", "spider", "bird", "cat",
        "dog", "goat", "cow", "horse"
    ]

    comments = {
        "spider": "It wriggled and jiggled and tickled inside her.",
        "bird": "How absurd to swallow a bird!",
        "cat": "Imagine that, to swallow a cat!",
        "dog": "What a hog, to swallow a dog!",
        "goat": "Just opened her throat and swallowed a goat!",
        "cow": "I don't know how she swallowed a cow!"
    }

    def build_chain(i):
        lines = []
        for j in range(i, 0, -1):
            curr = animals[j]
            prev = animals[j - 1]

            if curr == "bird" and prev == "spider":
                lines.append(
                    "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her."
                )
            else:
                lines.append(f"She swallowed the {curr} to catch the {prev}.")
        return lines

    result = []

    for i in range(start_verse - 1, end_verse):
        animal = animals[i]

        # Opening line
        result.append(f"I know an old lady who swallowed a {animal}.")

        # Special case: horse
        if animal == "horse":
            result.append("She's dead, of course!")
        else:
            # Comment line (if any)
            if animal in comments:
                result.append(comments[animal])

            # Cumulative chain
            if animal != "fly":
                result.extend(build_chain(i))

            # Ending line
            result.append("I don't know why she swallowed the fly. Perhaps she'll die.")

        # Blank line between verses (not after last)
        if i != end_verse - 1:
            result.append("")

    return result