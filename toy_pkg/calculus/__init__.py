"""
Functions to perform computations.
"""

from .calculator import (add, subtract,
                         multiply, divide)

from .lazy_calculator import (lazy_add, lazy_subtract,
                              lazy_multiply, lazy_divide)

from .linalg import dot, outer, inner, power

__all__ = ['add', 'subtract', 'multiply','divide', 'lazy_add',
           'lazy_subtract', 'lazy_multiply','lazy_divide',
           'dot', 'outer', 'inner', 'power']
