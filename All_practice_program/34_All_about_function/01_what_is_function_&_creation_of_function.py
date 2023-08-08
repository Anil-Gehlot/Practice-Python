'''
If a group of statements is repeatedly required then it is not recommended to write these
statements everytime seperately.    
                We have to define these statements as a single unit and
we can call that unit any number of times based on our requirement without rewriting.
This unit is nothing but function.

**** The main advantage of functions is code Reusability.

Python supports 2 types of functions : -
1. Built in Functions
2. User Defined Functions
 
1. Built in Functions:  The functions which are coming along with Python software automatically,are called built
                        in functions or pre defined functions.
                        Eg : id(), type(), input(), print(), eval(), etc.

2. User Defined Functions: The functions which are developed by programmer explicitly according to business
                            requirements ,are called user defined functions.

In Python a function is defined using the def keyword:

Eg : 
                def my_function():
                      print("Hello from a function")

Calling a Function : To call a function, use the function name followed by parenthesis:

Eg : 
                def my_function():
                    print("Hello from a function")

                my_function()


Note: While creating functions we can use 2 keywords :-
        1. def (mandatory)
        2. return (optional)
'''

# Q. Write a function to print Hello.

def wish():
    print("hello world !!!")

wish()              # hello world !!!
