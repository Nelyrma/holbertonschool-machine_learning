#!/usr/bin/env python3
"""function that multiplies matrix"""
import numpy as np


def np_matmul(mat1, mat2):
    """perform matrix multiplication

    Args:
        mat1 : the first matrix
        mat2 : the second matrix

    Returns:
        a new matrix
    """
    result = np.matmul(mat1, mat2)
    return result
