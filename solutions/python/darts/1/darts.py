import math

def score(x, y):
    """Calculate points scored for a dart at coordinates (x, y)."""
    distance = math.hypot(x, y)  # Euclidean distance from center (0,0)
    
    if distance <= 1:
        return 10  # Inner circle (bullseye)
    elif distance <= 5:
        return 5   # Middle circle
    elif distance <= 10:
        return 1   # Outer circle
    else:
        return 0   # Miss