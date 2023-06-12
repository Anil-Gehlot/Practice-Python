

'''
1. If we dont know anything about implementation, just we have requirement specification 
    then we should go for interface.


2. If we are talking about implementation but not completely,
    then we should go for abstract class(Partially Implemented Class).


3. If we are talking about implementation completely and ready to provide service then we
    should go for concrete class.  
'''

from abc import *

class CollegeAutomation(ABC):

    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m1(self):
        pass

class AbsCls(CollegeAutomation):
    def m1(self):
        print("m1 method implementation.")
    
    def m2(self):
        print('m2 method implementation.')

class ConcreteCls(AbsCls):
    def m3(self):
        print('m3 method implementation.')

    
c = ConcreteCls()
c.m1()
c.m2() 
c.m3()

'''
OUTPUT:

m1 method implementation.
m2 method implementation.
m3 method implementation.
'''