"""
Slow example
============

This example also runs useless computations but mimics
a very slow example by using the lazy versions of the
calculator module.
"""

#########################################################
# Load functions
from toy_pkg.calculus import lazy_multiply, lazy_divide

#########################################################
# Perform long computations

# Perform 1 * 1 and sleep for 1 minute...
result = lazy_multiply(1, 1, 60)
print(result)

# Perform 10 / 5 and sleep for 1 minute...
result = lazy_divide(10, 5, 60)
print(result)

# Perform 10 * 42 and sleeps for 1 minutes...
print(lazy_multiply(10, 42, 60))
