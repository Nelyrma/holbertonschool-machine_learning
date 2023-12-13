#!/usr/bin/env python3
"""function that calculates the derivate of a polynomial"""


def poly_derivative(poly):
    """calculate the derivate of a polynomial

    Args:
        poly:  list of coefficients representing a polynomial

    Returns:
        new list of coeff representing the derivative of the polynomial
    """
    #check if poly is a valid list
    if not isinstance(poly, list):
        return None

    # Check the length of the polynomial
    if len(poly) < 2:
        return None

    #calculate the derivate
    derivate = [i * poly[i] for i in range(1, len(poly))]

    # return [0] if the derivate is 0
    if all(coeff == 0 for coeff in derivate):
        return [0]

    return derivate
