
# Renaming a module at the time of import (module aliasing) :


import module as m       # here module is original  name and m is alias name.
                         # We can access members by using alias name m

print(m.x)          # 888
print(m.y)          # 999

m.add(354,3245)         # The addition is :  3599
m.sub(3254,2435)        # The substraction is :  819
m.product(2,425)        # The multiplication is :  850
m.div(23,45)            # Divison of both number is :  0.5111111111111111


"""
*** once we created alias name then we must use alias name only, because original 
name is gone.
"""

# print(module.x)           # NameError: name 'module' is not defined
# print(module.y)           # NameError: name 'module' is not defined
