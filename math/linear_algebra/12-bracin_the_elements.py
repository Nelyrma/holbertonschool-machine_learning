#!/usr/bin/env python3
"""that performs element-wise addition, subtraction, multiplication,
and division"""

def np_elementwise(mat1, mat2):
    """perform addition, subtraction, multiplication, and division

    Args:
        mat1 : the first matrix
        mat2 : the second matrix

    Returns:
        a tuple containingsum, difference, product, and quotient
    """
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
