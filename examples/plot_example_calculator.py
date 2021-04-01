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
print(result)

result = subtract(1, 3)
print(result)

#####################################
# Run more computations
print(subtract(100, 90))

#####################################
# Still more
print(add(2, 2))
print(add(1,1))

