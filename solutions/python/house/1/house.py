def recite(start_verse, end_verse):
    parts = [
        ("the house that Jack built.", ""),
        ("the malt", "that lay in"),
        ("the rat", "that ate"),
        ("the cat", "that killed"),
        ("the dog", "that worried"),
        ("the cow with the crumpled horn", "that tossed"),
        ("the maiden all forlorn", "that milked"),
        ("the man all tattered and torn", "that kissed"),
        ("the priest all shaven and shorn", "that married"),
        ("the rooster that crowed in the morn", "that woke"),
        ("the farmer sowing his corn", "that kept"),
        ("the horse and the hound and the horn", "that belonged to"),
    ]

    verses = []

    for verse_num in range(start_verse, end_verse + 1):
        line_parts = []
        subject, _ = parts[verse_num - 1]
        line_parts.append(f"This is {subject}")

        for i in range(verse_num - 1, 0, -1):
            prev_subject, connector = parts[i]
            earlier_subject, _ = parts[i - 1]
            line_parts.append(f"{connector} {earlier_subject}")

        verse = " ".join(line_parts)
        verses.append(verse)

    return verses