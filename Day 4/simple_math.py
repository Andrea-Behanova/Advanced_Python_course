"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    The sum of two numbers.

    Parameters
    ----------
    a : float
    First number for sum.
    b : float
    Second number for sum.

    Returns
    -------
    a+b
    The sum of a and b.

    Examples
    --------
    >>> simple_add(4,7)
    >>> 11
    >>> simple_add(2,5)
    >>> 7
    """
    return a+b

def simple_sub(a,b):
    """
    The Subtraction of two numbers.

    Parameters
    ----------
    a : float
    Minuend
    b : float
    Subtrahend

    Returns
    -------
    a-b
    The difference of a and b.
    Examples
    --------
    >>> simple_sub(8.5,3)
    >>> 5.5
    >>> simple_sub(5,7)
    >>> -2
    """
    return a-b

def simple_mult(a,b):
    """
    The multiplication of two numbers.

    Parameters
    ----------
    a : float
    Multiplicant
    b : float
    Multiplier

    Returns
    -------
    a*b
    The product of a and b.
    Examples
    --------
    >>> simple_mult(2,4)
    >>> 8
    >>> simple_mult(3,7)
    >>> 21
    """
    return a*b

def simple_div(a,b):
    """
    The division of two numbers.

    Parameters
    ----------
    a : float
    Divident
    b : float
    Divisor

    Returns
    -------
    a/b
    The result of division of a by b.
    Examples
    --------
    >>> simple_mult(8,4)
    >>> 2
    >>> simple_mult(9,3)
    >>> 3
    """
    return a/b

def poly_first(x, a0, a1):
    """
    Linear polynomial equation.

    Parameters
    ----------
    x : float
    Independent variable
    a0 : float
    Intercept
    a1 : float
    Slope

    Returns
    -------
    The result of linear polynomial equation a0 + a1*x.
    Examples
    --------
    >>> simple_mult(3, 1, 2)
    >>> 7
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    Quadratic polynomial equation.

    Parameters
    ----------
    x : float
    Independent variable
    a0 : float
    Intercept
    a1 : float
    Slope
    a1 : float
    Vertex

    Returns
    -------
    The result of quadratic polynomial equation a0 + a1*x + a2*(x**2).
    Examples
    --------
    >>> simple_mult(2, 5, 3, 1)
    >>> 15
    """
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
