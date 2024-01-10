#!/usr/bin/env python3
"""function that calculates the integral of a polynomial"""


def poly_integral(poly, C=0):
    """calculate the integral of a polynomial

    Args:
        poly : list of coefficients representing a polynomial
        C : integer representing the integration constant

    Returns:
        list : a new list of coefficients representing the integral of the polynomial
    """
    # verify if poly is a valid list and C an integer 
    if not poly or not isinstance(poly, list) \
            or not all(isinstance(coeff, (int, float)) for coeff in poly) \
            or not isinstance(C, int):
        return None
    
    # particular case: if poly is [0], the integral is [C]
    elif poly == [0]:
        return [float(C)]
    
    else:
        # Calculate the integral of the polynome
        # The integration formula for xn est x^(n+1)/(n+1) + C
        integral_coeff = [poly[idx] / (idx + 1) for idx in range(0, len(poly))]

        # Insert C at the beginning of the list
        integral_coeff.insert(0, float(C))

        # Return an integer if it is an integer, otherwise a float
        return [float(coeff) if not coeff.is_integer() else int(coeff)
                for coeff in integral_coeff]
