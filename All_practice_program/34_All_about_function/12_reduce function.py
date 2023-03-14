

'''
reduce function reduces sequence(group) of elememnts into a single element by applying the specified function.
SYNTAX : reduce(function,sequence)

reduce() function present in functools module and hence we should write import statement.
reduce function group of values lo leta he or unko ek value me convert kar deta h according to given condition.

'''

from functools import *

list1 = [10,20,30,40,50]
l2 = [234,34,35]
add = reduce(lambda x,y : x+y,list1)
sub = reduce(lambda x,y : x-y,list1)
mult = reduce(lambda x,y : x*y,list1)
div = reduce(lambda x,y : x/y,list1)
module = reduce(lambda x,y : x%y,list1)
maximun = reduce(lambda a,b :a if a>b else b,list1)
minimum = reduce(lambda a,b :a if a<b else b,list1)

print(add)                  # 150
print(sub)                  # -130
print(mult)                 # 12000000
print(div)                  # 8.333333333333332e-06
print(module)               # 10
print(maximun)              # 50
print(minimum)              # 10

result=reduce(lambda x,y:x+y,range(1,101))
print(result)    
                            #5050