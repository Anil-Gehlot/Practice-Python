"""
command line argument are stord in 'argv' variable , it is default list type.
all element are stored in list , and type of each element will be string.
argv is availabel in sys module.

but it also take as a argument at index 0 , which we write command for program execution.

We have to give command line argument seperated with whitespace.
if you are giving cmd line arguments as a string it must be in "double quotes" (or) , not in 'single quote'.
"""

from sys import argv

# print(type(argv))   
# print(argv)
# print(argv[1:])        # it will leave the element at 0 index.


# read a group of int values from the keyboard as cmd line arguments and print sum .
args=argv[1:]
sum = 0
# print(args)       # each element will be in string form.
for i in args:
    n = int(i)
    sum =sum + n
print('sum of all element is : ',sum)
