"""Calculator library containing basic math operations."""

import warnings
from typing import TypeVar
from toy_pkg._utils import fill_doc


T = TypeVar('T')


@fill_doc
def add(
    first_term: T,
    second_term: T,
    useless=None,
    useless2=None,
    verbose=None,
) -> T:
    """Add first and second term.

    This function adds ``first_term`` with ``second_term``.

    .. tip::
        When generating documentation locally, you can
        build only specific files to reduce building time.
        To do so, use the filename_pattern:

        .. code-block::

            python3 -m sphinx -D sphinx_gallery_conf.filename_pattern\\
            =plot_decoding_tutorial.py -b html -d _build/doctrees . _build/html

    Parameters
    ----------
    first_term : Number
        First term for the addition.

    second_term : Number
        Second term for the addition.

    useless : Number
        Useless parameter. Does nuthin.

        .. deprecated:: 0.0.3
           `useless` is deprecated in 0.0.3 and will be removed
           in 0.0.5.

    useless2 : Number
        Useless parameter.

        .. versionadded:: 0.0.3
    %(verbose)s

    Returns
    -------
    result : Number
        Result of the addition.

    See Also
    --------
    subtract : Subtraction.
    multiply : Multiplication.
    divide : Division.

    Notes
    -----
    Unrelated reference by :footcite:`Gensollen2020` for testing.
    Another ref to a website :footcite:`NicolasGensollen` for testing.

    References
    ----------
    .. footbibliography::

    Examples
    --------
    >>> add(1, 1)
    2
    >>> add(1, -1)
    0
    >>> add(0, 0)
    0
    """
    if useless is not None:
        warnings.warn(FutureWarning,
                      ("`useless` is deprecated in 0.0.3 "
                       "and will be removed in 0.0.5"))
    result = first_term + second_term
    if verbose:
        print(f"{first_term} + {second_term} = {result}")
    return result


@fill_doc
def subtract(first_term, second_term, verbose=None):
    """Subtract second term from first term.

    This function subtracts ``second_term`` from ``first_term``.

    .. epigraph::

        Try epigraph for fun...

    Parameters
    ----------
    first_term : Number
        First term for the subtraction.

    second_term : Number
        Second term for the subtraction.
    %(verbose)s

    Returns
    -------
    result : Number
        Result of the subtraction.

    See Also
    --------
    subtract : Subtraction.
    multiply : Multiplication.
    divide : Division.

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
    if verbose:
        print(f"{first_term} - {second_term} = {result}")
    return result


def multiply(
    first_term: T,
    second_term: T,
) -> T:
    """Multiply first term by second term.

    This function multiplies ``first_term`` with ``second_term``.

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
    add : Addition.
    subtract : Subtraction.
    divide : Division.

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

    This function divides ``first_term`` by ``second_term``.

    Parameters
    ----------
    first_term : Number
        First term for the division.

    second_term : Number
        Second term for the division.

        .. warning::
            Should not be zero!

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
    add : Addition.
    subtract : Subtraction.
    multiply : Multiplication.

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


def power(term, exponent):
    """Raise term to exponent.

    This function raises ``term`` to ``exponent``.

    Parameters
    ----------
    term : Number
        Term to be raised.

    exponent : int
        Exponent.

    Returns
    -------
    result : Number
        Result of the operation.

    Raises
    ------
    ValueError
        If exponent is not an integer.

    See Also
    --------
    add : Addition
    subtract : Subtraction
    multiply : Multiplication
    divide : Division

    Examples
    --------
    >>> power(1, 1)
    1
    >>> power(2, 2)
    4
    >>> power(4, 2)
    16
    >>> power(10, 2)
    100
    >>> power(100, 1)
    100
    >>> power(10, 3)
    1000
    """
    if not isinstance(exponent, int):
        raise ValueError("Exponent should be an integer. "
                         "You provided {}.".format(
                             type(exponent)
                         ))
    result = term**exponent
    return result
