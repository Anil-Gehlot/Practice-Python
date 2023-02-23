"""
string slicing
    1. There is no "char" data type in python, a char is also considered as a string datatype.
    2. syntax of slicing  ==>>  [ begin : end : stepper ] , by default stepper is 1.
    
    3. If there is logical error, it will print an empty string.

    4. if stepper is a positive integer, then slicing will be left to right .
    5. if stepper is a negative integer, then slicing will be right to left . 
"""

str="Hello I am Prabhas_bahubali."

print(str)
print("-------------")

print(str[13])                      # fetching value by index value
print("-------------")

print(str[-4])                      # fetching value by index value
print("-------------")

print(str[-9:-3])                   # string slicing
print("-------------")

print(str[-3:-9:-1])
print("---------------")

print(str[3:18])
print("-------------")

print(str[2:18:2])                     # string slicing with stepper. 
print("-------------")

print(str[0:30:3])
print("-------------")

print(str[-50:-1])
print("-------------")
