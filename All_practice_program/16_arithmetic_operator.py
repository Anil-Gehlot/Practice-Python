"""
Operators : 
            1. arithmetic operators
            2. relational &  comparison operators
            3. logical operators
            4. bitwise operators
            5. assignment operators
            6. special operators
            """

""" 
Arithmetic Operators : 
                
            1. addition operator (+)
            2. 	Subtraction operator (-)
            3. 	Multiplication operator (*)
            4. 	Division operator (/)
            5. 	Modulus operator(%)
            6.  Floor division operator (//)
            7.  Exponentiation operator(**)
            """

a = 10 
b = 20
c = 2
d = 2.5

print("addition of a & b : ",a+b)        #30
print("addition of a & d : ",a+d)        #12.5
print()

print("Subtraction of a & b : ",a-b)        #-10
print("Subtraction of a & d : ",a-d)        #7.5
print()

print("Multiplication of a & b : ",a*b)     # 200
print("Multiplication of a & d : ",a*d)     # 25.0
print()

# The division operator always generate float values.
print("Division of a & b : ",a/b)       #0.5
print("Division of a & d : ",a/d)       #4.0
print()

print("Modulus of a & c : ",a%c)        # 0
print("Modulus of a & d : ",a%d)        # 0.0
print()

""" floor devision generate int value if both argument are int type , 
    if any one argument is float then it will generate float value.
     The answer will be only integer part(after decimal point number will not be included.) """
print("Floor division of a & c : ",a//c)        # 5
print("Floor division of a & d : ",a//d)        # 4.0
print()

print("Exponentiation of a & c : ",a**c)        # 100
print("Exponentiation of a & d : ",a**d)        # 316.22776601683796 
print()



# the  "+" operater can also be used to string concatenation....

x = 'anil'
y = 'gehlot'
z = 2
z1 = '1'


print(x + y)   # anilgehlot
# print(x + z)    #TypeError: can only concatenate str (not "int") to str
print(x + z1)       # anil1
print()



# the "*" operater can also be used to string multiplication....
# any one argument must be an integer.

p = 'anil'
q = 'gehlot'
r = 2
s = '1'

print(p*r)       # anilanil
# print(p*q)      # TypeError: can't multiply sequence by non-int of type 'str'
# print(p*s)      # TypeError: can't multiply sequence by non-int of type 'str'
print()
print("------------------------------------------")

# print(10/0)     #ZeroDivisionError: division by zero
# print(10//0)        #ZeroDivisionError: integer division or modulo by zero
# print(10%0)       # ZeroDivisionError: integer division or modulo by zero
print(10**0)        # 1
