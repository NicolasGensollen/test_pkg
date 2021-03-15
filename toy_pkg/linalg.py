"""Matrix operations"""

import numpy as np

def dot(A, B):
    """Dot product of matrix A with matrix B.

    Parameters
    ----------
    A : ndarray
        First matrix of the dot product.

    B : ndarray
        Second matrix of the dot product.

    Returns
    -------
    result : ndarray
        Result of the dot product.

    Examples
    --------
    >>> dot(np.array([[1,0],[0,1]]), np.array([[1,1],[1,1]]))
    array([[1, 1],
           [1, 1]])

    See Also
    --------

    """
    if(not isinstance(A, np.ndarray) or
       not isinstance(B, np.ndarray)):
        raise TypeError("Dot function expects numpy arrays as inputs.")
    result = np.dot(A, B)
    return result


def outer(A, B):
    """Outer product of vector A with vector B.

    Parameters
    ----------
    A : ndarray
        First vector of the outer product.

    B : ndarray
        Second vector of the outer product.

    Returns
    -------
    result : ndarray
        Result of the outer product.

    Examples
    --------
    >>> x = np.array(['a', 'b', 'c'], dtype=object)
    >>> outer(x, [1, 2, 3])
    array([['a', 'aa', 'aaa'],
           ['b', 'bb', 'bbb'],
           ['c', 'cc', 'ccc']], dtype=object)

    See Also
    --------

    """
    result = np.outer(A, B)
    return result


def inner(A, B):
    """Inner product of matrix A with matrix B.

    Parameters
    ----------
    A : ndarray
        First matrix of the inner product.

    B : ndarray
        Second matrix of the inner product.

    Returns
    -------
    result : ndarray
        Result of the inner product.

    Examples
    --------
    >>> inner(np.array([1,2,3]), np.array([0,1,0]))
    2

    See Also
    --------

    """
    if(not isinstance(A, np.ndarray) or
       not isinstance(B, np.ndarray)):
        raise TypeError("Inner function expects numpy arrays as inputs.")
    result = np.inner(A, B)
    return result


def power(A, p):
    """Raise a square matrix A to the power p.

    Parameters
    ----------
    A : ndarray
        Square matrix to be elevated.

    p : int
        Exponent.

    Returns
    -------
    result : ndarray
        Matrix A to the power p.

    Examples
    --------
    >>> i = np.array([[0, 1], [-1, 0]])
    >>> power(i, 3)
    array([[ 0, 1],
           [-1, 0]])

    See Also
    --------

    """
    result = np.power(A, p)
    return result
