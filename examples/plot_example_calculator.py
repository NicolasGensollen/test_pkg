"""
Basic example
=============

A simple example.
"""

####################################
# Load the package
from toy_pkg.calculator import add, subtract


####################################
# Run some calculation
#
# Use the useless functions defined in
# toy_pkg to run some calculations
# and check the results...
result = add(1, 1)
assert result == 2
result = subtract(1, 3)
assert result == -2


