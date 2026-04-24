def proverb(*items, qualifier=None):
    if not items:
        return []

    lines = []

    # Build the main proverb lines using consecutive pairs
    for first, second in zip(items, items[1:]):
        lines.append(f"For want of a {first} the {second} was lost.")

    # Build the final line
    first_item = items[0]
    if qualifier:
        lines.append(f"And all for the want of a {qualifier} {first_item}.")
    else:
        lines.append(f"And all for the want of a {first_item}.")

    return lines