"""
1. Leading zeros in decimal integer literals are not permitted
    EX==>> num = 0787  ("It is not permitted")

2. Python print function always always print decimal form of any variable declared in binary,octal or 
    hexadecimal form.

3. The type function always print the type "int" for any declared value in binary,octal,hexadecimal.
"""

# for Decimal(Base-10)
# digit between (0-9)
a = 789
print(type(a))
print(a)
print("----------------------")


# for Binary(Base-2)
# digit between (0-1)
b = 0b1010                # "b" can be both in upper or lower case.
c = 0B0011
print(type(b))
print(type(c))
print(b)
print(c)
print("----------------------")

# for Octal(Base-2)
# digit between (0-7)
d = 0o1010              # "O" can be both in upper or lower case.
e = 0O0011
print(type(d))
print(type(e))
print(d)
print(e)
print("----------------------")

# for Hexadecimal(Base-16)
# digit between (0-9) and [ a-f  (in both upper or lower case.)]

f = 0x1010abf              # "x" can be both in upper or lower case.
g = 0X00beec
print(type(f))
print(type(g))
print(f)
print(g)
print("----------------------")

