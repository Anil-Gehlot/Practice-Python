'''
Inner classes:

Sometimes we can declare a class inside another class,such type of classes are called inner classes.

Without existing one type of object if there is no chance of existing another type of object,then we
should go for inner classes.

Example:
 Without existing Car object there is no chance of existing Engine object. Hence Engine
class should be part of Car class.

class Car:
 .....
    class Engine:
 ......

Example: 
Without existing university object there is no chance of existing Department object
class University:
 .....
    class Department:
 ......

eg3:

Without existing Human there is no chance of existin Head. Hence Head should be part of Human.

class Human:
     class Head:


**Note: Without existing outer class object there is no chance of existing inner class object. Hence
inner class object is always associated with outer class object.

'''
# Example1:

class Outer:
    def m1(self):
        print('Outer class method')
    
    class Inner:
        def m2(self):
            print("Inner class method")

o = Outer()     # Outer class object creation
o.m1()          # Outer class method

i = o.Inner()       # Inner class object creation
i.m2()              # Inner class method


'''

Note: The following are various possible syntaxes for calling inner class method:

SYNTAX 1:

o = Outer()
i = o.Inner()
i.m1()


SYNTAX 2:

i = Outer().Inner()
i.m1()


SYNTAX 3:

Outer().Inner().m1()
'''
print("------------------------------------------------------------------------------")


# Example 2:

class Person:
    def __init__(self):
        self.name = "Anil"
        self.db = self.Dob()

    def display(self):
        print('Hii ',self.name)
        
    class Dob:
        def __init__(self):
            self.dd = 11
            self.mm = 3
            self.year = 2000
        def display(self):
            print(f'Dob = {self.dd}/{self.mm}/{self.year}')

p = Person()
p.display()
x = p.db
x.display()

'''
output:

Hii  Anil
Dob = 11/3/2000
'''
print("------------------------------------------------------------------------------")


# Example 3:
# Inside a class we can declare any number of inner classes.


class Human:
    def __init__(self):
        self.name = 'anil'
        self.mouth = self.Mouth()
        self.legs = self.Legs()


    def display(self):
        print("hello",self.name)

    class Mouth:
        def talk(self):
            print("talking....")

    class Legs:
        def walk(self):
            print('Walking....')
        

h = Human()
h.display()

h.mouth.talk()
h.legs.walk()

'''
OUTPUT:

hello anil
talking....
Walking....
'''
