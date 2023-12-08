#!/usr/bin/env python3
"""function that ads two matrix element-wise"""


matrix_shape = __import__('2-size_me_please').matrix_shape


def add_matrices2D(mat1, mat2):
    """adds two matrix

    Args:
        mat1 : the first matrix
        mat2 : the second matrix

    Returns:
        a new matrix
    """
    shape_mat1 = matrix_shape(mat1)
    shape_mat2 = matrix_shape(mat2)

    if shape_mat1 != shape_mat2:
        return None

    # Initialize a matrix for the result of the sum
    result = []

    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            sum_elt = mat1[i][j] + mat2[i][j]
            row.append(sum_elt)

        result.append(row)

    return result
