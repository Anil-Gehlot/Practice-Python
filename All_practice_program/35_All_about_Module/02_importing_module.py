
import module           # In this way we import module

# accessing variables of that module.
print(module.x)             # 888
print(module.y)             # 999

# accessing function of that module.
module.add(23,56)           # The addition is :  79
module.sub(353,324)         # The substraction is :  29
module.product(34,2)        # The multiplication is :  68
module.div(234,32)          # Divison of both number is :  7.3125
module.div(2342,0)          # Can not divide by zero.

'''
In  this program we are importina module named "module", and using that functionalities in this program.
The main advantage of importing module is - we need not to write that code again & again which we have 
written once.

Note:
whenever we are using a module in our program, for that module compiled file will be
generated and stored in the hard disk permanently.

Advantages of modules :
1) Code reusability.
2) Readability improved.
3) Maintainability.
'''
