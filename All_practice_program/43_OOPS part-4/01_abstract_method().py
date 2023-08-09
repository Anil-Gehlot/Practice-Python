
'''
OOPS Part 4 contains following topics:

1. Abstract Method.
2. Abstract Class.
3. Interface.
4. Public, Private and Protected Members.
5. __str__() method.
6. Difference between str() and repr() functions
7. Small Banking Application.
'''



'''
# Abstract method:

    Sometimes we do not know about implementation, still we can declare a method,
    such types of methods are called Abstract Methods.

    Abstract method has only declaration but not implementation.

    IN python we can declare abstract method by using *@abstractmethod* decorator,
    which is present inside the *abc* module.

'''

# Example 1:

from abc import *
class Test():

    @abstractmethod
    def m1(self):
        pass

t = Test()

# Example 2:

from abc import *
class Fruit:

    @abstractmethod
    def tastes(self):
        pass

# *NOTE : Child classes are responsible to provide implementation for parent class abstract methods.
