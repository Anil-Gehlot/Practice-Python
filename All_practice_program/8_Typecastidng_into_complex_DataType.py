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

# typecasting all datatype into complex type :-
"""
There are to way we can use coplex function :-
    1. With one argument     complex(a) ==>> a + 0j      where a is Real part.
    2. With two argument     complex(a,b)==>> a + bj     where a is Real & b is Imaginary Part. 

    In oops 2nd type of functions are called "overloaded function."(because method name are same but argument are different.)
"""

# complex() with one argument ===>>>

print(complex(A))       # (234+0j)
print(complex(a))       # (123.456+0j)
print(complex(b))       # (10+20j)
print(complex(c))       # (1+0j)
print(complex(d))       # 0j
print(complex(e))       # (50+0j)
print(complex(f))       # (10.2+0j)
#print(complex(g))           # ValueError: complex() arg is a malformed string
print(complex(h))       # (30+0j)
print(complex(i))       # (4983+0j)
print(complex(j))       # (1830401+0j)
# print(complex(k))           # ValueError: complex() arg is a malformed string
# print(complex(l))           # ValueError: complex() arg is a malformed string
# print(complex(m))           # ValueError: complex() arg is a malformed string
print()

# complex() with two argument ===>>>

print(complex(10,20))            # (10+20j)
print(complex(10,20.5))          # (10+20.5j)
print(complex(30.4,20))          # (30.4+20j)
print(complex(2.3,45.6))         # (2.3+45.6j)
print(complex(True,False))       # (1+0j)

# print(complex("10","20"))      # TypeError: complex() can't take second arg if first is a string.

# print(complex(10,"20"))          # TypeError: complex() second arg can't be a string.
print("---------------------------------------------------------------------------------------------------------")









