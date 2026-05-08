from collections import Counter

# Score categories constants
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def score(dice, category):
    counts = Counter(dice)
    dice_sorted = sorted(dice)
    
    # Number-based categories (1-6)
    if ONES <= category <= SIXES:
        return counts[category] * category
    
    # Yacht: All five dice the same
    if category == YACHT:
        return 50 if len(counts) == 1 else 0
    
    # Full House: Three of one kind and two of another
    if category == FULL_HOUSE:
        if len(counts) == 2 and 3 in counts.values():
            return sum(dice)
        return 0
    
    # Four of a Kind: At least four dice showing the same face
    if category == FOUR_OF_A_KIND:
        for val, count in counts.items():
            if count >= 4:
                return val * 4
        return 0
    
    # Little Straight: 1-2-3-4-5
    if category == LITTLE_STRAIGHT:
        return 30 if dice_sorted == [1, 2, 3, 4, 5] else 0
    
    # Big Straight: 2-3-4-5-6
    if category == BIG_STRAIGHT:
        return 30 if dice_sorted == [2, 3, 4, 5, 6] else 0
    
    # Choice: Simple sum of all dice
    if category == CHOICE:
        return sum(dice)
    
    return 0