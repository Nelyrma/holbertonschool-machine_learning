#!/usr/bin/env python3
"""the function calculates the shape of a matrix"""


def matrix_shape(matrix):
    """calculate the shape of a matrix

    Args:
        matrix: matrix for which to calcute the shape

    Returns:
        list of integers
    """
    if not matrix or not isinstance(matrix, list):
        return []

    # rows = len(matrix)
    columns = matrix_shape(matrix[0])
    return [len(matrix)] + columns
