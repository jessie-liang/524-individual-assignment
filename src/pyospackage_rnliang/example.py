"""
A module that calculates the normal PDF value at a given location.
"""

import math

def normal_pdf_value(mu, sigma, x):
    """
    Return the PDF value of a custom normal distribution at a particular x.

    Parameters
    ----------
    mu : float
        The mean of the normal distribution
    sigma : float
        The standard deviation of the normal distribution
    x : float
        The x-value at which you want to evaluate the normal PDF value

    Returns
    -------
    float
        The PDF value of the given normal distribution

    Examples
    --------
    >>> normal_pdf_value(0, 1, 1)
    0.2419707245
    >>> normal_pdf_value(1, 0.5, 1.5)
    0.483941449

    """
    constant = 1 / (sigma * math.sqrt(2 * math.pi))
    exponential = math.exp(-1/2 * ((x - mu) / sigma) ** 2)

    return constant * exponential
