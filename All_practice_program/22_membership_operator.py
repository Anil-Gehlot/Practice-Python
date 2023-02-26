"""
Membership Operators : Membership Operators are used to check the specified value is present in the object are not.
            in : Returns True if  the specified value is present in the object.
            not in  : 	Returns True if  the specified value is not present in the object.
"""  

list1 = [23,30, 'anil', 5.6, True, False]

print('anil' in list1)      # True
print('anil' not in list1)      # False
print()

print(60 in list1)      # False
print(60 not in list1)      # True
print(1 in list1)       # True : because True = 1
print()

s = "Hello! welcome to the python world!!"

print('hello' in s)     # False
print('Hello' in s)     # True
print('py' in s)        # True
print()

print('hello' not  in s)     # True
print('Hello' not in s)     #  False
print('py' not in s)        # False