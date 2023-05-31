'''
1. Instance Variables:

If the value of a variable is varied from object to object, then such type of variables are called
instance variables.

For every object a separate copy of instance variables will be created.


==>> Where we can declare Instance variables:

1. Inside Constructor by using self variable
2. Inside Instance Method by using self variable
3. Outside of the class by using object reference variable

'''

# Declaring instance variable Inside Constructor by using self variable:

class Emp:
    def __init__(self):
        self.eno = 100
        self.ename = 'anil'
        self.esal = '1M'

e = Emp()       # creating object.

print(e.__dict__)   # to print all the instance variable in dictionary form.

'''
OUTPUT:

{'eno': 100, 'ename': 'anil', 'esal': '1M'}
'''


# accessing instance variable

print(e.eno)        # 100
print(e.ename)      # anil
print(e.esal)       # 1M

print("--------------------------------------------------------")


# Declaring instance variable Inside Instance Method by using self variable:
''' If any instance variable declared inside instance method, that instance variable will be added once we call taht method. '''

class Sample:
    def __init__(self):
        self.a = 10 
        self.b = 20
        self.c = 30
    def m1(self):
        self.d = 40
        self.e = 50
    
s1 = Sample()
print(s1.__dict__)
# output before calling method.
'''
{'a': 10, 'b': 20, 'c': 30}
'''

# output after calling method.
s1.m1()
print(s1.__dict__)
'''
{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
'''

# accessing instance variable
s2 = Sample()
# print(s2.e)     # AttributeError: 'Sample' object has no attribute 'e' :: because we didn't call m1() method.

print("--------------------------------------------------------")


# Declaring instance variable from outside of the class by object reference variable:

class Test:
    def __init__(self):
        self.A = 1
        self.B = 2
        self.C = 3
    def m2(self):
        self.D = 4
        self.E = 5

t1 = Test()
print(t1.__dict__)      # {'A': 1, 'B': 2, 'C': 3}
t1.F = 70
print(t1.__dict__)      # {'A': 1, 'B': 2, 'C': 3, 'F': 70}
t1.A = 999
t1.B = 888
print(t1.__dict__)      # {'A': 999, 'B': 888, 'C': 3, 'F': 70} 




t2 = Test()
print(t2.__dict__)      # {'A': 1, 'B': 2, 'C': 3}
t2.m2()
print(t2.__dict__)      # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

# accessing instance variable

print(t1.C)     # 3
print(t2.D)     # 4

print("--------------------------------------------------------")
print("--------------------------------------------------------")


'''
** By using one object reference, if we perform any changes to the instance
variables, the changes will not be effected to remaining objects...

LET's took an example below...'''

class SE:
    def __init__(self,x,y,z):
        self.name = x
        self.age = y
        self.salary = z

s1 = SE('anil',22,100000)
s2 = SE('anil1',18,12355)

s1.gf = 'Sunny'
s1.gf2 ='Confidencial'

s2.gf = 'mallika'
s2.gf2 = 'nora'

print(s1.__dict__)      # {'name': 'anil', 'age': 22, 'salary': 100000, 'gf': 'Sunny', 'gf2': 'Confidencial'}
print(s2.__dict__)      # {'name': 'anil1', 'age': 18, 'salary': 12355, 'gf': 'mallika', 'gf2': 'nora'}


