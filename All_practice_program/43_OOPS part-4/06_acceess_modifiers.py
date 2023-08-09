

'''

Python access modifiers are used to modify the default scope of a variable.

Python access modifiers play an important role to protect the data from unauthorized access.
When inheritance is implemented there is a huge risk for the data to get destroyed due to the transfer of unwanted data from the parent class to the child. 
That is why the access modifier is used.


A Class in Python has three types of access modifiers:

1.  Public Access Modifier
2.  Protected Access Modifier
3.  Private Access Modifier



1.  Public Access Modifier:

The members of a class that are declared public are easily accessible from any part of the program.
All data members and member functions of a class are public by default.
This access modifiers are define as usual as we define directly in our program such as variable, function etc.

Eg:     name = 'Anil'




2.  Protected Access Modifier:

The data member of the class is declared protected by adding a single underscore “_” and this prevents it from being access. 
The protected members of the class can be accessed by other members within the class also it can be accessible to the class derived from it.

Eg:     _Name = "Prabhas"



3.  Private Access Modifier:

A double underscore “__” makes the variable private as well as secure and the members of the class which is declared private are accessible within the class. 
Also, it is not possible to access them outside the class because it will throw an error.
private access modifier is the most secure access modifier.

Eg:     __name = "Raghav"

'''

# Demo Program



class Test:
    x = 10
    _y = 20
    __z = 30

    def m1(self):
        print(Test.x)
        print(Test._y)
        print(Test.__z)

t = Test()
t.m1()
print()

print(t.x)
print(t._y)
print(t.__z)

"""
OUTPUT

10
20
30

10
20
Traceback (most recent call last):
  File "c:\Users\anilg\OneDrive\Desktop\practice-python\All_practice_program\43_OOPS part-4\06_Acceess_Modifiers.py", line 70, in <module>
    print(t.__z)
AttributeError: 'Test' object has no attribute '__z'
"""
