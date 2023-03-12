'''
Anonymous Functions (or) Lambda Functions :
                                Sometimes we can declare a function without any name,such type of nameless functions
                                are called anonymous functions or lambda functions.

The lambda function can take any number of argument but takes only one expression'

The main purpose of anonymous function is just for instant use(i.e for one time usage)
By using Lambda Functions we can write very concise code so that readability of
    the program will be improved.

We can define by using lambda keyword.
Syntax ==>>  lambda arguments : expression
   
Eg : lambda n : n*n
'''
# Q 1. Write a program to create a lambda function to find square of given number?

x = lambda n:n*n

print(type(x))              # <class 'function'>
print(x(5))                 # 25
print(x(4))                 # 16
print(x(3))                 # 9
print(x(2))                 # 4

# Q 2. Lambda function to find sum of 2 given numbers
y = lambda a,b : a+b

print(y(4,5))           # 9
print(y(8,9))           # 17

# Q 3.Lambda Function to find biggest of given values.
z = lambda a,b : a if a>b else b

print(z(4,5))           # 5
print(z(8,9))           # 9

'''
Note:
        Lambda Function internally returns expression value and we are not required to write
        return statement explicitly.

        Sometimes we can pass function as argument to another function. In such cases
        lambda functions are best choice.

We can use lambda functions very commonly with filter(),map() and reduce() functions,because
these functions expect function as argument.

'''