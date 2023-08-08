
'''
Recursive Functions : A function that calls itself is known as Recursive Function.

Eg:
                factorial(3)=3*factorial(2)
                            =3*2*factorial(1)
                            =3*2*1*factorial(0)
                            =3*2*1*1
                            =6

The main advantages of recursive functions are:
            1. We can reduce length of the code and improves readability
            2. We can solve complex problems very easily.
'''
# Q. Write a Python Function to find factorial of given number with recursion.

def fact(num):
    if num==0:
        result = 1
    else :
        result=num*fact(num-1)
    return result

num = int(input("Enter no. to find the factorial : "))
ans = fact(num)
print(f'The factorial of {num} : {ans}')
