
'''
We can import particular members of module by using => from "modulename" import "membername"  

The main advantage of this is we can access members directly without using module name.
'''

from module import product

product(2,56)           # The multiplication is :  112
# add(2,3)                # NameError: name 'add' is not defined : Because we did not import "add".



# We can also import more than one member from that module.
from module import x,sub,div

print(x)                # 888
sub(24,234)             # The substraction is :  -210
div(234,54)             # Divison of both number is :  4.333333333333333



# Also we can imoport all members with * 
from module import *

print(x)            # 888
print(y)            # 999
add(2,4)            # The addition is :  6
sub(234.234,23)     # The substraction is :  211.234
div(2,32)           # Divison of both number is :  0.0625



# we also can alias the name of members while importing them.
from module import x,y,add as a,sub as s,product as p

print(x)            # 888
print(y)            # 999
a(2,4231)           # The addition is :  4233
s(23,4)             # The substraction is :  19
p(23,4)             # The multiplication is :  92

'''
*** Once we defined as alias name,we should use alias name only and we should not use
original name
'''
