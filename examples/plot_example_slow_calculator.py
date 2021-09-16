"""
Slow example
============

This example also runs useless computations but mimics
a slow example by using the lazy versions of the calculator
module.

Athor: Nicolas Gensollen
"""

#########################################################
# Load functions
from toy_pkg.calculus import lazy_add, lazy_subtract

#########################################################
# Perform some relatively long computations

# Perform 1 + 1 and sleep for 10 seconds...
result = lazy_add(1, 1, 10)
print(result)

# Perform 10 - 7 and sleep for 10 seconds...
result = lazy_subtract(10, 7, 10)
print(result)

# Perform 20 + 42 and sleeps for 30 seconds...
print(lazy_add(20, 42, 30))

# Perform 2 - 4 and sleeps for 3 seconds...
print(lazy_subtract(2, 4, 3))

# Perform 1 - 1 and sleeps for 3 seconds...
print(lazy_subtract(1, 1, 3))
