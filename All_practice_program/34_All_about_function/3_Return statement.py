
'''
The return keyword is used to exit a function and return a value.

after return statement nothing will be executed , even it breaks for loop too.'''

# Statements after the return line will not be executed:
def add(num1,num2):
    result = num1 + num2
    return result
    print(f"hii your addition of {num1} and {num2} : {result}")

print(add(34,36))           # 70


# If we are not writing return statement then default return value is None

def f1():
    print("Hii, I'm anil.")
f1()
print(f1())
'''
Output : 
        Hii, I'm anil.
        Hii, I'm anil.
        None
'''

# Q. Write a function to check whether the given number is even or odd?
def even_odd(num):
    if num%2==0:
        print(f'{num} is even number.')
    else:
        print(f"{num} is odd number.")
even_odd(23)        # 23 is odd number.
even_odd(46)        # 46 is even number.


# Q. Write a function to find factorial of given number ?

def factorial(num):
    fact = 1
    while num!=1:
        fact =fact*num
        num = num-1
    return fact
result = factorial(5)
print(result)           # 120



