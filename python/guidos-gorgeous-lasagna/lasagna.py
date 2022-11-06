"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
TIME_PER_LAYER = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Does something bla bla
    :param number_of_layers:
    :return:
    """
    return TIME_PER_LAYER * number_of_layers


def elapsed_time_in_minutes(numbers_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time
    Bla Bla Bla
    :param numbers_of_layers:
    :param elapsed_bake_time:
    :return:
    """
    return preparation_time_in_minutes(numbers_of_layers) + elapsed_bake_time
