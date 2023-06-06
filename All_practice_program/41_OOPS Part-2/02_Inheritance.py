'''

What ever variables, methods and constructors available in the parent class by default available to
the child classes and we are not required to rewrite. Hence the main advantage of inheritance is
Code Reusability and we can extend existing functionality with some more extra functionality.

SYNTAX:     class childclass(parentclass):

'''


# Example 1:
'''
In this example parent class having constructor, instance method, class method , static method,
class variable, instance varible etc, all will be also available for the Child class.
'''

class Parent:
    a = 10 
    def __init__(self):
        self.b = 10

    def m1(self):
        print("Parent instance method.")
    
    @classmethod
    def m2(cls):
        print("parent class method.")

    @staticmethod
    def m3():
        print("parent static method.")

class Child(Parent):        # Child class inherting Parent properties.
    pass

c = Child()
print(c.a)      # 10
print(c.b)      # 10
c.m1()          # Parent instance method.
c.m2()          # parent class method.
c.m3()          # parent static method.
print('------------------------------------------------------------------------')


# Example 2:

"""
TO call the properties of Parent class inside the child class, we have to use super() method.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eatnderink(self):
        print("Eat dal-chawal and drink Sambhar.")

class Employee(Person):
    def __init__(self, name, age, eno, esal):
        super().__init__(name, age)               # calling parent constructor.
        self.eno = eno
        self.esal = esal

    def work(self):
        print("Coding Python is very easy just like drinking Chilled Beer")
    
    def empinfo(self):
        print("Employee Name:",self.name)
        print("Employee Age:",self.age)
        print("Employee Number:",self.eno)
        print("Employee Salary:",self.esal)  

e = Employee('anil', 23, 100, 123456)     
e.eatnderink()                  # Eat dal-chawal and drink Sambhar.
e.work()                        # Coding Python is very easy just like drinking Chilled Beer


e.empinfo()
# Employee Name: anil
# Employee Age: 23
# Employee Number: 100
# Employee Salary: 123456