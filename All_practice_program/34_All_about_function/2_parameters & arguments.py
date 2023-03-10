'''
Parameters or Arguments ?

The terms parameter and argument can be used for the same thing: information that are passed into a function.

A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
'''

# : Write a function to take name of the student as input and print wish message by name.

def wish(name):                         
    print(f"hello {name} have a nice day.")

wish("anil")                    # hello anil have a nice day.         
wish("Prabhas")                 # hello Prabhas have a nice day.
# wish()                        # TypeError: wish() missing 1 required positional argument: 'name'
# wish('anil',"prabhas")        # TypeError: wish() takes 1 positional argument but 2 were given.

# in the above function 'anil & Prabhas' are arguments and  name is parameter.



# Q. Write a function to take number as input and print its square value.

def square(num):
    print(f'The square of {num} : {num*num}')

square(500)         # The square of 500 : 250000
square(45)          # The square of 45 : 2025

# in the above function 'num' is a parameter and 500 & 45 are arguments.
