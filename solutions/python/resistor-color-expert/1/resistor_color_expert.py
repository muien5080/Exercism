def resistor_label(colors):
    digit_map = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }

    tolerance_map = {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%"
    }

    # 1-band resistor
    if len(colors) == 1:
        return "0 ohms"

    # 4-band resistor
    if len(colors) == 4:
        value_digits = digit_map[colors[0]] * 10 + digit_map[colors[1]]
        multiplier = 10 ** digit_map[colors[2]]
        tolerance = tolerance_map[colors[3]]

    # 5-band resistor
    elif len(colors) == 5:
        value_digits = (
            digit_map[colors[0]] * 100 +
            digit_map[colors[1]] * 10 +
            digit_map[colors[2]]
        )
        multiplier = 10 ** digit_map[colors[3]]
        tolerance = tolerance_map[colors[4]]

    total_value = value_digits * multiplier

    # Format units with proper significant digits
    if total_value >= 1_000_000:
        value_str = f"{total_value / 1_000_000:.12g} megaohms"
    elif total_value >= 1_000:
        value_str = f"{total_value / 1_000:.12g} kiloohms"
    else:
        value_str = f"{total_value:.12g} ohms"

    return f"{value_str} ±{tolerance}"