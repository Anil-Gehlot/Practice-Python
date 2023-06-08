
'''

super() is a built-in method which is useful to call the super class(Parent class) constructors,variables and
methods from the child class.
'''


# Example 1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('Name: ',self.name)
        print('Age: ', self.age)

class Student(Person):
    def __init__(self, name, age, rollno, marks):
        super().__init__(name,age)
        self.rollno = rollno
        self.marks = marks

    def display(self):
        super().display()
        print('Roll no: ',self.rollno)
        print('Marks: ',self.marks)

s1 = Student('anil',23,'IC-2K20-11',99)
s1.display()

print("---------------------------------------------------------------------------------------------------------")

# Example 2

class P:
    a = 10
    def __init__(self):
        self.b = 20
    
    def m1(self):
        print("Parent Instance Method.")

    @classmethod
    def m2(cls):
        print("Parent Class Method.")

    @staticmethod
    def m3():
        print("Parent Static Method.")

class C(P):
    a = 888
    
    def __init__(self):
        self.b = 999

        print(super().a)             # 10
        print(C.a)                   # 888: child class static variavle

        # print(super().b)           # it will raise an error: because instance variable always will be called by self not by super().
        print(self.b)                # 999

        super().__init__()
        print(self.b)                # 20

        super().m1()                # Parent Instance Method.
        super().m2()                # Parent Class Method.
        super().m3()                # Parent Static Method.

c = C()

print("---------------------------------------------------------------------------------------------------------")

    
# Example 3 

class A:
    x = 10
    def __init__(self):
        self.y = 20
        
class B(A):
    def m1(self):
        print(super().x)#valid          # 10
        print(self.y)#valid1            # 20
        # print(super().y)            # it will raise an error: because of instance variable. 

b = B()
b.m1()
print("---------------------------------------------------------------------------------------------------------")


# Example 4

class M:
    a = 10
    def __init__(self):
        self.b = 20
        print("Parent class constructor.")
    
    def a1(self):
        print("Parent Instance Method.")

    @classmethod
    def a2(cls):
        print("Parent Class Method.")

    @staticmethod
    def a3():
        print("Parent Static Method.")
class N(M):

    @classmethod
    def a4(cls):

        # super().__init__()           # Error : because we cannot call constructor inside classmetohd using super().
        # super().a1()                   # Error : because we cannot call Instance method inside classmetohd using super().

        super(N,cls).__init__(cls)      # Parent class constructor.
        super(N,cls).a1(cls)            # Parent Instance Method.
        
        super().a2()                    # Parent class method
        super().a3()                    # Parent static method

       
N.a4()

print("---------------------------------------------------------------------------------------------------------")


# Example 4

class P:
    def __init__(self):
        print('Parent Constructor')
    def m1(self):
        print('Parent instance method')
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent static method')

class C(P):
    @staticmethod
    def m1():
        # super().m1()           # invalid : Because we are not allowed to use super()  within static() method.
        # super().m2()           # invalid : Because we are not allowed to use super()  within static() method.
        # super().m3()           # invalid : Because we are not allowed to use super()  within static() method.

        # we can only call parent static method from the child static method.
        super(C,C).m3()
C.m1() 