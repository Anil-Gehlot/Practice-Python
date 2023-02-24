"""
Typecasting :- converting one datatype into another datatype is known as Typecasting or 
                Typeconversion or Type coersion.
                There are 5 built-in function in python for typecasting-->>
                1. int()
                2. float()
                3. complex()
                4. bool()
                5. str()
                """

# typecasting all datatype into bool type :-

"""
If we are passing argument as integer value in bool() function Then :--
 
    if argument is 0 , it will be treated as False.
    if argument is non-zero , it will be treated as True.
    """
a = 0
b = 9
c = -9

print(bool(a))    # False
print(bool(b))    # True
print(bool(c))    # True
print()


"""
If we are passing argument as float value in bool() function Then :--
 
    if argument is total 0 (means before and after decimal point there is only zero) , it will be treated as False.
    if argument is non-zero (before and after decimal) , it will be treated as True.
    """

x = 0.0
y = 2.3
z = -0.34

print(bool(x))      # False
print(bool(y))      # True
print(bool(z))      # True
print()

"""
If we are passing argument as complex value in bool() function Then :--
 
    if both(real & imaginary part) are zero , only then  it will be treated as False.
    else : it will be treated as True.
    """

p = 0 + 0j
q = 10 + 29j
r = 0 + 2.3j

print(bool(p))      # False
print(bool(q))      # True
print(bool(r))      # # True
print()

"""
If we are passing argument as string value in bool() function Then :--
 
    if argument is an empty string than , it will be treated as "False".
    else : "True"
    """
s1 = ""        # False : because an empty string.
s2 = " "       # True : because a single space is also treated as string in python.
s3 = "anil"    # True

print(bool(s1))
print(bool(s2))
print(bool(s3))
print()

"""
If we are passing argument as binary,octal or hexa-decimal value in bool() function Then :--
 
    same rule     if all are zero then "False"
                  else : "True"
    """

b1 = 0b000
b2 = 0b101
o1 = 0o000
o2 = 0O345
h1 = 0x000
h2 = 0X2beef

print(bool(b1))     # False
print(bool(b2))     # True
print(bool(o1))     # False
print(bool(o2))     # True
print(bool(h1))     # False
print(bool(h2))     # True