"""Calculator library containing basic math operations."""


def add(first_term, second_term):
    """Add first and second term.

    Parameters
    ----------
    first_term : Number
        First term for the addition.

    second_term : Number
        Second term for the addition.

    Returns
    -------
    result : Number
        Result of the addition.

    Examples
    --------
    >>> add(1, 1)
    2
    >>> add(1, -1)
    0
    >>> add(0, 0)
    0

    See Also
    --------
    subtract : Subtraction
    multiply : Multiplication
    divide : Division

    """
    result = first_term + second_term
    return result


def subtract(first_term, second_term):
    """Subtract second term from first term.

    Parameters
    ----------
    first_term : Number
        First term for the subtraction.

    second_term : Number
        Second term for the subtraction.

    Returns
    -------
    result : Number
        Result of the subtraction.

    See Also
    --------
    subtract : Subtraction
    multiply : Multiplication
    divide : Division

    Examples
    --------
    >>> subtract(1, 1)
    0
    >>> subtract(1, -1)
    2
    >>> subtract(0, 0)
    0

    """
    result = first_term - second_term
    return result


def multiply(first_term, second_term):
    """Multiply first term by second term.

    Parameters
    ----------
    first_term : Number
        First term for the multiplication.

    second_term : Number
        Second term for the multiplication.

    Returns
    -------
    result : Number
        Result of the multiplication.

    See Also
    --------
    add : Addition
    subtract : Subtraction
    divide : Division

    Examples
    --------
    >>> multiply(1, 1)
    1
    >>> multiply(1, -1)
    -1
    >>> multiply(0, 0)
    0

    """
    result = first_term * second_term
    return result

def divide(first_term, second_term):
    """Divide first term by second term.

    Parameters
    ----------
    first_term : Number
        First term for the division.

    second_term : Number
        Second term for the division.

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
    add : Addition
    subtract : Subtraction
    multiply : Multiplication

    Examples
    --------
    >>> divide(1, 1)
    1.0
    >>> divide(1, -1)
    -1.0
    >>> divide(4, 2)
    2.0
    >>> divide(1, 2)
    0.5
    """
    result = first_term / second_term
    return result

