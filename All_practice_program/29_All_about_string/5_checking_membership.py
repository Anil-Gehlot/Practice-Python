'''
We can check whether the character or string is the member of another string or not by using in
and not in operators.
'''

a = 'anil prabhas'
print("n" in a)     # True
print('z' in a)     # False

# Program: 
s=input("Enter main string: ")
subs=input("Enter sub string: ")
if subs in s:
    print(subs,"is found in main string")
else:
    print(subs,"is not found in main string")

