"""
How to use one class members into another class.

There are two ways for this :
1.  By using Composition(Has-A Relationship)
2.  By using Inheritence(Is -A Relationship)



1.  By using Composition(Has-A Relationship):

making object of one class and passing that argument to another class as a argument,
is known as Has-A relationship.
The main advantage of this is *code reusability*.
"""



# Example 1

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

