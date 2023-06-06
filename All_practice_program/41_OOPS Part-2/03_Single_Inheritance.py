
'''
1. Single Inheritance: 

The concept of inheriting the properties from one class to another class is known as single
inheritance.

'''


# Example :

class P:
    def m1(self):
        print("Parent Method")
class C(P):
    def m2(self):
        print("Child Method")
c=C()
c.m1()
c.m2() 

'''
OUTOUT:

Parent Method
Child Method
'''