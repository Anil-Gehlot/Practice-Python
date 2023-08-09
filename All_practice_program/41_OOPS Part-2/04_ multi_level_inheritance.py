'''
Multi Level Inheritance:

The concept of inheriting the properties from multiple classes to single class with the concept of
one after another is known as multilevel inheritance.
'''

# Example :


class P:
    def m1(self):
        print("Parent Method")
class C(P):
    def m2(self):
        print("Child Method")
class CC(C):
    def m3(self):
        print("Sub Child Method") 

c = CC()
c.m1()
c.m2()
c.m3()

'''
OUTPUT:

Parent Method
Child Method
Sub Child Method
'''
