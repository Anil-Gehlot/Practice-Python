'''

We can use the same operator for multiple purposes, which is nothing but operator overloading.

The operator overloading in Python means provide extended meaning beyond their predefined operational meaning.

'''



# Demo program to use + operator for our class objects:

class Book:
    def __init__(self, pages):
        self.pages = pages

b1 = Book(100)
b2 = Book(500)

print(b1 + b2)                  # TypeError: unsupported operand type(s) for +: 'Book' and 'Book'


'''
For every operator **Magic Methods** are available. To overload any operator we have to override that Method in our class.

Internally + operator is implemented by using __add__() method.This method is called magic
method for + operator. We have to override this method in our class. '''



# Example 1: 

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages 

b1 = Book(1000)
b2 = Book(501)

b3 = Book('Anil')
b4 = Book("Gehlot")


print('Total no. of pages :',b1 + b2)     # Total no. of pages : 1501
print("Author Name: ", b3 + b4)           # Author Name: AnilGehlot

# Actual working when Binary(+) Operator is used.
print(b1.__add__(b2))       # 1501
print(b3.__add__(b4))       # AnilGehlot

#And can also be Understand as :
print(Book.__add__(b1, b2))         # 1501
print(Book.__add__(b3, b4))         # AnilGehlot


'''
Here, We defined the special function “__add__( )”  and when the objects b1 and b2 are coded as “ob1 + ob2“, 
the special function is automatically called as b1.__add__(b2) which simply means that b1 calls the __add__( ) function with b2 as an Argument
 and It actually means A .__add__(b1, b2).
 
'''
print("----------------------------------------------------------------------------------------------------------------------------------")


# Example 2: 

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks
    
    def __mul__(self, other):
        return self.name * other.marks
    
    def __gt__(self, other):
        return self.marks > other.marks
    
    def __lt__(self, other):
        return self.marks < other.marks

s1 = Student("ANil",100)
s2 = Student("Lokesh", 90)
s3 = Student("Harsh", 5)

print(s1 + s2)      # 190

print(s1 * s3)         # ANilANilANilANilANil

print(s1 > s2)  # True
print(s1 > s3)  # True

print(s1 < s2)  # False
print(s1 < s3)  # False
print("----------------------------------------------------------------------------------------------------------------------------------")



# Example 3: Program to overload multiplication operator to work on Employee objects:


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def __mul__(self,other):
        return self.salary*other.days
    
class TimeSheet:
        def __init__(self,name,days):
            self.name=name
            self.days=days


e = Employee('Anil', 5000)
t = TimeSheet('Anil', 10)

print('This month salary is: ',e * t)           # This month salary is:  50000

print("----------------------------------------------------------------------------------------------------------------------------------")


'''
The following is the list of operators and corresponding magic methods:


+ ---> object.__add__(self,other)

- ---> object.__sub__(self,other)

* ---> object.__mul__(self,other)

/ ---> object.__div__(self,other)

// ---> object.__floordiv__(self,other)

% ---> object.__mod__(self,other)

** ---> object.__pow__(self,other)

+= ---> object.__iadd__(self,other)

-= ---> object.__isub__(self,other)

*= ---> object.__imul__(self,other)

/= ---> object.__idiv__(self,other)

//= ---> object.__ifloordiv__(self,other)

%= ---> object.__imod__(self,other)

**= ---> object.__ipow__(self,other)

< ---> object.__lt__(self,other)

<= ---> object.__le__(self,other)

> ---> object.__gt__(self,other)

>= ---> object.__ge__(self,other)

== ---> object.__eq__(self,other)

!= ---> object.__ne__(self,other)
'''