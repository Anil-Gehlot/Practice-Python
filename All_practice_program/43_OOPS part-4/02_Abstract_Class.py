
'''
sometimes implemetation of a class is not complete, such type of partially implementation 
classes are called abstract classes.
Every abstract class in python should be derived from ABC class which is present in abc module.
'''


# Example 1: In the below code we can create object, even it is derived from ABC class, BECAUSE it doesnt contain any abstract method.
from abc import *
class Test(ABC):
    pass 

t = Test()




# Example 2: we can create object even class contains abstract method because we are not extending  ABC class.
from abc import *
class Test1:
    @abstractmethod
    def m(self):
        pass

t1 = Test1()





# Example 3: we cant create object of that class which contains ABC class and abstract method also.
from abc import *
class Test2(ABC):
    @abstractmethod
    def m1(self):
        pass

a = Test2()                    # TypeError: Can't instantiate abstract class Test2 with abstract method m1




# Example 4: 

from abc import *
class vehicle(ABC):
    @abstractmethod
    def noofWheels(self):
        pass

class Bus(vehicle):
    pass 

b = Bus()           # TypeError: Can't instantiate abstract class Bus with abstract method noofWheels.
# It is raising Error B'Coz we are inheriting abstratct method but in child class we are not completing its implementation.




# Example 5: Abstract class can contain both abstract and n0n-abstract methods also.

from abc import *
class Vehicle(ABC):
    @abstractmethod
    def noofWheels(self):
        pass

class Bus(Vehicle):
    def noofWheels(self):
        return 6
    
class Auto(Vehicle):
    def noofWheels(self):
        return 3
    
class Bike(Vehicle):
    def noofWheels(self):
        return 2
    
b = Bus()
print(b.noofWheels())           # 6

a = Auto()
print(a.noofWheels())           # 3
    
c = Bike()
print(c.noofWheels())           # 2