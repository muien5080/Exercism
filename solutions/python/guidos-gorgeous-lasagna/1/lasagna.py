# Constant for expected bake time (in minutes)
EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining bake time.

    :param elapsed_bake_time: int - time already spent baking (in minutes).
    :return: int - remaining bake time (in minutes).

    Subtracts the elapsed bake time from the expected bake time.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time based on number of layers.

    :param number_of_layers: int - number of layers in the lasagna.
    :return: int - preparation time in minutes.

    Assumes each layer takes 2 minutes to prepare.
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - time already spent baking (in minutes).
    :return: int - total time elapsed (in minutes) preparing and cooking.

    Combines preparation time and elapsed bake time to get total time spent.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
