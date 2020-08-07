"""
Python tuples are sort of like lists, except they're immutable and
are usually used to hold heterogenous data, as opposed to lists
which are typically used to hold homogenous data. Tuples use
parens instead of square brackets.

More specifically, tuples are faster than lists. If you're looking
to just define a constant set of values and that set of values
never needs to be mutated, use a tuple instead of a list.

Additionally, your code will be safer if you opt to "write-protect"
data that does not need to be changed. Tuples enforce immutability
automatically.
"""

# Example:

import math


def dist(a, b):
    """Compute the distance between two x,y points."""
    x0, y0 = a  # Destructuring assignment
    x1, y1 = b

    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)


a = (2, 7)   # <-- x,y coordinates stored in tuples
b = (-14, 72)

# Prints "Distance is 66.94"
print("Distance is: {:.2f}".format(dist(a, b)))


# Write a function `print_tuple` that prints all the values in a tuple

# function print_tuple lists out items in variable t
# 1. create function
# 2. give the function some information to run with
# 3. once the function has said information, it will iterate through the items in variable t
# 4. then the function will print the information from variable t

# YOUR CODE HERE
def print_tuple(banana):
    for i in banana:
        print(i)


t = (1, 2, 5, 7, 99)
print_tuple(t)  # Prints 1 2 5 7 99, one per line


# Declare a tuple of 1 element then print it
u = (1,)  # What needs to be added to make this work?
print_tuple(u)
