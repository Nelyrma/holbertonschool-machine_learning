#!/usr/bin/env python3
"""function that adds two arrays"""


def add_arrays(arr1, arr2):
    """add_arrays: function that adds two arrays

    Args:
        arr1 : the first array to add
        arr2 : the second array to add

    Returns:
        a new list
    """
    # check if the two arrays have the same shape
    if len(arr1) != len(arr2):
        return None

    # adding the two arrays
    result = [a + b for a, b in zip(arr1, arr2)]
    return result
