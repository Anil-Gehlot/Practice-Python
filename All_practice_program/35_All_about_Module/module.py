

'''
A group of functions, variables and classes saved to a file, which is nothing but a "Module". 
Every Python file (.py) acts as a module.

The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc).
'''

x = 888
y = 999

def add(a,b):
    print("The addition is : ",a+b)

def sub(x,y):
    print("The substraction is : ",x-y)

def product(p,q):
    print("The multiplication is : ",p*q)

def div(s,t):
    if t==0:
        print("Can not divide by zero.")
    else:
        print('Divison of both number is : ',s/t)

'''
This module contains 2 variable & 4 functions.

If we want to use member of this module in other program then we must import this module in that program.
'''
