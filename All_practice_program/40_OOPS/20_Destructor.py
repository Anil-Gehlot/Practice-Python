'''

Destructor is a special method and the name should be __del__

Just before destroying an object Garbage Collector always calls destructor to perform clean up

activities (Resource deallocation activities like close database connection etc).

Once destructor execution completed then Garbage Collector automatically destroys that object.

**Note: The job of destructor is not to destroy object and it is just to perform clean up activities.

'''

# Example 1:
import time
class Test:
    def __init__(self):
        print("Object Initialization.....")

    def __del__(self):
        print("Destructor: cleanup activities......")


t1 = Test()
t1 = None
time.sleep(5)
print("End of application")

"""
OUTPUT:

Object Initialization.....
Destructor: cleanup activities......

(after 5 second )

End of application"""
print("-------------------------------------------------------------------------")

'''
** Note:
If the object does not contain any reference variable then only it is eligible fo GC. ie if the
reference count is zero then only object eligible for GC
'''

# Example 2:

import time
class Sample:
    def __init__(slef):
        print("Constructor Execution...")

    def __del__(self):
        print("Destructor execution.....")

s1 = Sample()
s2 = s1
s3 = s2
del s1

time.sleep(5)
print("object not yet destroyed after deleting s1")

del s2
print("object not yet destroyed even after deleting s2") 

time.sleep(5)
del s3

"""
OUTPUT:

Constructor Execution...

(after 5 second )

object not yet destroyed after deleting s1
object not yet destroyed even after deleting s2 

(after 5 second )

Destructor execution.....
"""
print("-------------------------------------------------------------------------")


# Example 3

import time
class Car:
    def __init__(self):
        print("object constructor....")

    def __del__(self):
        print("object destructor...")

list = [Car(), Car(), Car()]
time.sleep(5)
del list
print("End of program")
'''
OUTPUT:

object constructor....
object constructor....
object constructor....
object destructor...
object destructor...
object destructor...
End of program
'''
