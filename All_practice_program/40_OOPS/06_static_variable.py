'''
1. Static variables:

If the value of a variable is not varied from object to object, such type of variables we have to
declare with in the class directly but outside of methods. Such type of variables are called Static
variables.

For total class only one copy of static variable will be created and shared by all objects of that
class.

We can access static variables either by class name or by object reference. 
**But recommended to use class name.**


Instance Variable vs Static Variable:

Note: In the case of instance variables for every object a seperate copy will be created,but in the
case of static variables for total class only one copy will be created and shared by every object of
that class.
'''

class Test:
    x = 10
    def __init__(self):
        self.y = 20

t1 = Test()
t2 = Test()

print('t1: ' ,t1.x,t1.y)    # 10  20
print('t2:', t2.x,t2.y)     # 10  20

Test.x = 888    # changing the value of static variable.
t1.y = 999      # changing value of instance variable y only for t1.

print('t1: ' ,t1.x,t1.y)    # 888   999
print('t2:', t2.x,t2.y)     # 888   20
print("---------------------------------------------------------------------------------")


'''
Various places to declare static variables:

#1. In general we can declare within the class directly but from out side of any method.
#2. Inside constructor by using class name.
#3. Inside instance method by using class name.
#4. Inside classmethod by using either class name or cls variable.
#5. Inside static method by using class name.
#6. Outside the class by using classname.
'''

class Sample:
    a = 10      #1
    def __init__(self):
        self.b = 20
        Sample.c = 30       #2
    def m1(self):
        Sample.d = 40       #3
    
    @classmethod
    def m2(cls):
        Sample.e = 50       #4
        cls.f = 60          #4

    @staticmethod
    def m3():
        Sample.g = 70       #5

Sample.h = 80       #6

s = Sample()        # creating object
s.m1()              # calling instance method
Sample.m2()         # calling class method
Sample.m3()         # calling static method


# To print all the static variables.
print(Sample.__dict__)

"""
OUTPUT:

{'__module__': '__main__', 'a': 10, '__init__': <function Sample.__init__ at 0x00000181C3BA53F0>, 'm1': <function Sample.m1 at 0x00000181C3BA5480>, 'm2': <classmethod(<function Sample.m2 at 0x00000181C3BA5510>)>, 'm3': <staticmethod(<function Sample.m3 at 0x00000181C3BA55A0>)>, '__dict__': <attribute '__dict__' of 'Sample' objects>, '__weakref__': <attribute '__weakref__' of 'Sample' objects>, '__doc__': None, 'h': 80, 'c': 30, 'd': 40, 'e': 50, 'f': 60, 'g': 70}
"""
print("---------------------------------------------------------------------------------")
