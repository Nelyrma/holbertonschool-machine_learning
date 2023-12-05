#!/usr/bin/env python3
"""the function calculates the shape of a matrix"""

def matrix_shape(matrix):
    if not matrix or not isinstance(matrix, list):
        return []

    # rows = len(matrix)
    columns = matrix_shape(matrix[0])
    return [len(matrix)] + columns
