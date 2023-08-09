
'''
Hybrid Inheritance:

Combination of Single, Multi level, multiple and Hierarchical inheritance is known as Hybrid
Inheritance.

'''

# Examaple:


class School:
    def func1(self):
        print("This function is in school.")
 
 
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")
 
 
class Student2(School):
    def func3(self):
        print("This function is in student 2.")
 
 
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")
 
 

object = Student3()
object.func1()
object.func2()

'''
OUTPUT:

This function is in school.
This function is in student 1.
'''

























print("-------------------------------------------------------------------")

'''

Cyclic Inheritance:

The concept of inheriting properties from one class to another class in cyclic way, is called Cyclic
inheritance.Python won't support for Cyclic Inheritance of course it is really not required.

Cyclic inheritence is not supported by any of languages.
'''


# Example:

class A(B):
    pass
class B(A):
    pass 

"""
OUTPUT:
NameError: name 'B' is not defined.
"""
