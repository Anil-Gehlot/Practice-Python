'''

3. Static Methods:

In general these methods are general utility methods.
Inside these methods we won't use any instance or class variables.

Here we won't provide self or cls arguments at the time of declaration.

We can declare static method explicitly by using @staticmethod decorator

We can access static methods by using classname or object reference

'''

class Math:

    @staticmethod
    def add(x,y):
        print("Sum: ",x+y)

    @staticmethod
    def product(x,y):
        print("Product: ",x*y)

    def average(x,y):
        print("Average: ",(x+y)/2)

Math.add(10,20)
Math.product(10,20)
Math.average(10,20)

'''
OUTPUT:

Sum:  30
Product:  200
Average:  15.0
'''

'''

**
Note: In general we can use only instance and static methods.Inside static method we can access

class level variables by using class name.
class methods are most rarely used methods in python.
'''
