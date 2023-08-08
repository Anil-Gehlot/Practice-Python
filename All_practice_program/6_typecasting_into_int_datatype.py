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

A = 234            # integer value
a = 123.456        # float value
b = 10+20j         # complex value
c = True           # boolean value
d = False          # boolean value
e = "50"           # integer value as a string
f = "10.2"         # float value as a atring  
g = "anil"         #  string value
h = 0B11110        # binary value
i = 0O11567        # octal value
j = 0X1bee01       # hexa-decimal valu

k = "0B11110"        # binary value in string form 
l = "0O11567"        # octal value in string form
m = "0X1bee01"       # hexa-decimal value in string form

# typecasting all datatype into int type :-

print(int(A))       # it will print integer value as it is.
print(int(a))       # it will print only integer part. 

#print(int(b))      # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'.

print(int(c))       # True is represented as 1.
print(int(d))       # False is represented as 0.
print(int(e))       # if any integer value given as string, it can be converted into integer DataType.

#print(int(f))       # ValueError: invalid literal for int() with base 10: '10.2'
#print(int(g))       # ValueError: invalid literal for int() with base 10: 'anil'

print(int(h))        # it will give output as integer value of binary value.
print(int(i))        # it will give output as integer value of octal value.
print(int(j))        # it will give output as integer value of hexa-decimal value.

#print(int(k))       # ValueError: invalid literal for int() with base 10: '0B11110'
#print(int(l))       # ValueError: invalid literal for int() with base 10: '0O11567'
#print(int(m))       # ValueError: invalid literal for int() with base 10: '0X1bee01'
