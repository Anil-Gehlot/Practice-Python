
'''
Python provides inbuilt module math.

This module defines several functions which can be used for mathematical operations.
The main important functions are-------
1. sqrt(x)
2. ceil(x)
3. floor(x)
4. fabs(x)
5. log(x)
6. sin(x)
7. tan(x)
etc...


****** Note:
We can find help for any module by using help() function.

Eg:
import math
help(math)
'''

from math import *

import math
# math.sqrt() method  returns the square root of a number:
print(sqrt(9))          # 3.0


# math.ceil() method rounds a number upwards to its nearest integer,
print(ceil(34))         # 34
print(ceil(3.2))        # 4
print(ceil(3.7))        # 4
print(ceil(5.0))        # 5


# math.floor() method rounds a number downwards to its nearest integer.
print(floor(34))         # 34
print(floor(3.2))        # 3
print(floor(3.7))        # 3
print(floor(5.0))        # 5

# fabs is used to write float absolute value.
print(fabs(-10.6))       # 10.6
print(fabs(10.6))        # 10.6

# math.pi returns the value of PI (3.14...)
print(pi)               # 3.141592653589793