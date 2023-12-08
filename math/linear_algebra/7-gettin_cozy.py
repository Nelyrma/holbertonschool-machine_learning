#!/usr/bin/env python3
"""function that concatenates two matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """concatenates 2 arrays along a specific axis

    Args:
        mat1 : the first matrix
        mat2 : the second matrix
        axis : matrix on which the concatenation is perfomed
    Returns:
        a new matrix
    """
    if not mat1 or not mat2:
        return None

    if axis == 0:
        return mat1 + mat2
    elif axis == 1:
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None
