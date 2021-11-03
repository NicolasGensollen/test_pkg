"""Calculator library containing basic math operations.

The following functions do the same things as the functions
in calculator but sleep for some time before returning the
results...

Authors: Nicolas Gensollen

"""

import time
from toy_pkg.calculus import (add, subtract,
                              multiply, divide)


def lazy_add(first_term, second_term, secs=0):
    """Lazy add first and second term.

    Add the terms using :func:`toy_pkg.calculus.add`
    and sleep for the provided number of seconds.

    Parameters
    ----------
    first_term : Number
        First term for the addition.

    second_term : Number
        Second term for the addition.

    secs : int, optional
        Number of seconds to sleep.
        Default=0.

    Returns
    -------
    result : Number
        Result of the addition.

    Examples
    --------
    >>> lazy_add(1, 1)
    2
    >>> lazy_add(1, -1, 2)
    0
    >>> lazy_add(0, 0, 10)
    0

    See Also
    --------
    lazy_subtract : Subtraction
    lazy_multiply : Multiplication
    lazy_divide : Division

    """
    result = add(first_term, second_term)
    time.sleep(secs)
    return result


def lazy_subtract(first_term, second_term, secs=0):
    """Subtract second term from first term.

    Subtract the terms using :func:`toy_pkg.calculus.subtract`
    and sleep for the provided number of seconds.

    Parameters
    ----------
    first_term : Number
        First term for the subtraction.

    second_term : Number
        Second term for the subtraction.

    secs : int, optional
        Number of seconds to sleep.
        Default=0.

    Returns
    -------
    result : Number
        Result of the subtraction.

    See Also
    --------
    lazy_add : Addition
    lazy_multiply : Multiplication
    lazy_divide : Division

    Examples
    --------
    >>> lazy_subtract(1, 1)
    0
    >>> lazy_subtract(1, -1, 1)
    2
    >>> lazy_subtract(0, 0, 4)
    0

    """
    result = subtract(first_term, second_term)
    time.sleep(secs)
    return result


def lazy_multiply(first_term, second_term, secs=0):
    """Multiply first term by second term.

    Multiply the terms using :func:`toy_pkg.calculus.multiply`
    and sleep for the provided number of seconds.

    Parameters
    ----------
    first_term : Number
        First term for the multiplication.

    second_term : Number
        Second term for the multiplication.

    secs : int, optional
        Number of seconds to sleep.
        Default=0.

    Returns
    -------
    result : Number
        Result of the multiplication.

    See Also
    --------
    lazy_add : Addition
    lazy_subtract : Subtraction
    lazy_divide : Division

    Examples
    --------
    >>> lazy_multiply(1, 1)
    1
    >>> lazy_multiply(1, -1, 3)
    -1
    >>> lazy_multiply(0, 0, 5)
    0

    """
    result = multiply(first_term, second_term)
    time.sleep(secs)
    return result


def lazy_divide(first_term, second_term, secs=0):
    """Divide first term by second term.

    Divide the terms using :func:`toy_pkg.calculus.divide`
    and sleep for the provided number of seconds.

    Parameters
    ----------
    first_term : Number
        First term for the division.

    second_term : Number
        Second term for the division.

    secs : int, optional
        Number of seconds to sleep.
        Default=0.

    Returns
    -------
    result : Number
        Result of the division.

    Raises
    ------
    ZeroDivisionError
        If second term is equal to zero.

    See Also
    --------
    lazy_add : Addition
    lazy_subtract : Subtraction
    lazy_multiply : Multiplication

    Examples
    --------
    >>> lazy_divide(1, 1)
    1.0
    >>> lazy_divide(1, -1, 1)
    -1.0
    >>> lazy_divide(4, 2, 0)
    2.0
    >>> lazy_divide(1, 2, 11)
    0.5

    """
    result = divide(first_term, second_term)
    time.sleep(secs)
    return result

