#!/usr/bin/env python3
"""the function returns the transpose of a matrix"""


def matrix_transpose(matrix):
    """return the traspose of a 2D matrix

    Args:
        matrix: the matrix to transpose

    Returns:
        a a transposed matrix
    """
    # initializing the transpose
    transpose =[[0 for _ in range(len(matrix))]
                for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transpose[j][i] = matrix[i][j]

    return transpose
