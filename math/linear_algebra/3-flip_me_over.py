#!/usr/bin/env python3
"""the function returns the transpose of a matrix"""


def transpose_matrix(matrix):
    """return the traspose of a 2D matrix

    Args:
        matrix: the matrix to transpose

    Returns:
        a a transposed matrix
    """
    #initializing the transpose
    matrix_transpose = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix_transpose[j][i] = matrix[i][j]

    return matrix_transpose
