"""
There are two boolean data type
    1. True  ("T" must be capital.)
    2. False ("F" must be capital.)
"""

a = True
b = False
c = 10
d = 20 

x = c < d      # it contains "True"
y = c > d      # it contains "False"

print(x)        
print(y)
print("--------------------")


"""
Internally True is represented as 1
    and False is tepresented as 0
"""
print("True + True : ",x+x)
print("--------------------")
print("False + False : ",y+y)
print("--------------------")
print("True + False : ",x+y)
print("--------------------")

