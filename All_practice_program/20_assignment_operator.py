"""
Assignment operator :Assignment operators are used to assign values to variables:

= , +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, <<=, >>= 
"""

a = 5                 # assignment op. to assign value.
x, y, z = 10, 4, 8     # we can also assign multiple value in single line.

# p, q, r, s = 7, 8, 9        #ValueError: not enough values to unpack (expected 4, got 3)
# g, h, i = 4, 6, 7, 9        # ValueError: too many values to unpack (expected 3)

print(a)        # 5
print(x)        # 10
print(z)        # 8
print()

a += 45
x -= 23
y *= 4
z /= 2
y %= 3

print(a)
print(x)
print(y)
print(z)
print(y)
print()


# increment & decrement operator doen not work in python like any other language.
#print(x++)      # SyntaxError: invalid syntax 
#print(x--)      # SyntaxError: invalid syntax 

print(++x)       # 10 : it is just treated as sign , like negative or positive numbers. 
print(--x)       # 10 : it is just treated as sign , like negative or positive numbers. 
print(-x)        #-10 : it is just treated as sign , like negative or positive numbers. 

y &= 5         # y = y & 5 = 4 & 5
print(y)       # 4   



"""
Ternary operator in python :

SYNTAX ==>>  X = first_value if (conditin) else second_value

"""
D = 30 if 10>20 else 40
print(D)                #  40

N = "anil" if z>y else "prabahs"
print(N)                # anil
print()

# Q. read two values from the keyboard and print the minimum value with the help of ternary operator.
first = int(input("Enter first number : "))
second =int(input("Enter second number : "))
minimum = first if first<second else second
print("The minimum number is : ",minimum) 

"""
 Nesting Ternary operator :

SYNTAX ==>>  X = first_value if (conditin1) else second_value if (condition2) else third_value
"""
T = 10 if 20<30 else 40 if 50<60 else 70
U = 10 if 20>30 else 40 if 50>60 else 70

print(T)        # 10
print(U)        # 70

# Q. read three values from the keyboard and print the maximium value with the help of ternary operator.

D = int(input("Enter first number : "))
E = int(input("Enter second number : "))
F = int(input("Enter third number : "))
max = D if D>E and D>F else E if E>F else F
print(max)
