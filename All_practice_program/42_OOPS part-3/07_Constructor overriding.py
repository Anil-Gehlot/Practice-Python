
'''

In the concept of constructor overiding, only the sub class constructor is accessible from the sub class object. 
That means the sub class constructor is replacing the super class constructor. This is called constructor overriding .
'''

# Example 1: Demo Program for Constructor overriding.

class P:
    def __init__(self):
        print("This is the super(Parent) class constructor")


class C(P):
    def __init__(self):
        print('This is child class constructor.')

c = C()                 # This is child class constructor.

# NOTE : In the above example,if child class does not contain constructor then parent class constructor will be executed
print("---------------------------------------------------------------------------------------------------------------------------")



# Example 2: From child class constuctor we can call parent class constructor by using super() method.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal

    def display(self):
        print('Employee Name:',self.name)
        print('Employee Age:',self.age)
        print('Employee Number:',self.eno)
        print('Employee Salary:',self.esal)

e1=Employee('Anil',48,872425,26000)
e1.display()
e2=Employee('Aman',39,872426,36000)
e2.display()

"""
OUTPUT:

Employee Name: Anil
Employee Age: 48
Employee Number: 872425
Employee Salary: 26000
Employee Name: Aman
Employee Age: 39
Employee Number: 872426
Employee Salary: 36000
"""
