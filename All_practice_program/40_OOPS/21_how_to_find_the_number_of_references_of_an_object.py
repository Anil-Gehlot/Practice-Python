'''
How to find the number of references of an object:

sys module contains *getrefcount()* function for this purpose.

SYNTAX :    sys.getrefcount(objectreference)

'''

# Example:

import sys
class Test:
    pass

t1 = Test()
t2 = t1
t3 = t2
t4 = t1

print(sys.getrefcount(t1))
# 5



# **Note: For every object, Python internally maintains one default reference variable self.
