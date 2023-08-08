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

# typecasting all datatype into float type :-

print(float(A))         # integer value can be converted into float value.
print(float(a))         # float value will be printed as it is while converting into float.

#print(float(b))        # TypeError: float() argument must be a string or a real number, not 'complex'
print(float(c))         # True is represented as 1.
print(float(d))         # False is represented as 0.
print(float(e))         # 50.0
print(float(f))         # 10.2
#print(float(g))         # ValueError: could not convert string to float: 'anil'

print(float(h))         # it will give output as float value of binary value.
print(float(i))         # it will give output as float value of octal value.
print(float(j))         # # it will give output as float value of hexa-decimal value.

#print(float(k))         # ValueError: could not convert string to float: '0B11110'
#print(float(l))         # ValueError: could not convert string to float: '0O11567'
#print(float(m))         # ValueError: could not convert string to float: '0X1bee01'
