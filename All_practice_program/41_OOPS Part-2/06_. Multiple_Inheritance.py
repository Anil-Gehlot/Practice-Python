'''

Multiple Inheritance:

The concept of inheriting the properties from multiple classes into a single class at a time, is
known as multiple inheritance.
'''

# Example 1:

class P1:
    def m1(self):
        print("Parent1 Method")
class P2:
    def m2(self):
        print("Parent2 Method")
class C(P1,P2):
    def m3(self):
        print("Child2 Method") 

c=C()

c.m1()
c.m2()
c.m3() 
'''
OUTPUT:

Parent1 Method
Parent2 Method
Child2 Method
'''
print("---------------------------------------------------------------------------------------------------")

'''
** Note:    

If the same method is inherited from both parent classes,then Python will always consider the
order of Parent classes in the declaration of the child class.
class C(P1,P2): ===>P1 method will be considered
class C(P2,P1): ===>P2 method will be considered
'''

# EXample 2:
class P1:
    def m1(self):
        print("Parent1 Method")
class P2:
    def m1(self):
        print("Parent2 Method")
class C(P1,P2):
    def m2(self):
        print("Child Method")
c=C()
c.m1()
c.m2()
"""
OUTPUT:

Parent1 Method
Child Method""" 