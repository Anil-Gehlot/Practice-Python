'''

In any programming language there are 2 types of errors are possible.
 1. Syntax Errors
 2. Runtime Errors

1. Syntax Errors:
The errors which occurs because of invalid syntax are called syntax errors.

Eg 1:
            x=10
            if x==10
                print("Hello")

    SyntaxError: invalid syntax

    
***  Programmer is responsible to correct these syntax errors. Once all syntax errors are
corrected then only program execution will be started.

2. Runtime Errors:

Also known as exceptions

While executing the program if something goes wrong because of end user input or
programming logic or memory problems etc then we will get Runtime Errors.

Eg: print(10/0) ==>ZeroDivisionError: division by zero

Exception Handling concept applicable for Runtime Errors but not for syntax errors.


What is Exception:
An unwanted and unexpected event that disturbs normal flow of program is called
exception.

Eg:
ZeroDivisionError
TypeError
ValueError
FileNotFoundError
EOFError
SleepingError
TyrePuncturedE
'''


print('hello')  # hello
print(10/0)                 # ZeroDivisionError: division by zero
print('hii')  # hii

#  This is the Abnormal termination/Non-Graceful Termination of the program.
print("-----------------------------------------")


'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
'''

# The code which may raise exception is called risky code and we have to take risky code inside try block.

try:
    print(10/0)             # Risky code
except :
    print("can not divide by zero")

# This is Normal termination/Graceful Termination of the program.
# Output : can not divide by zero
print("-----------------------------------------")



'''
You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:
'''

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# Output : Variable x is not defined
print("-----------------------------------------")



try:
    x=int(input("Enter First Number: "))
    y=int(input("Enter Second Number: "))
    print(x/y)
except ArithmeticError :
    print("ArithmeticError")
    
except ValueError:
   print("valueError")  

# Output1 : 
#   Enter First Number: 32
#   Enter Second Number: d
#   valueError  
# 
# 
# Output2 :
#   Enter First Number: 32
#   Enter Second Number: 0
#   ArithmeticError
print("-----------------------------------------")
