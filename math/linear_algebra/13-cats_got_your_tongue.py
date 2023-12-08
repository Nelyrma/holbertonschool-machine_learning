#!/usr/bin/env python3
"""function that concatenates two matrices
along a specific axis"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """concatenate two matrices along a specific axis

    Args:
        mat1 : the first matrix
        mat2 : the second matrix
        axis : axis along which is perfomed the concatenation

    Returns:
        a new matrix
    """
    result = np.concatenate((mat1, mat2), axis=axis)
    return result
