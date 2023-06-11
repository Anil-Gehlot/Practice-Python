
'''

What ever members available in the parent class are bydefault available to the child class through
inheritance. If the child class not satisfied with parent class implementation then child class is
allowed to redefine that method in the child class based on its requirement.
This concept is called overriding.

Overriding concept applicable for both methods and constructors.
'''



# Example 1: Demo Program for Method overriding.

class P:
    def property(self):
        print('Gold + Land + Cash + Power')

    def marry(self):
        print('Appalamma')

class C(P):
    def marry(self):
        print('Ammu')

c = C()
c.property()                # Gold + Land + Cash + Power
c.marry()                   # Ammu
print("-----------------------------------------------------------------------------------------")


# Example 2: From Overriding method of child class,we can call parent class method also by using super() method.



class P1:
    def property(self):
        print('Gold + Land + Cash + Power')

    def marry(self):
        print('Appalamma')

class C1(P1):
    def marry(self):
        super().marry()
        print('Ammu')

d = C1()
d.property()
d.marry()
'''
OUTPUT:

Gold + Land + Cash + Power

Appalamma
Ammu
'''