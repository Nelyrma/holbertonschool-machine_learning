#!/usr/bin/env python3
"""function that calculates the derivate of a polynomial"""


def poly_derivative(poly):
    """calculate the derivate of a polynomial

    Args:
        poly:  list of coefficients representing a polynomial

    Returns:
        new list of coeff representing the derivative of the polynomial
    """
    # check if poly is a valid list
    if not poly or not isinstance(poly, list) \
            or not all(isinstance(coeff, (int, float)) for coeff in poly):
        return None

    # calculate the derivate
    derivate = [n * coeff for n, coeff in enumerate(poly[1:], start=1)]

    # return [0] if the derivate is 0
    if not derivate:
        return [0]

    return derivate
