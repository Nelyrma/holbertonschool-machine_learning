#!/usr/bin/env python3
"""function that multiplies two matrices"""


def mat_mul(mat1, mat2):
    """multiply two matrices

    Args:
        mat1 : the first matrix
        mat2 : the second matrix

    Returns:
       a new matrix
    """
    if len(mat1[0]) != len(mat2):
        return None

    # initialise the result matrix
    result_matrix = [[0 for _ in range(len(mat2[0]))]
                     for _ in range(len(mat1))]

    # i : index column for mat1
    for i in range(len(mat1)):
        # j: index column for mat2
        for j in range(len(mat2[0])):
            # k: index line for mat2
            for k in range(len(mat2)):
                result_matrix[i][j] += mat1[i][k] * mat2[k][j]

    return result_matrix
