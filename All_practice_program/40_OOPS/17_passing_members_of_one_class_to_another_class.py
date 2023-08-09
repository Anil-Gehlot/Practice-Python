# We can access members of one class inside another class.

class Employee:
    x = 10
    def __init__(self, eno, ename, esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal
    def display(self):
        print('Hii ',self.ename)
        print('Your no. is: ',self.eno)
        print("Your Salary is: ",self.esal)

class Test:
    
    def modify(obj):
        obj.esal = obj.esal +1200
        obj.display()
    
e = Employee(1,'Anil',10999)
Test.modify(e)



'''
OUTPUT:

Hii  Anil
Your no. is:  1
Your Salary is:  12199
'''


'''
** If we want to access a class member inside another class 
we can do it very easily...

we have to simply have to access them as we access outside of that class.
'''
