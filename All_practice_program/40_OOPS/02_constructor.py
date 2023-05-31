'''

Constructor Concept:
* Constructor is a special method in python.
* The name of the constructor should be __init__(self)
* Constructor will be executed automatically at the time of object creation.
* The main purpose of constructor is to declare and initialize instance variables.
* Per object constructor will be exeucted only once.
* Constructor can take atleast one argument(atleast self)
* Constructor is optional and if we are not providing any constructor then python will provide
    default constructor.

    whenever we are creating object, constructor automatically will be called.
'''

class Student:
    """This is student class."""
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
        

s1 = Student("a",1,100)
print(s1.name,s1.rollno,s1.marks)

s2 = Student('b',2,200)
print(s2.name,s2.rollno,s2.marks)

print('--------------------------------------------')

# The above program we can also write this type.

class Student:
    def __init__(self,x,y,z):
        self.name = x
        self.rollno = y
        self.marks = z
    def display(self):
        print(f'Student Name: {self.name}, Student Rollno: {self.rollno}, Student Marks: {self.marks} ')


s3 = Student('c',3,300)
s3.display()    

print('--------------------------------------------')


# Program to demonistrate constructor will execute only once per object:

class Emp:
    def __init__(self):
        print('constructor called...')


a1 = Emp()
a2 = Emp()
a3 = Emp()

'''
OUTPUT:

constructor called...
constructor called...
constructor called...
'''


# constructor with multiple optional arguments.

class Emp:
    def __init__(self, name='.',salary=0):
        self.name = name
        self.salary = salary

    def show(self):
        print('Employee Name: ',self.name)
        print('Employee Salary: ',self.salary)

e1 = Emp()
e1.show()

'''
OUTPUT:

Employee Name:  .
Employee Salary:  0
'''

e2 = Emp('anil',90329)
e2.show()

'''
OUTPUT:

Employee Name:  anil
Employee Salary:  90329
'''


        