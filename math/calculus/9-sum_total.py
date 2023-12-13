#!/usr/bin/env python3
"""Function that calculates the summation"""


def summation_i_squared(n):
    """calculate the summmation

    Args:
        n (_int_): the stopping condition

    Returns:
        _int_: _an integer value of the sum_
    """
    # check if n is a valid integer
    if n < 1 or not isinstance(n, int):
        return None

    # sum of square of n numbers
    return (n * (n + 1) * (2 * n + 1)) // 6
