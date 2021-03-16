"""
Slow example
============

This example also runs useless computations but mimics
a very slow example by using the lazy versions of the
calculator module.
"""

#########################################################
# Load functions
from toy_pkg.lazy_calculator import lazy_add, lazy_subtract

#########################################################
# Perform long computations

# Perform 1 + 1 and sleep for 2 minutes...
result = lazy_add(1, 1, 2 * 60)
print(result)

# Perform 10 - 7 and sleep for 1 minute...
result = lazy_subtract(10, 7, 60)
print(result)

# Perform 20 + 42 and sleeps for 3 minutes...
print(lazy_add(20, 42, 3 * 60))
