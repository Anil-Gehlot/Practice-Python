'''
Q: Where we can modify the value of static variable:

Anywhere either with in the class or outside of class we can modify by using classname.
But inside class method, by using cls variable.


****
Note: By using object reference variable/self we can read static variables, but we cannot modify
or delete.
If we are trying to modify, then a new instance variable will be added to that particular object.
t1.a = 90
'''
class Person:
    a = 10
    def __init__(self):
        Person.a = 20

    def b1(self):
        Person.a = 30

    @classmethod
    def b2(cls):
        Person.a = 40
        print(Person.a)
        cls.a = 50

    @staticmethod
    def b3():
        Person.a = 60

print(Person.a)     # 10

Person.a = 80
print(Person.a)     # 80

p = Person()
print(Person.a)     # 20

p.b1()
print(Person.a)     # 30

Person.b2()
print(Person.a)     # 40   50

Person.b3()
print(Person.a)     # 60

print("--------------------------------------------------------------------------------------")

'''
If we change the value of static variable by using either self
or object reference variable:

**If we change the value of static variable by using either self or object reference variable, then the
value of static variable won't be changed,just a new instance variable with that name will be
added to that particular object.**

Let's take some example:
'''

# Example 1
class Test:
    a = 10
    def __init__(self):
        self.b = 20

t1 = Test()
t2 = Test()

# if we use object reference, than new instance variabel will be created.
t1.a = 999                      # not acceessing the static variable a.

t1.b    # accessing the instance variable b.

print(t1.a , t1.b)      # 999   20
print(t2.a , t2.b)      # 10    20

print(t1.__dict__)      # {'b': 20, 'a': 999}
print(t2.__dict__)      # {'b': 20}

print("--------------------------------------------------------------------------------------")

# Example 2
class Sample:
    a = 10
    def m1(self):
        self.a = 888
    
s1 = Sample()
s1.m1()

print(Sample.a)       # 10
print(s1.a)         # 888
print("--------------------------------------------------------------------------------------")

# Example 3
class Anil:
    x = 10
    def __init__(self):
        self.y = 20

a1=Anil()
a2=Anil()
print('a1:',a1.x,a1.y)      # 10    20
print('a2:',a2.x,a2.y)      # 10    20
a1.x=888
a1.y=999
print('a1:',a1.x,a1.y)      # 888   999
print('a2:',a2.x,a2.y)      #10     20
print("--------------------------------------------------------------------------------------")

# Example 4:

class Harsh:
    a = 10
    def __init__(self):
        self.b = 20

h1=Harsh()
h2=Harsh()

Harsh.a=888
h1.b=999

print(h1.a,h1.b)    # 888   999
print(h2.a,h2.b)    # 888   20
print("--------------------------------------------------------------------------------------")

# Example 5:

class Lokesh:
    c = 10
    def __init__(self):
        self.d = 20
    
    def m1(self):
        self.c = 888
        self.d = 999

l1=Lokesh()
l2=Lokesh()
l1.m1()
print(l1.c,l1.d)    # 888   999
print(l2.c,l2.d)    # 10    20
print("--------------------------------------------------------------------------------------")

# Example 6:
class Main:
    m = 10
    def __init__(self):
        self.n = 20
m1 = Main()
m2 = Main()

# it is creating instance variabel, not static variable.
m2.m +=1   #==>> m2.m = m2.m + 1

print(m2.m)         # 11
print(Main.m)       # 10
print(m1.m)         # 10





print("--------------------------------------------------------------------------------------")

# Example 7:
class Pari:
    u = 10
    def __init__(self):
        self.v = 20

    @classmethod
    def z1(cls):
        cls.u = 555
        cls.v = 333
p1 = Pari()
p2 = Pari()
p1.z1()


'''
** if we are calling any classmethod(z1) by object reference(p1) , 
no matters it will change the  value for each object and for whole 
class 'Pari' also....Beacause it is class level data
'''
print(p1.u, p1.v)       # 555   20
print(p2.u, p2.v)       # 555    20
print(Pari.u, Pari.v)   # 555   333    
print("--------------------------------------------------------------------------------------")
