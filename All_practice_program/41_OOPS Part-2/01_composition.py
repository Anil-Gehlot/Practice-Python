"""
How to use one class members into another class.

There are two ways for this :
1.  By using Composition(Has-A Relationship)
2.  By using Inheritence(Is -A Relationship)



1.  By using Composition(Has-A Relationship):

making object of one class and passing that argument to another class as a argument,
is known as Has-A relationship.

By using Class Name or by creating object we can access members of one class inside another class
is nothing but composition (Has-A Relationship)

The main advantage of this is *code reusability*.
"""



# Example 1
# class Employee Has-A Car reference. 

class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color

    def display(self):
        print(f'Car Name: {self.name}, Model: {self.model}, Color: {self.color}')


class Employee:
    def __init__(self,ename,eno,car):
        self.ename = ename
        self.eno = eno
        self.car = car
    def info(self):
        print('Employee Name: ',self.ename)
        print('Employee Number: ',self.eno)
        print('Car info: ',self.car.display())

c = Car('Benz', '22z', 'black')
e = Employee('anil', 2,c)
e.info()
# In this above program Employee class Has-A Car reference and hence Employee class can access all members of Car class.
print("--------------------------------------------------------------------")

# Example 2:

class Engine:
    a = 10
    def __init__(self):
        self.b = 20
    def m1(self):
        print('Engine specific functionality.')
    
class Cars:
    def __init__(self):
        self.engine = Engine()
    def m2(self):
        print("Cars using engine functionality...")
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()

c = Cars()
c.m2()
print('--------------------------------------------------------------------------------')

# Example 3:

class X:
    a = 20
    def __init__(self):
        self.b = 20
    def m1(self):
        print('m1 method of X class.')
    
class Y:
    c = 30
    def __init__(self):
        self.d = 40
    def m2(self):
        print('m2 method of class Y')
    def m3(self):
        x1 = X()            # creating object of that class.
        print(x1.a)
        print(x1.b)
        x1.m1()
        print(Y.c)      # accessing class variable by class name.
        print(self.d)
        self.m2()
        print('m3 of Y class.')
y1 = Y()
y1.m3()