"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    list = [number, number+1, number+2]
    return list


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1+rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    for i in range(len(rounds)):
        if number == rounds[i]:
            return True
    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    return sum(hand)/len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    actual_average = sum(hand) / len(hand)
    
    # Strategy 1: Average of first and last card
    first_last_average = (hand[0] + hand[-1]) / 2
    
    # Strategy 2: Median (middle card)
    # The hand is already sorted based on the examples and prompt context
    median = hand[len(hand) // 2]
    
    # Return True if either strategy matches the actual average
    return (first_last_average == actual_average) or (median == actual_average)

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    e = hand[0::2]
    o = hand[1::2]
    se = sum(e)/len(e)
    so = sum(o)/len(o)
    return so==se

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    n = len(hand)
    if hand[n-1] == 11:
        hand[n-1] = 22
    return hand