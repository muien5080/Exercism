def label(colors):
    """Return the resistance value of a 3-band resistor as a string with units."""
    
    digit_map = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }
    
    # Main value: first two digits
    main_value = digit_map[colors[0]] * 10 + digit_map[colors[1]]
    
    # Multiply by 10^third_band
    total_value = main_value * (10 ** digit_map[colors[2]])
    
    # Determine unit and divide appropriately
    if total_value >= 1_000_000_000:
        value = total_value / 1_000_000_000
        unit = "gigaohms"
    elif total_value >= 1_000_000:
        value = total_value / 1_000_000
        unit = "megaohms"
    elif total_value >= 1_000:
        value = total_value / 1_000
        unit = "kiloohms"
    else:
        value = total_value
        unit = "ohms"
    
    # Format number and remove unnecessary trailing zeros
    value_str = f"{value:.12g}"  # general format
    return f"{value_str} {unit}"