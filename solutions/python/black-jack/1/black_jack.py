"""Functions to help play and score a game of blackjack."""
    

def value_of_card(card):
    """Determine the scoring value of a card."""
    if card in ['J', 'Q', 'K']:
        return 10
    if card == 'A':
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    if value_two > value_one:
        return card_two
    return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card."""
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    # If there is already an ace in hand, the new ace must be 1
    if card_one == 'A' or card_two == 'A':
        return 1

    # Otherwise choose 11 if it doesn't bust (go over 21)
    if value_one + value_two + 11 <= 21:
        return 11
    return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a blackjack."""
    ten_cards = ['10', 'J', 'Q', 'K']

    return (
        (card_one == 'A' and card_two in ten_cards) or
        (card_two == 'A' and card_one in ten_cards)
    )


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can double down."""
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in [9, 10, 11]