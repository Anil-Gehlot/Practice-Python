


'''
Function Decorators: 
                    Decorator is a function which can take a function as argument and extend its functionality
                    and returns modified function with extended functionality

                    The main purpose of decorators is without modifying existing function,
                    we are able to extend its functionality.

                    ***Expected function or class declaration after decorator.****

                    
Decoraters help to make our code shorter and more pythonic.
Decoraters always going to take some function as a argument.
 


'''
# EXAMPLE 1. with @decor.............
def smartdivison(func):
    def inner(a,b):
        if b==0:
            return "Can't divide by zero."
        else:
            return func(a,b)
    return inner

@smartdivison
def division(a,b):
    return a/b

a = division(10,5)
print(a)                 # 2.0

b = division(10,0)
print(b)                # Can't divide by zero.
#------------------------------------------------------------------------------------------------------------------

# EXAMPLE 1. without @decor.............
def smartdivison(func):
    def inner(a,b):
        if b==0:
            return "Can't divide by zero."
        else:
            return func(a,b)
    return inner

def division(a,b):
    return a/b

realdivison = smartdivison(division)

print(realdivison(10,5))            # 2.0
print(realdivison(10,0))            # Can't divide by zero.
#------------------------------------------------------------------------------------------------------------------

# EXAMPLE 1. with @decor.............


def decor(func):
    def inner(name):
        if name=="harsh":
            return "Hello, harsh bad Morning....☹️☹️"
        else:
            return func(name)
    return inner

@decor
def wish(name):
    return f"Hello, {name} Good Morning....🌄🌄"


print(wish('anil'))     # Hello, anil Good Morning....🌄🌄
print(wish("Lokesh"))   # Hello, Lokesh Good Morning....🌄🌄
print(wish('harsh'))    # Hello, harsh bad Morning....☹️☹️

#------------------------------------------------------------------------------------------------------------------

# EXAMPLE 2. without @decor.............

def wish(name):
    return f"Hello, {name} Good Morning....🌄🌄"

def decor(func):
    def inner(name):
        if name=="harsh":
            return "Hello, harsh bad Morning....☹️☹️"
        else:
            return func(name)
    return inner

real = decor(wish)

print(real("anil"))           # Hello, anil Good Morning....🌄🌄
print(real("lokesh"))          # Hello, lokesh Good Morning....🌄🌄
print(real("harsh"))            # Hello, harsh bad Morning....☹️☹️
